---
title: "ROS2 기반 드론 최신 기술 보고서 (2026-08-29)"
created: 2026-08-29
updated: 2026-08-29
type: report
tags: [uav, ros2, detection, control, middleware]
sources:
  - raw/articles/2026-08-29-github-ros2-drone-data.md
  - raw/articles/2026-08-29-px4-release-notes.md
  - raw/articles/2026-08-29-ros2-release-notes.md
confidence: high
contested: false
contradictions: []
---

> 📎 **출처**: raw/articles/2026-08-29-github-ros2-drone-data.md

## 1. 핵심 패키지 (GitHub ⭐ 기준 top 5)

1. [ROS2-Drone-Project/autonomous-drone-control](https://github.com/ROS2-Drone-Project/autonomous-drone-control)  
   - 별표 수: 1250  
   - 설명: ROS2 기반 자율 비행 드론 제어 시스템  

2. [PX4-Autonomous-Flight/ros2_px4_bridge](https://github.com/PX4-Autonomous-Flight/ros2_px4_bridge)  
   - 별표 수: 890  
   - 설명: PX4 비행 콘트롤러와 ROS2 간의 다리 역할  

3. [Computer-Vision-YOLO/robotic-drone-detection](https://github.com/Computer-Vision-YOLO/robotic-drone-detection)  
   - 별표 수: 760  
   - 설명: YOLOv8를 사용한 드론 감지 및 추적  

4. [Drone-SLAM-ROS2/drone_slam_navigation](https://github.com/Drone-SLAM-ROS2/drone_slam_navigation)  
   - 별표 수: 620  
   - 설명: ROS2 기반 드론 SLAM 및 경로 계획  

5. [Zenoh-ROS2-Integration/drone_communication](https://github.com/Zenoh-ROS2-Integration/drone_communication)  
   - 별표 수: 480  
   - 설명: Zenoh을 통한 ROS2 드론 커뮤니케이션 시스템  

## 2. 객체인식 기술 (YOLOv8 / MediaPipe / ArUco)

- **YOLOv8**: Computer-Vision-YOLO/robotic-drone-detection 레포지토리에서 사용되는 최신 인공지능 모델로, 드론의 실시간 감지 및 추적을 가능하게 합니다.  
- **MediaPipe**: 실시간 비디오 분석을 통해 드론이 주변 환경을 인식하고, 이에 따라 비행을 조절할 수 있습니다.  
- **ArUco**: 고정된 마커를 활용하여 드론 위치 추정 및 목표 지점 지정을 가능하게 합니다.

## 3. 제어 인터페이스 (PX4 ROS2 Bridge)

- PX4-Autonomous-Flight/ros2_px4_bridge 레포지토리에서 제공하는 다리 역할로, PX4 비행 콘트롤러와 ROS2 시스템 간의 효율적인 통신이 가능하게 합니다.  
- 자율 비행 드론의 제어 및 상태 정보를 실시간으로 얻고 조정할 수 있습니다.

## 4. 미들웨어 (Zenoh)

- Zenoh-ROS2-Integration/drone_communication 레포지토리에서 활용되는 통신 프로토콜로, ROS2 시스템 내에서 드론 간 또는 드론과 지상국 간의 데이터 전송을 효율적으로 합니다.  
- 네트워크 지연이 적고, 실시간 데이터 처리가 가능합니다.

## 5. 헌터킬러 Applications 적용

- 드론의 자율 비행 및 센서 융합 알고리즘은 헌터킬러 시스템에 적용될 수 있습니다.  
- 실시간 감지와 추적 기술은 타겟을 지정하고 공격하는 데 사용됩니다.  
- 안전한 인터페이스가 필요하여 인간 승인 게이트가 적용되어야 합니다.

## 6. 결론

ROS2 기반 드론 시스템은 다양한 기술을 통합함으로써 자율 비행 및 객체 감지, 추적, 커뮤니케이션 등에 있어 뛰어난 성능을 발휘합니다. 특히, YOLOv8을 활용한 컴퓨터 비전 기술과 PX4와 ROS2 간의 통신을 제공하는 bridge 패키지는 이 분야에서 핵심적인 역할을 하고 있습니다. 이러한 기술들은 헌터킬러 시스템에 적용할 수 있으나, 반드시 안전, 방어 및 취소 차원이 포함되어야 합니다.