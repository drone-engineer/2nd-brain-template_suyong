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
  - concepts/uav-autopilot-stacks
  - concepts/uav-swarm-middleware
  - concepts/uav-formation-control
  - concepts/uav-swarm-path-planning
  - concepts/research-feedback-loop
confidence: low
contested: false
contradictions: []
---

# Text-to-UAV-Mission (자연어→미션 자동 생성)

## 질의 동기

유튜브 쇼츠 "2000배 속도로 설계해버리는 ai"(치직치직, 2026-07-22, 63만 조회)에서 본 핵심은 **"사람이 손으로 설계하지 않고 AI가 자동으로 미션을 짜주는 것"** 이다. (쇼츠라 정확한 툴·수치는 없음 — 속도 수식어보다 **자동 미션 생성** 자체가 본질.) 이를 군집드론 미션비행에 어떻게 접목할지 검토한다.

## 개념: Text-to-Mission 파이프라인

자연어/목표 명세를 입력받아 **실행 가능한 드론 미션**을 자동 생성하는 흐름.

```
"3기 V편대가 건물 둘레 정찰, 고도 50m, 10분"
        │  (LLM / 생성형 AI)
        ▼
┌─────────────────────────────────────┐
│ 1. 미션 생성    → PX4 .plan / MAVLink │
│ 2. 편대 배치    → 오프셋·리더-팔로워  │
│ 3. 경로 계획    → 궤적·클러스터링      │
│ 4. 인간 판정    → review-queue 승인    │
└─────────────────────────────────────┘
        │
        ▼
   기체 업로드 (QGC / MAVLink)
```

## 우리 위키 구성요소와의 매핑

| 파이프라인 단계 | 담당 위키 페이지 | 역할 |
| --- | --- | --- |
| 미션 생성 (PX4 plan) | [[uav-autopilot-stacks]] | PX4 Offboard/Companion 구조 위에서 mission item 생성 |
| 편대/통신 배치 | [[uav-swarm-middleware]] | MAVLink 메시지·ROS 2 노드로 각 기 지령 분배 |
| 편대 형상 | [[uav-formation-control]] | 리더-팔로워·가상구조 오프셋 자동 산출 |
| 경로/궤적 | [[uav-swarm-path-planning]] | 클러스터링·궤적 최적화로 안전 경로 생성 |
| 인간 승인 게이트 | [[research-feedback-loop]] | AI 미션을 사람이 Accepted before 실행 |

## 접목 시 고려사항

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
