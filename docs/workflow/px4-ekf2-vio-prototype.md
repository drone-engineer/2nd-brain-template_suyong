# PX4 EKF2 + VIO 통합 프로토타입 가이드

> 목적: GNSS-Denied 환경에서 PX4(EKF2)에 VIO/비전 항법을 통합해 지정 위치까지 자율 복귀(RTB)하는 최소 동작 프로토타입.
> 대상 하드웨어: `[[hunter-killer-drone-system]]` (Pixhawk 6X + Jetson Orin Nano) 또는 동급.
> 이론 배경: `[[gnss-denied-autonomous-navigation]]` (TRN/VIO/비전매칭).

## 0. 전체 구조

```
[Jetson Orin Nano]
  ├─ Camera (CSI/USB) → VIO node (대략: VINS-Fusion / ORB-SLAM3 / Kimera)
  │     → ROS2 topic: /visual_odometry (geometry_msgs/PoseWithCovarianceStamped)
  ├─ MicroXRCE-DDS Agent (udp4 -p 8888) ←→ [Pixhawk 6X]
  │     PX4는 EKF2에 VIO를 외부 비전 소스로融合
  └─ Fail-Safe 스크립트: GPS_STATUS==NOSOL 감지 → EKF2_AID_MASK에서 VISION 활성화
```

핵심: PX4는 자체 EKF2가 센서융합을 담당. VIO는 "외부 위치/속도 보조"로 주입.

## 1. PX4 파라미터 설정 (QGroundControl / MAVLink)

EKF2 보조 센서 마스크에서 비전 사용:

```bash
# EKF2 보조 센서 마스크: 비전 위치/속도 사용 (비트값 합산)
# 1=GPS, 2=비전위치, 8=비전속도, 16=외부추정 ... (PX4 문서 참조)
param set EKF2_AID_MASK 1        # 기본 GPS 우선
# GNSS-Denied 진입 시 아래로 전환 (스크립트/수동)
param set EKF2_AID_MASK 24       # 비전위치(2)+비전속도(8)+? → 정확히는 2+8+추정조합
param set EKF2_HGT_MODE 2        # 고도: 비전/거리센서 우선 (GPS 무효 시)
param set EKF2_EV_DELAY 10       # 비전 지연(ms) — 카메라~EKF 파이프라인 지연 보정
param set EKF2_RNG_AID 1         # 거리센서(LRF) 보조 활성화
param set SENS_FLOW_ROT 0        # 광류 센서 회전 (옵션)
```

> 주의: 정확한 비트값은 PX4 버전별 EKF2_AID_MASK 열거형을 따를 것. 위 값은 예시.

## 2. VIO 노드 (Jetson, ROS2)

VIO는 외부 패키지(VINS-Fusion/ORB-SLAM3)를 쓰되, PX4가 요구하는 토픽/프레임으로 브리지:

```python
# vio_to_px4_bridge.py (ROS2 노드, 개념 코드)
# 입력: VIO 결과 (카메라 프레임 상대위치)
# 출력: /fmu/in/vehicle_visual_odometry (PX4 uORB bridge 토픽)
import rclpy; from rclpy.node import Node
from px4_msgs.msg import VehicleVisualOdometry
from geometry_msgs.msg import PoseWithCovarianceStamped

class VIOBridge(Node):
    def __init__(self):
        super().__init__('vio_bridge')
        self.pub = self.create_publisher(VehicleVisualOdometry, '/fmu/in/vehicle_visual_odometry', 10)
        self.sub = self.create_subscription(PoseWithCovarianceStamped, '/vio/odometry', self.cb, 10)
    def cb(self, msg):
        v = VehicleVisualOdometry()
        v.timestamp = int(self.get_clock().now().nanoseconds/1000)
        v.x = msg.pose.pose.position.x; v.y = msg.pose.pose.position.y; v.z = msg.pose.pose.position.z
        v.q = [msg.pose.pose.orientation.x, msg.pose.pose.orientation.y,
               msg.pose.pose.orientation.z, msg.pose.pose.orientation.w]
        v.pose_covariance = list(msg.pose.covariance)  # 불확실성 전달 (EKF 융합 가중치)
        self.pub.publish(v)
rclpy.spin(VIOBridge())
```

## 3. Fail-Safe 전환 스크립트 (GNSS 손실 감지)

GPS가 NOSOL(해법 없음)이 되면 EKF2를 비전 모드로 전환:

```python
# gnss_denied_switch.py (개념)
# GPS_STATUS==NOSOL 지속 시 EKF2_AID_MASK를 비전중심으로 변경 + RTB 트리거
import rclpy; from px4_msgs.msg import VehicleGpsStatus, VehicleStatus
class Switcher(Node):
    def __init__(self):
        self.create_subscription(VehicleGpsStatus, '/fmu/out/vehicle_gps_status', self.gps_cb, 10)
        self.nosol_count = 0
    def gps_cb(self, msg):
        if msg.fix_type < 3:  # 3=3D fix 미만
            self.nosol_count += 1
            if self.nosol_count > 10:  # 약 1초 지속
                self.set_param('EKF2_AID_MASK', 24)   # 비전 모드
                self.set_param('EKF2_HGT_MODE', 2)
                self.trigger_rtb()                      # 지정 복귀점 항법
        else:
            self.nosol_count = 0
```

## 4. TRN/비전매칭 연동 (글로벌 좌표 복원)

VIO는 **상대위치**(출발점 기준)만 줌 → 글로벌 위경도가 필요하면:
- **TRN**: 하부 LiDAR/LRF 고도 프로파일 ↔ 사전 DTED 지도 대조 → 글로벌 좌표 역산
- **비전매칭**: 하부 카메라 ↔ 사전 위성/항공사진 특징점 매칭 → 수 미터 오차 글로벌 좌표
- 둘 중 하나로 VIO의 드리프트를 주기적 보정 (Loop closure)

## 5. 검증 체크리스트 (시뮬→실기체)

1. Gazebo/AirSim에서 GPS를 강제 disable → VIO만으로 위치 수렴 확인
2. VIO 드리프트 누적량 측정 (정지 60초 후 위치 편차 < 1m 목표)
3. TRN/비전매칭으로 글로벌 좌표 오차 < 5m 확인
4. Fail-Safe 스위치 동작 (GPS 끊기면 1초 내 비전모드 전환 + RTB)
5. `[[uav-swarm-defensive-countermeasures]]` 취약점 매핑 검증

## 6. 한계

- VIO는 texture-less/단조로운 지형에서 실패 → TRN/LRF 보강 필수
- 실내/터널 등 GNSS-Denied 극단 환경은 SLAM(2605.20484) 추가 필요
- Banshee 계열 비전기만은 VIO 추적에도 영향 → 다중센서 교차검증 권장

## 7. Kill-Switch: MAVLink 긴급 취소 명령 시퀀스

인간이 지상국에서 내리는 즉시 중단. PX4는 아래 명령을 최우선 처리.

```python
# abort_command.py (지상국 → 드론, MAVSDK 기준, 개념)
from mavsdk import System
import asyncio

async def emergency_abort():
    drone = System(mavsdk_server_address="localhost", port=50051)
    await drone.connect()
    # 1) 외부/오프보드 제어 즉시 해제 (AI 미션 권한 박탈)
    await drone.offboard.stop()
    # 2) 타격/충돌 페이로드 무효화 (페이로드 채널 차단 — 기체별 구현)
    await drone.action.set_actuator(1, 0.0)   # 예: 타격장치 아밍 해제
    # 3) 비행 종료 또는 안전 복귀
    #   (a) 즉시 착륙:
    await drone.action.land()
    #   (b) 또는 지정 복귀(RTB) 후 대기:
    # await drone.action.return_to_launch()
    print("ABORT issued: offboard stopped, payload disarmed, landing")

asyncio.run(emergency_abort())
```

> PX4 네이티브: `MAV_CMD_DO_FLIGHTTERMINATION`(즉시 모터 정지/낙하) 또는 `NAV_GUIDED` 해제 + `RTL`. 자율타격 체계는 **모터 정지보다 '락온 해제+RTB'가 윤리적으로 우선**.

## 8. 시간예약중단 (Time-boxed Abort) — 통신두절 대비

지상국 무응답 시 기체가 **스스로** 중단. 미션 생성 시 타이머를 내장(`[[uav-mission-approval-abort]]` 3절).

```python
# timeboxed_abort.py (기체 온보드, 개념)
# 지상국 heartbeat 수신 시마다 타이머 리셋. T초 무응답 → 자동 abort
import rclpy, time
from rclpy.node import Node
from mavsdk import System

class TimeboxedAbort(Node):
    def __init__(self, timeout_s=30.0):
        super().__init__('timeboxed_abort')
        self.timeout = timeout_s
        self.last_heartbeat = time.time()
        self.create_subscription(HeartbeatMsg, '/ground/heartbeat', self.hb_cb, 10)
        self.timer = self.create_timer(1.0, self.check)
    def hb_cb(self, msg):
        self.last_heartbeat = time.time()   # 지상국 응답 시 리셋
    def check(self):
        if time.time() - self.last_heartbeat > self.timeout:
            self.get_logger().warn(f"No heartbeat >{self.timeout}s → AUTO ABORT")
            # offboard 정지 + RTB
            asyncio.run(self._abort())
    async def _abort(self):
        drone = System(); await drone.connect()
        await drone.offboard.stop()
        await drone.action.return_to_launch()
```

> 핵심: **중단 권한은 지상국 독점이 아님**. 기체 로컬 타이머가 최종 보험.

## 9. 편대 abort 브로드캐스트 (PACNav 연동)

편대 일부가 중단 명령을 받거나 스스로 abort하면, **생존 기기가 동료에게 전파** → 군집 전체 안전 정지. `[[uav-swarm-middleware]]`(PACNav) 지역관측 토폴로지 활용.

```python
# swarm_abort_broadcast.py (개념)
# 임의 기체가 abort 발동 → ROS2 토픽 /swarm/abort 브로드캐스트
# 수신한 기체는 각자 로컬 abort 수행 (지상국 의존 없음)
from rclpy.node import Node
class SwarmAbort(Node):
    def __init__(self):
        self.pub = self.create_publisher(AbortMsg, '/swarm/abort', 10)
        self.sub = self.create_subscription(AbortMsg, '/swarm/abort', self.on_abort, 10)
    def trigger(self, reason):
        self.pub.publish(AbortMsg(reason=reason, src=self.id))   # 동료에게 전파
    def on_abort(self, msg):
        if msg.src != self.id:
            self.local_abort()   # 수신 즉시 자기 기체 중단
```

- 통신 두절 환경에서도 PACNav 계열 애드혹 토폴로지로 홉 단위 전파
- `[[uav-mission-approval-abort]]` 원칙 "중단은 항상 로컬 강제 가능" 구현

## 10. 위키 연결

- `[[uav-mission-approval-abort]]` — 승인/취소 설계 (이 가이드의 구현 대상)
- `[[uav-swarm-defensive-countermeasures]]` — 취소는 방어의 일부
- `[[gnss-denied-autonomous-navigation]]` — abort 후 GNSS-Denied 복귀
- `[[hunter-killer-drone-system]]` — PRD 인간게이트 부재 보완

## 11. VIO 패키지 설치 (Jetson Orin Nano, ROS2 Humble)

VIO는 외부 SLAM 패키지를 쓴다. 권장: **VINS-Fusion**(비전+IMU 융합, ROS2 포트 존재) 또는 ORB-SLAM3.

```bash
# Jetson Orin Nano (Ubuntu 22.04, ROS2 Humble)
# 1) 의존성
sudo apt install -y ros-humble-cv-bridge ros-humble-image-transport \
  ros-humble-vision-msgs ros-humble-rviz2
sudo apt install -y libopencv-dev libeigen3-dev libceres-dev

# 2) VINS-Fusion ROS2 (Humble 브랜치)
#   공식 저장소: https://github.com/HKUST-Aerial-Robotics/VINS-Fusion (ROS1 전용)
#   ROS2 Humble 포크: https://github.com/JunJie1213855/VINS_ROS2 (branch: main)
mkdir -p ~/vio_ws/src && cd ~/vio_ws/src
git clone https://github.com/JunJie1213855/VINS_ROS2.git
cd ~/vio_ws && colcon build --packages-select vins_fusion

# 3) 카메라→VINS 토픽 매핑 (theolaye.calib)
#   /camera/image_raw (mono 또는 stereo) + /imu/data → VINS 입력
# 4) 출력: /vio/odometry (geometry_msgs/PoseWithCovarianceStamped)
#   → 섹션 2 브리지(vio_to_px4_bridge.py)가 PX4로 전달
```

> Jetson Orin Nano는 컴퓨팅 한계 있음 → 해상도 다운(640×480), IMU 200Hz 제한, VINS-Fusion `freq` 낮춤 권장.

## 12. TRN (Terrain Referenced Navigation) 구현

VIO가 주는 **상대위치**를 **글로벌 좌표**로 보정. LiDAR/LRF 하부 고도 ↔ 사전 DTED 지도 대조.

```python
# trn_corrector.py (개념, 섹션 4 구현)
# 입력: LRF 고도(h_meas), 현재 VIO 추정 위치(x_vio,y_vio), DTED 격자
# 출력: 보정된 글로벌 좌표(x_glob,y_glob)
import numpy as np

class TRN:
    def __init__(self, dted_grid, cell_m=30.0):
        self.dem = dted_grid          # 2D_numpy (고도, m)
        self.cell = cell_m
    def correct(self, x_vio, y_vio, h_meas):
        # VIO 추정 근방 탐색: 지도 고도와 측정고도 차이 최소화 지점이 실제 위치
        r0, c0 = int(y_vio/self.cell), int(x_vio/self.cell)
        best=None; best_err=1e9
        for dr in range(-20,21):
            for dc in range(-20,21):
                r,c=r0+dr,c0+dc
                if 0<=r<self.dem.shape[0] and 0<=c<self.dem.shape[1]:
                    err=abs(self.dem[r,c]-h_meas)
                    if err<best_err: best_err=err; best=(c*self.cell,r*self.cell)
        return best  # (x_glob,y_glob) — VIO 드리프트 보정
```

- DTED는 사전 다운로드(예: NASADEM 30m) 후 `/maps/`에 저장, 비행 전 기체 메모리 로드
- **다운로드 스크립트**: `docs/workflow/download-dted.py` — BBOX 기반 USGS 3DEP S3 타일 자동 다운로드
  ```bash
  # 한국 전역 DTED 다운로드 (약 640MB)
  python3 docs/workflow/download-dted.py --bbox 124,33,131,39 --output ./maps/
  # 테스트용 작은 영역
  python3 docs/workflow/download-dted.py --bbox 126.9,37.5,127.0,37.6 --output ./maps/test/
  ```
- 보정 주기: 1~5Hz (LRF 갱신율). VIO 누적 오차를 루프클로징 없이 주기 보정

## 13. 빌드 & 테스트 체크리스트

| 단계 | 검증 | 목표 |
| --- | --- | --- |
| 1. VIO 빌드 | `colcon build` 성공, `/vio/odometry` 토픽 발행 | Jetson에서 10Hz+ |
| 2. 브리지 | `/fmu/in/vehicle_visual_odometry` 수신 확인 | PX4 EKF2가 vision 수용 |
| 3. GPS off 시뮬 | Gazebo에서 GPS disable → VIO만으로 hover 안정 | 위치 발산 없음 |
| 4. TRN 보정 | DTED 대조로 글로벌 좌표 오차 < 5m | VIO 드리프트 억제 |
| 5. Fail-Safe | GPS 끊기면 1초 내 비전모드+RTB | `[[gnss-denied-autonomous-navigation]]` |
| 6. Kill-Switch | 지상국 abort → 즉시 offboard정지+락온해제 | `[[uav-mission-approval-abort]]` |
| 7. 시간예약중단 | heartbeat 끊기 → T초 후 자동 abort | 로컬 보험 동작 |
| 8. 편대 브로드캐스트 | 1기 abort → 동료 전파 정지 | PACNav 토폴로지 |

> 실기체 테스트 전 **반드시 Gazebo/AirSim에서 1~7 통과**. 자율타격(Killer)은 6·7 없이 비행 금지.

## 15. GNSS-Denied 비행 시 경고 메시지 + 주치상

GNSS-Denied 환경에서 자주 발생하는 경고 메시지와 대응 주치상 (`docs/tech-stack/px4-ardupilot-warnings.csv` 83개 중 관련 항목):

| 경고 메시지 | 원인 | 주치상 (조치) |
|-------------|------|---------------|
| `COM_GNSSLOSS_ACT` | GPS 신호 손실 | `EKF2_AID_MASK=24`(비전+LRF), `EKF2_HGT_MODE=2`(고도 비전 우선) |
| `angular_velocity_invalid` | IMU 각속도 데이터 손상 | `EKF2_GYRO_NOISE` 경로 확인, IMU 캘리브레이션 재수행 |
| `global_position_invalid` | 글로벌 위치 추정 실패 | VIO 브리지 토픑 확인, `vehicle_visual_odometry` 발행 여부 |
| `local_position_invalid` | 로컬 위치 추정 실패 | `EKF2_AID_MASK`에서 비전 비트(2) 활성화, 거리센서 연결 |
| `EKF2_MAG_CAL` | 자력계 캘리브레이션 필요 | 금속/전자파 제거 후 나침반 캘리브레이션 |
| `COM_LOW_BAT_ACT` | 배터리 실패 | `BATT_LOW_MAH` 재설정, 스팬톤 배터리 교체 |
| `NAV_DLL_ACT` | 지오펜스 위반 | `FENCE_ENABLE=0`, 반경 늘리기 |
| `COM_RC_LOSS_T` | 조종기 연결 손실 | RC 안테나 고급화, `FS_GCS_ENABLE=2`(RTL) |
| `PREARM_TERRAIN` | 지형 데이터 없음 | `TERRAIN_FOLLOW` 비활성화, `RTL_ALT_TYPE=0`(고도 우선) |
| `ERROR_SUBSYSTEM_EKF_PRIMARY` | EKF 주축 전환 실패 | IMU/센서 교체, `EK3_SRC1_POSZ=3`(BARO 우선) |

> 📌 **실전 팁**: GNSS-Denied 비행 전 `param show EKF2_AID_MASK`로 현재 상태 확인 → 비전 비트(2)가 켜져 있는지 반드시 검증

## 16. YouTube 실전 경고 메시지 (추가 수집 예정)

실제 비행 중 경고 메시지 화면 녹화 영상을 수집하여 실시간 대응 가이드 작성:

| 비행 상황 | 발생 경고 | 대응 | 출처 |
|-----------|----------|------|------|
| 배터리 실패 | `BATT_LOW_MAH` / `BATT_LOW_VOLT` | 배터리 교체, 저전 임계치 재설정 | [Setup Battery Failsafe - Arducopter](https://www.youtube.com/watch?v=CCIEdyJcV-s) |
| 나침반 문제 | `PreArm Check: Compass not health` | 나침반 캘리브레이션, 금속 제거 | [PreArm Check: Compass not health](https://www.youtube.com/watch?v=mk1lMPLuXy8) |
| RC 신호 손실 | `FS_THR_ENABLE` / `RC_LOST` | RC 안테나 고급화, failsafe 재설정 | [ArduPilot Discuss #102748](https://discuss.ardupilot.org/t/102748) |
| GPS 신호 약화 | `BAD_GPS_POS` / `GPS_SIGNAL_WEAK` | GPS 안테나 위치 변경, 장애물 제거 | [ArduPilot Discuss #102574](https://discuss.ardupilot.org/t/102574) |
| EKF 주축 전환 | `ERROR_SUBSYSTEM_EKF_PRIMARY` | IMU/센서 교체, EKF2 파라미터 재설정 | [ArduPilot Discuss #12426](https://discuss.ardupilot.org/t/12426) |

> 📎 `daily-youtube-scout` 크론으로 `raw/youtube/`에 자동 수집된 영상에서 추가 경고 메시지 클립 추출 예정

- `[[uav-mission-approval-abort]]` — 승인/취소 설계
- `[[gnss-denied-autonomous-navigation]]` — TRN/VIO 이론
- `[[uav-swarm-defensive-countermeasures]]` — 방어 체계
- `[[hunter-killer-drone-system]]` — 대상 하드웨어
- `[[combat-swarm-drone-operations]]` — 5대 과제(윤리/보안)


