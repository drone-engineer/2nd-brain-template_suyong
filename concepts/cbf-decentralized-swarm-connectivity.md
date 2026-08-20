---
title: CBF 기반 탈중앙 UAV 군집 항법·결속 유지
created: 2026-08-20
updated: 2026-08-20
type: concept
tags:
  - uav
  - swarm
  - control
  - communication
  - research
sources:
  - raw/articles/2023-control-barrier-function-based-decentralized-uav-swarm-navigation-while-preservi.md
  - raw/articles/2024-connectivity-preserving-decentralized-uav-swarm-navigation-in-obstacle-laden-env.md
confidence: medium
contested: false
contradictions: []
---

# CBF 기반 탈중앙 UAV 군집 항법·결속 유지

장애물이 있는 환경에서 **리더–팔로워 UAV 군집**이 충돌·장애물을 피하면서도 **군집 결속(connectivity)** 을 잃지 않게 하는 제어 접근이다. 핵심 도구는 **제어장벽함수(Control Barrier Function, CBF)** 이며, [[uav-formation-control]]·[[uav-swarm-path-planning]]의 안전·분산 항법 축을 보강한다.

## 한 줄 요약

명시적 기체 간 통신 없이도, **로컬 센서 정보만**으로 CBF 제약을 걸어 충돌·장애물 회피 + 결속 유지를 동시에 노린다. 인공퍼텐셜(APF)에서 자주 나오는 **진동(vibratory) 움직임**을 줄이는 것이 동기 중 하나다. ^[raw/articles/2023-control-barrier-function-based-decentralized-uav-swarm-navigation-while-preservi.md]

## 2023 ACC 결과 (Palani et al.)

- 탈중앙 리더–팔로워 항법 + CBF
- 수치 최적화에 의존하지 않는 제어 입력 유도(논문 주장)
- 제약이 “깨지기 전”에 막는 방향
- APF 대비 더 부드러운 움직임(시뮬레이션) + 쿼드로터 실험 검증 ^[raw/articles/2023-control-barrier-function-based-decentralized-uav-swarm-navigation-while-preservi.md]

## 2024 후속·인접 (결속 보존, 장애물 지형)

같은 문제 계열에서 **명시적 통신 없이** 장애물 지형의 결속 보존 항법을 다룬 기록이 있다(최적화/비최적화 변주, APF 진동 문제 언급). ^[raw/articles/2024-connectivity-preserving-decentralized-uav-swarm-navigation-in-obstacle-laden-env.md]

## 이 wiki에서의 위치

| 인접 개념 | 관계 |
|-----------|------|
| [[uav-formation-control]] | 편대·상대위치 유지의 상위/형제 주제 |
| [[uav-swarm-path-planning]] | 궤적·충돌회피·분산 계획과의 접점 |
| [[uav-swarm-robotics]] | 군집 운용 전체 지형 |

통신이 약하거나 의도적으로 없는 설정은 [[combat-swarm-drone-operations]]·방어/생존 시나리오와도 맞닿는다. GNSS 불능 항법 자체는 [[gnss-denied-autonomous-navigation]]을 본다(본 페이지는 CBF·결속 제어에 초점).

## 한계 (솔직히)

- 근거는 초록·메타 수준 합성이다. 수식·실험 수치 세부는 PDF 전문 대조 전 `confidence: medium`으로 둔다.
- APF vs CBF “항상 우월”로 일반화하지 않는다 — 해당 논문 설정에서의 비교다.
