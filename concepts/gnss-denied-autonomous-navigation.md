---
title: GNSS-Denied Autonomous Navigation (UAV)
created: 2026-07-28
updated: 2026-08-09
type: concept
tags:
  - uav
sources:
  - raw/youtube/2026-07-31-V5ZMhFyWQa8.md
confidence: medium
contested: false
contradictions: []
---

GPS 교란/위성항법 기만(예: GPS 위치 조작) 시 사용하는 **탈중앙 항법 기법 3가지**를 정리.

## 1. TRN(DTED 대조) 비전항법

- 위성사진을 이용한 지형매칭 기반 항법 (TRN / DTED)
- GPS 기만/교란에 대한 비전 항법 복원력
- 기존 GPS 기반 항법의 대체/보완: `[[gnss-denied-autonomous-navigation]]`

## 2. VIO(시각 관성 항법) 

- IMU+비전 센서를 통한 자세 추정 + 위치 업데이트 (VIO)
- 위성항법 기만 대응 → `[[gnss-denied-autonomous-navigation]]`
- 이론적 구조: VIO = VIO(위성사진) + VIO(지표) 

## 3. PACNav 탈중앙 항법

- Wi-Fi Mesh 네트워크로 통신하고 중앙 집중적 항법 사용하는 방식의 대체
- 무선 교란 상황 시 `[[uav-swarm-middleware]]` 내 PACNav 를 위한 탈중앙 항법 복원력 활용
- 자율 항법/대응 기능으로 확장 가능: `[[gnss-denied-autonomous-navigation]]`

## 관련 페이지

- [[gnss-denied-autonomous-navigation]] — 위성항법 불능 항법 기초
- [[uav-swarm-middleware]] — PACNav 탈중앙 기반 중계 네트워크 (통신/지속성 보장)
- [[combat-swarm-drone-operations]] — 5대 과제 중 보안/통신보안

## 관련 영상 (YouTube 보강 2026-08-15)

새로 수집된 자료를 통해 항법 기술이 갱신됨.

- [GPS-Denied, Anti-Jam Autonomous DIY Drone: How It Works](https://youtu.be/p8frNNYQNV4) — GPS 없이 자율 비행 가능한 드론 제작법
- [How Do Military Drones Fly Without GPS? | Ian Laffey, Theseus](https://youtu.be/i1QRqu3Cocw) — 군용 드론의 GPS 무결항법 원리

## 관련 영상 (YouTube 보강 2026-08-18)

새로 수집된 자료를 통해 항법 기술이 갱신됨.

- [How Drones Navigate Without GPS: Explained Simply](https://youtu.be/V5ZMhFyWQa8) — 드론의 GPS 없이 항법하는 간단 설명
- [FPV Drone Autonomous Human Tracking Test | Edge AI Autohoming System | -12°C Field Test](https://youtu.be/sEiKDZ6pZo4) — 엣지 AI 자율 인간추적/오토호밍 FPV, 극한 환경 Killer 단말 실증
- [Edge AI Autohoming for FPV Drones — 500m Target Lock to Impact | No GPS, No Cloud, No Signal](https://youtu.be/w0z-362DkIU) — GPS/클라우드/신호 없이 500m 표적 록온→타격, GNSS 불능 환경 킬러 유도