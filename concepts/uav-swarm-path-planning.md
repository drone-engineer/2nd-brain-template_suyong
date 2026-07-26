---
title: UAV Swarm Path Planning
created: 2026-07-24
updated: 2026-07-26
type: concept
tags:
  - uav
  - swarm
  - control
  - survey
sources:
  - raw/papers/2024-08-from-pid-to-swarms-a-decade-of-advancements-in-drone-control-and-path-planning-a.md
  - raw/papers/2025-12-uav-swarm-clustering-and-trajectory-planning-a-taxonomy-systematic-review-curren.md
  - raw/papers/2025-01-uav-swarms-research-challenges-and-future-directions.md
  - raw/articles/2018-fundamental-tradeoffs-in-communication-and-trajectory-design-for-uav-enabled-wir.md
  - raw/articles/2022-trajectory-and-transmit-power-optimization-for-irs-assisted-uav-communication-un.md
  - raw/articles/2020-uav-trajectory-and-communication-co-design-flexible-path-discretization-and-path.md
  - raw/articles/2021-3d-uav-trajectory-and-data-collection-optimisation-via-deep-reinforcement-learni.md
  - raw/articles/2021-reconfigurable-intelligent-surface-assisted-multi-uav-networks-efficient-resourc.md
confidence: medium
contested: false
contradictions: []
---

# UAV Swarm Path Planning

군집 경로·궤적 계획은 개별 기체 제어를 넘어, 충돌 회피·커버리지·에너지·통신을 동시에 맞추는 문제다. [[uav-swarm-robotics]]의 운영 축 중 하나이며 [[uav-formation-control]]과 자주 결합된다.

## 문헌 상태 (이번 ingest 기준)

- Cetinsaya et al.(2024)은 2013–2023 드론 제어·경로계획과 swarm intelligence를 systematic review로 정리한다. ^[raw/papers/2024-08-from-pid-to-swarms-a-decade-of-advancements-in-drone-control-and-path-planning-a.md]
- Kaur et al.(2025)은 군집 파티셔닝(클러스터링)과 궤적계획 알고리즘을 taxonomy·SLR로 분류한다. ^[raw/papers/2025-12-uav-swarm-clustering-and-trajectory-planning-a-taxonomy-systematic-review-curren.md]
- Alqudsi & Makaraci(2025)도 coordinated path planning을 핵심 영역으로 둔다. ^[raw/papers/2025-01-uav-swarms-research-challenges-and-future-directions.md]

## 주의

Elsevier 두 편의 초록·본문이 로컬에 없어 이번 페이지는 **제목·서지·인접 서베이 교차** 수준이다(`confidence: low`). PDF 확보 후 갱신할 것.

## 궤적-통신 공동설계 최신 (2026-07-26 신규)

통신 품질과 궤적을 동시 최적화하는 흐름이 뚜렷하다. 대부분 IRS/RIS(지능형 반사면)와 DRL을 결합.

- **기본 트레이드오프(2018):** UAV를 공중 기지국 삼을 때 통신(LoS)과 궤적 설계의 근본 트레이드오프를 정식화. 3D 가동성 이점 vs 에너지·커버리지 한계를 최초로 규명. ^[raw/articles/2018-fundamental-tradeoffs-in-communication-and-trajectory-design-for-uav-enabled-wir.md]
- **유연한 경로 이산화(2020):** 연속시간 궤적 최적화의 무한 변수 문제를 piecewise-linear 근사 없이 유연히 이산화해 계산 복잡도를 크게 낮춤. ^[raw/articles/2020-uav-trajectory-and-communication-co-design-flexible-path-discretization-and-path.md]
- **IRS-assisted 트랙·전력(2022):** 재밍 환경에서 지상노드 송신전력·IRS 위상·UAV 궤적을 공동 최적화해 평균 전송률 최대화. 비볼록 문제를 분해해 풂. ^[raw/articles/2022-trajectory-and-transmit-power-optimization-for-irs-assisted-uav-communication-un.md]
- **3D DRL 데이터 수집(2021):** UAV-assisted IoT에서 최단 비행경로로 수집량 최대화를 DRL로 해결. 탑재 전력·비행시간 제약 하 자원 할당. ^[raw/articles/2021-3d-uav-trajectory-and-data-collection-optimisation-via-deep-reinforcement-learni.md]
- **RIS 다중 UAV(2021):** RIS 반사 + UAV 기동성 결합으로 에너지 효율 최대화. 전력 할당·RIS 위상행렬을 DRL로 연속 최적화. ^[raw/articles/2021-reconfigurable-intelligent-surface-assisted-multi-uav-networks-efficient-resourc.md]

시사점: 경로계획은 **단독 기하학 문제가 아니라 통신·에너지 공동최적화**로 이동. IRS/RIS가 핵심 인에이블러이며, DRL이 비볼록 공동최적화의 사실상 표준 해법. → confidence를 `low`에서 올릴 근거가 됨(5편 모두 초록 확보).
