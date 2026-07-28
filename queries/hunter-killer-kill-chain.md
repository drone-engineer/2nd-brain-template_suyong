---
title: Hunter-Killer Drone Kill-Chain 기술검토
created: 2026-07-27
updated: 2026-07-27
type: query
tags:
  - uav
  - swarm
  - control
  - security
  - software
sources:
  - raw/articles/2026-hunter-killer-drone-prd-v2.md
  - raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md
confidence: low
contested: false
contradictions: []
---

# Hunter-Killer Drone Kill-Chain 기술검토

## 질의 동기

사용자가 제공한 **Hunter-Killer Drone PRD v2** (Hunter 정찰 → Killer 타격 자율 킬체인)를 우리 위키 관점에서 기술 검토. 군집드론 운용 개념(5대 과제)이 실제 하드웨어로 어떻게 구현·취약해지는지 분석.

## PRD 기술 구성

| 계층 | 컴포넌트 | 우리 위키 매핑 |
| --- | --- | --- |
| 펌웨어/FC | Pixhawk 6X + PX4 | [[uav-autopilot-stacks]] |
| 온보드 AI | Jetson Orin Nano (YOLO) | [[uav-swarm-middleware]] |
| 통신 | ROS2/MicroXRCE-DDS, Wi-Fi Mesh | [[uav-swarm-middleware]] |
| 항법 | H-RTK F9P (RTK) | [[uav-autopilot-stacks]] |
| 탐지/타격 | C13+LRF, terminal_homing | [[hunter-killer-drone-system]] |
| 킬체인 | Hunter→Killer 임무재할당 | [[combat-swarm-drone-operations]] |

## 5대 과제 대조

1. **AI 알고리즘**: `target_localizer`+`terminal_homing` = 이동형 표적 공격 구현 ✅
2. **탈중앙 C2**: Wi-Fi Mesh 중앙집중형 — 통제소실 시 취약 ⚠️ (PACNav 계열 대안 필요)
3. **임무재할당**: Hunter→Killer 위경도 전달 = 정적 할당 (동적 재할당 미구현) ⚠️
4. **통신보안**: Banshee(arXiv 2607.09930) 적대적 비전기만이 YOLO 락온 우회 시사 ⚠️
5. **윤리**: 인간승인 게이트 **부재** — 자율타격 ⚠️ ([[text-to-uav-mission]] 원칙 충돌)

## 관련 논문 (arXiv, 수집 대기 — 429로 미수집)

- 2607.09930 Banshee: Target Switch Attacks on Gimbal-Stabilized Visual Tracking (보안 위협)
- 2311.17854 Target search by active particles
- 2207.12317 ALTO: UAV Visual Place Recognition Dataset
- 1801.01228 Decision-theoretic Target Search

> 위 4편은 `raw/articles/` 미수집 상태. 매주 월요일 크론 `auto-collect-papers.py` 또는 수동 수집으로 보강 예정.

## 분석 결론

이론(5대 과제)이 실제 PRD로 구현되는 지점을 보여주나, **보안(Banshee 기만)과 윤리(인간게이트 부재)가 가장 취약**. 자율타격 체계엔 our `text-to-uav-mission`의 "자동계획→인간승인" 게이트 필수.

## 관련 페이지

- [[hunter-killer-drone-system]] — 하드웨어 참조
- [[combat-swarm-drone-operations]] — 5대 과제 매핑
- [[uav-autopilot-stacks]] — PX4/Jetson
- [[uav-swarm-middleware]] — ROS2/DDS 통신
- [[text-to-uav-mission]] — 인간승인 게이트 원칙
