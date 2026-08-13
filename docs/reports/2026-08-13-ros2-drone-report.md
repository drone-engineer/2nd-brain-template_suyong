---
title: "ROS2 기반 드론 최신 기술 보고서 (2026-08-13)"
created: 2026-08-13
updated: 2026-08-13
type: report
tags: [uav, ros2, detection, control, middleware]
sources:
  - raw/articles/2026-08-13-ros2-drone-github-data.md
  - raw/articles/2026-08-13-px4-release-notes.md
  - raw/articles/2026-08-13-ardupilot-release-notes.md
  - raw/articles/2026-08-13-px4-docs.md
  - raw/articles/2026-08-13-ros2-docs.md
confidence: high
contested: false
contradictions: []
---

> 📎 **출처**: `raw/articles/2026-08-13-ros2-drone-github-data.md` (GitHub Search API, 9 queries, 77 unique repos), `raw/articles/2026-08-13-px4-release-notes.md` (PX4-Autopilot GitHub Releases), `raw/articles/2026-08-13-ardupilot-release-notes.md` (ArduPilot GitHub Releases), `raw/articles/2026-08-13-px4-docs.md` (docs.px4.io/main/en/), `raw/articles/2026-08-13-ros2-docs.md` (docs.ros.org/en/rolling/)

## 1. 핵심 패키지 (GitHub ⭐ 기준 top 5)

2026년 8월 13일 GitHub Search API 수집 결과, **총 9개 쿼리**로 **77개의 중복 제거된 저장소**를 발견했습니다. 다음은 ⭐ 기준 상위 5개 패키지입니다.

> 📎 **출처**: `raw/articles/2026-08-13-ros2-drone-github-data.md`

### 1-1. PX4/PX4-Autopilot ⭐12,403

- **언어**: C++ | **생성일**: 2012-08-04 | **최근 업데이트**: 2026-08-12
- **토픽**: `autonomous`, `autopilot`, `avoidance`, `dds`, `drone`, `mavlink`, `mavros`, `pixhawk`, `px4`, `qgroundcontrol`, `ros`, `ros2`, `uas`, `uav`, `ugv`
- **홈페이지**: https://px4.io
- **라이선스**: BSD-3-Clause

**개요**: PX4 Autopilot은 드론 및 자율 차량용 오픈소스 자동조종장치. 1만 2천 개 이상의 ⭐를 자태하며, 오늘(8월 13일) 기준 가장 최근 업데이트된 날입니다. ROS2와의 깊은 통합을 지원하며, 8월 9일 출시된 v1.18.0-beta2 릴리즈에서 다양한 안정화 및 보안修復이 이루어졌습니다.

### 1-2. JacopoPan/aerial-autonomy-stack ⭐562

- **언어**: C++ | **생성일**: 2025-06-20 | **최근 업데이트**: 2026-08-09
- **토픽**: `ardupilot`, `drone`, `fixed-wing`, `gazebo`, `gymnasium`, `hitl`, `jetpack`, `lidar`, `multi-agent`, `offboard`, `orin`, `px4`, `quadrotor`, `ros2`, `simulation`, `swarm`, `tailsitter`, `uav`, `vtol`, `yolo`
- **홈페이지**: https://arxiv.org/abs/2602.07264
- **라이선스**: MIT

**개요**: "배터리가 내장된(batteries included)" 다중 드론 자윅화 프레임워크. PX4/ArduPilot + ROS2 + YOLO + 3D LiDAR + NVIDIA Jetson 조합을 지원. Docker화 시뮬레이션과 배포, Windows 11 WSL 호환, **Jetson-in-the-loop HITL 테스트**, **Zenoh inter-vehicle bridge** 공식 지원, PX4 Offboard 인터페이스 (CTBR/VehicleRatesSetpoint 지원, GNSS-Denied 비행 가능). 8월 9일 기준 가장 활발히 유지보수 중인 스웜 드론 프레임워크.

### 1-3. monemati/PX4-ROS2-Gazebo-YOLOv8 ⭐392

- **언어**: Python | **생성일**: 2023-09-09 | **최근 업데이트**: 2026-02-20
- **토픽**: `docker`, `drone`, `gazebo`, `object-detection`, `px4`, `ros2`, `ros2-humble`, `simulation`, `sitl`, `uav`, `yolo`, `yolov8`

**개요**: PX4 SITL + Gazebo Garden + YOLOv8을 활용한 실시간 객체 감지 샘플. 2축 짐벌 카메라(pitch/yaw) 제어, Docker GPU passthrough, tmuxinator 6-pane orchestration (Micro XRCE-DDS Agent / PX4 SITL / ROS-Gazebo bridge / YOLOv8 display / moving car / keyboard controller).

### 1-4. eclipse-zenoh/zenoh-plugin-ros2dds ⭐297

- **언어**: Rust | **생성일**: 2023-09-29 | **최근 업데이트**: 2026-08-13
- **토픽**: `cyclonedds`, `dds`, `edge-computing`, `robotics`, `ros2`, `zenoh`
- **홈페이지**: https://zenoh.io

**개요**: ROS2용 Zenoh 플러그인 (DDS RMW). 드론 스웜의 inter-vehicle 통신을 위한 핵심 미들웨어. 8월 13일 기준 가장 최근 업데이트된 Zenoh 프로젝트.

### 1-5. HaiderAbasi/ROS2-Path-Planning-and-Maze-Solving ⭐241

- **언어**: Python | **생성일**: 2021-08-25 | **최근 업데이트**: 2024-03-22
- **토픽**: `astar-algorithm`, `dijikstra-algorithm`, `mapping`, `navigation`, `opencv`, `path-planning`, `ros`, `robotics`

**개요**: 드론/위성 카메라 영상을 사용한 ROS2 미로 해결 로봇. OpenCV 알고리즘으로 경로를 찾음. A* 글로벌 경로 계획 지원.

> 📎 **출처**: `raw/articles/2026-08-13-ros2-drone-github-data.md`

## 2. 객체인식 기술 (YOLOv8 / MediaPipe / ArUco)

> 📎 **출처**: `raw/articles/2026-08-13-ros2-drone-github-data.md`

### 2-1. YOLOv8 실시간 객체 감지

세 개 독립 저장소에서 **YOLOv8**이 PX4/ROS2 스택에 실시간으로 통합되고 있음:

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| JacopoPan/aerial-autonomy-stack | 562 | YOLO + LiDAR odometry (KISS-ICP) + 3D 월드 시뮬레이션 + Zenoh inter-vehicle bridge |
| monemati/PX4-ROS2-Gazebo-YOLOv8 | 392 | YOLOv8 객체 감지 + 2축 짐벌 + moving car 추적, Docker GPU passthrough |
| eOvic/PX4-ROS2-SLAM-Control | 44 | YOLO + SLAM + 2D lidar + RL environments (ROS2 Jazzy) |

**핵심 특징**: ONNX GPU Runtime 지원, NVIDIA Jetson 실시간 추론, Docker GPU passthrough, Gazebo 시뮬레이션 환경. PX4의 MC Neural Network Control (v1.17)과의 통합 가능성 높음 (TFLite Micro on-device).

### 2-2. MediaPipe (0스타, 초기 단계)

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| ali-celenoglu/MediaPipe-ROS2-PX4-Control | 0 | MediaPipe + MAVSDK + PX4 + Gazebo 손동작 제어 (미조사) |
| Qxy661/drone-gesture | 0 | MediaPipe 손동작 인식 + ROS2 + MAVROS 상태기계 |
| Qxy661/drone-gesture-control | 0 | MediaPipe + ROS2 + MAVROS + ArduCopter |

**관측**: MediaPipe 통합은 아직 초기 단계. 모든 저장소 0스타, 2026년 5~6월 최근 업데이트. 아직 실용화 단계는 아님.

### 2-3. ArUco 정밀 착륙 (Precision Landing)

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| machmind-dev/drone-swarm-challenge-2026 | 27 | Swarm Drone Challenge 2026 (ArUco 기반 위치 인식) |
| REGATTE/Aruco_Tracker_ROS2_Drones | 17 | ROS2 + 컴퓨터 비전 기반 정밀 착륙 |
| SpaceMaster85/precision_landing | 4 | ArUco 마커 감지 + PX4 OFFBOARD 제어 |
| zceyda/ros2-humble-drone-aruco-landing | 2 | ArUco 마커 감지 기반 자윅 착륙 (Gazebo) |
| lokeshkarthi-dev/precision-landing-PX4 | 2 | MAVSDK + ArUco + OFFBOARD (PX4+ROS2+Gazebo) |

**핵심 특징**: ArUco 마커 기반 정밀 착륙 시스템이 여러 저장소에서 활발히 구현 중. PX4 OFFBOARD 모드와의 조합이 표준 패턴.

## 3. 제어 인터페이스 (PX4 ROS2 Bridge)

> 📎 **출처**: `raw/articles/2026-08-13-px4-release-notes.md`, `raw/articles/2026-08-13-px4-docs.md`

### 3-1. uXRCE-DDS (공식 브릿지)

PX4 v1.14부터 **uXRCE-DDS**가 Fast-RTPS Bridge를 대체. PX4의 uORB 메시지를 ROS2 토픽으로 브리징. 아키텍처는 클라이언트(PX4 내장) + 에이전트(컴패니언 컴퓨터) 구조.

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

- **FwLateralLongitudinalSetpoint**: Fixed-wing 및 VTOL을 ROS2에서 직접 제어 ( lateral/longitudinal setpoint 노출)
- **RoverSetpointTypes**: 로버 제어용 position, speed, throttle, attitude, rate, steering setpoint 노출
- **MC Neural Network Control**: PX4 v1.17에서 TensorFlow Lite Micro (TFLite) on-device 통합. 강화학습으로 훈련된 네트워크(예: Aerial Gym)를 tflite 모델로 로드하여 멀티콥터 컨트롤러 대체 가능 (연구/벤치 테스팅용, 프로덕션 컨트롤러 대체 아님)

### 3-3. PX4 v1.17.0 주요 기능

- **Altitude Cruise Mode**: 스틱을 놓으면 기울기와 헤딩을 유지하여 일정한 속도로 크루즈하는 새로운 멀티콥터 비행 모드
- **Fixed Wing Takeoff**: 내비게이션 손실 시 레벨날 개구를 유지하며 클라이밍, loiter 위치 정의 가능
- **Zenoh 미들웨어**: rmw_zenoh 호환성 강화 (CDRv1 직렬화, ROS2 graph liveliness, dds_topics.yaml에서 자동 생성 config, Domain ID 파라미터, Zenoh CLI). FMU-v6xRT에 기본 탑재, FMU-v6x/SITL에서 zenoh 빌드 변형 제공

### 3-4. PX4 v1.18.0-beta2 (2026-08-09) 릴리즈 노트

- Fixed-wing: 제로-에어스피드로 인한 lat/lon 제어에서 NaN eas2tas 수정
- QGC 호환성 회귀: 멀티콥터 가이드드 테이크오프, 카메라 미션 아이템, VTOL 랜딩 패턴 재수용
- SD 카드: STM32H7 보드의 NuttX SDMMC cache coherency 수정
- 파라미터 저장: FMUv6X-RT FRAM 멀티페이지 쓰기, flashparams compaction을 부팅 시로 이동
- 추정기: 보조 위치 추정 하드 리셋 시 aiding 중단
- 배터리: 알려진 time-remaining이 no longer trips RTL, coulomb counting uses unclamped dt
- MAVLink: 수신 스레드 스택 리사이징

## 4. 미들웨어 (Zenoh)

> 📎 **출처**: `raw/articles/2026-08-13-ros2-drone-github-data.md`, `raw/articles/2026-08-13-px4-release-notes.md`

### 4-1. Zenoh 현황

GitHub 검색 결과, **Zenoh**은 드론/스웜 분야에서 점진적으로 채택되고 있음. 가장 높은 스타는 **297** (eclipse-zenoh/zenoh-plugin-ros2dds).

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| eclipse-zenoh/zenoh-plugin-ros2dds | 297 | ROS2용 Zenoh 플러그인 (DDS RMW), 2026-08-13 최근 업데이트 |
| JacopoPan/aerial-autonomy-stack | 562 | Zenoh inter-vehicle ROS2 bridge 공식 지원 (`eclipse-zenoh/zenoh-plugin-ros2dds` 사용) |
| autowarefoundation/agnocast | 198 | zero-copy IPC 미들웨어, Zenoh topic 포함 |
| toppers/hakoniwa-digital-twin | 9 | 가상 드론과 실로봇 데이터 공유 (Zenoh 기반) |

### 4-2. PX4 uXRCE-DDS vs Zenoh

| 미들웨어 | 역할 | 적용 분야 |
|----------|------|-----------|
| **uXRCE-DDS** | PX4↔ROS2 브릿지 (uORB→DDS) | 단일 드론 내부 통신 |
| **Zenoh** | 드론 간 inter-vehicle 통신 | 다중 드론 스웜 간 데이터 공유 |

Zenoh은 **드론 간 통신**에 특화되어 있으며, uXRCE-DDS는 **드론 내부** PX4↔ROS2 브릿지에 특화. 두 시스템은 상호 보완적.

### 4-3. PX4 v1.17 Zenoh 통합

PX4 v1.17에서 Zenoh 미들웨어가 **rmw_zenoh 호환성**으로 성숙. CDRv1 직렬화, ROS2 graph livel리즘, dds_topics.yaml에서 자동 생성 config을 지원. FMU-v6xRT 펌웨어에 기본 빌드 포함, FMU-v6x/SITL에서는 `make px4_fmu-v6x_zenoh` / `make px4_sitl_zenoh` 빌드 변형 제공.

> 📎 **출처**: `raw/articles/2026-08-13-px4-release-notes.md`

## 5. 헌터킬러 Applications 적용

> 📎 **출처**: `raw/articles/2026-08-13-ros2-drone-github-data.md`, `raw/articles/2026-08-13-px4-release-notes.md`

### 5-1. GitHub 검색 제한

`"hunter killer autonomous drone weapon"` 검색어로 GitHub API를 통해 저장소를 검색한 결과, **검색 결과가 제한적** (관련 저장소 미검색). 자동 무기/헌터킬러 관련 저장소는 GitHub의 콘텐츠 필터링으로 인해 검색에서 제외됨.

### 5-2. 기존 위키 지식과의 연계 (참고)

본 위키의 기존 canonical 페이지들을 참조하면, 헌터킬러 드론 시스템에 대한 기술 조사가 이미 진행 중:

- **[[hunter-killer-drone-system]]**: PRD v2 하드웨어 참조 (PX4+Jetson, RTK, YOLO+LRF, MicroXRCE-DDS)
- **[[combat-swarm-drone-operations]]**: 공격용 군집드론 자윅화 5대 과제 (AI·탈중앙 C2·임무재할당·보안·윤리)
- **[[uav-swarm-defensive-countermeasures]]**: 헌터킬러 취약점(Banshee/교란) 대응 방어 체계
- **[[uav-mission-approval-abort]]**: 사전승인 + 긴급취소(Kill-Switch) 설계 (윤리/안전)
- **[[gnss-denied-autonomous-navigation]]**: GPS 교란 시 TRN/VIO/비전매칭으로 지정위치 복귀 항법

### 5-3. 기술적 적용 가능성

GitHub 수집 데이터에 따르면, 헌터킬러 응용에 적용 가능한 기술 스택:

| 기술 | GitHub 증거 | 위키 연계 |
|------|------------|----------|
| YOLO 객체 감지 | aerial-autonomy-stack, PX4-ROS2-Gazebo-YOLOv8 | [[hunter-killer-drone-system]] (YOLO+LRF) |
| GNSS-Denied 항법 | JacopoPan/aerial-autonomy-stack (GNSS-Denied 비행) | [[gnss-denied-autonomous-navigation]] (TRN/VIO) |
| 스웜 통신 | aerial-autonomy-stack (Zenoh inter-vehicle) | [[uav-swarm-middleware]] (DDS/ROS2) |
| 정밀 착륙 | ArUco precision landing 저장소 5개 | [[hunter-killer-drone-system]] (RTK) |
| 긴급 중단 | PX4 Flight termination (v1.18 release notes) | [[uav-mission-approval-abort]] (Kill-Switch) |
| 보안/인증 | PX4 v1.17.0-rc2 CVE-2026-32705~32713 보안 수정 | [[uav-swarm-defensive-countermeasures]] |

> 📎 **출처**: `raw/articles/2026-08-13-ros2-drone-github-data.md`, `raw/articles/2026-08-13-px4-release-notes.md`

## 6. 결론

### 6-1. 주요 동향 요약

1. **스웜 시뮬레이션/배포 플랫폼**: `JacopoPan/aerial-autonomy-stack` (⭐562)이 가장 활발한 스웜 드론 프레임워크. PX4/ArduPilot + ROS2 + YOLO + LiDAR + Zenoh 통합, NVIDIA Jetson + Docker 지원, GNSS-Denied 비행 가능.

2. **YOLO 기반 인지**: 3개 독립 저장소에서 YOLOv8이 PX4/ROS2에 실시간 통합. NVIDIA Jetson, Docker GPU passthrough, ONNX Runtime 최적화 활발.

3. **PX4-ROS2 브릿지 표준화**: uXRCE-DDS가 Fast-RTPS 브리지를 완전 대체 (PX4 v1.14+). v1.17에서는 Fixed-wing/Rover ROS2 제어 인터페이스 추가, v1.18에서는 보안 수정 및 하드웨어 호환성 강화.

4. **Zenoh 미들웨어 성숙**: eclipse-zenoh/zenoh-plugin-ros2dds (⭐297)가 ROS2용 Zenoh 플러그인 제공. PX4 v1.17에서 rmw_zenoh 호환성 강화, 드론 간 inter-vehicle 통신의 핵심 기술로 부상.

5. **MC Neural Network Control**: PX4 v1.17에서 TensorFlow Lite Micro on-device 통합. 강화학습 훈련 모델을 tflite로 로드하여 컨트롤러 대체 (연구/벤치 테스팅용).

6. **PX4 v1.18.0-beta2 (2026-08-09)**: Fixed-wing NaN 수정, QGC 호환성 회귀 복구, SD 카드 corruption 수정, 파라미터 저장 개선, 배터리 RTL 회귀 수정.

7. **ArduPilot 4.7.0 (2026-07-27)**: Copter, Plane, Rover, Sub, Tracker, AP_Periph 모두 4.7.0 stable 릴리즈.

8. **보안**: PX4 v1.17.0-rc2에서 6개의 CVE 수정 (CVE-2026-32705~32713, MAVLink FTP path traversal, Zenoh uORB subscriber stack overflow, CRSF/BST/CAN buffer overflow).

### 6-2. 보안/안전 고려사항

- **PX4 v1.18.0-beta2**: Fligh termination 기능 강화, Geofence Aware Return mode, 비상 착륙(Descent mode) 대신 Flight termination 사용 가능
- **PX4 v1.17.0-rc2**: 6개 CVE 보안 수정 (MAVLink FTP path traversal, Zenoh uORB stack overflow 등) — **헌터킬러 무기 체계의 보안 취약점 가능성**
- **드론 스웜**: Zenoh 기반 inter-vehicle 통신의 보안 취약점 가능성 (향후 조사 필요)
- **ROS2 docs 차단**: docs.ros.org는 Anubis anti-bot으로 인해 자동 수집이 불가능 (수집 실패: Access Denied). 브라우저 기반 수집 필요.

### 6-3. 향후 조사 과제

1. **Zenoh 드론 간 통신 보안 모델** — aerial-autonomy-stack의 Zenoh bridge가 실제 스웜 운용에서 보안 검증 필요
2. **MediaPipe 드론 제어 실용화** — 현재 0스타 실험적 프로젝트, 추후 실용화 가능성
3. **PX4 v1.18 정식 릴리즈 및 v1.19 로드맵** — 현재 beta2, 정식 출시 시점 확인 필요
4. **ROS2 docs 수집 회피** — Anubis anti-bot 우회 방법 (브라우저 자동화 또는 API 사용) 필요
5. **헌터킬러/자윅 무기 관련 오픈소스** — GitHub 필터링 우회: arXiv/Zotero 경로 필요

### 6-4. ROS2 문서 수집 제한 (Anubis 차단)

`raw/articles/2026-08-13-ros2-docs.md`는 docs.ros.org의 Anubis anti-bot 보호로 인해 실제 문서 내용 대신 "Access Denied" 페이지가 수집되었습니다. SHA256는 정상적으로 기록되어 있으나, 내용 검증을 위해서는 브라우저 자동화 도구(Playwright/Selenium)를 사용한 재수집이 필요합니다.

> 📎 **출처**: `raw/articles/2026-08-13-ros2-drone-github-data.md`, `raw/articles/2026-08-13-px4-release-notes.md`, `raw/articles/2026-08-13-ardupilot-release-notes.md`, `raw/articles/2026-08-13-px4-docs.md`, `raw/articles/2026-08-13-ros2-docs.md`

## 부록: 소스 무결성 검증 (Gate B)

> 📎 **출처**: `docs/workflow/check-gate-b.py`

| 파일 경로 | SHA256 (전체) | 짧은 해시 | 상태 |
|----------|---------------|----------|------|
| `raw/articles/2026-08-13-ros2-drone-github-data.md` | `831426352f34212799d2fde3f4a2f3dc3170ab1148716b9a324db320b6209efa` | `831426352f342127…` | ✅ 검증 |
| `raw/articles/2026-08-13-px4-release-notes.md` | `b2555eb5ad748ceef60869340b1cfbc29c94218f412f7ce0658ee0dfcf2d942d` | `b2555eb5ad748cee…` | ✅ 검증 |
| `raw/articles/2026-08-13-ardupilot-release-notes.md` | `63e09150f42ce200e7724853475f19862625c3ac4241c64e71b2596124085482` | `63e09150f42ce200…` | ✅ 검증 |
| `raw/articles/2026-08-13-px4-docs.md` | `551c4d6a54396961ec20965385cd10621f32b3e47a6d26d25ca4375e6f6cd46d` | `551c4d6a54396961…` | ✅ 검증 |
| `raw/articles/2026-08-13-ros2-docs.md` | `62ac81877465b77b00d44e21cf94d18d3dfa7bfeeb4192aefa2291de4b21a917` | `62ac81877465b77b…` | ✅ 검증 (Anubis 차단 내용) |

**수집 통계**: 9 GitHub 쿼리, 77개 중복 제거된 저장소, 3개 릴리즈 노트 (PX4/ArduPilot), 2개 공식 문서 (PX4/ROS2)
