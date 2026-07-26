---
title: UAV Swarm Middleware (MAVLink / ROS 2 / DDS)
created: 2026-07-26
updated: 2026-07-26
type: concept
tags:
  - uav
  - swarm
  - software
  - communication
sources:
  - raw/articles/2022-faster-consensus-via-a-sparser-controller-0.md
  - raw/articles/2017-a-survey-of-multi-agent-deep-reinforcement-learning-with-communication-0.md
  - raw/articles/2024-pacnav-enhancing-collective-navigation-for-uav-swarms-in-communication-denied-env.md
  - raw/articles/2024-ros2swarm-a-ros-2-package-for-swarm-robot-behaviors.md
confidence: medium
contested: false
contradictions: []
---

# UAV Swarm Middleware (MAVLink / ROS 2 / DDS)

군집드론 소프트웨어 스택의 **L2(통신/미들웨어)** 계층. 개별 기체(펌웨어)와 상위 지능/제어 로직, 그리고 기체 상호간을 연결하는 메시지 버스다. 위키의 제어·합의 연구가 "통신이 있다/끊긴다"는 가정 하에 돌아가므로, 그 가정을 실제로 구현하는 층이다.

## 핵심 미들웨어

- **MAVLink**: PX4/ArduPilot 표준 경량 메시지 프로토콜. heartbeat/telemetry/command. 대역폭 작아 임베디드 적합하나 평문 전송 → 보안 취약 ([BGG, 2021] 블록체인 인증으로 보완).
- **ROS 2 / DDS**: 분산 노드 토픽 퍼블리시-서브스크라이브. QoS·실시간성 제어 가능. Companion Computer(온보드 컴퓨터) 위주로 군집 코디네이션 구현.
- **CycloneDDS / FastDDS**: ROS 2 하부 DDS 구현. 멀티캐스트로 대규모 스웜 브로드캐스트에 유리.

## 위키 증거와의 연결

- [Faster Consensus, 2022]는 합의 프로토콜에서 **"통신 지연은 홉 수에 비례 증가"** 임을 모델링. 이는 MAVLink 홉-바이-홉 relay나 ROS 2 멀티캐스트 토폴로지 설계와 직결 → 모두 연결보다 **전략적 희소 연결**이 수렴 빠르다.
- [Comm-MADRL Survey, 2017]는 MARL에서 통신을 "데이터링크가 아닌 조정 기제"로 재정의. 실제론 ROS 2 토픽 발행 패턴/주기 튜닝이 학습된 통신 정책을 구현하는 수단.
- [PACNav, 2024]는 통신두절 환경 복원력 강조 → 미들웨어가 끊겨도 기체가 지역관측으로 항법. 오프라인/store-and-forward 미들웨어 필요성 시사.

## 일반 지식 한계 명시

스택 비교는 제조사/커뮤니티 문서 기반 일반 지식. 위키 논문이 특정 미들웨어 벤치마크를 직접 측정한 건 아님. 실증 강화는 플랫폼 실측 논문 수집 필요 (→ `uav-autopilot-stacks`, `uav-swarm-simulation`).

## 관련 페이지

- [[uav-autopilot-stacks]] — MAVLink가 펌웨어와 상위 로직을 잇는 프로토콜
- [[uav-swarm-simulation]] — 미들웨어가 시뮬 노드와 어떻게 붙는지
- [[multi-agent-rl-uav-control]] — Comm-MADRL 통신 정책이 ROS 2 토픽으로 구현되는 지점
