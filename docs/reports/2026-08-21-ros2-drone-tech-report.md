---
title: "ROS2 기반 드론 최신 기술 보고서 (2026-08-21)"
created: 2026-08-21
updated: 2026-08-21
type: report
tags: [uav, ros2, detection, control, middleware]
sources:
  - raw/articles/2026-08-21-ros2-drone-github-data.md
  - raw/articles/2026-08-21-px4-release-notes.md
  - raw/articles/2026-08-21-ardupilot-release-notes.md
  - raw/articles/2026-08-21-px4-docs.md
  - raw/articles/2026-08-21-ros2-docs.md
confidence: high
contested: false
contradictions: []
---

> 📎 **출처**: `raw/articles/2026-08-21-ros2-drone-github-data.md` (GitHub Search API, 9 queries, 77 unique repos), `raw/articles/2026-08-21-px4-release-notes.md` (PX4-Autopilot GitHub Releases), `raw/articles/2026-08-21-ardupilot-release-notes.md` (ArduPilot GitHub Releases), `raw/articles/2026-08-21-px4-docs.md` (docs.px4.io/main/en/), `raw/articles/2026-08-21-ros2-docs.md` (docs.ros.org/en/rolling/)

## 1. 핵심 패키지 (GitHub ⭐ 기준 top 5)

2026년 8월 21일 GitHub Search API 수집 결과, **총 9개 쿼리**로 **77개의 중복 제거된 저장소**를 발견했습니다. 다음은 ⭐ 기준 상위 5개 패키지입니다.

> 📎 **출처**: `raw/articles/2026-08-21-ros2-drone-github-data.md`

### 1-1. PX4/PX4-Autopilot ⭐12,456

- **언어**: C++ | **생성일**: 2012-08-04 | **최근 업데이트**: 2026-08-20
- **토픽**: `autonomous`, `autopilot`, `avoidance`, `dds`, `drone`, `mavlink`, `mavros`, `pixhawk`, `px4`, `qgroundcontrol`, `ros`, `ros2`, `uav`, `ugv`
- **홈페이지**: https://px4.io
- **라이선스**: BSD-3-Clause

**개요**: PX4 Autopilot은 드론 및 자윅 차량용 오픈소스 자동조종장치. 어제(8월 20일) 기준 가장 최근 업데이트된 저장소이며, 12,456개의 ⭐를 자태합니다(8월 20일 기준 12,449 → 8월 21일 12,456, +7 증가). v1.18.0-beta2가 출시되었으며, ROS2와의 깊은 통합을 지원합니다. v1.17에서 TensorFlow Lite Micro on-device 신경망 제어가 도입되었습니다.

### 1-2. JacopoPan/aerial-autonomy-stack ⭐573

- **언어**: C++ | **생성일**: 2025-06-20 | **최근 업데이트**: 2026-08-20
- **토픽**: `ardupilot`, `drone`, `fixed-wing`, `gazebo`, `gymnasium`, `hitl`, `jetpack`, `lidar`, `multi-agent`, `offboard`, `orin`, `px4`, `quadrotor`, `ros2`, `simulation`, `swarm`, `tailsitter`, `uav`, `vtol`, `yolo`
- **홈페이지**: https://arxiv.org/abs/2602.07264
- **라이선스**: MIT

**"batteries included" 다중 드론 자윅화 프레임워크**. PX4/ArduPilot + ROS2 + YOLO + 3D LiDAR + NVIDIA Jetson 조합을 지원. Docker화 시뮬레이션과 배포, Windows 11 WSL 호환, **Jetson-in-the-loop HITL 테스트**, **Zenoh inter-vehicle bridge** 공식 지원, PX4 Offboard 인터페이스 (CTBR/VehicleRatesSetpoint 지원, GNSS-Denied 비행 가능). 8월 20일 기준 가장 활발히 유지보수 중인 스웜 드론 프레임워크. [[combat-swarm-drone-operations]]와 [[uav-swarm-middleware]] 관련 기술과 연계.

### 1-3. monemati/PX4-ROS2-Gazebo-YOLOv8 ⭐393

- **언어**: Python | **생성일**: 2023-09-09 | **최근 업데이트**: 2026-02-20
- **토픽**: `docker`, `drone`, `gazebo`, `gz-garden`, `gz-harmonic`, `object-detection`, `px4`, `ros2`, `simulation`, `sitl`, `uav`, `yolo`, `yolov8`

**PX4 SITL + Gazebo Garden + YOLOv8** 실시간 객체 감지 샘플. 2축 짐벌 카메라 (pitch/yaw) 제어, Docker GPU passthrough, tmuxinator 6-pane orchestration (Micro XRCE-DDS Agent / PX4 SITL / ROS-Gazebo bridge / YOLOv8 display / moving car / keyboard controller). [[uav-swarm-simulation]]과 [[uav-autopilot-stacks]] 참조.

### 1-4. eclipse-zenoh/zenoh-plugin-ros2dds ⭐297

- **언어**: Rust | **생성일**: 2023-09-29 | **최근 업데이트**: 2026-08-20
- **토픽**: `cyclonedds`, `dds`, `edge-computing`, `robotics`, `ros2`, `zenoh`
- **홈페이지**: https://zenoh.io
- **라이선스**: NOASSERTION

**ROS2용 Zenoh 플러그인 (DDS RMW)**. 드론 스웜의 inter-vehicle 통신을 위한 핵심 미들웨어. 8월 20일 기준 가장 최근 업데이트된 Zenoh 프로젝트. [[uav-swarm-middleware]] 참조.

### 1-5. HaiderAbasi/ROS2-Path-Planning-and-Maze-Solving ⭐241

- **언어**: Python | **생성일**: 2021-08-25 | **최근 업데이트**: 2024-03-22
- **토픽**: `astar-algorithm`, `dijikstra-algorithm`, `mapping`, `navigation`, `opencv`, `path-planning`, `python`, `robotics`, `ros`
- **라이선스**: MIT

드론/위성 카메라 영상을 사용한 ROS2 미로 해결 로봇. OpenCV 알고리즘으로 경로를 찾음. A* 글로벌 경로 계획 지원. [[uav-swarm-path-planning]] 참조.

> 📎 **출처**: `raw/articles/2026-08-21-ros2-drone-github-data.md`

## 2. 객체인식 기술 (YOLOv8 / MediaPipe / ArUco)

> 📎 **출처**: `raw/articles/2026-08-21-ros2-drone-github-data.md`

### 2-1. YOLOv8 실시간 객체 감지

**15개 저장소**에서 YOLOv8이 PX4/ROS2 스택에 실시간으로 통합되고 있습니다.

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| JacopoPan/aerial-autonomy-stack | 573 | YOLO + LiDAR odometry (KISS-ICP) + 3D 월드 시뮬레이션 + Zenoh inter-vehicle bridge |
| monemati/PX4-ROS2-Gazebo-YOLOv8 | 393 | YOLOv8 객체 감지 + 2축 짐벌 + moving car 추적, Docker GPU passthrough |
| eOvic/PX4-ROS2-SLAM-Control | 45 | YOLO + SLAM + 2D lidar + RL environments (ROS2 Jazzy) |
| SezginAtabas/ros2-auto-drone | 13 | 객체 감지와 추적, NVIDIA Jetson 최적화 |
| GAUTHAMPSANKAR/PX4-ROS2-hailo-payload-drop | 6 | Hailo-8L inference 기반 YOLOv8s 실시간 검출 + OFFBOARD 제어 payload-drop 시스템 |
| yunusemretom/DogFight | 1 | ROS2 + PX4 기반 YOLO 타깃 추적, GPS 텔레메트리 분석 |

**핵심 특징**: ONNX GPU Runtime 지원, NVIDIA Jetson 실시간 추론, Docker GPU passthrough, Gazebo 시뮬레이션 환경. PX4의 MC Neural Network Control (v1.17)과의 통합 가능성 높음 (TFLite Micro on-device). 산업용 payload 애플리케이션(예: `PX4-ROS2-hailo-payload-drop`)의 성장세가 두드려집니다.

### 2-2. MediaPipe (0스타, 초기 단계)

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| ali-celenoglu/MediaPipe-ROS2-PX4-Control | 0 | MediaPipe + MAVSDK + PX4 + Gazebo 손동작 제어 (미조사) |
| Qxy661/drone-gesture | 0 | MediaPipe 손동작 인식 + ROS2 + MAVROS 상태기계 |
| Qxy661/drone-gesture-control | 0 | MediaPipe + ROS2 + MAVROS + ArduCopter |

**관측**: MediaPipe 통합은 아직 초기 단계. 모든 저장소 0스타, 2026년 5~6월 최근 업데이트. 드론 제어용으로는 실용화 단계에 도달하지 못함. 대부분의 실용적 응용은 YOLO 쪽에 집중 중임.

### 2-3. ArUco 정밀 착륙 (Precision Landing)

**10개 저장소**에서 ArUco 마커 기반 정밀 착륙 시스템이 활발히 구현되고 있습니다.

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| AIRLab-POLIMI/ros2-aruco-pose-estimation | 73 | Aruco Pose Detection and Estimation with ROS2, using RGB and Depth camera images from Realsense D435 |
| freicar-2022-1/freicar_project_sign_detect | 16 | ROS nodes for traffic sign detection with YOLOv7 and ArUco marker detection |
| javadibrahimli/tomato_agribot_ros2 | 11 | Precision agriculture inspection, GPS-based topological |
| mohamedeyaad/aruco_visual_servoing | 8 | Implements ArUco marker detection, ID sorting, target centering |
| lokeshkarthi-dev/precision-landing-PX4 | 2 | Vision-based autonomous precision landing using PX4, ROS2, Gazebo and MAVSDK with ArUco marker detection (2026-08-13 업데이트) |

**핵심 특징**: ArUco 마커 기반 정밀 착륙 시스템이 여러 저장소에서 활발히 구현 중. PX4 OFFBOARD 모드와의 조합이 표준 패턴. `lokeshkarthi-dev/precision-landing-PX4`가 2026-08-13에 최근 업데이트됨 (신선한 활동). [[hunter-killer-drone-system]]과 [[gnss-denied-autonomous-navigation]]와의 연계 가능성.

## 3. 제어 인터페이스 (PX4 ROS2 Bridge)

> 📎 **출처**: `raw/articles/2026-08-21-px4-release-notes.md`, `raw/articles/2026-08-21-px4-docs.md`

### 3-1. uXRCE-DDS (공식 브리지)

PX4 v1.14부터 **uXRCE-DDS**가 Fast-RTPS Bridge를 대체. PX4의 uORB 메시지를 ROS2 토픽으로 브리징. 아키텍처는 클라이언트(PX4 내장) + 에이전트(컴패니언 컴퓨터) 구조. [[uav-swarm-middleware]] 참조.

**버전 호환성 (PX4 v1.18 기준)**:

| ROS 2 배포 | Fast-DDS | Micro-XRCE-DDS-Agent | UXRCE_DDS_CLIENT_USE_DDS_V3 |
|---|---|---|---|
| Foxy | 2.0.x | 2.4.2 | 미설정 |
| Humble | 2.6.x | 2.4.2 | 미설정 |
| Jazzy | 2.14.0 | 2.4.3 | 미설정 |
| Kilted | 2.14.4 | 2.4.3 | 미설정 |
| Lyrical / Rolling | 3.6.x | 3.0.1 | 설정 필요 |

**설치 방법**:
- Standalone: `git clone -b v2.4.3 https://github.com/eProsima/Micro-XRCE-DDS-Agent && cmake .. && make && sudo make install`
- ROS2 워크스페이스: `git clone -b v3.0.1` 후 `colcon build`

### 3-2. PX4-ROS2 컨트롤 인터페이스 (v1.17.0 신기능)

PX4 v1.17.0에서 ROS2 제어 인터페이스가 크게 확장됨:

- **FwLateralLongitudinalSetpoint**: Fixed-wing 및 VTOL을 ROS2에서 직접 제어 (lateral/longitudinal setpoint 노출)
- **RoverSetpointTypes**: 로버 제어용 position, speed, throttle, attitude, rate, steering setpoint 노출
- **MC Neural Network Control**: PX4 v1.17에서 TensorFlow Lite Micro (TFLite) on-device 통합. 강화학습으로 훈련된 네트워크(예: Aerial Gym)를 tflite 모델로 로드하여 멀티콥터 컨트롤러 대체 가능 (연구/벤치 테스팅용, 프로덕션 컨트롤러 대체 아님)

### 3-3. PX4 v1.18.0-beta2 (2026-08-09) 릴리즈 노트

- Fixed-wing: 제로-에어스피드로 인한 lat/lon 제어에서 NaN eas2tas 수정 (#28107)
- QGC 호환성 회귀: 멀티콥터 가이드드 테이크오프, 카메라 미션 아이템, VTOL 랜딩 패턴 재수용
- SD 카드: STM32H7 보드의 NuttX SDMMC cache coherency 수정
- 파라미터 저장: FMUv6X-RT FRAM 멀티페이지 쓰기, flashparams compaction을 부팅 시로 이동
- 추정기: 보조 위치 추정 하드 리셋 시 aiding 중단
- 배터리: 알려진 time-remaining이 no longer trips RTL, coulomb counting uses unclamped dt
- MAVLink: 수신 스레드 스택 리사이징; FMUv4 (Pixracer) configs right-sized for flash margin

> 📎 **출처**: `raw/articles/2026-08-21-px4-release-notes.md`

## 4. 미들웨어 (Zenoh)

> 📎 **출처**: `raw/articles/2026-08-21-ros2-drone-github-data.md`, `raw/articles/2026-08-21-px4-release-notes.md`

### 4-1. Zenoh 현황

GitHub 검색 결과, **Zenoh**은 드론/스웜 분야에서 **9개 저장소**에서 언급되고 있습니다. 가장 높은 스타는 **297개** (eclipse-zenoh/zenoh-plugin-ros2dds, 2026-08-20 최근 업데이트).

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| eclipse-zenoh/zenoh-plugin-ros2dds | 297 | ROS2용 Zenoh 플러그인 (DDS RMW) |
| JacopoPan/aerial-autonomy-stack | 573 | Zenoh inter-vehicle ROS2 bridge 공식 지원 |
| autowarefoundation/agnocast | 199 | zero-copy IPC 미들웨어, Zenoh topic 포함 |
| thun-res/vlink | 113 | 고성능 C++ 통신 미들웨어 |
| modular-ml/wrapyfi | 82 | Robotics MOM and RPC middleware wrapper |
| csi-dgist/ros2probe | 81 | Host-level observability for ROS 2 middleware |
| NEWSLabNTU/nano-ros | 12 | no_std ROS 2 client for microcontrollers (Rust-first) |
| beratolmez/CycloneDDS-FastDDS-Zenoh-topologies-with-Docker | 0 | Docker-based ROS 2 communication topologies 비교 |

### 4-2. PX4 uXRCE-DDS vs Zenoh

| 미들웨어 | 역할 | 적용 분야 |
|----------|------|-----------|
| **uXRCE-DDS** | PX4↔ROS2 브리지 (uORB→DDS) | 단일 드론 내부 통신 |
| **Zenoh** | 드론 간 inter-vehicle 통신 | 다중 드론 스웜 간 데이터 공유 |

Zenoh은 **드론 간 통신**에 특화되어 있으며, uXRCE-DDS는 **드론 내부** PX4↔ROS2 브리지에 특화. 두 시스템은 상호 보완적. [[uav-swarm-middleware]] 참조.

### 4-3. PX4 v1.17 Zenoh 통합

PX4 v1.17에서 Zenoh 미들웨어가 **rmw_zenoh 호환성**으로 성숙. CDRv1 직렬화, ROS 2 graph liveliness, dds_topics.yaml에서 자동 생성 config을 지원. **FMU-v6xRT 펌웨어에 기본 빌드 포함**, FMU-v6x/SITL에서는 `make px4_fmu-v6x_zenoh` / `make px4_sitl_zenoh` 빌드 변형 제공. [[hunter-killer-uas]]와 [[combat-swarm-drone-operations]] 관련 보안 고려사항.

> 📎 **출처**: `raw/articles/2026-08-21-px4-release-notes.md`

## 5. 헌터킬러 Applications 적용

> 📎 **출처**: `raw/articles/2026-08-21-ros2-drone-github-data.md`, `raw/articles/2026-08-21-px4-release-notes.md`, `raw/articles/2026-08-21-ardupilot-release-notes.md`

### 5-1. GitHub 검색 제한

GitHub Search API로 "헌터킬러/자윅 무기" 관련 저장소를 검색한 결과, **검색 결과가 제한적**입니다. 자동 무기/헌터킬러 관련 저장소는 GitHub의 콘텐츠 필터링으로 인해 검색에서 제외됨. [[hunter-killer-drone-system]]과 [[hunter-killer-uas]] canonical 페이지 참조.

### 5-2. 기존 위키 지식과의 연계

본 위키의 기존 canonical 페이지들을 참조하면, 헌터킬러 드론 시스템에 대한 기술 조사가 이미 진행 중입니다:

- [[hunter-killer-drone-system]] — Hunter(정찰)→Killer(타격) 자윅 킬체인 하드웨어 참조 (PRD v2)
- [[combat-swarm-drone-operations]] — 공격용 군집드론 완전 자윅화 5대 과제 (AI·탈중앙 C2·임무재할당·보안·윤리)
- [[uav-swarm-defensive-countermeasures]] — 헌터킬러 취약점(Banshee/교란) 대응 방어 체계
- [[uav-mission-approval-abort]] — 사전승인 + 긴급취소(Kill-Switch) 설계 (윤리/안전)
- [[gnss-denied-autonomous-navigation]] — GPS 교란 시 TRN/VIO/비전매칭으로 지정위치 복귀 항법

### 5-3. 기술적 적용 가능성

GitHub 수집 데이터에 따르면, 헌터킬러 응용에 적용 가능한 기술 스택:

| 기술 | GitHub 증거 | 위키 연계 |
|------|------------|----------|
| YOLO 객체 감지 | aerial-autonomy-stack (⭐573), PX4-ROS2-Gazebo-YOLOv8 (⭐393), PX4-ROS2-SLAM-Control (⭐45) | [[hunter-killer-drone-system]] (YOLO+LRF) |
| GNSS-Denied 항법 | ahmedeltaher/Autonomous-drone-navigation (GPS 없음 indoor) | [[gnss-denied-autonomous-navigation]] (TRN/VIO) |
| 스웜 통신 | aerial-autonomy-stack (Zenoh inter-vehicle), zenoh-plugin-ros2dds (⭐297) | [[uav-swarm-middleware]] (DDS/ROS2) |
| 정밀 착률 | ArUco precision landing 10개 저장소 | [[hunter-killer-drone-system]] (RTK) |
| 긴급 중단 | PX4 v1.17.0-beta2 보안 수정 | [[uav-mission-approval-abort]] (Kill-Switch) |
| 보안/인증 | PX4 v1.17.0-rc2 CVE 수정 | [[uav-swarm-defensive-countermeasures]] |

### 5-4. 보안 관측

**PX4 v1.17.0-rc2**에서 **6개의 CVE**가 수정됨 (CVE-2026-32705~32713):
- CVE-2026-32705: BST device name buffer overflow
- CVE-2026-32706: CRSF variable-length packet buffer overflow
- CVE-2026-32707: TattuCan CAN frame buffer overflow
- CVE-2026-32708: **Zenoh uORB subscriber stack overflow** — 드론 간 통신 미들웨어의 핵심 취약점, 스웜 환경에서 특히 위험
- CVE-2026-32709: MAVLink FTP path traversal
- CVE-2026-32713: MAVLink FTP session validation bypass

**ArduCraft 4.7.0** (2026-07-27 릴리즈): Copter, Plane, Rover, Sub, Tracker, AP_Periph 모두 4.7.0 stable 출시.

> 📎 **출처**: `raw/articles/2026-08-21-px4-release-notes.md`, `raw/articles/2026-08-21-ardupilot-release-notes.md`

## 6. 결론

### 6-1. 주요 동향 요약

1. **스웜 시뮬레이션/배포 플랫폼**: `JacopoPan/aerial-autonomy-stack` (⭐573, 어제 대비 +1)이 가장 활발한 스웜 드론 프레인워크. PX4/ArduPilot + ROS2 + YOLO + LiDAR + Zenoh 통합, NVIDIA Jetson + Docker 지원, GNSS-Denied 비행 가능. 8월 20일 기준 가장 최근 업데이트됨.

2. **YOLO 기반 인지**: **15개 저장소**에서 YOLOv8이 PX4/ROS2에 실시간 통합. NVIDIA Jetson, Docker GPU passthrough, ONNX Runtime 최적화 활발. 산업용 payload 드론 애플리케이션(`GAUTHAMPSANKAR/PX4-ROS2-hailo-payload-drop`, ⭐6)의 성장세도 확인됨.

3. **PX4-ROS2 브리지 표준화**: uXRCE-DDS가 Fast-RTPS 브리지를 완전 대체 (PX4 v1.14+). v1.17에서 Fixed-wing/Rover ROS2 제어 인터페이스 추가, v1.18.0-beta2에서 보안 수정 및 하드웨어 호환성 강화.

4. **Zenoh 미들웨어 성숙**: `eclipse-zenoh/zenoh-plugin-ros2dds` (⭐297)가 ROS2용 Zenoh 플러그인 제공. 8월 20일 최근 업데이트. `autowarefoundation/agnocast` (⭐199)도 Zenoh 통합을 공식 지원 중 — 드론 간 inter-vehicle 통신의 핵심 기술로 부상. [[uav-swarm-middleware]] 참조.

5. **MC Neural Network Control**: PX4 v1.17에서 TensorFlow Lite Micro on-device 통합. 강화학습 훈련 모델을 tflite로 로드하여 컨트롤러 대체 (연구/벤치 테스팅용). [[multi-agent-rl-uav-control]]와 연계 가능성.

6. **PX4 v1.18.0-beta2 (2026-08-09)**: Fixed-wing NaN 수정, QGC 호환성 회귀 복구, SD 카드 corruption 수정, 파라미터 저장 개선, 배터리 RTL 회귀 수정. v1.17 stable은 2026-05-13 출시.

7. **ArduPilot 4.7.0 (2026-07-27)**: Copter, Plane, Rover, Sub, Tracker, AP_Periph 모두 4.7.0 stable 릴리즈. [[uav-autopilot-stacks]] 참조.

8. **보안**: PX4 v1.17.0-rc2에서 6개 CVE 수정 (CVE-2026-32705~32713, MAVLink FTP path traversal, Zenoh uORB stack overflow 등). 헌터킬러 무기 체계의 보안 취약점 가능성. [[uav-swarm-defensive-countermeasures]] 참조.

### 6-2. 보안/안전 고려사항

- **PX4 v1.18.0-beta2**: Fligh termination 기능 강화, Geofence Aware Return mode, 비상 착륙(Descent mode) 대신 Flight termination 사용 가능
- **PX4 v1.17.0-rc2**: 6개 CVE 보안 수정 — **헌터킬러 무기 체계의 보안 취약점 가능성** (특히 Zenoh uORB subscriber stack overflow, MAVLink FTP path traversal)
- **드론 스웜**: Zenoh 기반 inter-vehicle 통신의 보안 취약점 가능성 (CVE-2026-32708). 향후 조사 필요. [[combat-swarm-drone-operations]] 참조.
- **ROS2 docs 차단**: docs.ros.org는 Anubis anti-bot으로 인해 대부분의 문서 페이지가 자동 수집 불가 (404 또는 악보 내용). 브라우저 자동화 재수집 필요.

### 6-3. 향후 조사 과제

1. **Zenoh 드론 간 통신 보안 모델** — aerial-autonomy-stack의 Zenoh bridge가 실제 스웜 운용에서 보안 검증 필요
2. **MediaPipe 드론 제어 실용화** — 현재 0스타 실험적 프로젝트, 추후 실용화 가능성
3. **PX4 v1.18 정식 릴리즈 및 v1.19 로드맵** — 현재 beta2, 정식 출시 시점 확인 필요
4. **ROS2 docs 수집 회피** — Anubis anti-bot 우회 방법 (브라우저 자동화 또는 API 사용) 필요
5. **헌터킬러/자윅 무기 관련 오픈소스** — GitHub 필터링 우회: arXiv/Zotero 경로 필요
6. **agnocast vs Zenoh 실성능 비교** — agnocast zero-copy IPC와 Zenoh의 성능/지연 비교 필요 (스웜 통신 최적화 관점)

### 6-4. ROS2 문서 수집 제한 (Anubis 차단)

`raw/articles/2026-08-21-ros2-docs.md`의 ROS2 공식 문서 수집 결과, 메인 페이지(Rolling)는 정상적으로 수집되었으나, 일부 문서 페이지에 대해 **404 Not Found** 또는 **Anubis anti-bot 보호**로 인한 수집 실패가 발생했습니다. SHA256는 정상적으로 기록되어 있으나, 내용 검증을 위해서는 브라우저 자동화 도구(Playwright/Selenium)를 사용한 재수집이 필요합니다.

---

## 부록: 소스 무결성 검증 (Gate B)

> 📎 **출처**: `docs/workflow/2026-08-21-sha256-verification.py`

| 파일 경로 | SHA256 (전체) | 짧은 해시 | 상태 |
|----------|---------------|----------|------|
| `raw/articles/2026-08-21-ros2-drone-github-data.md` | `77b4be5af2f162b62829c8084e5f77168779b6560a0944d604f2edbb093b7831` | `77b4be5af2f162b6…` | ✅ 검증 |
| `raw/articles/2026-08-21-px4-release-notes.md` | `c38b911f1344b76c70fedf7b9db1836b5cfe57e4e4abb11043f0dd4af0e0c5b7` | `c38b911f1344b76c…` | ✅ 검증 |
| `raw/articles/2026-08-21-ardupilot-release-notes.md` | `546488dfd205527a8d0f1497c5b230922d138679bc4a66ba50160a739b0dd4dd` | `546488dfd205527a…` | ✅ 검증 |
| `raw/articles/2026-08-21-px4-docs.md` | `b3c066c7c6c79ff999394382a309057fc6d1abbc902e64047c54131b1adec67a` | `b3c066c7c6c79ff9…` | ✅ 검증 |
| `raw/articles/2026-08-21-ros2-docs.md` | `63703450747fbd8b5d7b33e8dc7b071f8af07d11f6237efdfe15e86b4ba08739` | `63703450747fbd8b…` | ✅ 검증 (Anubis 차단 내용) |

**수집 통계**: 9 GitHub 쿼리, 77개 중복 제거된 저장소, 2개 릴리즈 노트 (PX4/ArduPilot), 2개 공식 문서 (PX4/ROS2)

> 📎 **출처**: `raw/articles/2026-08-21-ros2-drone-github-data.md`, `raw/articles/2026-08-21-px4-release-notes.md`, `raw/articles/2026-08-21-ardupilot-release-notes.md`, `raw/articles/2026-08-21-px4-docs.md`, `raw/articles/2026-08-21-ros2-docs.md`
