---
title: UAV Swarm Simulation (Gazebo / AirSim / Webots)
created: 2026-07-26
updated: 2026-07-26
type: concept
tags:
  - uav
  - swarm
  - software
  - simulation
sources:
  - raw/articles/2024-pacnav-enhancing-collective-navigation-for-uav-swarms-in-communication-denied-env.md
  - raw/articles/2018-closing-the-gap-in-swarm-robotics-simulations-an-extended-ardupilot-ga.md
confidence: medium
contested: false
contradictions: []
---

# UAV Swarm Simulation (Gazebo / AirSim / Webots)

군집드론 소프트웨어 스택의 **L3(시뮬레이션)** 계층. 알고리즘을 실기체 위험 없이 검증하는 필수 인프라. 위키 수집 논문 다수가 "시뮬에서 검증"을 전제로 하며, 그 시뮬 백엔드가 무엇인지 명시하는 게 재현성 핵심이다.

## 주요 시뮬레이터

- **Gazebo / Ignition (현 Gazebo Sim)**: ROS 2 표준 통합, 물리엔진(ODE/Bullet), 센서·플러그인 풍부. PX4 SITL과 직결.
- **AirSim** (Microsoft): Unreal Engine 기반 고품질 비전·심층 센서. 학습용(강화학습 비전)에 유리.
- **Webots**: 크로스플랫폼, 교육·연구용. ArduPilot SITL과 호환.
- **jMAVSim / PX4 SITL**: 경량 펌웨어 전용, 대규모 스웜 부하 테스트엔 부적합.

## 위키 증거와의 연결

- [PACNav, 2024]는 통신두절 집단 항법을 **시뮬레이션 프레임워크**로 검증. 대개 Gazebo + PX4 SITL 조합.
- *(일반 지식)* EM 사이드채널 도메인에선 커스텀 시뮬(예: TriSweep 4드론 프레임워크) 필요성 논의 있음 — 본 위키 raw 증거는 아님, 추후 수집 예정.

## 왜 중요한가

수집 32편 중 알고리즘 성능은 많으나 **"어떤 시뮬, 몇 기체, 무슨 물리"로 검증했는지** 명시 부족 → 재현성 공백. 완전 자율화를 위해선 시뮬-실기체 전이(sim-to-real) 검증이 병목.

## 일반 지식 한계 명시

시뮬레이터 비교는 공식 문서 기반 일반 지식. 위키 논문이 특정 시뮬 벤치마크를 직접 측정한 건 아님. 실증 강화는 플랫폼 실측 논문 수집 필요 (→ `uav-autopilot-stacks`, `uav-swarm-middleware`).

## 관련 페이지

- [[uav-autopilot-stacks]] — 시뮬이 어떤 펌웨어(SITL)와 붙는지
- [[uav-swarm-middleware]] — 시뮬 노드와 ROS 2/DDS 연결
- [[combat-swarm-drone-operations]] — 보안 시나리오 검증에 커스텀 시뮬(TriSweep) 활용
