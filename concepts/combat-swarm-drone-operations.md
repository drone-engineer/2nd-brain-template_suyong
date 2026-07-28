---
title: Combat Swarm Drone Operations
created: 2026-07-26
updated: 2026-07-27
type: concept
tags:
  - uav
  - swarm
  - control
  - research
sources:
  - raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md
  - raw/articles/2021-advanced-drone-swarm-security-blockchain-governance.md
  - raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md
  - raw/articles/2022-survey-multi-agent-drl-communication.md
  - raw/articles/2022-bc-iodt-blockchain-based-framework-for-authentication-in-internet-of-drone-thing.md
  - raw/articles/2025-integrated-sensing-and-communication-with-uav-swarms-via-decentralized-consensus.md
  - raw/articles/2026-trisweep-a-four-drone-swarm-framework-for-electromagnetic-side-channel-analysis.md
  - raw/articles/2026-occlusion-based-object-transportation-around-obstacles-with-a-swarm-of-miniature.md
  - raw/articles/2026-hunter-killer-drone-prd-v2.md
confidence: high
contested: false
contradictions: []
---

# Combat Swarm Drone Operations

전장에서 공격용 군집드론을 인간 운용에서 완전 자율 무기체계로 전환하기 위한 운용·발전 방향을 다루는 연구 주제이다. 러시아-우크라이나 전쟁에서 공격용 드론이 기존 재래식 전쟁의 통념을 깨는 게임체인저로 부상한 점을 근거로, 향후 지능화 전장에서 자율 군집드론의 역할을 분석한다. ^[raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md]

## 완전 자율화를 위한 5대 과제

채희·이경석·엄정호(2023)는 인간 운용 군집드론을 완전 자율화하기 위해 다음 5개 축을 제시한다. ^[raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md]

1. **군집드론 운용 최적화 AI 알고리즘** — 드론 간 충돌방지 및 이동형 표적 공격 알고리즘
2. **탈중앙식 지휘통제** — 급변하는 전장에 빠르게 대처하는 분산 C2 체계
3. **드론 간 임무 분석·할당 자동화** — 적 공격으로 드론 손실 시 임무 재할당
4. **드론 통신 보안 강화**
5. **무인화 윤리기준 확정**

## 교차 출처로 본 각 과제의 기술적 토대

다중 소스 검토 결과 5대 과제는 개별 기술 연구와 일관되게 연결된다.

- **과제 1·3 (AI 알고리즘 / 임무 할당):** 다개체 심층 강화학습 + 통신(MA-DRL) 서베이가 학습 기반 협업 제어·통신 프로토콜을 정리한다. ^[raw/articles/2022-survey-multi-agent-drl-communication.md]
- **과제 2·4 (탈중앙 C2 / 통신 보안):** PACNav는 통신 두절 환경에서도 지역 관측만으로 탈중앙 집단 항법을 가능케 해, 중앙 통제 소실 상황의 대안을 제시한다. ^[raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md] 블록체인 거버넌스 게임(BGG)은 공격 전 선제 보안 행동을 예측하는 스마트 드론 swarm 보안 설계를 제시한다. ^[raw/articles/2021-advanced-drone-swarm-security-blockchain-governance.md]
- **과제 5 (윤리):** KCI 원문이 무인화 윤리기준 확정을 명시적으로 과제로 든다. ^[raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md]

## 인접 연구와의 관계

이 주제는 [[uav-swarm-robotics]]가 정리한 연구 지형(형성 제어, 경로·클러스터링, 다개체 학습 제어) 위에 **군사 운용·자율화·윤리** 층을 더한다. 기술적 임무 할당·경로 문제는 [[multi-agent-rl-uav-control]]의 학습 기반 다개체 제어와 겹치며, 충돌방지·이동 표적 공격은 [[uav-swarm-path-planning]]의 궤적 계획 문제와 연결된다. 기존 서베이들이 기술·인프라 중심인 반면, 이 페이지는 **운용 개념과 규범(윤리·보안)** 에 무게를 둔다.

## 신뢰도

`confidence: high` — KCI 논문(운용·정책 제언) 1건 + arXiv 논문(보안 설계, 탈중앙 항법, MA-DRL 통신 서베이) 3건으로, 5대 과제 각각이 독립 출처로 지지된다. ^[raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md] ^[raw/articles/2021-advanced-drone-swarm-security-blockchain-governance.md] ^[raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md] ^[raw/articles/2022-survey-multi-agent-drl-communication.md]

## 보안·인증·정찰 최신 (2026-07-26 신규)

최신 4편이 과제 2·4(탈중앙 C2·통신 보안)와 새로운 전장 응용을 구체화한다.

- **BC-IoDT 블록체인 인증(2022):** Internet of Drone Things(IoDT)에서 블록체인으로 드론 노드 인증. 악성 노드를 자격 검증 후 제거하고, 클러스터 헤드(CH) 에너지 고갈을 적응형 저에너지 기법으로 완화. ^[raw/articles/2022-bc-iodt-blockchain-based-framework-for-authentication-in-internet-of-drone-thing.md]
- **ISAC 탈중앙 합의(2025):** UAV 군집이 가상 안테나 배열로 통합 센싱·통신(ISAC)을 할 때, 개별 기체의 전역 시야 부재를 **탈중앙 합의**로 극복해 전역 최적 swarm geometry 도출. ^[raw/articles/2025-integrated-sensing-and-communication-with-uav-swarms-via-decentralized-consensus.md]
- **TriSweep EM 사이드채널(2026):** 4대 드론으로 임베디드 마이크로컨트롤러의 **비접촉 EM 사이드채널 분석** 시뮬 프레임워크. 공중 적 대역 폭 협대역 스탠드오프 탐지 위협 모델을 최초로 정식화. ^[raw/articles/2026-trisweep-a-four-drone-swarm-framework-for-electromagnetic-side-channel-analysis.md]
- **Occlusion 물체 운반(2026):** 미니어처 군집이 장애물 우회 물체 운반 시, 가려짐(occlusion)을 하위 목표(sub-goal) 생성으로 해결. 단순 차단 전략의 한계(목표-물체 시선 필요)를 극복. ^[raw/articles/2026-occlusion-based-object-transportation-around-obstacles-with-a-swarm-of-miniature.md]

시사점: 탈중앙 보안·인증은 블록체인(IoDT, BGG)으로, 전장 인식은 ISAC 합의로, 적 대역 탐지는 EM 사이드채널로 각각 진전. **군집드론은 무기화뿐 아니라 전자전·정찰 플랫폼**으로도 확장 중.

## 실증 킬체인 사례: Hunter-Killer Drone System (PRD v2, 2026-07-27 신규)

Hunter(정찰)→Killer(타격) 2계층 자율 킬체인의 하드웨어 참조 구현 [[hunter-killer-drone-system]]. PX4+Jetson 통합 보드, RTK GPS, YOLO+LRF 타격으로 우리 5대 과제와 정확히 맞닿는다.

- **과제 1·3 (AI/임무할당):** Hunter가 `target_localizer`로 목표 위경도 산출 → Killer가 `terminal_homing`으로 YOLO 락온 후 직충돌. 이동형 표적 공격 알고리즘의 구체적 구현.
- **과제 2·4 (탈중앙 C2/보안):** Wi-Fi Mesh + MicroXRCE-DDS로 기간통신 — 단 jamming·기만에 취약. **Banshee(arXiv 2607.09930)는 짐벌 안정화 비전추적을 적대적으로 속이는 기법**으로, YOLO 락온 우회 가능성 시사 → 과제 4(통신보안)의 실증적 위협 사례. ^[raw/articles/2026-hunter-killer-drone-prd-v2.md]
- **과제 5 (윤리):** PRD는 인간 승인 게이트가 없이 자율타격을 상정. 우리 `text-to-uav-mission`의 "자동계획→인간승인" 원칙과 충돌 → 무인화 윤리기준 확정이 설계 단계에서 필수임을 시사.

시사점: 이론(5대 과제)이 실제 하드웨어 PRD로 구현되는 지점을 보여주며, **보안(Banshee)과 윤리(인간게이트 부재)가 가장 취약한 고리**임을 드러냄.
