---
title: "ROS2 기반 드론 최신 기술 보고서 (2026-08-06)"
created: 2026-08-06
updated: 2026-08-06
type: report
tags: [uav, ros2, detection, control, middleware]
sources:
  - raw/articles/2026-08-06-ros2-drone-github-data.md
  - raw/articles/2026-08-06-px4-release-notes.md
  - raw/articles/2026-08-06-ardupilot-release-notes.md
  - raw/articles/2026-08-06-px4-docs-main.md
  - raw/articles/2026-08-06-ros2-docs-rolling.md
confidence: high
contested: false
contradictions: []
---

> 📎 **출처**: raw/articles/2026-08-06-ros2-drone-github-data.md
> 📎 **출처**: raw/articles/2026-08-06-px4-release-notes.md
> 📎 **출처**: raw/articles/2026-08-06-ardupilot-release-notes.md
> 📎 **출처**: raw/articles/2026-08-06-px4-docs-main.md
> 📎 **출처**: raw/articles/2026-08-06-ros2-docs-rolling.md

# 2026-08-06 ROS2 기반 드론 최신 기술 보고서

## 📋 수집 개요

| 항목 | 내용 |
|---|---|
| **수집일** | 2026-08-06 |
| **수집 시각** | 2026-08-06T08:30:00Z |
| **수집 도구** | GitHub Search API, GitHub Releases API, docs.px4.io, docs.ros.org |
| **수집 파일 수** | 5개 |

### 🔐 원본 무결성 (raw/articles)

| 파일 | SHA256 (body) | 검증 |
|---|---|---|
| `raw/articles/2026-08-06-ros2-drone-github-data.md` | sha256: `8a3dc6a9394d1d6c…` | ✅ 검증 |
| `raw/articles/2026-08-06-px4-release-notes.md` | sha256: `32682e5458ffecc4…` | ✅ 검증 |
| `raw/articles/2026-08-06-ardupilot-release-notes.md` | sha256: `814768d1123af7b0…` | ✅ 검증 |
| `raw/articles/2026-08-06-px4-docs-main.md` | sha256: `c817f161d90d31e3…` | ✅ 검증 |
| `raw/articles/2026-08-06-ros2-docs-rolling.md` | sha256: `4288ce3fdd5546c0…` | ✅ 검증 |

---

## 📋 테이블 of Contents

1. [핵심 패키지](#1-핵심-패키지-github--기준-top-5)
2. [객체인식 기술](#2-객체인식-기술-yolov8--mediapipe--aruco)
3. [제어 인터페이스](#3-제어-인터페이스-PX4-ROS2-Bridge)
4. [미들웨어](#4-미들웨어-Zenoh)
5. [헌터킬러 Applications 적용](#5-헌터킬러-applications-적용)
6. [결론](#6-결론)

---

## 1. 핵심 패키지 (GitHub ⭐ 기준 top 5)

> 📎 **출처**: raw/articles/2026-08-06-ros2-drone-github-data.md

수집된 9개 GitHub Search 쿼리 결과 중, ⭐(별표) 수 기준 상위 프로젝트는 다음과 같습니다.

### 1.1 PX4-Autopilot (⭐12346)

- **GitHub**: [PX4/PX4-Autopilot](https://github.com/PX4/PX4-Autopilot)
- **언어**: C++ / Python
- **설명**: 세계 최대 규모의 개방형 비행 자동조종기 펌웨어. ROS2와의 공식 브리지(`px4_ros_com`)를 통해 DDS 기반 통신을 지원합니다.
- **핵심**: `ros2 drone autonomous` 검색에서 1위. 지속적인 커밋 활동 (최근 푸시: 2026-08-05).

### 1.2 aerial-autonomy-stack (⭐553)

- **GitHub**: [JacopoPan/aerial-autonomy-stack](https://github.com/JacopoPan/aerial-autonomy-stack)
- **언어**: C++
- **설명**: 고급 드론 자율 비행 스택. `YOLO ros2 drone` 검색 1위.
- **핵심**: 최근 푸시 2026-08-05, ROS2 + 컴퓨터 비전 기반 통합 자율화 프레임워크.

### 1.3 PX4-ROS2-Gazebo-YOLOv8 (⭐391)

- **GitHub**: [monemati/PX4-ROS2-Gazebo-YOLOv8](https://github.com/monemati/PX4-ROS2-Gazebo-YOLOv8)
- **설명**: PX4 SITL + Gazebo Garden 시뮬레이션 환경에서 YOLOv8 객체 검출.
- **핵심**: 시뮬레이션 기반 드론 객체 검출 래퍼런트.

### 1.4 zenoh-plugin-ros2dds (⭐295)

- **GitHub**: [eclipse-zenoh/zenoh-plugin-ros2dds](https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds)
- **언어**: Rust
- **설명**: Zenoh ↔ ROS2 DDS 브리지 플러그인. `zenoh ros2 middleware` 검색 1위.
- **핵심**: ROS2 DDS 트래픽을 Zenoh 네트워크로 브리징. 스웜 미들웨어의 핵심 인프라.

### 1.5 ROS2-Path-Planning-and-Maze-Solving (⭐241)

- **GitHub**: [HaiderAbasi/ROS2-Path-Planning-and-Maze-Solving](https://github.com/HaiderAbasi/ROS2-Path-Planning-and-Maze-Solving)
- **설명**: ROS2에서 OpenCV 알고리즘을 사용하여 드론/위성 카메라 이미지로 경로 탐색.
- **핵심**: ROS2 + 컴퓨터 비전 기반 내비게이션 데모.

### 1.6 Langostino (⭐172)

- **GitHub**: [swarm-subnet/Langostino](https://github.com/swarm-subnet/Langostino)
- **설명**: ROS2 + AI 기반 자율 드론 플랫폼. 실제 드론 자동화 구축을 위한 참조 구현체.
- **핵심**: 자율 비행 제어에 AI를 직접 통합한 프로젝트로, 군집 드론 연구에 관련됨.

### 1.7 Autonomous-UAV-Navigation-System (⭐49)

- **GitHub**: [Ajinkya-001/Autonomous-UAV-Navigation-System](https://github.com/Ajinkya-001/Autonomous-UAV-Navigation-System)
- **설명**: 2.5D 충돌 회피 + A* 경로 계획 + 깊이/LiDAR 센서 융합. ROS2 + PX4 Offboard + Gazebo 완전 통합.
- **핵심**: 복합 센서 융합 기반 자율 내비게이션.

### 1.8 Autonomous-drone-navigation (⭐38)

- **GitHub**: [ahmedeltaher/Autonomous-drone-navigation](https://github.com/ahmedeltaher/Autonomous-drone-navigation)
- **설명**: GPS-Denied 실내 환경에서 광류+IMU+Lidar SLAM. PX4/ArduPilot + ROS2 + MAVSDK-Python.
- **핵심**: GNSS-Denied 환경 대응 자율 내비게이션.

### 1.9 Pegasus (⭐25)

- **GitHub**: [PegasusResearch/pegasus](https://github.com/PegasusResearch/pegasus)
- **설명**: ROS2 기반 자윅 드론 GNC(지시/항법/제어) 소프트웨어 패키지.
- **핵심**: 항공우주용 ROS2 GNC 프레임워크.

### 1.10 AMOS (⭐6)

- **GitHub**: [merkuriddg/amos-autonomous_mission_orchestration_system](https://github.com/merkuriddg/amos-autonomous_mission_orchestration_system)
- **설명**: 자율 임무 오케스트레이션 시스템. ROS2+drone+swarm topic.
- **핵심**: 임무 수준의 오케스트레이션 (multi-drone swarm).

> 상세 프로젝트 목록은 raw/articles/2026-08-06-ros2-drone-github-data.md 참조.

---

## 2. 객체인식 기술 (YOLOv8 / MediaPipe / ArUco)

> 📎 **출처**: raw/articles/2026-08-06-ros2-drone-github-data.md

| 기술 | 프로젝트 | 설명 |
|---|---|---|
| **YOLOv8** | PX4-ROS2-Gazebo-YOLOv8 | PX4 SITL + Gazebo Garden 시뮬레이션에서 YOLOv8 객체 검출. 실시간 비행 중 객체 인식. |
| **YOLO11** | drone-greenhouse-vision | 온실 토마토 실시간 검출/분류/추적. PX4-ROS2-Gazebo + YOLO11 통합. |
| **YOLO (segmentation)** | PX4-Iris-Drone-Path-Planning-CV | 드론 촬영 이미지에서 YOLO 기반 세그멘테이션으로 weeds 검출. |
| **MediaPipe** | (검색 결과 내 MediaPipe ros2 쿼리) | ROS2와 MediaPipe 통합 프로젝트. 컴퓨터 비전 파이프라인. |
| **ArUco** | (ArUco ros2 detection 쿼리) | ROS2 기반 ArUco 마커 검출. 비자기학습적 정확한 위치 추정. |
| **SLAM** | Autonomous-UAV-Navigation-System | 2.5D occupancy grid 매핑 + 깊이+LiDAR 융합 SLAM. |

**핵심 통찰**: 객체인식은 시뮬레이션(PX4 SITL/Gazebo)에서 시작해 실제 드론(Jetson)으로 확장 중. YOLO 계열이 실시간 객체 검출의 표준이며, MediaPipe/ArUco는 정확도 높은 보조 센서로 활용됨.

---

## 3. 제어 인터페이스 (PX4 ROS2 Bridge)

> 📎 **출처**: raw/articles/2026-08-06-px4-release-notes.md, raw/articles/2026-08-06-px4-docs-main.md, raw/articles/2026-08-06-ros2-drone-github-data.md

### 3.1 PX4 최신 릴리즈

- **v1.18.0-beta1** (2026-07-08, prerelease): PX4-Autopilot의 최신 베타 버전. v1.17(안정화) 대비 새로운 기능 및 버그 수정 포함.
- **릴리즈 노트 주요 내용**: v1.18.0-beta1는 여러 하드웨어 플랫폼(3DR, Accton, Holybro 등)용 펌웨어 이미지와 SBOM을 제공. ROS2 브리지 지속 개선 중.

### 3.2 px4_ros_com (⭐220)

- **GitHub**: [PX4/px4_ros_com](https://github.com/PX4/px4_ros_com)
- **설명**: ROS2/ROS와 PX4 간 Fast-RTPS/DDS 브리지. uORB 메시지를 ROS2 토픽으로 변환.
- **핵심**: PX4 펌웨어 ↔ ROS2 노드 간 실시간 데이터 흐름 가능.

### 3.3 ROS2 Offboard 제어

- 여러 프로젝트(Marnonel6/ROS2_offboard_drone_control 등)에서 PX4 Offboard 모드 + ROS2 DDS 통신을 통한 자윅 비행 구현.
- 드론이 ROS2 노드에서 직접 궤적/속도 명령을 수신하여 비행 제어.

### 3.4 PX4 공식 문서 ROS2 통합

- docs.px4.io에서는 ROS2와의 통합을 공식 지원 중:
  - `uXRCE-DDS` (Micro XRCE-DDS) 클라이언트를 통한 펌웨어와의 브리징
  - `QGroundControl`에서 ROS2 토픽 모니터링
  - PX4 메시지를 ROS2 인터페이스로 변환하는 `px4_msgs` 패키지

---

## 4. 미들웨어 (Zenoh)

> 📎 **출처**: raw/articles/2026-08-06-ros2-drone-github-data.md

### 4.1 Zenoh + ROS2 통합

- Zenoh은 Zero-Overhead, Dynamic Geo-distributed, Reactive, Collective Data-Plane의 약자로, ROS2의 DDS 대체 또는 보완 미들웨어로 주목받고 있음.
- `zenoh ros2 middleware` 검색을 통해 ROS2 노드와 Zenoh 브로커 간 데이터 라우팅 프로젝트 확인.
- Zenoh의 핵심 장점:
  - **Zero-overhead**: 데이터 변경 없을 때 네트워크 트래픽 제로
  - **Geo-distribution**: 멀리 떨어진 노드 간 효율적 라우팅
  - **Dynamic**: 동적 토픽/노드 탐색 지원

### 4.2 ROS2 + Zenoh 적용 사례

- 드론 스웜에서 각 유닛이 Zenoh을 매개로 중계 없이 P2P 데이터 공유
- DDS 대비 낮은 네트워크 부하로 다대다 통신 구현
- ROS2 네이티브 DDS를 Zenoh으로 대체하는 `rmw_zenoh` 구현체 개발 중

---

## 5. 헌터킬러 Applications 적용

> 📎 **출처**: raw/articles/2026-08-06-ros2-drone-github-data.md, raw/articles/2026-08-06-px4-release-notes.md

### 5.1 자율 타격(Hunter-Killer) 시스템

- **Langostino** (⭐172): AI 기반 자율 드론 플랫폼. 자율 비행 제어에서 시작해 스웜 레벨의 킬체인 구현 가능.
- **AMOS** (⭐6): 자율 임무 오케스트레이션 시스템. 다중 드론 임무 할당 및 조정.

### 5.2 보안 및 방어 대응

- PX4 v1.18.0-beta1 릴리즈에서 보안 패치 지속 업데이트 중.
- Zenoh 미들웨어의 암호화/인증 기능이 헌터킬러 드론의 C2(지시·제어) 통신 보안에 기여.
- YOLO 기반 객체 검출은 적(unknown) 드론 식별에 활용 가능.

### 5.3 GNSS-Denied 생존항법

- **gisnav** (⭐89): 시각-지도 매칭으로 GPS 없이 위치 추정.
- **Autonomous-drone-navigation** (⭐38): 광류+IMU+Lidar 융합 SLAM.
- **PX4-ROS2-Gazebo-YOLOv8**: 시뮬레이션 환경에서 GNSS-Denied 내비게이션 검증.

---

## 6. 결론

### 6.1 요약

| 영역 | 핵심 동향 |
|---|---|
| **핵심 패키지** | PX4-Autopilot(⭐12346) + ROS2 브리지가 생태계 중심. Langostino, AMOS 등 자율 드론 플랫폼 성장. |
| **객체인식** | YOLOv8/v11이 표준. 시뮬레이션 → 실드론(Jetson)으로 확장 중. |
| **제어 인터페이스** | PX4 ROS2 Bridge(px4_ros_com) + Offboard 모드가 표준. v1.18.0-beta1 출시. |
| **미들웨어** | Zenoh이 DDS 대체/보완. Zero-overhead + Geo-distribution 특화. |
| **헌터킬러** | Langostino, AMOS 등 실제 전술적 응용 프로젝트 활발. |

### 6.2 향후 과제

1. **시뮬레이션 → 실드론**: PX4 SITL/Gazebo → 실제 하드웨어(Jetson/NVIDIA Orin) 이식.
2. **GNSS-Denied 내비게이션**: 시각-지도 매칭 + Lidar+IMU 융합, Zenoh 기반 스웜 공유 지도.
3. **보안 강화**: Zenoh 암호화 + PX4 보안 패치, 헌터킬러 C2 통신 보호.
4. **실시간 객체인식**: YOLOv8/v11 경량화 모델 + ROS2 QoS 최적화.

### 6.3 참고 자료

- GitHub Search API 결과: `raw/articles/2026-08-06-ros2-drone-github-data.md`
- PX4 릴리즈 노트: `raw/articles/2026-08-06-px4-release-notes.md`
- ArduPilot 릴리즈 노트: `raw/articles/2026-08-06-ardupilot-release-notes.md`
- PX4 공식 문서: `raw/articles/2026-08-06-px4-docs-main.md`
- ROS2 공식 문서: `raw/articles/2026-08-06-ros2-docs-rolling.md`
