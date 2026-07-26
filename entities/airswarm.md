---
title: AirSwarm
created: 2026-07-24
updated: 2026-07-25
type: entity
tags:
  - uav
  - swarm
  - control
  - research
sources:
  - raw/papers/2025-03-airswarm-enabling-cost-effective-multi-uav-research-with-cots-drones.md
confidence: medium
contested: false
contradictions: []
---

# AirSwarm

AirSwarm은 고가 커스텀 기체·모션캡처 의존을 줄이고, Tello·Anafi 같은 COTS 드론으로 다기체 연구를 가능하게 하려는 플랫폼이다. ^[raw/papers/2025-03-airswarm-enabling-cost-effective-multi-uav-research-with-cots-drones.md]

## 구성 포인트

- 계층적 제어로 다UAV 조율
- 외부 모션캡처 없는 visual SLAM 기반 위치추정
- ROS 기반 군집 개발 프레임워크
- cm급 추적, 저지연 제어, 통신 장애 내성, 편대·궤적 추종 실험

[[uav-swarm-robotics]]의 “연구·교육 접근성” 축에 해당하고, 편대·궤적 실험은 [[uav-formation-control]]·[[uav-swarm-path-planning]]과 맞닿는다.

## 출처

원문 캡처: `raw/papers/2025-03-airswarm-enabling-cost-effective-multi-uav-research-with-cots-drones.md` (arXiv HTML + Zotero PDF `D89J3ZU4`, parent `QZ35WT85`).
