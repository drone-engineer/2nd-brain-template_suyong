---
title: UAV Swarm Defensive Countermeasures
created: 2026-07-28
updated: 2026-08-09
type: concept
tags:
  - uav
sources:
  - raw/youtube/2026-07-31-M5YyDGfKhE8.md
confidence: medium
contested: false
contradictions: []
---

# UAV Swarm 방어 대책 (Hunter-Killer 취약점)

군집드론(특히 Hunter-Killer 자율 킬체인)이 처한 **취약점 3가지**와 대응 기술.

## 취약점 및 대응

| 취약점 | 공격 | 대응 방안 |
|--------|------|------------|
| 비전추적 기만 | Banshee(짐벌 안정화 추적 속임) | 다중센서 융합·추적 신뢰도 게이팅 |
| 무선 교란 | Wi-Fi Mesh 두절 | PACNav 탈중앙 항법·통신두절 복원력 |
| 위성항법 기만 | GPS 위치 조작 | `[[gnss-denied-autonomous-navigation]]` 항법 사용 |

## 관련 문서

- [[hunter-killer-drone-system]] — 대상 하드웨어
- [[gnss-denied-autonomous-navigation]] — 위성항법 불능 항법
- [[uav-swarm-middleware]] — PACNav 탈중앙 기반 통신

## 관련 영상 (YouTube 보강 2026-08-15)

새로 수집된 자료를 통해 방어 체계가 갱신됨.

- [Force Protection Capabilities Against Ariel Threats - Counter UAS](https://youtu.be/aGINGHexT7k) — 드론 군집 대항 방어 시스템, 킬체인 방어 차원

## 관련 영상 (YouTube 보강 2026-08-18)

새로 수집된 자료를 통해 비전추적 기만/무선 교란/위성항법 기만에 대한 대응 기술이 갱신됨.

- [Sanctum™ vs. the Swarm: Next-Gen Counter-UAS in Action](https://youtu.be/M5YyDGfKhE8) — Sanctum 대드론군 방어 체계 교전 데모, 차세대 C-UAS 실증
- [MyDefence Drone Swarm Counter UAS Jammer](https://youtu.be/HMKXMaAzByU) — 군집 드론 대항 C-UAS 재머 시연, 통신/센서 교란 방어
- [Vortex Cannon vs Drone](https://youtu.be/SrGENEXocJU) — 공기 저항/물리적 무기 vs 드론 시청각적 실험