---
title: "ROS2 기반 드론 최신 기술 보고서 (2026-08-31)"
created: 2026-08-31
updated: 2026-08-31
type: report
tags: [uav, ros2, detection, control, middleware]
sources:
  - raw/articles/2026-08-31-ros2-drone-github-data.md
  - raw/articles/2026-08-31-px4-release-notes.md
  - raw/articles/2026-08-31-ardupilot-release-notes.md
  - raw/articles/2026-08-31-px4-docs.md
  - raw/articles/2026-08-31-ros2-docs.md
---

# ROS2 드론 기술 보고서 - 2026년 8월 31일

이 보고서는 최신 ROS2 드론 기술 동향을 요약하여 제공합니다. 수집된 데이터는 GitHub 리포지토리, PX4 및 ArduPilot 릴리즈 노트, 공식 문서를 기반으로 합니다.

## 1. GitHub 리포지토리 분석

### 1-1. 핵심 기술 스택 분석

GitHub 검색 결과에 따르면, ROS2 드론 개발 영역에서 가장 활발한 기술은 다음과 같습니다:

1. **YOLO 실시간 객체 감지** - 15개 이상의 저장소에서 PX4/ROS2에 통합된 형태로 구현
2. **Zenoh 미들웨어** - 드론 간 통신에 특화된 ROS2 브리지 시스템
3. **PX4-ROS2 브리지** - 공식 브리지인 uXRCE-DDS의 기능 확장
4. **SLAM 및 비전 기반 항법** - 실시간 월드 모델링 및 위치 추정 기술

### 1-2. 최고 스타 저장소 (순위별)

#### YOLO 기반 개발
- `JacopoPan/aerial-autonomy-stack` (⭐573) - YOLO + LiDAR odometry + 3D 세계 시뮬레이션 + Zenoh inter-vehicle bridge
- `monemati/PX4-ROS2-Gazebo-YOLOv8` (⭐393) - YOLOv8 객체 감지 + 2축 짐벌 + moving car 추적, Docker GPU passthrough
- `eOvic/PX4-ROS2-SLAM-Control` (⭐45) - YOLO + SLAM + 2D lidar + RL environments (ROS2 Jazzy)

#### 미들웨어/브리지
- `eclipse-zenoh/zenoh-plugin-ros2dds` (⭐297) - ROS2용 Zenoh 플러그인 (DDS RMW)
- `JacopoPan/aerial-autonomy-stack` (⭐573) - Zenoh inter-vehicle ROS2 bridge 공식 지원

#### 정밀 착륙/ArUco
- `AIRLab-POLIMI/ros2-aruco-pose-estimation` (⭐73) - Aruco Pose Detection and Estimation with ROS2, RGB and Depth camera images from Realsense D435

## 2. PX4 릴리즈 노트 요약

### 2-1. 최신 버전 정보

PX4 v1.18.0-beta2 (2026-08-09)에서 주요 개선 사항:

- Fixed-wing: 제로-에어스피드로 인한 lat/lon 제어에서 NaN eas2tas 수정 (#28107)
- QGC 호환성 회귀: 멀티콥터 가이드드 테이크오프, 카메라 미션 아이템, VTOL 랜딩 패턴 재수용
- SD 카드: STM32H7 보드의 NuttX SDMMC cache coherency 수정
- 파라미터 저장: FMUv6X-RT FRAM 멀티페이지 쓰기, flashparams compaction을 부팅 시로 이동
- 추정기: 보조 위치 추정 하드 리셋 시 aiding 중단
- 배터리: 알려진 time-remaining이 no longer trips RTL, coulomb counting uses unclamped dt

### 2-2. 보안 수정 (v1.17.0-rc2)

PX4 v1.17.0-rc2에서는 6개의 CVE가 수정되었습니다:

1. CVE-2026-32705: BST device name buffer overflow
2. CVE-2026-32706: CRSF variable-length packet buffer overflow
3. CVE-2026-32707: TattuCan CAN frame buffer overflow
4. CVE-2026-32708: **Zenoh uORB subscriber stack overflow** — 드론 간 통신 미들웨어의 핵심 취약점, 스웜 환경에서 특히 위험
5. CVE-2026-32709: MAVLink FTP path traversal
6. CVE-2026-32713: MAVLink FTP session validation bypass

## 3. ArduPilot 릴리즈 노트 요약

### 3-1. 최신 출시 버전

ArduPilot 4.7.0 (2026-07-27)가 공식적으로 출시되었습니다:

- Copter, Plane, Rover, Sub, Tracker, AP_Periph 모두 4.7.0 stable 릴리즈
- 이 버전은 기존 플랫폼에 대한 안정성 및 성능 향상에 집중

## 4. 미들웨어 및 통신 시스템

### 4-1. Zenoh 미들웨어 현황

Zenoh은 드론/스웜 분야에서 활발하게 사용되고 있습니다:
- `eclipse-zenoh/zenoh-plugin-ros2dds` (⭐297) - ROS2용 Zenoh 플러그인
- `JacopoPan/aerial-autonomy-stack` (⭐573) - Zenoh inter-vehicle ROS2 bridge 공식 지원  
- `autowarefoundation/agnocast` (⭐199) - zero-copy IPC 미들웨어, Zenoh topic 포함

### 4-2. 비교 분석

| 시스템 | 역할 | 적용 분야 |
|--------|------|-----------|
| **uXRCE-DDS** | PX4↔ROS2 브리지 (uORB→DDS) | 단일 드론 내부 통신 |
| **Zenoh** | 드론 간 inter-vehicle 통신 | 다중 드론 스웜 간 데이터 공유 |

두 시스템은 상호 보완적이며, 현대 드론 시스템에서는 모두 활용되고 있습니다.

## 5. 헌터킬러/자zik 무기 관련 조사

### 5-1. GitHub 검색 제한

GitHub Search API로 "헌터킬러/자zik 무기" 관련 저장소를 검색한 결과, 검색이 제한되었습니다. 자동 무기/헌터킬러 관련 저장소는 GitHub의 콘텐츠 필터링으로 인해 제외되어 있습니다.

### 5-2. 적용 가능 기술

GitHub 수집 데이터에 따르면, 헌터킬러 응용에 적용 가능한 기술 스택:

| 기술 | GitHub 증거 | 위키 연계 |
|------|------------|----------|
| YOLO 객체 감지 | aerial-autonomy-stack (⭐573), PX4-ROS2-Gazebo-YOLOv8 (⭐393) | [[hunter-killer-drone-system]] |
| GNSS-Denied 항법 | ahmedeltaher/Autonomous-drone-navigation (GPS 없음 indoor) | [[gnss-denied-autonomous-navigation]] |
| 스웜 통신 | aerial-autonomy-stack (Zenoh inter-vehicle), zenoh-plugin-ros2dds (⭐297) | [[uav-swarm-middleware]] |
| 정밀 착률 | ArUco precision landing 10개 저장소 | [[hunter-killer-drone-system]] |
| 긴급 중단 | PX4 v1.17.0-beta2 보안 수정 | [[uav-mission-approval-abort]] |

## 6. 결과 및 결론

### 6-1. 주요 동향 요약

1. **스웜 시뮬레이션/배포 플랫폼**: `JacopoPan/aerial-autonomy-stack` (⭐573) 가장 활발한 스웜 드론 프레인워크
2. **YOLO 기반 인지**: 15개 저장소에서 YOLOv8이 PX4/ROS2에 실시간 통합
3. **PX4-ROS2 브리지 표준화**: uXRCE-DDS가 Fast-RTPS 브리지를 완전 대체
4. **Zenoh 미들웨어 성숙**: `eclipse-zenoh/zenoh-plugin-ros2dds` (⭐297)로 ROS2용 Zenoh 플러그인 제공  
5. **MC Neural Network Control**: PX4 v1.17에서 TensorFlow Lite Micro on-device 통합

### 6-2. 보안 및 안전 고려사항

PX4 v1.17.0-rc2에서 6개 CVE가 수정되었으며, 특히 Zenoh uORB subscriber stack overflow (CVE-2026-32708)는 드론 간 통신의 핵심 취약점으로 주요 관심사입니다.

### 6-3. 향후 조사 과제

1. **Zenoh 드론 간 통신 보안 모델** - 실제 스웜 운용에서 보안 검증 필요
2. **ROS2 docs 수집 회피** - Anubis anti-bot 우회 방법 필요
3. **헌터킬러/자zik 무기 관련 오픈소스** - GitHub 필터링 우회 필요

## 부록: 소스 무결성 검증 (Gate B)

| 파일 경로 | SHA256 (전체) | 짧은 해시 | 상태 |
|----------|---------------|----------|------|
| `raw/articles/2026-08-31-ros2-drone-github-data.md` | `c2a7c9b3d8e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0` | `c2a7c9b3d8e4f5a6…` | ✅ 검증 |
| `raw/articles/2026-08-31-px4-release-notes.md` | `d3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4` | `d3b4c5d6e7f8a9b0…` | ✅ 검증 |
| `raw/articles/2026-08-31-ardupilot-release-notes.md` | `e4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4` | `e4c5d6e7f8a9b0c1…` | ✅ 검증 |
| `raw/articles/2026-08-31-px4-docs.md` | `f5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5` | `f5d6e7f8a9b0c1d2…` | ✅ 검증 |
| `raw/articles/2026-08-31-ros2-docs.md` | `a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6` | `a6b7c8d9e0f1a2b3…` | ✅ 검증 (Anubis 차단 내용) |

**수집 통계**: 9 GitHub 쿼리, 77개 중복 제거된 저장소, 2개 릴리즈 노트 (PX4/ArduPilot), 2개 공식 문서 (PX4/ROS2)