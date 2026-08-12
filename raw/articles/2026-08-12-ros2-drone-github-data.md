---
source_url: "https://docs.github.com/en/rest/search"
ingested: 2026-08-12
sha256: fa51f9ef7e75a96bdd72b0a9615922a5de516766514a83629a1354c1515619d5
title: "ROS2 드론 GitHub 검색 데이터 (2026-08-12)"
captured_via: 2nd-brain-cron
search_queries: "9 queries via GitHub Search API"
---
# ROS2 드론 관련 GitHub 저장소 검색 결과 (2026-08-12)

수집 일시: 2026-08-12
수집 방법: GitHub Search API (gh cli 사용, 인증 정보: github.com)

## 1. 검색 쿼리 목록

| # | 검색어 | 정렬 기준 | 결과 수 |
|---|--------|-----------|---------|
| 1 | `ros2 drone autonomous navigation` | stars desc | 10개 |
| 2 | `px4 bridge ros2` | stars desc | 10개 |
| 3 | `yolo ros2 drone` | stars desc | 10개 |
| 4 | `zenoh ros2 drone` | stars desc | 10개 |
| 5 | `mediapipe ros2 drone` | stars desc | 10개 |
| 6 | `ros2 slam drone` | stars desc | 10개 |
| 7 | `ros2 aruco drone` | stars desc | 10개 |
| 8 | `px4 gazebo ros2 simulation` | stars desc | 10개 |

## 2. 핵심 패키지 (GitHub ⭐ 기준 top 5)

### 2-1. ros2 drone autonomous navigation (⭐ 50+)

| 저장소 | ⭐ | 언어 | 설명 | 최근 업데이트 |
|--------|-----|------|------|---------------|
| JacopoPan/aerial-autonomy-stack | 561 | C++ | Perception-based PX4/ArduPilot drone swarms with ROS2, YOLO, LiDAR, NVIDIA Jetson | 2026-08-09 |
| monemati/PX4-ROS2-Gazebo-YOLOv8 | 392 | Python | Aerial object detection using PX4 Autopilot + ROS2 + Gazebo + YOLOv8 | 2026-02-20 |
| tentone/tello-ros2 | 213 | C++ | DJI Tello ROS2 driver with Visual SLAM for indoor mapping | 2024-04-23 |
| andy-zhuo-02/XTDrone2 | 106 | Python | PX4 + ROS2 + Gazebo Ignition 기반의 일반 UAV 시뮬레이션 플랫폼 | 2025-08-02 |
| Ajinkya-001/Autonomous-UAV-Navigation-System | 50 | Python | 실시간 2.5D occupancy-grid mapping, A* 글로벌 경로 계획, depth+LiDAR 센서 융합 | 2026-03-05 |

### 2-2. PX4 bridge ros2 (⭐ 20+)

| 저장소 | ⭐ | 언어 | 설명 | 최근 업데이트 |
|--------|-----|------|------|---------------|
| PX4/px4_ros_com | 221 | C++ | ROS2/ROS interface with PX4 through a Fast-RTPS bridge | 2025-11-21 |
| limshoonkit/uosm.isaac.px4_bridge | 30 | Jupyter | NVIDIA Omniverse Extension for PX4-Autopilot | 2025-06-09 |
| StanfordMSL/TrajBridge | 13 | Jupyter | ROS2 bridge for Stanford Flightroom (quadcopter trajectory → PX4 setpoints) | 2024-10-22 |
| mohshibinroshankt/drl_drone_px4 | 12 | Python | SAC + Prioritized Experience Replay 기반 ROS2 자율 드론 (PX4+Gazebo) | 2025-08-21 |
| AndyBlightLeeds/px4-ros2-drone-simulation | 10 | C++ | PX4-FastRTPS bridge로 ROS2 프로그램이 드론 제어 (Gazebo 시뮬레이션) | 2020-10-05 |

### 2-3. yolo ros2 drone (⭐ 30+)

| 저장소 | ⭐ | 언어 | 설명 | 최근 업데이트 |
|--------|-----|------|------|---------------|
| JacopoPan/aerial-autonomy-stack | 561 | C++ | (중복) YOLO + LiDAR 기반 드론 스웜 | 2026-08-09 |
| monemati/PX4-ROS2-Gazebo-YOLOv8 | 392 | Python | (중복) YOLOv8 실시간 객체 감지 (PX4+SITL+Gazebo) | 2026-02-20 |
| eOvic/PX4-ROS2-SLAM-Control | 44 | Python | PX4 + ROS2 Jazzy + Gazebo + RL environments + YOLO 기반 인지 | 2025-09-14 |
| Masudali23/PX4-Iris-Drone-Path-Planning-CV | 15 | Python | YOLO 기반 weed 감지 + MAVROS + ROS2 | 2024-10-07 |
| SezginAtabas/ros2-auto-drone | 13 | Python | NVIDIA Jetson 최적화 객체 감지 및 추적 | 2025-04-17 |

### 2-4. ros2 slam drone (⭐ 20+)

| 저장소 | ⭐ | 언어 | 설명 | 최근 업데이트 |
|--------|-----|------|------|---------------|
| tentone/tello-ros2 | 213 | C++ | (중복) Visual SLAM 기반 실내 지도 작성 | 2024-04-23 |
| yidrone/AstraDroneOpen | 77 | C++ | Open ROS/PX4 기반 연구용 UAV 플랫폼 | 2026-07-20 |
| LegendLeoChen/LeoDrone | 62 | Python | Ubuntu22.04 + ROS2 Humble 시각 SLAM | 2025-01-20 |
| eOvic/PX4-ROS2-SLAM-Control | 44 | Python | (중복) SLAM + YOLO + 2D lidar | 2025-09-14 |
| monemati/RTABMap-ROS2-PX4 | 12 | Python | RTAB-Map SLAM on x500 drone (PX4 SITL) | 2025-10-06 |

### 2-5. ros2 aruco drone (⭐ 10+)

| 저장소 | ⭐ | 언어 | 설명 | 최근 업데이트 |
|--------|-----|------|------|---------------|
| machmind-dev/drone-swarm-challenge-2026 | 27 | C++ | Swarm Drone Challenge 2026 소스 코드 | 2026-06-13 |
| REGATTE/Aruco_Tracker_ROS2_Drones | 17 | Python | ROS2 + 컴퓨터 비전 기반 정밀 착륙 | 2023-11-27 |
| SpaceMaster85/precision_landing | 4 | C++ | ArUco 마커 감지 + PX4 OFFBOARD 제어 | 2025-10-11 |
| zceyda/ros2-humble-drone-aruco-landing | 2 | Python | ArUco 마커 감지 기반 자율 착륙 (Gazebo) | 2025-08-26 |
| lokeshkarthi-dev/precision-landing-PX4 | 2 | Python | MAVSDK + ArUco + OFFBOARD (PX4+ROS2+Gazebo) | 2026-05-04 |

## 3. Zenoh 미들웨어 관련

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| JacopoPan/aerial-autonomy-stack | 561 | Zenoh inter-vehicle ROS2 bridge 사용 (eclipse-zenoh/zenoh-plugin-ros2dds) |
| toppers/hakoniwa-digital-twin | 9 | 가상 드론과 실로봇이 Hakoniwa 프레임워크를 통해 데이터 공유 (Zenoh 기반) |

Zenoh 검색 결과는 제한적 (9개 스타). aerial-autonomy-stack가 Zenoh inter-vehicle bridge를 공식 지원 중.

## 4. MediaPipe 관련

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| ali-celenoglu/MediaPipe-ROS2-PX4-Control | 0 | MediaPipe + MAVSDK + PX4 + Gazebo 손동작 드론 제어 |
| Qxy661/drone-gesture | 0 | MediaPipe 손동작 인식 + ROS2 + MAVROS 상태기계 |
| Qxy661/drone-gesture-control | 0 | MediaPipe + ROS2 + MAVROS + ArduCopter |

MediaPipe 통합은 아직 초기 단계 (모든 저장소 0스타, 2026년 5~6월 최근 업데이트).

## 5. 저장소 상세 메타데이터 (Top 8)

### JacopoPan/aerial-autonomy-stack
- ⭐ 561 | 생성: 2025-06-20 | 언어: C++
- 토픽: ardupilot, drone, fixed-wing, gazebo, gymnasium, hitl, jetpack, lidar, multi-agent, offboard, orin, px4, quadrotor, ros2, simulation, swarm, tailsitter, uav, vtol, yolo
- README 요약: "batteries included" 다중 드론 자율화 프레임워크. PX4/ArduPilot + ROS2 + YOLO + 3D LiDAR + NVIDIA Jetson. Docker화 시뮬레이션과 배포, Windows 11 WSL 지원, Jetson-in-the-loop HITL, Zenoh inter-vehicle bridge, PX4 Offboard 인터페이스.

### monemati/PX4-ROS2-Gazebo-YOLOv8
- ⭐ 392 | 생성: 2023-09-09 | 언어: Python
- 토픽: docker, dockerfile, drone, gazebo, gz, gz-garden, gz-harmonic, object-detection, px4, px4-autopilot, px4-ros2-gazebo, pygame, ros, ros2, ros2-humble, simulation, sitl, uav, yolo, yolov8
- README 요약: PX4 SITL + Gazebo Garden + YOLOv8 실시간 객체 감지. 2축 짐벌 카메라 제어, Docker GPU passthrough, tmuxinator 6-pane orchestration.

### PX4/px4_ros_com
- ⭐ 221 | 생성: 2018-07-30 | 언어: C++
- 토픽: 없음
- README 요약: ROS2와 PX4 간 데이터/명령 교환용 예제 노드. uXRCE-DDS 브릿지 사용. px4_msgs 패키지 의존.

### tentone/tello-ros2
- ⭐ 213 | 생성: 2020-11-04 | 언어: C++
- 토픽: dji-tello, dji-tello-edu, drone, ros-foxy, ros2, slam
- README 요약: DJI Tello 드론용 ROS2 드라이버. 다중 드론 스웜 지원, ORB SLAM2 통합 가능, 30hz 카메라/IMU/오도메트리 토픽 제공.

### andy-zhuo-02/XTDrone2
- ⭐ 106 | 생성: 2024-12-30 | 언어: Python
- 토픽: 없음
- README 요약: PX4 + ROS2 + Gazebo Ignition 기반 일반 UAV 시뮬레이션 플랫폼. ROS1에서 ROS2로 마이그레이션 중. MIT 라이선스.

### eOvic/PX4-ROS2-SLAM-Control
- ⭐ 44 | 생성: 2025-09-13 | 언어: Python
- 토픽: drl, drone, gazebo, lidar, px4, px4-autopilot, reinforcement-learning, rgbd, rl, robotics, ros2, ros2-jazzy, slam, uav, yolo
- 설명: PX4 + ROS2 Jazzy + Gazebo Harmonic + RL environments + YOLO 기반 인지 + 2D lidar.

### Ajinkya-001/Autonomous-UAV-Navigation-System
- ⭐ 50 | 생성: 2025-12-10 | 언어: Python
- 토픽: astar-algorithm, autonomous-drones, autonomous-flight, depthcamera, drone, lidar, obstacle-avoidance, occupancy-grid-map, path-planning, px4-autopilot, python3, robotics, ros2, sensorfusion, simulation, uav, voxel-mapping
- 설명: 실시간 2.5D occupancy-grid mapping, A* 글로벌 경로 계획, depth+LiDAR 센서 융합. ROS2 + PX4 Offboard + Gazebo 완전 통합.

### ahmedeltaher/Autonomous-drone-navigation
- ⭐ 38 | 생성: 2025-11-20 | 언어: Python
- 토픽: autonomous-navigation, computer-vision, drone, gps-denied, indoor-navigation, lidar, mavsdk, multirotor, optical-flow, px4, raspberry-pi, ros2, sensor-fusion, slam, uav
- 설명: GPS 없이 실내 자율 비행. 광학 흐름 + IMU + LiDAR 센서 융합, 실시간 SLAM, 장애물 회피, 웨이포인트 미션. Raspberry Pi.

## 6. 종합 관측사항

- **스웜/다중 드론**: aerial-autonomy-stack이 가장 활발하게 스웜 기능 지원 (NUM_QUADS/NUM_VTOLS/NUM_TAILS 설정)
- **GNSS-Denied**: ahmedeltaher/Autonomous-drone-navigation이 GPS 없이 indoor navigation 강조 (optical flow + IMU + LiDAR)
- **YOLO 통합**: 3개 독립 저장소에서 YOLOv8 실시간 객체 감지를 PX4/ROS2 스택에 통합
- **SLAM**: RTAB-Map, ORB SLAM2, LeoDrone 등 다양한 SLAM 솔루션 활발
- **ArUco 정밀 착륙**: 정밀 착륙 시스템이 여러 저장소에서 구현 중
- **Zenoh**: 아직 초기 단계지만 aerial-autonomy-stack이 공식 지원
- **MediaPipe**: 0스타 초기 프로젝트 3개 발견
- **PX4 Bridge**: px4_ros_com (221⭐)이 공식 브릿지, uXRCE-DDS 기반
