---
title: UAV 미션 인간 승인 및 긴급 취소 (Kill-Switch)
created: 2026-07-27
updated: 2026-07-27
type: concept
tags:
  - uav
  - swarm
  - control
  - security
sources:
  - raw/articles/2026-hunter-killer-drone-prd-v2.md
  - raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md
confidence: medium
contested: false
contradictions: []
---

# UAV 미션 인간 승인 및 긴급 취소 (Kill-Switch)

자율 미션(특히 Hunter-Killer 타격)에 필요한 **양방향 인간 루프**: ① 사전 승인(Pre-flight Approval) + ② 긴급 승인 취소(Emergency Abort / Kill-Switch). `[[text-to-uav-mission]]`의 "자동계획→인간승인"을 **취소 가능성**까지 완성한다.

## 1. 사전 승인 (Pre-flight Approval)

- AI 생성 미션 계획(DSL) → `[[research-feedback-loop]]`의 review-queue에서 사람이 Accepted
- 승인 전까지 실행 파일 생성·업로드 금지 (환각 방지)
- 승인 기록은 감사 추적(audit trail)으로 보존

## 2. 긴급 승인 취소 (Emergency Abort / Kill-Switch)

승인 후 비행 중이라도 인간이 **즉시 미션을 중단**할 수 있어야 함. 중단 대상:
- 타격 직전 락온 해제 (Banshee 오인/민간 노출 시)
- 편대 비행 중단 및 RTB
- 자폭/충돌 명령 무효화

## 3. 위급 상황에서의 취소 전달 (통신 교란 대비)

Hunter-Killer PRD는 Wi-Fi Mesh 기반이라 **jamming 시 중단 명령 자체가 전달 안 됨** — 가장 위험한 고리. 대응:

| 상황 | 취소 전달 방식 | 기술 |
| --- | --- | --- |
| 기간통신 정상 | 지상국→드론 직접 명령 | MAVLink `MAV_CMD_DO_FLIGHTTERMINATION` / `NAV_GUIDED` 해제 |
| 통신 두절(Jamming) | **사전 예약 중단(Time-boxed Abort)** | 미션에 "T초 후 자동 abort" 타이머 내장 → 지상국 무응답 시 자동 중단 |
| GNSS-Denied 병행 | 교란 속에서도 복귀 | `[[gnss-denied-autonomous-navigation]]`으로 지정점 복귀 후 대기 |
| 편대 일부 손실 | 생존기기가 동료 중단 전파 | `[[uav-swarm-middleware]]`(PACNav) 지역관측으로 abort 브로드캐스트 |

핵심 원칙: **"중단 명령은 항상 로컬에서 강제 가능"** — 지상국 의존 없이 기체 자체 타이머/센서 조건으로 abort.

## 4. 우리 위키와의 연결

- `[[text-to-uav-mission]]`: 사전 승인 단계(자동계획→인간승인) — 이 페이지는 취소까지 확장
- `[[uav-swarm-defensive-countermeasures]]`: 통신두절 복원력이 abort 전달의 전제
- `[[hunter-killer-drone-system]]`: PRD의 인간게이트 부재를 이 설계로 보완
- `[[combat-swarm-drone-operations]]`: 5대 과제 중 과제 5(무인화 윤리기준)의 구체적 메커니즘
- `[[research-feedback-loop]]`: 승인/기각 피드백 루프

## 관련 페이지

- [[text-to-uav-mission]] — 사전 승인(자동계획→인간승인)
- [[uav-swarm-defensive-countermeasures]] — 방어 체계 (취소도 방어의 일부)
- [[hunter-killer-drone-system]] — 대상 하드웨어(PRD)
- [[gnss-denied-autonomous-navigation]] — 교란 속 복귀 항법
- [[combat-swarm-drone-operations]] — 5대 과제(윤리)
- [[px4-ekf2-vio-prototype]] — Kill-Switch/시간예약중단/편대브로드캐스트 구현 가이드

