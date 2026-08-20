---
title: UAV Formation Control
created: 2026-07-24
updated: 2026-08-20
type: concept
tags:
  - uav
  - swarm
  - control
  - survey
sources:
  - raw/papers/2024-07-advancement-challenges-in-uav-swarm-formation-control-a-comprehensive-review.md
  - raw/papers/2025-02-research-on-swarm-control-based-on-complementary-collaboration-of-unmanned-aeria.md
  - raw/papers/2018-08-a-survey-on-aerial-swarm-robotics.md
  - raw/articles/2023-e2copre-energy-efficient-and-cooperative-collision-avoidance-for-uav-swarms-with.md
  - raw/articles/2025-a-learning-framework-for-cooperative-collision-avoidance-of-uav-swarms-leveragin.md
confidence: medium
contested: false
contradictions: []
---

# UAV Formation Control

편대 제어는 [[uav-swarm-robotics]]에서 다수 기체의 상대 위치·대형을 유지하거나 전환하는 핵심 하위 문제다.

## 전통 방법과 AI 방법

Bu, Yan, Yang(2024)은 leader–follower, virtual structure, behavior-based, consensus, artificial potential field 같은 전통 방법과 신경망·심층강화학습 같은 AI 방법을 대비한다. 전통 방법은 단순·신뢰성이, AI 방법은 적응·최적화 능력이 강점으로 정리된다. 둘을 결합한 하이브리드가 열린 과제다. ^[raw/papers/2024-07-advancement-challenges-in-uav-swarm-formation-control-a-comprehensive-review.md]

## 이종 군집·복잡 환경

Zhao, Chen, Hu(2025)는 산불 진화처럼 이질적 능력·제약이 섞인 환경에서 보완 협업(complementary collaboration) 제어를 제안한다. 행동 특성 추출 → 조합 탐색 → 동적 할당 → 행동 학습으로 정책을 개선하며, 다유형 UAV 협업에서 대형 안정성을 보고한다. ^[raw/papers/2025-02-research-on-swarm-control-based-on-complementary-collaboration-of-unmanned-aeria.md]

학습 기반 제어의 세부 지형은 [[multi-agent-rl-uav-control]], 궤적·클러스터링은 [[uav-swarm-path-planning]], 명시적 통신 없이 결속을 지키는 CBF 항법은 [[cbf-decentralized-swarm-connectivity]]와 연결된다.

## 충돌회피: 전통+학습 하이브리드 (2026-07-26 신규)

최신 2편이 충돌회피를 분산(decentralized) 방식으로 푼다.

- **E2CoPre (2023):** 인공퍼텐셜필드(APF)로 환경 인식·암묵적 조정을 하고, 입자군집최적화(PSO)로 충돌 없는 에너지 효율 궤적을 분산 탐색. 중앙 제어 없이 협력 충돌회피를 달성. ^[raw/articles/2023-e2copre-energy-efficient-and-cooperative-collision-avoidance-for-uav-swarms-with.md]
- **Learning Framework (2025):** MARL에 도메인 지식 기반 보상(2D 필드 등고선 근사)을 부여해 장애물을 피크로 모델링. 윤곽선이 교차하지 않으므로 충돌이 본질적으로 회피되며, 궤적이 부드럽고 에너지 효율적. ^[raw/articles/2025-a-learning-framework-for-cooperative-collision-avoidance-of-uav-swarms-leveragin.md]

시사점: 충돌회피는 단일 알고리즘이 아니라 **APF/PSO 하이브리드**와 **도메인 보상 MARL** 두 축으로 성숙 중. 대규모 군집에서는 통신 부하를 줄이려는 분산 설계가 공통.
