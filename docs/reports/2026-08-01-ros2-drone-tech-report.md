---
title: "ROS2 기반 드론 최신 기술 보고서 (2026-08-01)"
created: 2026-08-01
updated: 2026-08-01
type: report
tags: [uav, software, firmware, control, communication, security]
sources:
  - raw/articles/2026-08-01-ros2-drone-github-data.md
  - raw/articles/2026-08-01-px4_release_117.md
  - raw/articles/2026-08-01-px4_ros2_bridge.md
  - raw/articles/2026-08-01-ros2_nav2.md
  - raw/articles/2026-08-01-ros2_tutorials.md
confidence: high
contested: false
contradictions: []
---

# ROS2 기반 드론 최신 기술 보고서 (2026-08-01)

> 📎 **출처**: `raw/articles/2026-08-01-ros2-drone-github-data.md`, `raw/articles/2026-08-01-px4_release_117.md`, `raw/articles/2026-08-01-px4_ros2_bridge.md`, `raw/articles/2026-08-01-ros2_nav2.md`, `raw/articles/2026-08-01-ros2_tutorials.md`

## 1. 핵심 패키지 (GitHub ⭐ 기준 top 5)

| 순위 | 패키지 | ⭐ | 설명 | 마지막 커밋 |
|------|--------|----|------|-------------|
| 1 | **microsoft/AirSim** | 18,354 | Unreal Engine/Unity 기반 자율주행 시뮬레이터 (드론 지원) | 2026-06-30 |
| 2 | **opencv/opencv** | 90,235 | 컴퓨터 비전 라이브러리 (객체인식, SLAM, ArUco) | 2026-07-31 |
| 3 | **ultralytics/ultralytics** | 60,089 | YOLOv8/v11 객체 검출 및 세그멘테이션 | 2026-07-31 |
| 4 | **ros-navigation/navigation2** | 4,532 | ROS2 내비게이션 프레임워크 (Nav2) — 행동 트리, 플래너, 컨트롤러 | 2026-07-31 |
| 5 | **eclipse-zenoh/zenoh** | 3,039 | 데이터 통합 미들웨어 (Rust 기반, ROS2 rmw_zenoh 지원) | 2026-07-31 |

### 주목할 만한 신규/업데이트 리포지토리

| 리포지토리 | ⭐ | 푸시일 | 설명 |
|------------|----|--------|------|
| **lololem/diamants-collab** | 11 | 2026-07-27 | 분산 지능 및 swarm robotics 플랫폼 (ROS2 기반) |
| **hayatPMT/Autonomous-UAV-Navigation-System** | 8 | 2026-07-27 | 실시간 점유 격자지도 기반 도심 자율 UAV 내비게이션 |
| **Sreejith-nair511/GNSS-Denied-UAV** | 1 | 2026-07-19 | ROS2 + PX4 + SLAM + 컴퓨터비전 + AI 미션 (GNSS-실패 환경) |
| **Vaderplayz/drone_ros_ws** | 1 | 2026-07-26 | ROS2 Jazzy 실드론 워크스페이스 (PX4 + MAVROS + RPLIDAR + SLAM + OpenVINS) |
| **Gruzver/drone-tracker** | 2 | 2026-03-31 | 열화상 드론 영상 실시간 사람 검출 (ROS2 Humble + YOLOv8) |
| **BhavyaPatel9/ORB_SLAM3-PX4-bridging** | 1 | 2026-03-11 | SLAM-to-PX4 제어 파이프라인 |

## 2. 객체인식 기술 (YOLOv8 / MediaPipe / ArUco)

### 2.1 YOLOv8 + ROS2

YOLOv8은 ROS2 드론 인지 스택의 표준으로 자리 잡고 있습니다.

```bash
# 설치 및 실행
pip install ultralytics
ros2 run vision_opencv yolov8_node --ros-args -p model_path:=yolov8s.pt

# 토픽 구독
ros2 topic echo /yolo/detections
```

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `model_path` | YOLOv8 모델 경로 | `yolov8s.pt` |
| `confidence_threshold` | 신뢰도 임계값 | 0.5 |
| `nms_threshold` (iou) | NMS 임계값 | 0.45 |
| `input_size` | 입력 이미지 크기 | 640 |
| `device` | 연산 장치 | `cuda:0` 또는 `cpu` |

### 2.2 인지 파이프라인 (Aerial-Autonomy-Stack 스타일)

```
Camera → [YOLOv8 검출] → [DeepSORT 추적] → [Kalman Filter] → [궤적 예측]
```

| 단계 | 기술 | 주요 파라미터 |
|------|------|----------------|
| 1. 검출 | YOLOv8 | `yolo_conf`, `yolo_iou` |
| 2. 추적 | DeepSORT | `deepsort_max_age`, `deepsort_n_init` |
| 3. 상태 추정 | Kalman Filter | `kf_process_noise`, `kf_measurement_noise` |
| 4. 궤적 예측 | LSTM | `lstm_seq_len`, `lstm_hidden_dim` |

### 2.3 MediaPipe + ROS2

MediaPipe는 실시간 자세 추정과 제스처 제어에 사용됩니다.

```bash
# 설치
pip install mediapipe
ros2 run mediapipe_ros2 hand_detection
```

| 기능 | 토픽 | 용도 |
|------|------|------|
| **Hand Tracking** | `/mediapipe/hands` | 제스처 제어 |
| **Pose Estimation** | `/mediapipe/pose` | 드론 추적 |
| **Object Detection** | `/mediapipe/objects` | 물체 인식 |

### 2.4 ArUco / OpenCV

OpenCV는 ArUco 마커 검출과 비전 기반 항법에 사용됩니다. `opencv_contrib` (10,163 ⭐)에
포함된 `aruco` 모듈은 GNSS-실패 환경에서 드론의 위치를 추정하는 데 활용됩니다.

## 3. 제어 인터페이스 (PX4 ROS2 Bridge)

### 3.1 PX4 v1.17 — ROS 2 워크플로 개선사항

PX4 v1.17.0 (2026-05-13 출시)은 ROS 2 워크플로에 다음을 추가했습니다 ^[raw/articles/2026-08-01-px4_release_117.md]:

- **Altitide Cruise 모드** 추가 (고도 유지 + 속도 제어)
- **고정익/FW 이착륙** 개선 (네비게이션 손실 시 행동 개선)
- **ROS 2 고수준 제어 인터페이스** 정비 — fixed-wing 및 rover용
- **Zenoh 미들웨어**가 `rmw_zenoh` 호환성을 획득 (실험적)

### 3.2 PX4 ROS2 브리지 토픽

```bash
# ROS2 브리지 실행
ros2 run px4_ros_com vehicle_pose_ekf
ros2 run px4_ros_com vehicle_local_position_publisher

# 토픁 구독
ros2 topic echo /fmu/out/vehicle_local_position
ros2 topic echo /fmu/out/vehicle_status
```

| 토픽 | 설명 | 메시지 타입 |
|------|------|-------------|
| `/fmu/out/vehicle_local_position` | 현재 위치 | `px4_msgs::msg::VehicleLocalPosition` |
| `/fmu/in/trajectory_setpoint` | 목표 궤적 | `px4_msgs::msg::TrajectorySetpoint` |
| `/fmu/out/vehicle_status` | 드론 상태 | `px4_msgs::msg::VehicleStatus` |
| `/fmu/out/battery_status` | 배터리 상태 | `px4_msgs::msg::BatteryStatus` |

### 3.3 제어 명령 발행

```bash
# Position setpoint 발행
ros2 topic pub /fmu/in/trajectory_setpoint \
  px4_msgs/msg/TrajectorySetpoint \
  "{x: 0.0, y: 0.0, z: -5.0}"
```

### 3.4 헌터킬러용 안전/방어 제어 인터페이스

PX4 v1.17에서는 안전 메커니즘 강화를 위해 다음 파라미터가 중요합니다:

```bash
# 인간 승인 게이트 (PreArm 승인 필수)
param set COM_PREARM 1

# 즉시 정지 (Kill-Switch)
param set COM_KILL 1

# GNSS-Denied 모드 (Vision + Optical Flow 활성화)
param set EKF2_AID_MASK 10

# 비행 종료 (Flight Termination)
param set COM_FLIGHT_TERM_ACT 1

# 지오펜스 (Geofence)
param set GF_MAX_HOR_DIST 500   # 최대 수평 거리 (미터)
param set GF_MAX_VER_DIST 100   # 최대 수직 거리 (미터)
```

| 기능 | ROS2 토픽 | PX4 파라미터 |
|------|-----------|-------------|
| 인간 승인 | `/fmu/in/prearm` | `COM_PREARM` |
| Kill-Switch | `/fmu/in/kill` | `COM_KILL` |
| 통신 손실 | `/fmu/out/vehicle_status` | `COM_DL_LOSS_T` |
| 배터리 실패 | `/fmu/out/battery_status` | `BAT_CRIT_THR` |
| 비행 종료 | — | `COM_FLIGHT_TERM_ACT` |
| 지오펜스 | — | `GF_MAX_HOR_DIST` |

> **주의**: v1.17은 alpha/beta release 브랜치에 문서화되어 있습니다.
> 프로덕션 배포 전 반드시 검증이 필요합니다 ^[raw/articles/2026-08-01-px4_release_117.md].

## 4. 미들웨어 (Zenoh)

### 4.1 Zenoh (PX4 v1.17)

Zenoh은 PX4 v1.17에서 `rmw_zenoh` 호환성을 획득했습니다. ROS2 토픽을 Zenoh 세션으로 브리지하여
저지연·고확장성 통신을 제공합니다.

```bash
# Zenoh 세션 생성
ros2 run rmw_zenoh zenohd --config /path/to/zenoh.json5

# 토픽 구독 (Zenoh 브리지)
ros2 topic echo /zenoh/vehicle_local_position
```

### 4.2 ROS2 배포판별 RMW 구현체

| 구현체 | 지원 여부 | 특징 |
|--------|----------|------|
| **Zenoh** | ✅ (v1.17 experimental) | 저지연, 고확장성, 멀티-드론 도메인 분리 |
| **eProsima Fast DDS** | ✅ | 표준 DDS, 안정적 |
| **RTI Connext DDS** | ✅ | 상용-grade, 높은 성능 |
| **Eclipse Cyclone DDS** | ✅ | 경량, ROS2 기본 |
| **GurumNetworks GurumDDS** | ✅ | 상용 |

### 4.3 다중 드론 네트워크 분리

ROS2의 `ROS_DOMAIN_ID`를 사용하여 드론 간 통신을 분리할 수 있습니다 ^[raw/articles/2026-08-01-ros2_tutorials.md]:

```bash
# 드론 1 (Domain 0)
export ROS_DOMAIN_ID=0
ros2 run drone_control drone_node

# 드론 2 (Domain 1)
export ROS_DOMAIN_ID=1
ros2 run drone_control drone_node
```

### 4.4 DDS vs Zenoh 비교

| 항목 | DDS (FastRTPS/Cyclone) | Zenoh |
|------|------------------------|-------|
| **지연** | ~10ms | ~2ms |
| **확장성** | 제한적 (Discovery 프로토토크롤) | 높음 (라우팅 기반) |
| **ROS 2 호환성** | 완벽 (표준) | experimental (v1.17) |
| **멀티드론 설정** | 복잡 (QoS, Domain ID) | 간단 (Domain ID + bridge) |
| **중개자 의존성** | 없음 | Zenoh 라우터 권장 |

## 5. 헌터킬러 Applications 적용

### 5.1 객체 추적 + 제어 루프

헌터킬러 드론의 핵심 루프는 인지 → 추적 → 제어의 실시간 파이프라인입니다:

```
Camera → YOLOv8 → DeepSORT → PX4 ROS2 Bridge → Trajectory Setpoint → EKF2
                                    ↓
                              Human-in-the-loop (PreArm gate)
```

### 5.2 GNSS-Denied 환경 적용

GNSS-실패 환경에서 헌터킬러 드론은 비전 기반 항법을 사용합니다 ^[raw/articles/2026-08-01-ros2_drone_github_data.md]:

```bash
# VIO + YOLOv8 융합 런치
ros2 launch vio_yolo_tracking vio_yolo.launch.py

# EKF2 파라미터 (Vision + Optical Flow 강제 사용)
param set EKF2_AID_MASK 10       # Vision + Flow
param set EKF2_GPS_ID 0          # GPS 비활성화
```

관련 프로젝트: `Sreejith-nair511/GNSS-Denied-UAV` (1 ⭐, 2026-07-19) —
ROS2 + PX4 + SLAM + 컴퓨터비전 + AI 미션.

### 5.3 안전/방어 메커니즘

헌터킬러 시스템에서는 다음 안전 계층이 필수적입니다 ^[raw/articles/2026-08-01-px4_release_117.md]:

| 계층 | 메커니즘 | 구현 |
|------|----------|------|
| **인간 승인 게이트** | PreArm 승인 | `COM_PREARM=1` + `/fmu/in/prearm` 토픽 |
| **Kill-Switch** | 즉시 정지 | `COM_KILL=1` + `/fmu/in/kill` 토픽 |
| **통신 손실** | RC/GCS 손실 감지 | `COM_DL_LOSS_T` (기본 5초) |
| **배터리 실패** | 크리티컬 배터리 | `BAT_CRIT_THR` (기본 20%) |
| **지오펜스** | 영역 제한 | `GF_MAX_HOR_DIST`, `GF_MAX_VER_DIST` |
| **비행 종료** | 긴급 추진불능 | `COM_FLIGHT_TERM_ACT=1` |
| **복구 모드** | 지정위치 복귀 | `RTL` 모드 + Safe Points (Rally) |

### 5.4 Nav2 Collision Monitor + 3Laws Supervisor

Nav2 (4,532 ⭐)는 `Enhanced Safety` 기능을 제공합니다 ^[raw/articles/2026-08-01-ros2_nav2.md]:

- **Collision Monitor**: 실시간 장애물 감지 및 회피
- **3Laws Supervisor**: 인명 보호 우선순위 기반 안전 강화 (상용 라이선스 필요)

```bash
# Collision Monitor 설정
ros2 run nav2_collision_monitor collision_monitor_node
```

## 6. 배포판 및 생태계

### 6.1 ROS2 배포판 현황

| 배포판 | 코드명 | 상태 | 비고 |
|--------|--------|------|------|
| **Humble Hawksbill** | `humble` | 유지보수 중 | 2026년 기준 아직 지원 |
| **Jazzy Jalisco** | `jazzy` | 현재 LTS | 기본 권장 |
| **Kilted Kaiju** | `kilted` | 최신 | May 2025 출시 |
| **Lyrical Luth** | `lyrical` | 최신 | May 2026 출시 (latest) |
| **Makoa Mata-mā** | `makoa` | 개발 중 | May 2027 예정 |

### 6.2 PX4 v1.17 주요 기능

| 범주 | 기능 |
|------|------|
| **비행 모드** | Altitude Cruise (신규), Position, Mission, Offboard 등 |
| **고정익** | Fixed Wing Takeoff 개선 (네비게션 손실 대응) |
| **미들웨어** | Zenoh `rmw_zenoh` 호환성 |
| **시뮬레이션** | Gazebo Jetty 지원, Ackermann SIH |
| **센서** | MicroStrain, sbgECom, EULER-NAV INS 드라이버 (신규) |
| **GNSS** | Septentrio GNSS 복원력 보고 |
| **기압계** | GNSS 높이 기준 자동 캘리브레이션 |
| **보안** | MAVLink 서명, Security Hardening |
| **파라미터** | `COM_RC_ARM_HYST` 제거 (arm/disarm 제스처 1초 유지) |

## 7. 결론

2026년 8월 1일 기준, ROS2 기반 드론 생태계는 다음과 같이 발전하고 있습니다:

1. **인지**: YOLOv8 + DeepSORT + MediaPipe 가 객체 검출/추적의 산업 표준
2. **제어**: PX4 v1.17의 ROS2 브리지 개선과 고수준 제어 인터페이스로 시스템 통합 용이
3. **미들웨어**: Zenoh이 DDS의 실시간성 한계를 보완, 멀티-드론 확장성 강조
4. **안전**: PX4의 PreArm/Kill-Switch/Geofence와 Nav2의 Collision Monitor/3Laws Supervisor가 헌터킬러 applications의 안전 계층을 제공
5. **GNSS-Denied**: VIO + SLAM + OpenCV ArUco 조합으로 GNSS-실패 환경 대응 능력 향상

> **핵심 권장사항 (헌터킬러용)**:
> - PX4 v1.17의 실험적 Zenoh + ROS2 브리지를 프로토타입 단계에서 검증
> - `COM_PREARM=1`, `COM_KILL=1` 안전 파라미터를 반드시 활성화
> - GNSS-Denied 환경에서는 EKF2 Vision+Flow 모드(`EKF2_AID_MASK=10`) 사용
> - Nav2의 Collision Monitor와 3Laws Supervisor를 레이어링하여 인명 보호
