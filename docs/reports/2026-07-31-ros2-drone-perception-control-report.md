---
title: "ROS2 기반 드론 디텍션/객체인식/제어 종합 보고서"
created: 2026-07-31
updated: 2026-07-31
type: report
tags: [uav, ros2, detection, object-recognition, control]
sources:
  - raw/articles/2026-07-31-ros2-drone-packages.md
  - raw/articles/2026-07-31-px4-ardupilot-release-comparison.md
confidence: high
contested: false
contradictions: []
---

# ROS2 기반 드론 디텍션/객체인식/제어 종합 보고서

> 📎 **출처**: `raw/articles/2026-07-31-ros2-drone-packages.md`, `raw/articles/2026-07-31-px4-ardupilot-release-comparison.md`

## 1. 개요

ROS2 기반 드론 시스템은 **인지 + 제어** 통합 스택으로 발전하고 있습니다.
2026년 7월 기준, **YOLOv8/Mediapipe 객체인식**, **PX4 ROS2 브릿지**, **Zenoh 미들웨어**가
핵심 기술로 떠오르고 있습니다.

## 2. 핵심 ROS2 드론 패키지

| 패키지 | 설명 | GitHub | ⭐ |
|--------|------|--------|-----|
| **PX4-Autopilot** | 공식 PX4 ROS2 브릿지, MAVLink 통신 | [PX4/PX4-Autopilot](https://github.com/PX4/PX4-Autopilot) | 12,306 |
| **PX4-ROS2-Gazebo-YOLOv8** | YOLOv8 객체인식 + Gazebo 시뮬레이션 | [monemati/...](https://github.com/monemati/PX4-ROS2-Gazebo-YOLOv8) | 390 |
| **aerial-autonomy-stack** | 인지 기반 항공 자율주행 프레임워크 | [JacopoPan/...](https://github.com/JacopoPan/aerial-autonomy-stack) | 547 |
| **CarlaAir** | CARLA 시뮬레이션 드론 | [louiszengCN/...](https://github.com/louiszengCN/CarlaAir) | 1,054 |
| **turtlebot3** | 드론용이 아니지만 ROS2 인지 패키지 참조용 | [ROBOTIS-GIT/...](https://github.com/ROBOTIS-GIT/turtlebot3) | 7,200+ |

## 3. 객체인식 (Detection / Object Recognition)

### 3.1 YOLOv8 + ROS2
```bash
# 설치
pip install ultralytics
ros2 run vision_opencv yolov8_node --ros-args -p model_path:=yolov8s.pt

# 토픽 구독
ros2 topic echo /detectron2/object_recognition
```

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `model_path` | YOLOv8 모델 경로 | `yolov8s.pt` |
| `confidence_threshold` | 신뢰도 임계값 | 0.5 |
| `nms_threshold` | NMS 임계값 | 0.45 |
| `input_size` | 입력 이미지 크기 | 640 |
| `device` | 연산 장치 | `cuda:0` or `cpu` |

### 3.2 MediaPipe + ROS2
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

### 3.3 인지 파이프라인 (Aerial-Autonomy-Stack)
```
Camera → [YOLOv8] → [DeepSORT] → [Kalman Filter] → [Trajectory Prediction]
```

| 단계 | 기술 | 파라미터 |
|------|------|----------|
| **1. 검출** | YOLOv8 | `yolo_conf`, `yolo_iou` |
| **2. 추적** | DeepSORT | `deepsort_max_age`, `deepsort_n_init` |
| **3. 예측** | Kalman Filter | `kf_process_noise`, `kf_measurement_noise` |
| **4. 경로 예측** | LSTM | `lstm_seq_len`, `lstm_hidden_dim` |

## 4. 제어 (Control)

### 4.1 PX4 ROS2 브릿지
```bash
# 설치 및 실행
ros2 run px4_ros_com vehicle_pose_ekf
ros2 run px4_ros_com vehicle_local_position_publisher

# 토픽
ros2 topic echo /fmu/out/vehicle_local_position
ros2 topic echo /fmu/out/vehicle_local_position_setpoint
```

| 토픽 | 설명 | 사용법 |
|------|------|--------|
| `/fmu/out/vehicle_local_position` | 현재 위치 | `px4_msgs::msg::VehicleLocalPosition` |
| `/fmu/in/trajectory_setpoint` | 목표 궤적 | `px4_msgs::msg::TrajectorySetpoint` |
| `/fmu/out/vehicle_status` | 드론 상태 | `px4_msgs::msg::VehicleStatus` |

### 4.2 ROS2 제어 인터페이스
```bash
# 제어 명령 발행
ros2 topic pub /fmu/in/trajectory_setpoint trajectory_setpoint_interfaces/msg/TrajectorySetpoint "{x: 0.0, y: 0.0, z: -5.0}"
```

| 인터페이스 | 설명 |
|------------|------|
| `FwLateralLongitudinalSetpointType` | Fixed-Wing 제어 (PX4 v1.17) |
| `RoverSetpointTypes` | Rover 제어 (PX4 v1.17) |
| `GeometrySetpoint` | 일반적인 위치/자세 제어 |

### 4.3 안전/방어 제어 (Hunter-Killer용)
```bash
# 인간 승인 게이트
param set COM_PREARM 1  # PreArm 승인 필수

# Kill-Switch
param set COM_KILL 1  # 즉시 정지

# GNSS-Denied 모드
param set EKF2_AID_MASK 10  # Vision + Flow 활성화
```

## 5. 미들웨어 (Middleware)

### 5.1 Zenoh (PX4 v1.17)
```bash
# Zenoh 세션 생성
ros2 run rmw_zenoh zenohd --config /path/to/zenoh.json5

# 토픽 구독
ros2 topic echo /zenoh/vehicle_local_position
```

| 기능 | 설명 |
|------|------|
| **CDRv1 직렬화** | 데이터 효율적 전송 |
| **ROS 2 그래프 활성성** | 노드 간 연결 상태 모니터링 |
| **Domain ID** | 네트워크 분리 (다중 드론) |

### 5.2 DDS vs Zenoh 비교
| 항목 | DDS (FastRTPS) | Zenoh |
|------|----------------|-------|
| **지연** | ~10ms | ~2ms |
| **확장성** | 제한적 | 높음 ( multicast) |
| **ROS 2 호환성** | 완벽 | experimental |
| **멀티드론** | 복잡한 설정 | 간단 (Domain ID) |

## 6. 시뮬레이션 (Simulation)

### 6.1 Gazebo + ROS2
```bash
# 시뮬레이션 실행
ros2 launch px4_ros2_sim drag_x500_moving_obstacles.sdf

# 드론 스폰
ros2 service call /spawn_entity gazebo_msgs/srv/SpawnEntity "{model_name: 'drone', x: 0, y: 0}"
```

### 6.2 CARLA (CarlaAir)
```bash
# CARLA 실행
python CarlaAir/carla/run_carla.py --world-port 2000

# 드론 제어
ros2 topic pub /carla/drone/control carla_msgs/msg/CarlaEgoVehicleControl "{throttle: 0.5, steer: 0.0}"
```

| 시뮬레이터 | 장점 | 단점 |
|------------|------|------|
| **Gazebo** | PX4 공식 지원, 물리 엔진 정확 | 무겁고 느림 |
| **CARLA** | 도시 환경, 실제 센서 시뮬 | 드론 지원 제한 |
| **AirSim** | Microsoft, 고품질 그래픽 | 유지보수 중단 위험 |

## 7. 헌터킬러 applications 적용

### 7.1 객체 추적 + 제어 루프
```
Camera → YOLOv8 → DeepSORT → PX4 ROS2 Bridge → Trajectory Setpoint
```

### 7.2 GNSS-Denied 추적
```bash
# VIO + YOLOv8 융합
ros2 launch vio_yolo_tracking vio_yolo.launch.py

# 파라미터
param set EKF2_AID_MASK 10  # Vision + Flow
param set EKF_USES_GPS_NOT_FLOW 1  # Flow 강제 사용
```

### 7.3 안전 메커니즘
| 기능 | ROS2 토픽 | PX4 파라미터 |
|------|-----------|--------------|
| **인간 승인** | `/fmu/in/prearm` | `COM_PREARM` |
| **Kill-Switch** | `/fmu/in/kill` | `COM_KILL` |
| **통신 손실** | `/fmu/out/vehicle_status` | `COM_DL_LOSS_T` |
| **배터리 실패** | `/fmu/out/battery_status` | `BAT_CRIT_THR` |

## 8. 결론

ROS2 기반 드론 시스템은 **YOLOv8 + DeepSORT 객체인식**과 **PX4 ROS2 브릿지**가
핵심이며, **Zenoh 미들웨어**로 멀티드론 확장성을 높이고 있습니다.
헌터킬러 applications에서는 **GNSS-Denied 환경**에서의 **VIO + YOLOv8 추적**과
**안전 메커니즘** (PreArm, Kill-Switch)이 필수적입니다.
