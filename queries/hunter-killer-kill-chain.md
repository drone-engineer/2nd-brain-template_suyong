---
title: Hunter-Killer Drone Kill-Chain 기술검토
created: 2026-07-27
updated: 2026-07-31
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
  - raw/articles/2026-banshee-target-switch-attacks-on-gimbal-stabilized-visual-tracking-sys.md
  - raw/articles/2023-target-search-by-active-particles.md
  - raw/articles/2022-alto-a-large-scale-dataset-for-uav-visual-place-recognition-and-locali.md
  - raw/articles/2018-a-decision-theoretic-approach-to-detection-based-target-search-with-a-.md
  - raw/youtube/2026-07-29-MGggtBIzvtg.md
  - raw/youtube/2026-07-29-DK6IGG5zRU8.md
  - raw/youtube/2026-07-29-5knSEDXDa_0.md
  - raw/youtube/2026-07-29-EKpxP2YieZw.md
  - raw/youtube/2026-07-29-5k9F7QK66Ws.md
  - raw/youtube/2026-07-29-hGakXrt1EFo.md
  - raw/youtube/2026-07-31-MGggtBIzvtg.md
  - raw/youtube/2026-07-31-DK6IGG5zRU8.md
  - raw/youtube/2026-07-31-5k9F7QK66Ws.md
  - raw/youtube/2026-07-31-hGakXrt1EFo.md
  - raw/youtube/2026-07-31-EKpxP2YieZw.md
confidence: medium
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

## 관련 논문 (arXiv, 수집 완료 2026-07-27)

- **2607.09930 Banshee: Target Switch Attacks on Gimbal-Stabilized Visual Tracking** — 짐벌 안정화 비전추적 기만 적대공격. PRD의 YOLO 락온 우회 위협. ^[raw/articles/2026-banshee-target-switch-attacks-on-gimbal-stabilized-visual-tracking-sys.md]
- 2311.17854 Target search by active particles — 능동 입자 기반 목표 탐색. ^[raw/articles/2023-target-search-by-active-particles.md]
- 2207.12317 ALTO: UAV Visual Place Recognition Dataset — 비전 위치인식 데이터셋. ^[raw/articles/2022-alto-a-large-scale-dataset-for-uav-visual-place-recognition.md]
- 1801.01228 Decision-theoretic Target Search — 탐색 의사결정 이론. ^[raw/articles/2018-a-decision-theoretic-approach-to-detection-based-target-search.md]

> 위 4편은 `raw/articles/` 수집 완료. Banshee는 PRD 보안 취약점(과제 4)의 실증적 근거로 [[combat-swarm-drone-operations]]에 연결됨.

## 분석 결론

이론(5대 과제)이 실제 PRD로 구현되는 지점을 보여주나, **보안(Banshee 기만)과 윤리(인간게이트 부재)가 가장 취약**. 자율타격 체계엔 our `text-to-uav-mission`의 "자동계획→인간승인" 게이트 필수.

## 관련 페이지

- [[hunter-killer-drone-system]] — 하드웨어 참조
- [[combat-swarm-drone-operations]] — 5대 과제 매핑
- [[uav-autopilot-stacks]] — PX4/Jetson
- [[uav-swarm-middleware]] — ROS2/DDS 통신
- [[text-to-uav-mission]] — 인간승인 게이트 원칙

## 관련 영상 (YouTube 보강 2026-07-29)

실전·개념 보강: 중국의 신형 '킬체인' 군집 체계와 Atlas 드론군 공개, DEW/전자전 킬체인 시뮬레이션, 자율 살상 드론 개요 등으로 킬체인 운용 개념의 최신 사례가 추가됨.

- [Spectrum UV — Autonomous killer drones](https://youtu.be/MGggtBIzvtg) — 자율 살상 드론 개요.
- [Data Engineering Edge — Autonomous killer drones](https://youtu.be/DK6IGG5zRU8) — 자율 살상 드론 개요 (조회 45만+).
- [Saint — Hunter-Killer drones (Terminator 1/2)](https://youtu.be/5knSEDXDa_0) — 영화 터미네이터 속 헌터-킬러 드론 묘사.
- [NOOB-S@@B — Ultimate Drone War Simulation (DEW/EW Kill Chain)](https://youtu.be/EKpxP2YieZw) — DEW·미사일·전자전 킬체인 포함 무인전 시뮬레이션.
- [The Sun — China's new 'kill chain' swarm system](https://youtu.be/5k9F7QK66Ws) — 중국 신형 '킬체인' 군집 체계가 바꿀 전장 변화.
- [New York Post — China Atlas Drone Swarm System](https://youtu.be/hGakXrt1EFo) — 중국 Atlas 드론군 체계 공개, 1기당 정밀드론 96기 제어.

## 관련 영상 (YouTube 보강 2026-07-31)

킬체인 운용 개념 보강: The Sun 중국 킬체인 군집 체계, New York Post Atlas 드론군 공개, DEW/전자전 킬체인 시뮬레이션 재캡처, Spectrum UV·Data Engineering Edge 자율 살상 드론 대중적 개요, Saint 터미네이터 헌터-킬러 묘사 추가.

- [The Sun — China's new 'kill chain' swarm system](https://youtu.be/5k9F7QK66Ws) — 중국 신형 '킬체인' 군집 체계가 바꿀 전장 변화 (재캡처).
- [New York Post — China Atlas Drone Swarm System](https://youtu.be/hGakXrt1EFo) — 중국 Atlas 드론군 체계 공개, 1기당 정밀드론 96기 제어 (재캡처).
- [NOOB-S@@B — Ultimate Drone War Simulation (DEW/EW Kill Chain)](https://youtu.be/EKpxP2YieZw) — DEW·미사일·전자전 킬체인 포함 무인전 시뮬레이션 (재캡처).
- [Spectrum UV — Autonomous killer drones](https://youtu.be/MGggtBIzvtg) — 자율 살상 드론 개요 (재캡처).
- [Data Engineering Edge — Autonomous killer drones](https://youtu.be/DK6IGG5zRU8) — 자율 살상 드론 대중적 설명 (재캡처, 조회 45만+).
