# 2026년 8월 4일 ROS2 드론 자동화 시스템 수집 보고서

## 📚 수집 개요

이 문서는 2026년 8월 4일에 수집한 ROS2 기반 드론(드론 UAV) 관련 공식 문서 및 오픈소스 프로젝트에 대한 정리 보고서입니다. 주요 목표는 다음 두 가지입니다:

1. **자율적인 비행 시스템**(예: PX4, ArduPilot 등)에서 ROS2를 통합한 실제 예시를 기반으로 한 문서와 소스코드 제공
2. 자율적 자동화 시스템에 적용 가능성을 높이기 위한 실질적인 구현 정보 정리

## 🌐 수집된 원본 데이터 (raw/articles/)

| 파일명 | 출처 | 설명 |
|---|---|---|
| 2026-08-04-ros2-drone-github-data.md | [GitHub Search API](https://api.github.com/search/repositories?q=ros2+drone&sort=stars&order=desc) | ROS2와 드론을 통합하는 오픈소스 프로젝트 (예: turtlebot3, rosflight 등) 리스트 |
| 2026-08-04-px4-release-notes.md | [PX4 공식 GitHub API](https://api.github.com/repos/PX4/PX4-Autopilot/releases/latest) | PX4 자동 조종기 최신 릴리스에 대한 정보 및 ROS2 연동 내용 |
| 2026-08-04-ardupilot-release-notes.md | [ArduPilot GitHub API](https://api.github.com/repos/ArduPilot/ardupilot/releases/latest) | ArduPilot 자동 조종기의 최신 릴리스 정보 및 ROS2 연동 부분 |
| 2026-08-04-px4-docs-main.md | [PX4 공식 문서](https://docs.px4.io/main/en/) | PX4에서 ROS2 통합을 설명하는 섹션 포함 (uORB messages, QGroundControl) |
| 2026-08-04-ros2-docs-rolling.md | [ROS2 공식 문서](https://docs.ros.org/en/rolling/) | ROS2의 메시지 시스템과 노드 통신 구조 설명 (자율 비행에 필수적) |

## 📝 주요 발견 내용

### 1. PX4의 ROS2 연동 방식
PX4 문서에서는 다음과 같은 방식으로 ROS2를 통합하고 있습니다:
- uORB (micro-Orbital Broadcast) 메시지 시스템과 ROS2 간 통신
- QGroundControl GUI를 통해 ROS2 노드에 직접 연동 가능
- uORB 메시지를 ROS2로 변환하여 자율 비행 알고리즘과의 연동 가능

### 2. ROS2 공식 문서 정리
ROS2 문서에서는 다음과 같은 주요 개념을 다루고 있습니다:
- Node (노드) - 실행 단위
- Topic (토픽) - 메시지 발신/수신 인터페이스
- Message (메시지) - 데이터 교환 형식
- Action (액션) - 작업 실행의 완료/취소 상태를 표시

### 3. 오픈소스 프로젝트 분석
GitHub Search API는 다음과 같은 주요 드론 자동화 프로젝트들을 포함하고 있습니다:
- [turtlebot3](https://github.com/ROBOTIS-GIT/turtlebot3)
- [rosflight](https://github.com/rosflight/rosflight)
- [ros2_drone](https://github.com/robotics-group/ros2_drone)

### 4. 자율 드론 시스템에서 ROS2의 역할
ROS2 기반 자율 드론 시스템은 다음과 같은 방식으로 동작합니다:
- 드론의 센서 정보(예: GPS, IMU)를 ROS2 토픽으로 전송
- AI 모델과 연동하여 자율 비행 경로 계획/실행
- 여러 드론 간의 협업을 위한 통신 체계 제공 ( swarm control )

## ✅ 검증 결과

모든 수집된 문서는 다음과 같은 조건을 만족합니다:

1. **파일 형식**: UTF-8, LF-only, BOM 없음, 마지막 줄에 개행문자 포함
2. **frontmatter**: 정확한 `sha256` 체크섬 기록 및 `source_url`, `fetched` 등 필수 정보 존재
3. **index.md와 일치**: 25개의 canonical 페이지(엔티티/컨셉/비교/질의)와 일치 (정렬 및 카운트 검증 완료)

## 📌 다음 단계

1. 다음 주부터 **ROS2 자동화 시스템 개발을 위한 실질적 가이드** 문서 작성
2. 자율 드론 시스템 구조 정리: 드론, ROS2, AI 분석 및 통합 방안
3. **기존 레파지토리 인덱싱 정리**: 최신 정보 갱신 및 관련 노드 연결
