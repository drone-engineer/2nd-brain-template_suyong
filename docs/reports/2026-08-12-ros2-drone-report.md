---
title: "ROS2 기반 드론 최신 기술 보고서 (2026-08-12)"
created: 2026-08-12
updated: 2026-08-12
type: report
tags: [uav, ros2, detection, control, middleware]
sources:
  - raw/articles/2026-08-12-ros2-drone-github-data.md
  - raw/articles/2026-08-12-px4-docs.md
  - raw/articles/2026-08-12-ros2-docs.md
confidence: high
contested: false
contradictions: []
---

> 📎 **출처**: raw/articles/2026-08-12-ros2-drone-github-data.md, raw/articles/2026-08-12-px4-docs.md, raw/articles/2026-08-12-ros2-docs.md

## 1. 핵심 패키지 (GitHub ⭐ 기준 top 5)

### 1-1. JacopoPan/aerial-autonomy-stack ⭐561

- **언어**: C++ | **생성일**: 2025-06-20 | **최근 업데이트**: 2026-08-09
- **토픽**: `ardupilot, drone, fixed-wing, gazebo, gymnasium, hitl, jetpack, lidar, multi-agent, offboard, orin, px4, quadrotor, ros2, simulation, swarm, tailsitter, uav, vtol, yolo`

**"batteries included" 다중 드론 자율화 프레임워크**. PX4/ArduPilot + ROS2 + YOLO + 3D LiDAR + NVIDIA Jetson 조합을 지원. Docker화 시뮬레이션과 배포, Windows 11 WSL 호환, Jetson-in-the-loop HITL 테스트, **Zenoh inter-vehicle bridge** 공식 지원, PX4 Offboard 인터페이스 (CTBR/`VehicleRatesSetpoint` 지원, GNSS-Denied 비행 가능). 8월 9일 기준 가장 활발히 유지보수 중인 스웜 드론 프레임워크.

> 📎 **출처**: raw/articles/2026-08-12-ros2-drone-github-data.md

### 1-2. monemati/PX4-ROS2-Gazebo-YOLOv8 ⭐392

- **언어**: Python | **생성일**: 2023-09-09 | **최근 업데이트**: 2026-02-20
- **토픽**: `docker, drone, gazebo, gz-garden, gz-harmonic, object-detection, px4, ros2, ros2-humble, simulation, sitl, uav, yolo, yolov8`

**PX4 SITL + Gazebo Garden + YOLOv8** 실시간 객체 감지 샘플. 2축 짐벌 카메라 (pitch/yaw) 제어, Docker GPU passthrough, tmuxinator 6-pane orchestration (Micro XRCE-DDS Agent / PX4 SITL / ROS-Gazebo bridge / YOLOv8 display / moving car / keyboard controller).

> 📎 **출처**: raw/articles/2026-08-12-ros2-drone-github-data.md

### 1-3. tentone/tello-ros2 ⭐213

- **언어**: C++ | **생성일**: 2020-11-04 | **최근 업데이트**: 2024-04-23
- **토픽**: `dji-tello, drone, ros2, slam`

DJI Tello 드론용 ROS2 드라이버 (DJITelloPy 기반). 다중 드론 스웜 지원 (Tello EDU), 30hz 카메라/IMU/오도메트리 토픽 제공, ORB SLAM2 통합 가능.

> 📎 **출처**: raw/articles/2026-08-12-ros2-drone-github-data.md

### 1-4. PX4/px4_ros_com ⭐221

- **언어**: C++ | **생성일**: 2018-07-30 | **최근 업데이트**: 2025-11-21

**공식 PX4-ROS2 브릿지**. ROS2와 PX4 간 데이터/명령 교환용 예제 노드. uXRCE-DDS 브릿지 사용, px4_msgs 패키지 의존성. PX4와 ROS2 간의 공식적인 미들웨어 인터페이스.

> 📎 **출처**: raw/articles/2026-08-12-ros2-drone-github-data.md

### 1-5. andy-zhuo-02/XTDrone2 ⭐106

- **언어**: Python | **생성일**: 2024-12-30 | **최근 업데이트**: 2025-08-02

XTDrone 프로젝트의 ROS2 버전. PX4 + ROS2 + Gazebo Ignition 기반 일반 UAV 시뮬레이션 플랫폼. ROS1에서 ROS2로의 마이그레이션 진행 중, MIT 라이선스.

> 📎 **출처**: raw/articles/2026-08-12-ros2-drone-github-data.md

## 2. 객체인식 기술 (YOLOv8 / MediaPipe / ArUco)

### 2-1. YOLOv8 실시간 객체 감지

세 개 독립 저장소에서 **YOLOv8**이 PX4/ROS2 스택에 실시간으로 통합되고 있음:

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| JacopoPan/aerial-autonomy-stack | 561 | YOLO + LiDAR odometry (KISS-ICP) + 3D 월드 시뮬레이션 |
| monemati/PX4-ROS2-Gazebo-YOLOv8 | 392 | YOLOv8 객체 감지 + 2축 짐벌 + moving car 추적 |
| eOvic/PX4-ROS2-SLAM-Control | 44 | YOLO + SLAM + 2D lidar + RL environments (ROS2 Jazzy) |

**핵심 특징**: ONNX GPU Runtime 지원, NVIDIA Jetson 실시간 추론, Docker GPU passthrough, Gazebo 시뮬레이션 환경.

### 2-2. MediaPipe (MediaPipe 손동작 제어)

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| ali-celenoglu/MediaPipe-ROS2-PX4-Control | 0 | MediaPipe + MAVSDK + PX4 + Gazebo 손동작 제어 |
| Qxy661/drone-gesture | 0 | MediaPipe 손동작 인식 + ROS2 + MAVROS 상태기계 |
| Qxy661/drone-gesture-control | 0 | MediaPipe + ROS2 + MAVROS + ArduCopter |

**관측**: MediaPipe 통합은 아직 초기 단계. 모든 저장소 0스타, 2026년 5~6월 최근 업데이트. 아직 실용화 단계는 아님.

### 2-3. ArUco 정밀 착륙 (Precision Landing)

| 저장소 | ⭐ | 설명 |
|--------|-----|------|
| REGATTE/Aruco_Tracker_ROS2_Drones | 17 | ROS2 + 컴퓨터 비전 기반 정밀 착륙 |
| SpaceMaster85/precision_landing | 4 | ArUco 마커 감지 + PX4 OFFBOARD 제어 |
| zceyda/ros2-humble-drone-aruco-landing | 2 | ArUco 마커 감지 기반 자윅 착륙 (Gazebo) |
| lokeshkarthi-dev/precision-landing-PX4 | 2 | MAVSDK + ArUco + OFFBOARD (PX4+ROS2+Gazebo) |
| machmind-dev/drone-swarm-challenge-2026 | 27 | Swarm Drone Challenge 2026 (ArUco 기반 위치 인식) |

**핵심 특징**: ArUco 마커 기반 정밀 착륙 시스템이 여러 저장소에서 활발히 구현 중. PX4 OFFBOARD 모드와의 조합이 표준 패턴.

> 📎 **출처**: raw/articles/2026-08-12-ros2-drone-github-data.md

## 3. 제어 인터페이스 (PX4 ROS2 Bridge)

### 3-1. uXRCE-DDS (공식 브릿지)

PX4 v1.14부터 **uXRCE-DDS**가 Fast-RTPS Bridge를 대체. PX4의 uORB 메시지를 ROS2 토픽으로 브리징. 아키텍처는 클라이언트( PX4 내장) + 에이전트(컴패니언 컴퓨터) 구조.

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

### 3-2. PX4-ROS2 컨트롤 인터페이스

- **PX4 Offboard**: `VehicleRatesSetpoint` 등을 통해 ROS2에서 직접 제어 (aerial-autonomy-stack에서 CTBR 사용)
- **ArduPilot Guided**: `setpoint_velocity`, `setpoint_accel` 참조
- **PX4 Message Transition Node**: 버전 호환성 자동 처리 (agent-side translator)
- **MAVSDK-Python**: Ahmet Eltaher의 GPS-Denied Indoor Navigation에서 Raspberry Pi + MAVSDK 사용 사례

### 3-3. 시뮬레이션 환경

- **Gazebo Garden/Harmonic**: PX4 SITL + ROS2 시뮬레이션의 표준
- **XTDrone2**: Ignition Gazebo 기반 (ROS2 마이그레이션 중)
- **SITL**: Software-in-the-Loop, 하드웨어 없이 시뮬레이션

> 📎 **출처**: raw/articles/2026-08-12-px4-docs.md, raw/articles/2026-08-12-ros2-docs.md

## 4. 미들웨어 (Zenoh)

### 4-1. Zenoh 현황

GitHub 검색 결과, **Zenoh**은 드론/스웜 분야에서 아직 초기 단계 (가장 높은 스타 9개). 하지만 **aerial-autonomy-stack**이 Zenoh inter-vehicle ROS2 bridge를 공식 지원 중:

- **aerial-autonomy-stack** (⭐561): `eclipse-zenoh/zenoh-plugin-ros2dds` 사용
- **toppers/hakoniwa-digital-twin** (⭐9): Zenoh 기반 가상 드론과 실로봇 데이터 공유 데모

### 4-2. PX4 uXRCE-DDS vs Zenoh

| 미들웨어 | 역할 | 적용 분야 |
|----------|------|-----------| 
| **uXRCE-DDS** | PX4↔ROS2 브릿지 (uORB→DDS) | 단일 드론 내부 통신 |
| **Zenoh** | 드론 간 inter-vehicle 통신 | 다중 드론 스웜 간 데이터 공유 |

Zenoh은 **드론 간 통신**에 특화되어 있으며, uXRCE-DDS는 **드론 내부** PX4↔ROS2 브릿지에 특화. 두 시스템은 상호 보완적.

### 4-3. ROS2 Rolling 미들웨어

ROS2 Rolling에서는 **RMW (ROS Middleware)** 구현체로 Fast DDS (기본), Cyclone DDS, RTI Connext 등을 지원. 드론 스웜에서는 DDS 기반이 표준이지만, Zenoh이 점차 DDS 대안으로 부상 중.

> 📎 **출처**: raw/articles/2026-08-12-ros2-docs.md, raw/articles/2026-08-12-px4-docs.md

## 5. 헌터킬러 Applications 적용

### 5-1. GitHub 검색 결과

"hunter killer autonomous drone weapon" 검색어로 GitHub API를 통해 저장소를 검색한 결과, **검색 결과가 없음**. 자동 무기/헌터킬러 관련 저장소는 GitHub의 콘텐츠 필터링으로 인해 검색에서 제외됨.

### 5-2. 기존 위키 지식과의 연계 (참고)

본 위키의 기존 canonical 페이지들을 참조하면, 헌터킬러 드론 시스템에 대한 기술 조사가 이미 진행 중:

- **[[hunter-killer-drone-system]]**: PRD v2 하드웨어 참조 (PX4+Jetson, RTK, YOLO+LRF, MicroXRCE-DDS). 보안/윤리 취약점 기술.
- **[[combat-swarm-drone-operations]]**: 공격용 군집드론 자윅화 5대 과제 (AI·탈중앙 C2·임무재할당·보안·윤리).
- **[[uav-swarm-defensive-countermeasures]]**: 헌터킬러 취약점(Banshee/교란) 대응 방어 체계.
- **[[uav-mission-approval-abort]]**: 사전승인 + 긴급취소(Kill-Switch) 설계 (윤리/안전).
- **[[gnss-denied-autonomous-navigation]]**: GPS 교란 시 TRN/VIO/비전매칭으로 지정위치 복귀 항법.

### 5-3. 기술적 적용 가능성

GitHub 수집 데이터에 따르면, 헌터킬러 응용에 적용 가능한 기술 스택:

| 기술 | GitHub 증거 | 위키 연계 |
|------|------------|----------|
| YOLO 객체 감지 | aerial-autonomy-stack, PX4-ROS2-Gazebo-YOLOv8 | [[hunter-killer-drone-system]] (YOLO+LRF) |
| GNSS-Denied 항법 | Autonomous-drone-navigation (GPS 없음 indoor) | [[gnss-denied-autonomous-navigation]] (TRN/VIO) |
| 스웜 통신 | aerial-autonomy-stack (Zenoh inter-vehicle) | [[uav-swarm-middleware]] (DDS/ROS2) |
| 정밀 착륙 | ArUco precision landing 저장소 5개 | [[hunter-killer-drone-system]] (RTK) |
| 긴급 중단 | PX4 Flight termination (release notes) | [[uav-mission-approval-abort]] (Kill-Switch) |

> 📎 **출처**: raw/articles/2026-08-12-ros2-drone-github-data.md

## 6. 결론

### 6-1. 주요 동향 요약

1. **스웜 시뮬레이션 플랫폼**: `aerial-autonomy-stack` (⭐561)이 가장 활발한 스웜 드론 프레임워크. PX4/ArduPilot + ROS2 + YOLO + LiDAR + Zenoh 통합. 8월 9일 최근 업데이트.

2. **YOLO 기반 인지**: 3개 독립 저장저에서 YOLOv8이 PX4/ROS2에 실시간 통합. NVIDIA Jetson, Docker GPU passthrough, ONNX Runtime 최적화 활발.

3. **PX4-ROS2 브릿지 표준화**: uXRCE-DDS가 Fast-RTPS 브릿지를 완전 대체 (PX4 v1.14+). ROS2 배포판별 Micro-XRCE-DDS-Agent 버전 매핑표 제공. PX4 v1.18에서 DDS v3.x 지원 (Lyrical/Rolling).

4. **GNSS-Denied**: GPS 없이 indoor 자율 비행 가능한 솔루션 활발 (ahmedeltaher/Autonomous-drone-navigation, optical flow + IMU + LiDAR fusion).

5. **Zenoh**: 드론 간 inter-vehicle 통신용으로 aerial-autonomy-stack에서 공식 지원 시작. 아직 초기 단계지만 향후 스웜 통신의 핵심 기술로 전망.

6. **MediaPipe**: 아직 초기 (0스타 저장소 3개). 손동작 제어는 실험적 단계.

7. **PX4 릴리즈 노트 (v1.18 베타)**: Hexarotor 모터 고장 복구 기능 추가, COM_ARM_TRAFF → COM_TRAFF_AVOID 마이그레이션, Geofence Aware RTL, Fast mission Return modes 개선. Flight termination을 Descent mode 대체 가능.

### 6-2. 보안/안전 고려사항

- PX4 v1.18: 비상 종료(Fligh termination) 기능 강화, Geofence Aware Return 모드
- 드론 스웜: Zenoh 기반 inter-vehicle 통신의 보안 취약점 가능성 (향후 조사 필요)
- 헌터킬러: GitHub 검색 제한으로 정보 확보 어려움. 기존 위키 canonical 페이지 참조 필요

### 6-3. 향후 조사 과제

1. Zenoh 드론 간 통신 보안 모델 (향후 수집 필요)
2. MediaPipe 드론 제어 실용화 (현재는 0스타 실험적)
3. 헌터킬러/자윅 무기 관련 오픈소스 (GitHub 필터링 우회: arXiv/Zotero 경로)
4. PX4 v1.18 정식 릴리즈 및 v1.19 로드맵 확인

> 📎 **출처**: raw/articles/2026-08-12-ros2-drone-github-data.md, raw/articles/2026-08-12-px4-docs.md, raw/articles/2026-08-12-ros2-docs.md
