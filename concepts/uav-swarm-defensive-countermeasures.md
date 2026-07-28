---
title: UAV Swarm 방어 대책 (Hunter-Killer 취약점 대응)
created: 2026-07-27
updated: 2026-07-29
type: concept
tags:
  - uav
  - swarm
  - security
  - control
  - firmware
sources:
  - raw/articles/2026-hunter-killer-drone-prd-v2.md
  - raw/articles/2026-banshee-target-switch-attacks-on-gimbal-stabilized-visual-tracking-sys.md
  - raw/articles/2026-enhancing-graph-based-slam-in-gnss-denied-environments-by-leveraging-l.md
  - raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md
  - raw/youtube/2026-07-29-M5YyDGfKhE8.md
  - raw/youtube/2026-07-29-HMKXMaAzByU.md
  - raw/youtube/2026-07-29-a5kumlJqkQQ.md
confidence: medium
contested: false
contradictions: []
---

# UAV Swarm 방어 대책 (Hunter-Killer 취약점 대응)

군집드론(특히 Hunter-Killer 자율 킬체인)이 처한 **취약점 3가지**와 대응 기술. `[[hunter-killer-drone-system]]`의 PRD 한계를 방어 관점에서 정리.

## 취약점 → 대응 매핑

| 취약점 | 공격/위협 | 대응 기술 | 위키 연결 |
| --- | --- | --- | --- |
| 비전추적 기만 | Banshee(짐벌 안정화 추적 속임) | 다중센서 융합·추적 신뢰도 게이팅 | `[[combat-swarm-drone-operations]]` 보안 |
| 무선 교란 (Jamming) | Wi-Fi Mesh 두절 | PACNav 탈중앙 항법·통신두절 복원력 | `[[uav-swarm-middleware]]` |
| 위성항법 교란 (GNSS Spoofing/Jamming) | GPS 위치 조작 | TRN/VIO 비전항법으로 복귀 | `[[gnss-denied-autonomous-navigation]]` |
| 인간 승인 부재 | 자율타격 오판 | 자동계획→인간승인 게이트 + 긴급취소(Kill-Switch) | `[[text-to-uav-mission]]` · `[[uav-mission-approval-abort]]` |

## 1. 비전추적 기만(Banshee) 대응

- YOLO 단일 센서 락온은 기만에 취약 → **다중모달(EO/IR/LRF) 교차검증** + 추적 신뢰도 임계치 하회 시 락온 해제
- 짐벌 안정화 추적기에 적대적 패치 주입 차단 (입력 무결성 검증)

## 2. GNSS-Denied 생존 항법

- GPS 교란 시 즉시 `[[gnss-denied-autonomous-navigation]]` 전환: TRN(DTED 대조) + 비전매칭(위성사진) + VIO(오차보정)
- 사전 입력 경로·지형정보로 지정 복귀점(RTB) 자율 항법

## 3. 통신두절 복원력

- 중앙 집중(Wi-Fi Mesh) 대신 PACNav 계열 지역관측 탈중앙 항법으로 통제소실 대비

## 관련 페이지

- [[hunter-killer-drone-system]] — 대상 하드웨어(PRD)
- [[gnss-denied-autonomous-navigation]] — 위성항법 불능 항법
- [[combat-swarm-drone-operations]] — 5대 과제 중 보안/통신보안
- [[uav-swarm-middleware]] — PACNav 탈중앙 복원력
- [[text-to-uav-mission]] — 인간승인 게이트

## 관련 영상 (YouTube 보강 2026-07-29)

실전 방어 데모 보강: Lockheed Martin의 Sanctum™ 대드론군 교전, MyDefence의 군집 C-UAS 재머, Divyania의 스마트 탐지·위협관리 체계 시연으로 기존 '취약점→대응' 매핑에 실증 사례가 추가됨.

- [Lockheed Martin — Sanctum™ vs. the Swarm: 차세대 C-UAS 실전](https://youtu.be/M5YyDGfKhE8) — Sanctum™ 대드론군 방어 체계 교전 데모, 차세대 C-UAS 실증.
- [MyDefence — Drone Swarm Counter UAS Jammer](https://youtu.be/HMKXMaAzByU) — 군집 드론 대항 C-UAS 재머(Jammer) 시연, 통신/센서 교란 방어.
- [Divyania Defence — Swarm Counter Drone System](https://youtu.be/a5kumlJqkQQ) — 스마트 탐지·위협관리 군집 방어 드론 체계, 탐지→대응 자동화.
