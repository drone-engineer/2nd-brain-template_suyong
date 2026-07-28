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
