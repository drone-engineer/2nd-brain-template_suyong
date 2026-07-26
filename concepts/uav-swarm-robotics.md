---
title: UAV Swarm Robotics
created: 2026-07-24
updated: 2026-07-26
type: concept
tags:
  - uav
  - swarm
  - research
  - survey
sources:
  - raw/papers/2018-08-a-survey-on-aerial-swarm-robotics.md
  - raw/papers/2025-01-uav-swarms-research-challenges-and-future-directions.md
  - raw/papers/2024-08-from-pid-to-swarms-a-decade-of-advancements-in-drone-control-and-path-planning-a.md
  - raw/papers/2025-07-systematic-review-of-multi-objective-uav-swarm-mission-planning-systems-from-reg.md
  - raw/articles/2013-evolution-of-swarm-robotics-systems-with-novelty-search.md
  - raw/articles/2012-exploiting-particle-swarm-optimization-in-multiple-faults-fuzzy-detection.md
confidence: high
contested: false
contradictions: []
---

# UAV Swarm Robotics

UAV swarm robotics는 다수 무인항공기가 협력해 단일 기체가 감당하기 어려운 감시·탐색·물류·방어 임무를 수행하는 연구 영역이다. 공중 군집은 3차원 운동과 개별 기체 동역학이 더해져 지상 군집보다 궤적 생성·할당·통신이 어렵다. ^[raw/papers/2018-08-a-survey-on-aerial-swarm-robotics.md]

## 핵심 하위 문제

최근 서베이들은 공통적으로 다음 축을 다룬다.

- 편대·형성 제어 → [[uav-formation-control]]
- 경로·클러스터링·궤적 계획 → [[uav-swarm-path-planning]]
- 학습 기반 다개체 제어 → [[multi-agent-rl-uav-control]]
- 인프라·보안·규제·임무계획 → [[uav-swarm-survey-landscape]]

Alqudsi & Makaraci(2025)는 인프라, 경로계획, 작업할당, 형성 제어, 보안과 AI/ML 통합, 민·군 응용, 규제·윤리를 한꺼번에 정리한다. ^[raw/papers/2025-01-uav-swarms-research-challenges-and-future-directions.md]

## Alqudsi(2025) 과제 표 (PDF 전문)

Zotero 첨부 `H89MMR98` 전문에서 Table 6이 정리한 한계·방향(요지). raw 본문은 SCHEMA상 초록 캡처를 유지하고, 해석은 여기에만 둔다. ^[raw/papers/2025-01-uav-swarms-research-challenges-and-future-directions.md]

- 이종 군집·감시 윤리 → blockchain/IoT·책임 있는 배치
- 에너지 효율·대규모 제어 알고리즘 → energy-aware AI/ML/DL
- 자율 제어·작업 할당 → 협업 할당 + AI/ML 의사결정
- 통신·조율 (규모↑ 시 통신량 급증) → 5G/6G·분산·강건 프로토콜
- 강건성·확장성 → 동적 환경의 할당·경로·운동 조율
- 동기화·환경 외란 → 적응 제어
- 보안·안전 → 위협 탐지·완화, 정책·윤리 프레임

## 현장 도입 장벽

기술 성능만으로는 산업 확산이 어렵다. Checker et al.(2025)은 군집 임무계획 기능과 법·규제 요구 사이 간극이 현장 적용을 막는 주요 요인이라고 본다. ^[raw/papers/2025-07-systematic-review-of-multi-objective-uav-swarm-mission-planning-systems-from-reg.md]

저비용 연구 플랫폼으로는 [[airswarm]]처럼 COTS 기체 기반 접근이 등장한다.

군사 운용·자율화 관점은 [[combat-swarm-drone-operations]]에서 다룬다(채희 외 2023: 완전 자율화 5대 과제, 탈중앙 C2·임무 재할당·윤리기준). ^[raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md]

## 소프트웨어 스택 (2026-07-26 신규)

위 알고리즘 연구가 실제로 돌아가는 플랫폼 계층. 위키는 알고리즘(L4)은 두텁고 펌웨어/미들웨어/시뮬(L1–L3)은 얇어 보완함.

- **펌웨어/비행 스택** → [[uav-autopilot-stacks]] (PX4 vs ArduPilot, Offboard/Companion 구조)
- **통신/미들웨어** → [[uav-swarm-middleware]] (MAVLink/ROS 2/DDS; 합의·Comm-MADRL과 직결)
- **시뮬레이션** → [[uav-swarm-simulation]] (Gazebo/AirSim/Webots; 재현성·sim-to-real)

## 진화·최적화 방법론 기초 (2026-07-26 신규)

군집 지능의 알고리즘적 뿌리가 되는 두 방법론.

- **노벨티 서치(2013):** 사전 목표 없이 "새로움(novelty)"으로 보상해 조기 수렴을 막는 진화 기법. 동질 군집의 신경망 제어기를 NEAT와 결합해 진화시킨 실증. 기존 fitness 함수의 기만성(deceptive)을 회피하는 원리 제공. ^[raw/articles/2013-evolution-of-swarm-robotics-systems-with-novelty-search.md]
- **PSO 결함 탐지(2012):** 입자군집최적화(PSO)로 퍼지 검출기의 멤버십 함수를 최적 설계. 본드 그래프 잔차 기반 다중 결함 온라인 탐지에 적용. → PSO가 제어기 튜닝·결함 탐지에도 쓰임을 시사(충돌회피 E2CoPre의 PSO 사용과 통함). ^[raw/articles/2012-exploiting-particle-swarm-optimization-in-multiple-faults-fuzzy-detection.md]

시사점: 군집 지능의 토대는 **진화 연산(노벨티 서치)** 과 **군집 최적화(PSO)** 다. 최신 MARL·충돌회피도 이 기초 위에 서 있음.

## 한계

IEEE/Elsevier·MDPI 일부는 아직 로컬 PDF가 없어 초록·메타 수준이다. Alqudsi·AirSwarm만 Zotero PDF 확인됨 (`docs/workflow/zotero-pdf-status.md`).
