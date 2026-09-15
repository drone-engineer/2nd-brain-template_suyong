---
title: "ROS2 기반 드론 최신 기술 보고서 (2026-09-09)"
created: 2026-09-09
updated: 2026-09-09
type: report
tags: [uav, ros2, detection, control, middleware]
sources:
  - raw/articles/2026-09-09-ros2-drone-github-data.md
  - raw/articles/2026-09-09-px4-release-notes.md
  - raw/articles/2026-09-09-ardupilot-release-notes.md
confidence: high
contested: false
contradictions: []
---

> 📎 **출처**: raw/articles/2026-09-09-*.md

## 1. 핵심 패키지 (GitHub ⭐ 기준 top 5)
1. [PX4-ROS2-Gazebo-YOLOv8](https://github.com/monemati/PX4-ROS2-Gazebo-YOLOv8) (396 stars)
2. [aerial-autonomy-stack](https://github.com/JacopoPan/aerial-autonomy-stack) (593 stars)
3. [PX4-ROS2-SLAM-Control](https://github.com/eOvic/PX4-ROS2-SLAM-Control) (47 stars)
4. [PX4-Iris-Drone-Path-Planning-CV](https://github.com/Masudali23/PX4-Iris-Drone-Path-Planning-CV) (15 stars)
5. [ros2-auto-drone](https://github.com/SezginAtabas/ros2-auto-drone) (13 stars)

## 2. 객체인식 기술 (YOLOv8 / MediaPipe / ArUco)
### YOLO 기반 접근
- **PX4-ROS2-Gazebo-YOLOv8**: YOLOv8을 이용한 드론의 물체 인식 시스템 구현. PX4 SITL과 Gazebo Garden을 사용한 시뮬레이션 환경에서 개발.
- **aerial-autonomy-stack**: ROS2, YOLO, LiDAR 및 NVIDIA Jetson을 활용한 드론 스웜의 퍼셉션 기반 자율 주행 시스템.
- **PX4-ROS2-SLAM-Control**: YOLO 기반 인식과 2D LiDAR를 통합한 UAV 제어 및 SLAM 시스템.

### MediaPipe 기반 접근
- **MediaPipe-ROS2-PX4-Control**: MediaPipe, MAVSDK, PX4, Gazebo를 사용한 손 동작을 통한 드론 제어 시스템.
- **drone-gesture-control**: MediaPipe 손 인식 기술을 활용한 드론 제어 시스템.

### ArUco 기반 접근
- **Aruco_Tracker_ROS2_Drones**: PX4와 ROS2를 통한 ArUco 마커 인식과 정밀 이착륙 구현.
- **precision_landing**: ArUco 마커를 이용한 PX4 및 ROS2 기반 자동 정밀 이착륙 시스템.

## 3. 제어 인터페이스 (PX4 ROS2 Bridge)
### 주요 PX4 ROS2 브릿지
- **px4_ros_com**: PX4와 ROS2 간의 Fast-RTPS 브릿지로, ROS2/ROS 프로토콜을 지원.
- **uosm.isaac.px4_bridge**: Omniverse를 위한 PX4-Autopilot 확장.
- **TrajBridge**: Stanford Flightroom에서 Quadcopter 궤적 데이터를 입력받아 PX4에 해당 setpoint 출력.
- **px4-ros2-drone-simulation**: Gazebo를 통한 PX4 펌웨어 시뮬레이션 및 ROS2 프로그램 제어.

## 4. 미들웨어 (Zenoh)
### Zenoh 기반 시스템
- **Sonny**: Rust 기반의 소프트웨어 미들웨어인 Zenoh을 활용한 로봇용 초경량 마이크로커널. 메모리 누수 및 지연 문제를 제거.
- **hakoniwa-digital-twin**: Hakoniwa 프레임워크를 통해 가상 드론과 실제 로봇 간의 데이터 공유를 구현.

## 5. 헌터킬러 Applications 적용
가상의 "헌터킬러 어플리케이션" 시나리오에 따른 적용 사례:
1. **사용자 정의 목적**: 드론을 통해 실시간 인식된 대상을 추적하여 자동 제어 및 관리 가능한 스마트 컨트롤링.
2. **AI 기반 분류 시스템**: YOLO 기반으로 감지된 물체는 정확한 인식과 추적 및 실시간 정보 전달을 제공하여 헌터킬러 시스템의 효과성 제고.

## 6. 결론
ROS2 기반 드론 시스템은 YOLO, MediaPipe, ArUco 등 다양한 컴퓨터 비전 기술과 PX4 브릿지 및 Zenoh 미들웨어를 통해 자율주행 기능과 강력한 제어 성능을 갖추고 있습니다. 이는 현재 드론 연구 및 응용 분야의 발전을 이끄는 핵심적인 기술 집합으로, 향후 AI 기반의 더 높은 자동화와 통합 시스템이 가능해질 것으로 기대됩니다.