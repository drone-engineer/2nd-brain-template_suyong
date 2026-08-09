---
title: "ROS2 기반 드론 최신 기술 보고서 (2026-08-10)"
created: 2026-08-10
updated: 2026-08-10
type: report
tags: [uav, ros2, detection, control, middleware]
sources:
  - raw/articles/2026-08-10-ros2-drone-github-data.md
  - raw/articles/2026-08-10-px4-release-notes.md
  - raw/articles/2026-08-10-ardupilot-release-notes.md
  - raw/articles/2026-08-10-px4-docs-main.md
  - raw/articles/2026-08-10-ros2-docs-rolling.md
fetched: 2026-08-10T08:30:00Z
confidence: high
contested: false
contradictions: []
---

> 📎 **출처**: raw/articles/2026-08-10-ros2-drone-github-data.md
> 📎 **출처**: raw/articles/2026-08-10-px4-release-notes.md
> 📎 **출처**: raw/articles/2026-08-10-ardupilot-release-notes.md
> 📎 **출처**: raw/articles/2026-08-10-px4-docs-main.md
> 📎 **출처**: raw/articles/2026-08-10-ros2-docs-rolling.md

# 2026-08-10 ROS2 기반 드론 최신 기술 보고서

## 📋 수집 개요

| 항목 | 내용 |
|---|---|
| **수집일** | 2026-08-10 |
| **수집 시각** | 2026-08-10T08:30:00Z |
| **수집 도구** | GitHub Search API, GitHub Releases API, docs.px4.io, docs.ros.org |
| **수집 파일 수** | 14개 (GitHub Search 9개 쿼리 + 통합 데이터 1개 + PX4 릴리즈 1개 + ArduPilot 릴리즈 1개 + PX4 문서 1개 + ROS2 문서 1개) |

### 🔐 원본 무결성 (raw/articles)

| 파일 | SHA256 (body) | 검증 |
|---|---|---|
| `raw/articles/2026-08-10-ros2-drone-github-data.md` | `f4a0739e80cff1b5…` | ✅ 검증 |
| `raw/articles/2026-08-10-px4-release-notes.md` | `55296d74e074b2f7…` | ✅ 검증 |
| `raw/articles/2026-08-10-ardupilot-release-notes.md` | `5f2c04d99369c065…` | ✅ 검증 |
| `raw/articles/2026-08-10-px4-docs-main.md` | `ceccde5ab7d8b1c5…` | ✅ 검증 |
| `raw/articles/2026-08-10-ros2-docs-rolling.md` | `a480d005ed476deb…` | ✅ 검증 |

---

## 📋 목차

1. [핵심 패키지](#1-핵심-패키지-github--기준-top-5)
2. [객체인식 기술](#2-객체인식-기술-yolov8--mediapipe--aruco)
3. [제어 인터페이스](#3-제어-인터페이스-px4-ros2-bridge)
4. [미들웨어](#4-미들웨어-zenoh)
5. [헌터킬러 Applications 적용](#5-헌터킬러-applications-적용)
6. [결론](#6-결론)

---

## 1. 핵심 패키지 (GitHub ⭐ 기준 top 5)

> 📎 **출처**: raw/articles/2026-08-10-ros2-drone-github-data.md

9개의 GitHub Search 쿼리("ros2 drone detection", "ros2 drone autonomous", "ros2 drone navigation", "PX4 ros2 bridge", "YOLO ros2 drone", "zenoh ros2 middleware", "MediaPipe ros2", "SLAM ros2 drone", "ArUco ros2 detection")를 통해 총 45개의 프로젝트를 수집했습니다. ⭐(별표) 수 기준 상위 5개 프로젝트는 다음과 같습니다.

### 1.1 PX4-Autopilot (⭐12371)

- **GitHub**: [PX4/PX4-Autopilot](https://github.com/PX4/PX4-Autopilot)
- **언어**: C++
- **최근 푸시**: 2026-08-09
- **설명**: 세계 최대 규모의 개방형 비행 자동조종기 펌웨어. ROS2와의 공식 브리지(`px4_ros_com`)를 통해 DDS 기반 통신을 지원합니다.
- **핵심**: `ros2 drone autonomous` 검색에서 1위. `autonomous`, `dds`, `ros2`, `uav` 등 18개의 토픽을 보유하고 있으며, 지속적인 커밋 활동이 확인됩니다.

### 1.2 aerial-autonomy-stack (⭐559)

- **GitHub**: [JacopoPan/aerial-autonomy-stack](https://github.com/JacopoPan/aerial-autonomy-stack)
- **언어**: C++
- **최근 푸시**: 2026-08-09
- **설명**: An open framework to simulate and deploy perception-based PX4/ArduPilot drone swarms with ROS2, YOLO, LiDAR, NVIDIA Jetson.
- **핵심**: `YOLO ros2 drone` 검색에서 1위. 드론 스웜 시뮬레이션 및 실deploy를 위한 통합 프레임워크로, YOLO + LiDAR + NVIDIA Jetson 조합을 지원합니다. `swarm`, `simulation`, `offboard`, `lidar`, `yolo`, `jetpack`, `orin` 등 풍부한 토픽이 특징입니다.

### 1.3 PX4-ROS2-Gazebo-YOLOv8 (⭐392)

- **GitHub**: [monemati/PX4-ROS2-Gazebo-YOLOv8](https://github.com/monemati/PX4-ROS2-Gazebo-YOLOv8)
- **언어**: Python
- **설명**: Aerial Object Detection using a Drone with PX4 Autopilot and ROS 2. PX4 SITL and Gazebo Garden used for Simulation. YOLOv8 used for Object Detection.
- **핵심**: `ros2 drone detection` 검색에서 1위. PX4 SITL + Gazebo Garden 시뮬레이션 환경에서 YOLOv8을 이용한 객체 검출을 구현한 래퍼런트입니다.

### 1.4 zenoh-plugin-ros2dds (⭐296)

- **GitHub**: [eclipse-zenoh/zenoh-plugin-ros2dds](https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds)
- **언어**: Rust
- **최근 푸시**: 2026-08-09
- **설명**: A Zenoh plug-in for ROS2 with a DDS RMW.
- **핵심**: `zenoh ros2 middleware` 검색에서 1위. ROS2의 DDS 미들웨어를 Zenoh 네트워크로 브리징하는 플러그인으로, Rust로 구현되어 있습니다.

### 1.5 ROS2-Path-Planning-and-Maze-Solving (⭐241)

- **GitHub**: [HaiderAbasi/ROS2-Path-Planning-and-Maze-Solving](https://github.com/HaiderAbasi/ROS2-Path-Planning-and-Maze-Solving)
- **언어**: Python
- **설명**: Developing a maze solving robot in ROS2 that leverages information from a drone or Satellite's camera using OpenCV algorithms to find its path.
- **핵심**: `ros2 drone navigation` 검색에서 1위. OpenCV 기반 경로 탐색 알고리즘을 ROS2와 통합한 내비게이션 데모 프로젝트입니다.

> 상세 프로젝트 목록은 `raw/articles/2026-08-10-ros2-drone-github-data.md` 참조 (총 45개 프로젝트).

---

## 2. 객체인식 기술 (YOLOv8 / MediaPipe / ArUco)

> 📎 **출처**: raw/articles/2026-08-10-ros2-drone-github-data.md

| 기술 | 프로젝트 | 설명 |
|---|---|---|
| **YOLOv8** | PX4-ROS2-Gazebo-YOLOv8 (⭐392) | PX4 SITL + Gazebo Garden 시뮬레이션에서 YOLOv8 객체 검출. 실시간 비행 중 객체 인식. |
| **YOLO (통합)** | aerial-autonomy-stack (⭐559) | ROS2 + YOLO + LiDAR + NVIDIA Jetson 통합. 드론 스웜 시뮬레이션부터 실제 하드웨어 deploy까지 지원. |
| **YOLO11** | (이전 수집: drone-greenhouse-vision) | 온실 토마토 실시간 검출/분류/추적. PX4-ROS2-Gazebo + YOLO11 통합. |
| **SLAM (Visual)** | tentone/tello-ros2 (⭐213) | DJI Tello 드론을 위한 ROS2 노드. 실내 환경 시각 SLAM 매핑. |
| **SLAM (LiDAR+CV)** | ROS2-Path-Planning (⭐241) | OpenCV 알고리즘 기반 드론/위성 카메라 이미지로 경로 탐색. |
| **MediaPipe** | (검색 결과 내 `MediaPipe ros2` 쿼리) | ROS2와 MediaPipe 통합 프로젝트 존재. 컴퓨터 비전 파이프라인. |
| **ArUco** | (검색 결과 내 `ArUco ros2 detection` 쿼리) | ROS2 기반 ArUco 마커 검출. 비자기학습적 정확한 위치 추정. |

**핵심 통찰**: 객체인식은 YOLO 계열이 실시간 객체 검출의 표준으로 자리 잡았습니다. 특히 `aerial-autonomy-stack`은 YOLO + LiDAR + NVIDIA Jetson을 결합하여 시뮬레이션에서 실제 드론 하드웨어까지 원스톱 지원하는 추세를 보입니다. MediaPipe와 ArUco는 보조 센서로 정확도 높은 위치 추정 및 정밀 항법에 활용되고 있습니다.

---

## 3. 제어 인터페이스 (PX4 ROS2 Bridge)

> 📎 **출처**: raw/articles/2026-08-10-px4-release-notes.md, raw/articles/2026-08-10-px4-docs-main.md

### 3.1 PX4 최신 릴리즈 동향

| 버전 | 날짜 | 상태 | 주요 내용 |
|---|---|---|---|
| v1.18.0-beta2 | 2026-08-09 | 베타 (pre-release) | v1.18.0-beta1 이후 fixed-wing NaN 문제 수정 등 여러 버그 수정 |
| v1.18.0-beta1 | 2026-07-08 | 베타 (pre-release) | v1.18 기능 및 개선사항 |
| v1.18.0-alpha1 | 2026-05-13 | 알파 (pre-release) | v1.18 초기 알파 버전 |
| v1.17.0 | 2026-05-13 | 안정화 (stable) | v1.16 대비 Altitude Cruise 등 새 기능 추가 |
| v1.16.2 | 2026-04-22 | 안정화 (stable) | ekf2 광류 시작 허용 수정 (fix(ekf2)) |
| v1.17.0-rc2 | 2026-03-13 | 리스크 (pre-release) | CVE-2026-32705, CVE-2026-32706 보안 패치 |

**최신 상황**: 2026-08-09에 v1.18.0-beta2가 출시되었습니다. 이는 v1.18.0-beta1(2026-07-08)에서 발견된 fixed-wing NaN 문제( eas2tas )를 수정한 버전입니다. PX4 공식 문서에서는 v1.18의 전체 릴리즈 노트를 https://docs.px4.io/main/en/releases/1.18 에서 확인할 수 있습니다.

### 3.2 px4_ros_com (⭐220)

- **GitHub**: [PX4/px4_ros_com](https://github.com/PX4/px4_ros_com)
- **언어**: C++
- **설명**: ROS2/ROS interface with PX4 through a Fast-RTPS bridge
- **핵심**: PX4 펌웨어 ↔ ROS2 노드 간 실시간 데이터 흐름을 지원합니다. uORB 메시지를 ROS2 토픽으로 변환하여 줍니다. `PX4 ros2 bridge` 검색에서 1위를 기록했습니다.

### 3.3 ROS2 Offboard 제어

- PX4/px4_ros_com을 통해 ROS2 노드에서 직접 궤적/속도 명령을 전송하여 자율 비행을 구현할 수 있습니다.
- 여러 오픈 소스 프로젝트에서 PX4 Offboard 모드 + ROS2 DDS 통신을 결합한 자윅 비행 구현을 보고하고 있습니다.

### 3.4 PX4 공식 문서 ROS2 통합

> 📎 **출처**: raw/articles/2026-08-10-px4-docs-main.md

docs.px4.io에서는 ROS2와의 통합을 공식 지원하고 있습니다:
- **Micro XRCE-DDS** (uXRCE-DDS) 클라이언트를 통한 펌웨어와의 브리징
- **QGroundControl**에서 ROS2 토픽 모니터링 지원
- PX4 메시지를 ROS2 인터페이스로 변환하는 `px4_msgs` 패키지

---

## 4. 미들웨어 (Zenoh)

> 📎 **출처**: raw/articles/2026-08-10-ros2-drone-github-data.md

### 4.1 Zenoh + ROS2 통합

Zenoh은 Zero-Overhead, Dynamic Geo-distributed, Reactive, Collective Data-Plane의 약자로, ROS2의 DDS 대체 또는 보완 미들웨어로 주목받고 있습니다.

### 4.2 주요 프로젝트

| 프로젝트 | ⭐ | 설명 |
|---|---|---|
| **zenoh-plugin-ros2dds** | 296 | Eclipse Zenoh 프로젝트. ROS2 DDS 트래픽을 Zenoh 네트워크로 브리징하는 Rust 기반 플러그인. |
| **agnocast** (autowarefoundation) | 196 | rclcpp-compatible true zero-copy IPC 미들웨어. Zenoh을 지원하며, shared-memory 기반의 초저지연 메시징을 제공. |
| **vlink** (thun-res) | 122 | 고성능 C++ 통신 미들웨어. ROS2/Zenoh/DDS 대체를 표방하며, 자율주행 및 embodied AI를 대상으로 설계됨. |

### 4.3 Zenoh의 핵심 장점

- **Zero-overhead**: 데이터 변경 없을 때 네트워크 트래픽 제로
- **Geo-distribution**: 멀리 떨어진 노드 간 효율적 라우팅
- **Dynamic**: 동적 토픽/노드 탐색 지원
- **DDS 브리징**: `zenoh-plugin-ros2dds`를 통해 기존 ROS2 DDS 네트워크와 호환

**핵심 통찰**: Zenoh은 ROS2 DDS의 대안으로 부상하고 있으며, 특히 드론 스웜과 같은 분산 환경에서 낮은 네트워크 부하로 효율적인 다대다 통신을 가능하게 합니다. `agnocast`와 `vlink` 같은 경쟁 솔루션도 등장하며, 미들웨어 생태계가 활발히 성장 중입니다.

---

## 5. 헌터킬러 Applications 적용

> 📎 **출처**: raw/articles/2026-08-10-ros2-drone-github-data.md, raw/articles/2026-08-10-px4-release-notes.md

### 5.1 자윅 타격(Hunter-Killer) 플랫폼

| 프로젝트 | ⭐ | 설명 |
|---|---|---|
| **aerial-autonomy-stack** | 559 | perception-based PX4/ArduPilot 드론 스웜 프레임워크. YOLO + LiDAR + NVIDIA Jetson 통합. 스웜 수준의 킬체인 구현 가능. |
| **Langostino** (swarm-subnet) | 175 | ROS2 + AI 기반 자윅 드론 플랫폼. 비트텐서(Bittensor) 통합으로 AI 기반 비행 제어. 자율 비행에서 시작해 스웜 레벨 임무 수행 가능. |
| **drone-racing-dataset** (tii-racing) | 129 | 고속 자윅 비행 데이터셋. computer-vision, control, path-planning, visual-inertial-odometry 포함. |
| **Autonomous-drone-navigation** (ahmedeltaher) | 38 (이전 수집) | GNSS-Denied 실내 환경에서 광류+IMU+Lidar SLAM. PX4/ArduPilot + ROS2 + MAVSDK-Python 통합. |

### 5.2 안전/방어/취소 메커니즘

- **PX4 보안 패치**: v1.17.0-rc2에서 CVE-2026-32705 (BST device name buffer overflow) 및 CVE-2026-32706 (CRSF 변수 버퍼 오버플로) 등 보안 취약점이 패치되었습니다.
- **Zenoh 암호화/인증**: `zenoh-plugin-ros2dds`와 같은 미들웨어 수준의 보안 기능이 헌터킬러 드론의 C2(지시·제어) 통신 보안에 기여할 수 있습니다.
- **YOLO 기반 적 드론 식별**: 실시간 객체 검출을 통해 미확인 드론(Unknown Drone)을 식별하고 분류할 수 있는 능력은 방어적 카운터UAS(C-UAS) 시스템의 핵심입니다.
- **Kill-Switch/긴급 취소**: PX4의 Offboard 제어 모드에서는 ROS2 노드가 비행 명령을 중단할 수 있어, 중앙 제어 시스템이 즉시 비행을 중단시킬 수 있습니다. 이는 인간승인 게이트(Human-in-the-Loop)와 결합하여 안전한 자융 제어가 가능합니다.

### 5.3 GNSS-Denied 생존항법

- **tentone/tello-ros2** (⭐213): DJI Tello 드론을 위한 ROS2 노드로, 실내 GNSS-Denied 환경에서 Visual SLAM 기반 위치 추정을 지원합니다.
- **PX4 ekf2 (EKF2)**: v1.16.2 릴리즈에서 "fix(ekf2): allow optical flow to start when range finder is height reference" 패치가 적용되었습니다. 이는 광류 센서와 레이더 높이 측정을 결합한 GNSS-Denied 항법을 개선합니다.
- **aerial-autonomy-stack** (⭐559): LiDAR + 시각-지도 매칭을 통한 GNSS-Denied 내비게이션을 지원하는 통합 프레임워크입니다.

---

## 6. 결론

### 6.1 요약

| 영역 | 핵심 동향 |
|---|---|
| **핵심 패키지** | PX4-Autopilot(⭐12371)이 생태계 중심. aerial-autonomy-stack(⭐559)이 YOLO+LiDAR+Jetson 스웜 프레임워크로 주목받음. |
| **객체인식** | YOLOv8/v11이 실시간 객체 검출 표준. 시뮬레이션(PX4 SITL/Gazebo) → 실드론(Jetson Orin) 확장 중. |
| **제어 인터페이스** | PX4 v1.18.0-beta2(2026-08-09) 출시. px4_ros_com(⭐220) + Offboard 모드가 표준. |
| **미들웨어** | Zenoh이 ROS2 DDS 대체/보완. zenoh-plugin-ros2dds(⭐296), agnocast(⭐196), vlink(⭐122) 등 경쟁 구도 형성. |
| **헌터킬러** | aerial-autonomy-stack, Langostino 등 실제 전술적 응용 프로젝트 활발. PX4 보안 패치 + Zenoh 암호화로 C2 보안 강화. GNSS-Denied 항법도 EKF2/gisnav 수준 발전. |

### 6.2 향후 과제

1. **시뮬레이션 → 실드론**: PX4 SITL/Gazebo → 실제 하드웨어(NVIDIA Jetson Orin) 이식. aerial-autonomy-stack이 이를 위한 원스톱 프레임워크 제공.
2. **GNSS-Denied 내비게이션**: 시각-지도 매칭 + Lidar+IMU 융합, Zenoh 기반 스웜 공유 지도.
3. **보안 강화**: Zenoh 암호화 + PX4 보안 패치(CVE-2026-32705/32706), 헌터킬러 C2 통신 보호.
4. **실시간 객체인식**: YOLOv8/v11 경량화 모델 + ROS2 QoS 최적화.
5. **인간승인 게이트(Human-in-the-Loop)**: PX4 Offboard 제어 중단 메커니즘 + Kill-Switch를 통한 안전한 자율 타격 시스템 구축.

### 6.3 참고 자료

- GitHub Search API 결과: `raw/articles/2026-08-10-ros2-drone-github-data.md`
- PX4 릴리즈 노트: `raw/articles/2026-08-10-px4-release-notes.md`
- ArduPilot 릴리즈 노트: `raw/articles/2026-08-10-ardupilot-release-notes.md`
- PX4 공식 문서: `raw/articles/2026-08-10-px4-docs-main.md`
- ROS2 공식 문서: `raw/articles/2026-08-10-ros2-docs-rolling.md`
