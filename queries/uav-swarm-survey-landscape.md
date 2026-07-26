---
title: UAV Swarm Survey Landscape
created: 2026-07-24
updated: 2026-07-26
type: query
tags:
  - uav
  - swarm
  - survey
  - research
  - notebooklm
sources:
  - raw/papers/2018-08-a-survey-on-aerial-swarm-robotics.md
  - raw/papers/2024-07-advancement-challenges-in-uav-swarm-formation-control-a-comprehensive-review.md
  - raw/papers/2025-01-uav-swarms-research-challenges-and-future-directions.md
  - raw/papers/2025-07-a-survey-on-uav-control-with-multi-agent-reinforcement-learning.md
  - raw/papers/2024-08-from-pid-to-swarms-a-decade-of-advancements-in-drone-control-and-path-planning-a.md
  - raw/papers/2025-02-research-on-swarm-control-based-on-complementary-collaboration-of-unmanned-aeria.md
  - raw/papers/2025-12-uav-swarm-clustering-and-trajectory-planning-a-taxonomy-systematic-review-curren.md
  - raw/papers/2025-07-systematic-review-of-multi-objective-uav-swarm-mission-planning-systems-from-reg.md
  - raw/papers/2025-03-airswarm-enabling-cost-effective-multi-uav-research-with-cots-drones.md
  - raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md
  - raw/articles/2021-advanced-drone-swarm-security-blockchain-governance.md
  - raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md
  - raw/articles/2022-survey-multi-agent-drl-communication.md
confidence: medium
contested: false
contradictions: []
---

# UAV Swarm Survey Landscape

2026-07-24에 Zotero에서 수집·ingest한 군집 드론 9편을 역할별로 묶은 질의 메모다.  
2026-07-25에 NotebookLM 노트북 `UAV Swarm Survey Landscape` (`9c0c0bf7-…`)로 동일 raw 묶음을 질의하고, 재사용 가능한 공백·읽기 순서만 이 페이지에 증분했다. 대화 전문은 저장하지 않는다 ([[notebooklm-query-compounding]]).  
2026-07-26에 같은 노트북에 KCI 1편 + arXiv 3편(`raw/articles/` 4편)을 소스로 추가하고 재질의해, 완전 자율화 관점의 신규 합성을 증분했다 (conv `a9ac16fb-…` turn 1).

## 지도

| 역할 | 문헌 | 위키 연결 |
| --- | --- | --- |
| 고전 공중군집 서베이 | Chung et al. 2018 | [[uav-swarm-robotics]] |
| 인프라·응용·미래과제 | Alqudsi & Makaraci 2025 | [[uav-swarm-robotics]] |
| 편대 제어 리뷰 | Bu et al. 2024 | [[uav-formation-control]] |
| 이종 보완 협업 | Zhao et al. 2025 | [[uav-formation-control]] |
| MARL 제어 서베이 | Ekechi et al. 2025 | [[multi-agent-rl-uav-control]] |
| 제어·경로 10년 SLR | Cetinsaya et al. 2024 | [[uav-swarm-path-planning]] |
| 클러스터링·궤적 SLR | Kaur et al. 2025 | [[uav-swarm-path-planning]] |
| 임무계획×규제 | Checker et al. 2025 | [[uav-swarm-robotics]] |
| COTS 연구 플랫폼 | AirSwarm 2025 | [[airswarm]] |
| 완전 자율화 운용 개념 | 채희 외 2023 (KCI) | [[combat-swarm-drone-operations]] |
| Swarm 보안 (블록체인 거버넌스) | Kim 2021 | [[combat-swarm-drone-operations]] |
| 탈중앙 항법 (통신 두절) | Ahmad et al. 2024 (PACNav) | [[uav-swarm-path-planning]] |
| MA-DRL + 통신 서베이 | 2022 | [[multi-agent-rl-uav-control]] |

## 신규 합성 — 완전 자율화 관점 (NotebookLM 재질의, 2026-07-26)

KCI 1편 + arXiv 3편 추가 후 재질의한 합성. 기존 9편 서베이는 기술·인프라 중심인 반면, 이 4편은 **운용·보안·통신·윤리** 층을 더한다. ^[raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md] ^[raw/articles/2021-advanced-drone-swarm-security-blockchain-governance.md] ^[raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md] ^[raw/articles/2022-survey-multi-agent-drl-communication.md]

### 기존 서베이를 수정·확장하는 소견
1. **통신 무관 항법 (PACNav):** 기존 서베이가 5G/6G 고대역폭 동기화를 강조하는 것과 달리, PACNav는 **통신 0** 상태에서도 지역 관측만으로 집단 항법이 가능함을 보인다 (path persistence / path similarity 메트릭). → "완전 자율화 = 항상 연결됨" 가정에 균열.
2. **보안을 거버넌스 게임으로:** 기존이 암호화·탐지 중심인 보안을 BGG는 이론 게임으로 모델링해 **공격 시점 예측 + 최적 책임성**을 제시.
3. **다차원 통신 (Comm-MADRL):** 기존 문헌에 빠진 통신 유형 체계적 분류(9차원)를 제안. 통신을 단순 데이터링크가 아닌 **환경 시야 확장·그룹별 조정 기제**로 재정의.

### 완전 자율화를 막는 신규 공백
- **전투 손실 관리:** 적 화력으로 기체 소실 시, 인간 개입 없이 남은 기체가 임무 우선순위를 실시간 재계산하는 알고리즘 부족.
- **책임성 모델링:** 탈중앙 네트워크에서 개별 자율 기체의 "최적 책임성"을 보안/연산 오버헤드와 균형짓는 방법 미비.
- **조건부 통신:** 엄호/은밀 요구 시 어느 하위그룹에만 메시지할지 자율 결정하는 연구 부재.

## 공통 연구 공백 (NotebookLM 합성, 2026-07-25)

소스 교차로 반복 언급된 공백 후보. PDF 전문이 없는 항목은 초록·웹 페이지 수준이므로 confidence는 medium이다.

1. **대규모 확장성** — 소규모 성공과 달리 대규모 군집에서 통신·계산 부하.
2. **실환경·Reality Gap** — 돌풍, 조명, GPS 거부 등 시뮬레이션–현실 간극.
3. **에너지·자원 제약** — 제한 배터리 하에서 AI/제어 부하를 감당하는 energy-aware 전략.

## 읽기 순서 제안

1. Alqudsi(2025)로 최신 인프라·과제 지형 파악 (또는 Chung 2018 고전 서베이)  
2. Bu(2024)로 전통 vs AI 편대 제어 구분  
3. Ekechi(2025)로 MARL 축 심화  
4. AirSwarm([[airswarm]])으로 저비용 실험 연결; 현장·법은 Checker(2025)

경로·클러스터링은 Cetinsaya·Kaur([[uav-swarm-path-planning]])를 관심에 따라 끼운다.

## 데이터 한계

Zotero PDF는 Alqudsi(`H89MMR98`)·AirSwarm(`D89J3ZU4`)만 로컬 첨부. Alqudsi 전문으로 [[uav-swarm-robotics]] 과제표를 보강했고, raw Extracted Text는 SCHEMA 불변으로 초록 캡처를 유지한다. MDPI OA 4편은 자동 DL 403 — Zotero **Find Full Text** 필요 (`docs/workflow/zotero-pdf-status.md`). Elsevier·IEEE는 기관 접근이 필요할 수 있다.
