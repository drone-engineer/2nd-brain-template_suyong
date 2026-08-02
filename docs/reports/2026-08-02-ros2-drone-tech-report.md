---
title: "ROS2 기반 드론 최신 기술 보고서 (2026-08-02)"
created: 2026-08-02
updated: 2026-08-02
type: report
tags: [uav, software, firmware, control, communication, security]
sources:
  - raw/articles/2026-08-02-ros2-drone-github-data.md
  - raw/articles/2026-08-02-px4-release-notes.md
  - raw/articles/2026-08-02-ardupilot-release-notes.md
  - raw/articles/2026-08-02-px4-docs-main.md
  - raw/articles/2026-08-02-ros2-docs-rolling.md
confidence: high
contested: false
contradictions: []
---

# ROS2 기반 드론 최신 기술 보고서 (2026-08-02)

> 📎 **출처**: `raw/articles/2026-08-02-ros2-drone-github-data.md`, `raw/articles/2026-08-02-px4-release-notes.md`, `raw/articles/2026-08-02-ardupilot-release-notes.md`, `raw/articles/2026-08-02-px4-docs-main.md`, `raw/articles/2026-08-02-ros2-docs-rolling.md`

## 1. 핵심 패키지 (GitHub ⭐ 기준 top 5)

| 순위 | 패키지 | ⭐ | 설명 | 마지막 커밋 |
|------|--------|----|------|-------------|
| 1 | **opencv/opencv** | 90,235 | 컴퓨터 비전 라이브러리 (객체인식, SLAM, ArUco) | 2026-07-31 |
| 2 | **ultralytics/ultralytics** | 60,089 | YOLOv8/v11 객체 검출 및 세그멘테이션 | 2026-07-31 |
| 3 | **microsoft/AirSim** | 18,354 | Unreal Engine/Unity 기반 자율주행 시뮬레이터 (드론 지원) | 2026-06-30 |
| 4 | **opencv/opencv_contrib** | 10,163 | OpenCV 추가 모듈 (ArUco, SFM 등) | 2026-07-29 |
| 5 | **ros-navigation/navigation2** | 4,532 | ROS2 내비게이션 프레임워크 (Nav2) — 행동 트리, 플래너, 컨트롤러 | 2026-07-31 |

### 주목할 만한 신규/업데이트 리포지토리

| 리포지토리 | ⭐ | 푸시일 | 설명 |
|------------|----|--------|------|
| **JacopoPan/aerial-autonomy-stack** | 549 | 2026-08-01 | PX4/ArduPilot 드론 스웜을 위한 인지 기반 시뮬레이션·배포 프레임워크 |
| **eclipse-zenoh/zenoh-plugin-ros2dds** | 292 | 2026-08-01 | ROS2용 Zenoh DDS RMW 플러그인 — DDS와 Zenoh 간 브리지 |
| **autowarefoundation/agnocast** | 195 | 2026-07-31 | rclcpp 호환 true zero-copy IPC 미들웨어 (ROS2 메시지 지원) |
| **thun-res/vlink** | 123 | 2026-08-01 | 자율주행용 고성능 C++ 통신 미들웨어 |
| **NEWSLabNTU/nano-ros** | 12 | 2026-08-01 | no_std ROS 2 클라이언트 (Zephyr, FreeRTOS, NuttX, Thread 지원) |
| **yasincavusoglu/ros2-counter-uav-turret** | 1 | 2026-07-28 | ROS2 기반 자율 counter-UAS(반드론) 포탑 시뮬레이션 |

## 2. 객체인식 기술 (YOLOv8 / MediaPipe / ArUco)

### 2.1 YOLOv8 + ROS2

YOLOv8은 ROS2 드론 인지 스택의 표준으로 자리 잡고 있습니다. ultralytics/ultralytics (60,089 ⭐)가 YOLOv8/v11을 유지 관리합니다.

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

OpenCV는 ArUco 마커 검출과 비전 기반 항법에 사용됩니다. `opencv_contrib` (10,163 ⭐)에 포함된 `aruco` 모듈은 GNSS-실패 환경에서 드론의 위치를 추정하는 데 활용됩니다.

## 3. 제어 인터페이스 (PX4 ROS2 Bridge)

### 3.1 PX4 v1.18.0-beta1 — 새 릴리즈 (2026-07-08)

PX4 v1.18.0-beta1은 2026-07-08에 출시된 prerelease로, v1.17.0 이후의 변경사항을 포함합니다. v1.17.0의 ROS2 워크플로 개선사항(Altitude Cruise 모드, 고정익 제어 인터페이스, Zenoh rmw_zenoh 호환)은 v1.18.0-beta1에서도 유지됩니다.

> **주의**: v1.18.0-beta1은 prerelease 브랜치에 문서화되어 있습니다. 프로덕션 배포 전 반드시 검증이 필요합니다.

### 3.2 PX4 ROS2 브리지 토픽

```bash
# ROS2 브리지 실행
ros2 run px4_ros_com vehicle_pose_ekf
ros2 run px4_ros_com vehicle_local_position_publisher

# 토픽 구독
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

PX4 v1.17/v1.18의 안전 메커니즘 강화를 위해 다음 파라미터가 중요합니다:

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

## 4. 미들웨어 (Zenoh)

### 4.1 Zenoth (PX4 v1.17/v1.18)

Zenoh은 PX4 v1.17에서 `rmw_zenoh` 호환성을 획득했습니다. ROS2 토픽을 Zenoh 세션으로 브리지하여 저지연·고확장성 통신을 제공합니다. v1.18.0-beta1에서도 이 기능이 유지됩니다.

```bash
# Zenoh 세션 생성
ros2 run rmw_zenoh zenohd --config /path/to/zenoh.json5

# 토픽 구독 (Zenoh 브리지)
ros2 topic echo /zenoh/vehicle_local_position
```

### 4.2 ROS2 배포판별 RMW 구현체

| 구현체 | 지원 여부 | 특징 |
|--------|----------|------|
| **Zenoh** | ✅ (v1.17/v1.18 experimental) | 저지연(~2ms), 고확장성, 멀티-드론 도메인 분리 |
| **eProsima Fast DDS** | ✅ | 표준 DDS, 안정적 |
| **RTI Connext DDS** | ✅ | 상용-grade, 높은 성능 |
| **Eclipse Cyclone DDS** | ✅ | 경량, ROS2 기본 |
| **GurumNetworks GurumDDS** | ✅ | 상용 |

### 4.3 다중 드론 네트워크 분리

ROS2의 `ROS_DOMAIN_ID`를 사용하여 드론 간 통신을 분리할 수 있습니다.

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
| **확장성** | 제한적 (Discovery 프로토콜) | 높음 (라우팅 기반) |
| **ROS 2 호환성** | 완벽 (표준) | experimental (v1.17/v1.18) |
| **멀티드론 설정** | 복잡 (QoS, Domain ID) | 간단 (Domain ID + bridge) |
| **중개자 의존성** | 없음 | Zenoh 라우터 권장 |

### 4.5 신규 미들웨어 동향 (2026-08-02 기준)

| 리포지토리 | ⭐ | 설명 |
|------------|----|------|
| **eclipse-zenoh/zenoh-plugin-ros2dds** | 292 | ROS2↔DDS 브리지 via Zenoh — ROS2와 DDS 간 통신 통합 |
| **autowarefoundation/agnocast** | 195 | rclcpp 호환 true zero-copy IPC — ROS2 메시지 직접 전달 |
| **NEWSLabNTU/nano-ros** | 12 | no_std ROS 2 클라이언트 — 마이크로컨트롤러/RTOS에서 ROS2 사용 가능 |
| **thun-res/vlink** | 123 | 고성능 C++ 통신 미들웨어 — 자율주행/드론 간 저지연 통신 |

## 5. 헌터킬러 Applications 적용

### 5.1 객체 추적 + 제어 루프

헌터킬러 드론의 핵심 루프는 인지 → 추적 → 제어의 실시간 파이프라인입니다:

```
Camera → YOLOv8 → DeepSORT → PX4 ROS2 Bridge → Trajectory Setpoint → EKF2
                                    ↓
                              Human-in-the-loop (PreArm gate)
```

### 5.2 GNSS-Denied 환경 적용

GNSS-실패 환경에서 헌터킬러 드론은 비전 기반 항법을 사용합니다:

```bash
# VIO + YOLOv8 융합 런치
ros2 launch vio_yolo_tracking vio_yolo.launch.py

# EKF2 파라미터 (Vision + Optical Flow 강제 사용)
param set EKF2_AID_MASK 10       # Vision + Flow
param set EKF2_GPS_ID 0          # GPS 비활성화
```

관련 프로젝트: `Sreejith-nair511/GNSS-Denied-UAV` (1 ⭐, 2026-07-19) — ROS2 + PX4 + SLAM + 컴퓨터비전 + AI 미션.

### 5.3 안전/방어 메커니즘

헌터킬러 시스템에서는 다음 안전 계층이 필수적입니다:

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

Nav2 (4,532 ⭐)는 `Enhanced Safety` 기능을 제공합니다:

- **Collision Monitor**: 실시간 장애물 감지 및 회피
- **3Laws Supervisor**: 인명 보호 우선순위 기반 안전 강화 (상용 라이선스 필요)

```bash
# Collision Monitor 설정
ros2 run nav2_collision_monitor collision_monitor_node
```

### 5.5 신규 헌터킬러 관련 프로젝트 (2026-08-02)

| 프로젝트 | ⭐ | 설명 |
|----------|----|------|
| **yasincavusoglu/ros2-counter-uav-turret** | 1 | ROS2 기반 자율 counter-UAS(반드론) 포탑 — detection + tracking + turret 제어 |
| **JacopoPan/aerial-autonomy-stack** | 549 | PX4/ArduPilot 스웜용 인지 기반 자율주행 프레임워크 — 헌터킬러 스웜에 직접 적용 가능 |

## 6. 배포판 및 생태계

### 6.1 PX4 배포판 현황

| 버전 | 상태 | 출시일 | 비고 |
|------|------|--------|------|
| **v1.18.0-beta1** | prerelease | 2026-07-08 | 최신 베타 — v1.17 기능 유지 + 추가 개선 |
| **v1.18.0-alpha1** | prerelease | 2026-05-13 | 알파 |
| **v1.17.0** | stable | 2026-05-13 | Altitude Cruise, Zenoh rmw_zenoh, 고정-wing/rover ROS2 제어 |

### 6.2 ArduPilot 배포판 현황

| 버전 | 상태 | 출시일 | 비고 |
|------|------|--------|------|
| **Tracker-4.7.0** | stable | 2026-07-27 | 탐색기/트래커용 |
| **Sub-4.7.0** | stable | 2026-07-27 | 잠수정용 |
| **Rover-4.7.0** | stable | 2026-07-27 | 육상/보트용 |

### 6.3 ROS2 배포판 현황

| 배포판 | 코드명 | 상태 | 비고 |
|--------|--------|------|------|
| **Humble Hawksbill** | `humble` | 유지보수 중 | 2026년 기준 아직 지원 |
| **Jazzy Jalisco** | `jazzy` | 현재 LTS | 기본 권장 |
| **Kilted Kaiju** | `kilted` | 최신 | May 2025 출시 |
| **Lyrical Luth** | `lyrical` | 최신 | May 2026 출시 (latest) |
| **Makoa Mata-mā** | `makoa` | 개발 중 | May 2027 예정 |

## 7. 결론

2026년 8월 2일 기준, ROS2 기반 드론 생태계는 다음과 같이 발전하고 있습니다:

1. **인지**: YOLOv8 + DeepSORT + MediaPipe 가 객체 검출/추적의 산업 표준
2. **제어**: PX4 v1.18.0-beta1의 ROS2 브리지 개선과 고수준 제어 인터페이스로 시스템 통합 용이 — v1.17의 Zenoh rmw_zenoh, 고정-wing/rover 제어 기능 유지
3. **미들웨어**: Zenoth이 DDS의 실시간성 한계를 보완, 멀티-드론 확장성 강조. 새로운 zenoh-plugin-ros2dds(292⭐), agnocast(195⭐), vlink(123⭐)가 통신 미들웨어 다양화
4. **안전**: PX4의 PreArm/Kill-Switch/Geofence와 Nav2의 Collision Monitor/3Laws Supervisor가 헌터킬러 applications의 안전 계층을 제공
5. **GNSS-Denied**: VIO + SLAM + OpenCV ArUco 조합으로 GNSS-실패 환경 대응 능력 향상
6. **신규 트렌드**: counter-UAS(반드론) 프로젝트 출현, no_std ROS 2 클라이언트(nano-ros)로 마이크로컨트롤러 기체 지원 확대, zero-copy IPC(agnocast)로 통신 지연 추가 감소

> **핵심 권장사항 (헌터킬러용)**:
> - PX4 v1.18.0-beta1의 Zenoth + ROS2 브리지를 프로토타입 단계에서 검증
> - `COM_PREARM=1`, `COM_KILL=1` 안전 파라미터를 반드시 활성화
> - GNSS-Denied 환경에서는 EKF2 Vision+Flow 모드(`EKF2_AID_MASK=10`) 사용
> - Nav2의 Collision Monitor와 3Laws Supervisor를 레이어링하여 인명 보호
> - counter-UAS 응용을 위한 `yasincavusoglu/ros2-counter-uav-turret` 참고
> - 멀티-드론 통신에는 Zenoth(저지연) 또는 agnocast(zero-copy) 고려
