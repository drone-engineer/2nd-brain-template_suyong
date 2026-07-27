---
title: Text-to-UAV-Mission (자연어→미션 자동 생성)
created: 2026-07-27
updated: 2026-07-27
type: query
tags:
  - uav
  - swarm
  - software
  - workflow
  - automation
sources:
  - raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md
  - raw/articles/2023-e2copre-energy-efficient-and-cooperative-collision-avoidance-for-uav-swarms-with.md
  - raw/articles/2025-a-learning-framework-for-cooperative-collision-avoidance-of-uav-swarms-leveragin.md
  - raw/articles/2022-survey-multi-agent-drl-communication.md
  - raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md
confidence: low
contested: false
contradictions: []
---

# Text-to-UAV-Mission (자연어→미션 자동 생성)

## 질의 동기

유튜브 쇼츠 "2000배 속도로 설계해버리는 ai"(치직치직, 2026-07-22, 63만 조회)에서 본 핵심은 **"사람이 손으로 설계하지 않고 AI가 자동으로 미션을 짜주는 것"** 이다. (쇼츠라 정확한 툴·수치는 없음 — 속도 수식어보다 **자동 미션 생성** 자체가 본질.) 이를 군집드론 미션비행에 어떻게 접목할지 검토한다.

## 개념: Text-to-Mission 파이프라인 (환각 방지형)

자연어/목표 명세를 입력받아 **실행 가능한 드론 미션**을 자동 생성하되, LLM 환각(그럴싸하지만 틀린 출력)을 막기 위해 **"자동 계획 → 인간 승인"** 2단 방어를 둔다.

```
"3기 V편대가 건물 둘레 정찰, 고도 50m, 10분"
        │  (LLM / 생성형 AI — 자유텍스트 금지, 정형 DSL만 출력)
        ▼
┌─────────────────────────────────────────────┐
│ 1. 자동 계획    → 미션 명세(DSL) 생성          │  ← 환각 1차 차단: 문법/스키마 검증
│ 2. 검증기       → 물리·충돌·배터리 체크        │  ← 환각 2차 차단: 위반 시 플래그
│ 3. 인간 승인    → review-queue 에서 Accepted   │  ← 환각 3차 차단: 사람이 최종 도장
└─────────────────────────────────────────────┘
        │ Accepted
        ▼
┌─────────────────────────────────────────────┐
│ 4. 미션 생성    → PX4 .plan / MAVLink         │
│ 5. 편대 배치    → 오프셋·리더-팔로워           │
│ 6. 사전 시뮬    → Gazebo/AirSim 검증          │
└─────────────────────────────────────────────┘
        │
        ▼
   기체 업로드 (QGC / MAVLink)
```

핵심: LLM은 **직접 실행파일을 내뱉지 않고 "계획(DSL)"만** 생성하므로, 환각이 섞여도 실기체 위험을 인간 승인 단계에서 차단한다.

## 환각 방지 메커니즘 (왜 이 구조가 효과적인가)

| 방어선 | 위치 | 동작 | 실패 시 |
| --- | --- | --- | --- |
| 1차 | 계획 생성 | LLM 출력을 자유텍스트가 아닌 **정형 DSL/스키마**로 강제 → 파서가 문법 오류 차단 | 재생성 유도 |
| 2차 | 검증기 | 배터리·충돌·통신범위·물리법칙 이탈 탐지 → 위반 시 플래그 | 인간 게이트로 전달 전 차단 |
| 3차 | 인간 승인 | [[research-feedback-loop]]의 review-queue에서 사람이 Accepted/Rejected | 기각 시 폐기 |

→ 자동화의 이점(속도)을 취하면서도, **자동 실행 금지**로 환각 피해를 원천 차단. 우리 위키 아키텍처의 "자동 생성 ≠ 자동 실행" 원칙과 일치.

## 우리 위키 구성요소와의 매핑

| 파이프라인 단계 | 담당 위키 페이지 | 역할 |
| --- | --- | --- |
| 미션 생성 (PX4 plan) | [[uav-autopilot-stacks]] | PX4 Offboard/Companion 구조 위에서 mission item 생성 |
| 편대/통신 배치 | [[uav-swarm-middleware]] | MAVLink 메시지·ROS 2 노드로 각 기 지령 분배 |
| 편대 형상 | [[uav-formation-control]] | 리더-팔로워·가상구조 오프셋 자동 산출 |
| 경로/궤적 | [[uav-swarm-path-planning]] | 클러스터링·궤적 최적화로 안전 경로 생성 |
| 인간 승인 게이트 | [[research-feedback-loop]] | AI 미션을 사람이 Accepted before 실행 |

## 접목 시 고려사항

- **환각 방지 = 자동계획→인간승인**: LLM이 직접 미션 파일을 내뱉지 않게 하고, 정형 DSL 계획→검증기→review-queue 승인 구조로 환각 피해를 차단한다 (위 "환각 방지 메커니즘" 참조).
- **안전**: AI 생성 미션은 사전 시뮬(Gazebo/AirSim, [[uav-swarm-simulation]]) 검증 후 실기체 업로드 권장.
- **인간 게이트 필수**: 자동 생성 ≠ 자동 실행. 우리 파이프라인의 review-queue가 그 역할.
- **출처**: 영상은 "동기/방향"일 뿐 실증 증거 아님. 실제 text-to-mission 툴(예: LLM→MAVLink codegen) 실증 논문은 추후 수집 필요.

## 한계 / 미해결

- 영상 1개뿐(증거 부족) → confidence: low.
- 실제 구현(codegen 정확도, PX4 호환성)은 미검증. AUTOSWARM 등 COTS 플랫폼 실증과 교차검증 필요.

## 관련 페이지

- [[uav-autopilot-stacks]] — 미션 생성 대상 펌웨어
- [[uav-swarm-middleware]] — 생성된 미션의 전달 계층
- [[uav-formation-control]] — 편대 오프셋 자동 배치
- [[uav-swarm-path-planning]] — 경로 자동 계획
- [[research-feedback-loop]] — 인간 판정 게이트
