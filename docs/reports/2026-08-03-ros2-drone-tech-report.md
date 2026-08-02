---
title: "ROS2 기반 드론 최신 기술 보고서 (2026-08-03)"
created: 2026-08-03
updated: 2026-08-03
type: report
tags: [uav, ros2, detection, control, middleware]
sources:
  - ('raw/articles/2026-08-03-ros2-drone-github-data.md', '1d570b6a3d46a0af0eaf74d1310a8ae720c5fecb50db64faa2a36151822de37d')
  - ('raw/articles/2026-08-03-px4-release-notes.md', '2dfa85f087715e34e002a191b3c792992c520fdbe27756c7318d7c8be4c5e036')
  - ('raw/articles/2026-08-03-ardupilot-release-notes.md', '5c3bcd3fedbfafa88ab1b0658aec9d43594dc4926b3b3a1b0b338b8ff9911929')
  - ('raw/articles/2026-08-03-px4-docs-main.md', '2d880287b3761adc98aaed73c1461edc5e35f2a4c2b91dfd9b052cbcc03bf52e')
  - ('raw/articles/2026-08-03-ros2-docs-rolling.md', 'cc09a31de54c98b03c8cb09610c99d77b427204a67b0b05824904ae873394b85')
confidence: high
contested: false
contradictions: []
---

> 📎 **출처**: `('raw/articles/2026-08-03-ros2-drone-github-data.md', '1d570b6a3d46a0af0eaf74d1310a8ae720c5fecb50db64faa2a36151822de37d')`, `('raw/articles/2026-08-03-px4-release-notes.md', '2dfa85f087715e34e002a191b3c792992c520fdbe27756c7318d7c8be4c5e036')`, `('raw/articles/2026-08-03-ardupilot-release-notes.md', '5c3bcd3fedbfafa88ab1b0658aec9d43594dc4926b3b3a1b0b338b8ff9911929')`, `('raw/articles/2026-08-03-px4-docs-main.md', '2d880287b3761adc98aaed73c1461edc5e35f2a4c2b91dfd9b052cbcc03bf52e')`, `('raw/articles/2026-08-03-ros2-docs-rolling.md', 'cc09a31de54c98b03c8cb09610c99d77b427204a67b0b05824904ae873394b85')`

# ROS2 기반 드론 최신 기술 보고서 (2026-08-03)

## 1. 핵심 패키지 (GitHub ⭐ 기준 top 5)

| 순위 | 패키지 | ⭐ | 설명 | 마지막 커밋 |
|------|--------|----|------|-------------|
| 1 | **JacopoPan/aerial-autonomy-stack** | ⭐ 549 | An open framework to simulate and deploy perception-based PX4/ArduPilot drone sw | 2026-08-02 |
| 2 | **eclipse-zenoh/zenoh-plugin-ros2dds** | ⭐ 292 | A Zenoh plug-in for ROS2 with a DDS RMW. See https://discourse.ros.org/t/ros-2-a | 2026-08-02 |
| 3 | **autowarefoundation/agnocast** | ⭐ 195 | A rclcpp-compatible true zero-copy IPC middleware that supports all ROS message  | 2026-07-31 |
| 4 | **thun-res/vlink** | ⭐ 123 | VLink is a high-performance C++ communication middleware for autonomous driving  | 2026-08-01 |
| 5 | **csi-dgist/ros2probe** | ⭐ 78 | Host-level observability for ROS 2 middleware traffic, without creating any ROS  | 2026-07-21 |

### 주목할 만한 신규/업데이트 리포지토리

| 리포지토리 | ⭐ | 푸시일 | 설명 |
|------------|----|--------|------|
| **yasincavusoglu/ros2-counter-uav-turret** | ⭐ 1 | 2026-07-28 | Autonomous counter-UAS (anti-drone) turret simulation in ROS 2: detection, track |
| **oussamaelmessaoudi/uav-precision-landing** | ⭐ 0 | 2026-07-16 | Autonomous UAV precision landing system using nested AprilTag visual detection,  |
| **NoahClouser/autonomous-drone** | ⭐ 0 | 2026-07-01 | Autonomous quadrotor in Gazebo simulation using ROS2. C++ flight controller at 1 |
| **hayatPMT/Autonomous-UAV-Navigation-System** | ⭐ 8 | 2026-07-27 | 🛸 Navigate urban environments with this autonomous UAV system using real-time oc |
| **aravindsairam/auto-drone** | ⭐ 0 | 2026-07-19 | ROS2/PX4 text-to-drone autonomous navigation platform with Safety Kernel |
| **Sreejith-nair511/GNSS-Denied-UAV** | ⭐ 1 | 2026-07-19 | An autonomous drone navigation system featuring ROS2, PX4, SLAM, computer vision |
| **madhukarkalyan40-dev/vision-guided-autonomous-drone** | ⭐ 0 | 2026-07-17 | Vision-Guided Autonomous Drone System for Aerial Crowd Monitoring and Adaptive N |

## 2. 객체인식 기술 (YOLOv8 / MediaPipe / ArUco)

### 2.1 YOLOv8 + ROS2

YOLOv8은 ROS2 드론 인지 스택의 표준으로 자리 잡고 있습니다.
- **somikm-robotics/multi-agent-hazard-detection** (⭐ 0): ``` Multi-agent ROS2 system for autonomous hazard detection in ore mining — aerial drone, ground rob
- **Seonghunpp/ros2-patrol-fall-detection-v2** (⭐ 0): TurtleBot3 병실 순찰 로봇 v2 — Nav2 자율 순찰, ArUco 병실 인식, 자체 학습 YOLOv8-pose 낙상 감지 + 웹 대시보드수정·DB·앱 추가

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

### 2.2 MediaPipe + ROS2

MediaPipe는 실시간 자세 추정과 제스처 제어에 사용됩니다.
- **Apsara-kaiser/-Gesture-Control-Robot** (⭐ 0): A ROS 2-based gesture-controlled robot using OpenCV and MediaPipe for real-time hand gesture recogni
- **tchoopojcharoen/mediapipe_control** (⭐ 1): A ROS2 package for mediapipe gesture control incorporating MEKF for estimating feedforward twist inp
- **flowercastle/ros2-gesture-gazebo-arm** (⭐ 0): ROS 2 and Gazebo Sim robotic arm controlled by MediaPipe hand gestures

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

### 2.3 ArUco / OpenCV

OpenCV는 ArUco 마커 검출과 비전 기반 항법에 사용됩니다.
- **madhukarkalyan40-dev/vision-guided-autonomous-drone** (⭐ 0): Vision-Guided Autonomous Drone System for Aerial Crowd Monitoring and Adaptive Navigation using ROS2

### 2.4 SLAM + ROS2

- **jiyak2804/uav-ros2-multidrone-slam** (⭐ 0): ROS2 multi-drone SLAM simulation using PX4 SITL, Gazebo Harmonic, LiDAR and SLAM Toolbox.
- **aadhi4200/autonomous_drone_perception_slam-** (⭐ 0): Autonomous delivery drone — ROS2 Humble + PX4 SITL + ArUco precision landing + SLAM 

## 3. 제어 인터페이스 (PX4 ROS2 Bridge)

### 3.1 PX4 v1.18.0-beta1 (2026-07-08, prerelease)

**주요 변경사항:**
- Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.17.0-alpha1...v1.18.0-beta1

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

### 3.3 헌터킬러용 안전/방어 제어 인터페이스

PX4의 안전 메커니즘 강화를 위한 핵심 파라미터입니다:

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

### 4.1 Zenoh (PX4 v1.17/v1.18)

Zenoh은 PX4 v1.17에서 `rmw_zenoh` 호환성을 획득했습니다. ROS2 토픽을 Zenoh 세션으로 브리지하여 저지연·고확장성 통신을 제공합니다.

```bash
# Zenoh 세션 생성
ros2 run rmw_zenoh zenohd --config /path/to/zenoh.json5

# 토픽 구독 (Zenoh 브리지)
ros2 topic echo /zenoh/vehicle_local_position
```

### 4.2 Zenoh 관련 프로젝트

- **eclipse-zenoh/zenoh-plugin-ros2dds** (⭐ 292): A Zenoh plug-in for ROS2 with a DDS RMW. See https://discourse.ros.org/t/ros-2-alternative-middlewar

### 4.3 DDS vs Zenoh 비교

| 항목 | DDS (FastRTPS/Cyclone) | Zenoh |
|------|------------------------|-------|
| **지연** | ~10ms | ~2ms |
| **확장성** | 제한적 (Discovery 프로토콜) | 높음 (라우팅 기반) |
| **ROS 2 호환성** | 완벽 (표준) | experimental |
| **멀티드론 설정** | 복잡 (QoS, Domain ID) | 간단 (Domain ID + bridge) |
| **중개자 의존성** | 없음 | Zenoh 라우터 권장 |

### 4.4 ROS2 배포판 현황

| 배포판 | 코드명 | 상태 | 비고 |
|--------|--------|------|------|
| **Humble Hawksbill** | `humble` | 유지보수 중 | 2026년 기준 아직 지원 |
| **Jazzy Jalisco** | `jazzy` | 현재 LTS | 기본 권장 |
| **Kilted Kaiju** | `kilted` | 최신 | May 2025 출시 |
| **Lyrical Luth** | `lyrical` | 최신 | May 2026 출시 (latest) |
| **Makoa Mata-mā** | `makoa` | 개발 중 | May 2027 예정 |

## 5. 헌터킬러 Applications 적용

### 5.1 Counter-UAS (반드론) 프로젝트

- **yasincavusoglu/ros2-counter-uav-turret** (⭐ 1): Autonomous counter-UAS (anti-drone) turret simulation in ROS 2: detection, tracking, 6D Kalman, lead
- **yasincavusoglu/ros2-counter-uav-turret** (⭐ 1): Autonomous counter-UAS (anti-drone) turret simulation in ROS 2: detection, tracking, 6D Kalman, lead

### 5.2 군집(Swarm) 관련 프로젝트

- **somikm-robotics/multi-agent-hazard-detection** (⭐ 0): ``` Multi-agent ROS2 system for autonomous hazard detection in ore mining — aerial drone, ground rob

### 5.3 헌터킬러 인지→추적→제어 파이프라인

헌터킬러 드론의 핵심 루프는 인지 → 추적 → 제어의 실시간 파이프라인입니다:

```
Camera → YOLOv8 → DeepSORT → PX4 ROS2 Bridge → Trajectory Setpoint → EKF2
                                    ↓
                              Human-in-the-loop (PreArm gate)
```

### 5.4 GNSS-Denied 환경 적용

GNSS-실패 환경에서 헌터킬러 드론은 비전 기반 항법을 사용합니다:

```bash
# VIO + YOLOv8 융합 런치
ros2 launch vio_yolo_tracking vio_yolo.launch.py

# EKF2 파라미터 (Vision + Optical Flow 강제 사용)
param set EKF2_AID_MASK 10       # Vision + Flow
param set EKF2_GPS_ID 0          # GPS 비활성화
```

### 5.5 안전/방어 계층 (헌터킬러 필수)

헌터킬러 시스템에서는 다음 안전 계층이 반드시 포함되어야 합니다:

| 계층 | 메커니즘 | 구현 |
|------|----------|------|
| **인간 승인 게이트** | PreArm 승인 | `COM_PREARM=1` + `/fmu/in/prearm` 토픽 |
| **Kill-Switch** | 즉시 정지 | `COM_KILL=1` + `/fmu/in/kill` 토픽 |
| **통신 손실** | RC/GCS 손실 감지 | `COM_DL_LOSS_T` (기본 5초) |
| **배터리 실패** | 크리티컬 배터리 | `BAT_CRIT_THR` (기본 20%) |
| **지오펜스** | 영역 제한 | `GF_MAX_HOR_DIST`, `GF_MAX_VER_DIST` |
| **비행 종료** | 긴급 추진불능 | `COM_FLIGHT_TERM_ACT=1` |
| **복구 모드** | 지정위치 복귀 | `RTL` 모드 + Safe Points (Rally) |

## 6. 결론

2026-08-03 기준, ROS2 기반 드론 생태계는 다음과 같이 발전하고 있습니다:

1. **인지**: YOLOv8 + DeepSORT + MediaPipe 가 객체 검출/추적의 산업 표준
2. **제어**: PX4의 ROS2 브리지 개선과 고수준 제어 인터페이스로 시스템 통합 용이
3. **미들웨어**: Zenoth이 DDS의 실시간성 한계를 보완, 멀티-드론 확장성 강조
4. **안전**: PX4의 PreArm/Kill-Switch/Geofence와 Nav2의 Collision Monitor가 헌터킬러 applications의 안전 계층을 제공
5. **GNSS-Denied**: VIO + SLAM + OpenCV ArUco 조합으로 GNSS-실패 환경 대응 능력 향상
6. **신규 트렌드**: counter-UAS(반드론) 프로젝트 출현, zero-copy IPC(agnocast)로 통신 지연 추가 감소

> **핵심 권장사항 (헌터킬러용)**:
> - PX4의 Zenoth + ROS2 브리지를 프로토타입 단계에서 검증
> - `COM_PREARM=1`, `COM_KILL=1` 안전 파라미터를 반드시 활성화
> - GNSS-Denied 환경에서는 EKF2 Vision+Flow 모드(`EKF2_AID_MASK=10`) 사용
> - Nav2의 Collision Monitor를 레이어링하여 인명 보호
> - 멀티-드론 통신에는 Zenoth(저지연) 또는 agnocast(zero-copy) 고려
