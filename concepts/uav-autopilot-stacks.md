---
title: UAV Autopilot Stacks (PX4 vs ArduPilot)
created: 2026-07-26
updated: 2026-07-26
type: concept
tags:
  - uav
  - swarm
  - software
  - firmware
sources:
  - raw/articles/2024-pacnav-enhancing-collective-navigation-for-uav-swarms-in-communication-denied-env.md
  - raw/articles/2021-advanced-drone-swarm-security-by-using-blockchain-governance-game-bgg-0.md
  - raw/articles/2022-a-learning-framework-for-cooperative-collision-avoidance-of-uav-swarms-u.md
  - raw/articles/2025-a-modular-and-scalable-system-architecture-for-heterogeneous-uav-swarm.md
  - raw/articles/2023-tinyslam-based-exploration-with-a-swarm-of-nano-uavs.md
confidence: medium
contested: false
contradictions: []
---

# UAV Autopilot Stacks (PX4 vs ArduPilot)

군집드론 소프트웨어 스택의 **L1(펌웨어/비행 스택)** 계층. 개별 기체의 자세·위치 제어, 모터 믹싱, 상태추정, 안전 모드를 담당하는 온보드 소프트웨어다. 위키에 수집된 알고리즘 연구(합의, MARL, 충돌회피)는 사실상 이 비행 스택 위에서 돌아가는 상위 로직이다.

## 두 개의 지배적 오픈소스 스택

| 항목 | PX4 (PX4 Autopilot) | ArduPilot |
| --- | --- | --- |
| 언어/구조 | C++ / 모듈형 uORB 메시지버스 | C++ / 태스크 루프 |
| 생태계 | ROS 2 연동 표준(MAVLink), 상용 드론 많음 | 범용성(비행기/로버/보트), 커뮤니티 방대 |
| 군집 지원 | Offboard 모드 + MAVLink로 다기체 지령 | 스왐/대형비행 스크립트 지원 |
| 시뮬 | Gazebo/Ignition, jMAVSim, AirSim | SITL + Gazebo/Webots |

두 스택 모두 **MAVLink**를 기본 통신 프로토콜로 쓰며, 외부 컴퓨터(지상국 또는 온보드 Companion Computer)에서 상위 제어를 내리는 **Offboard/Companion** 구조를 표준으로 삼는다. [PACNav, 2024] 같은 통신두절 복원력 연구나 [Advanced Drone Swarm Security(BGG), 2021] 같은 보안 연구는 이 분산 기체 전제 위에서 성립한다.

## 왜 중요한가 (위키 관점)

- 수집된 32편 중 알고리즘/제어 논문은 많지만, **어떤 펌웨어 위에서 검증됐는지 명시한 실증이 없다**. 대개 "시뮬 또는 하드웨어 추상화"로 끝남 → 재현성 공백.
- 완전 자율화 5대 과제(보안/윤리/복원력 등) 중 **보안**은 펌웨어 메시지(MEXLink 평문) 취약점과 직결 → `combat-swarm-drone-operations`의 블록체인 인증([BGG, 2021])과 연결.

## 일반 지식 한계 명시

이 페이지의 스택 비교는 **제조사 문서 기반 일반 지식**이며, 위키 수집 논문이 직접 벤치마크한 결과는 아니다. 실증 비중을 높이려면 `raw/articles/`에 "PX4 swarm" / "ArduPilot swarm" 실측 논문을 추가 수집해야 한다 (→ `uav-swarm-middleware`, `uav-swarm-simulation` 참조).

## 관련 페이지

- [[uav-swarm-middleware]] — MAVLink/ROS 2 토픽이 펌웨어와 상위 로직을 어떻게 잇는지
- [[uav-swarm-simulation]] — PX4/ArduPilot이 어떤 시뮬과 붙는지
- [[combat-swarm-drone-operations]] — 보안 계층(블록체인 인증)이 펌웨어 메시지와 만나는 지점