---
title: STM32 보드 활용 가능성 검토 (Hunter-Killer/GNSS-Denied)
created: 2026-07-27
updated: 2026-07-27
type: query
tags:
  - uav
  - swarm
  - firmware
  - control
  - security
sources:
  - raw/articles/2026-hunter-killer-drone-prd-v2.md
  - raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md
  - raw/articles/2018-dsvo-direct-stereo-visual-odometry.md
  - raw/articles/2021-autonomous-navigation-system-for-a-delivery-drone.md
  - raw/articles/2020-alphapilot-autonomous-drone-racing.md
  - raw/articles/2021-df-vo-what-should-be-learnt-for-visual-odometry.md
  - raw/articles/2025-lego-slam-language-embedded-gaussian-optimization-slam.md
confidence: low
contested: false
contradictions: []
---

# STM32 보드 활용 가능성 검토

## 질의 동기

Hunter-Killer PRD는 **Pixhawk 6X(STM32H7 FC) + Jetson Orin Nano** 구조. "STM32 보드만으로(또는 더 활용해서) 자율타격/GNSS-Denied 항법이 가능한가?" 검토. STM32는 이미 시스템 중심(FC)에 있으나, 고연산 처리(YOLO, VIO, TRN)는 Jetson이 담당.

## 사실 관계: STM32는 이미 핵심

- **Pixhawk 6X = STM32H743/H753 기반 FC** → PX4 Autopilot이 STM32에서 도는 구조. 즉 현재 아키텍처의 항법·제어·Fail-Safe는 **이미 STM32가 수행**.
- Jetson은 고수준 AI( YOLO 타격, VIO 융합 보조)만 담당. STM32 단독이면 이 고수준 기능이 빠짐.

## 활용 시나리오 3가지

### A. STM32 단독 (Jetson 제거) — 경량화
- 가능: 기본 자율비행(PX4), 단순 경로, GPS/RTK 항법, 기본 Fail-Safe
- 불가: YOLO 타격, 실시간 VIO(연산 부족), TRN DTED 대조(메모리/플롭스 부족)
- 한계: STM32H7(480MHz, RAM ~1MB)은 딥러닝 추론·SLAM에 턱없이 부족. DSVO/DF-VO 계열 경량 VIO도 Cortex-M에서 실시간 어려움.
- 용도: **초경량 정찰기, 저비용 decoy, 단순 RTB only 드론**

### B. STM32 보조 MCU 활용 (Jetson + STM32 분업 강화) — 권장
- STM32를 **안전 보험**으로 격상: Kill-Switch 로컬 강제, 시간예약중단 타이머, 센서퓨전 백업
- Jetson 죽어도 STM32가 즉시 abort/RTL 수행 → `[[uav-mission-approval-abort]]` 원칙 "중단은 로컬 강제" 구현
- PACNav 계열 통신두절 복원력도 STM32 레벨에서 보조 가능

### C. STM32H7 + 저전력 NPU 보드 조합
- STM32H7 + GAP8/사우스브릿지 NPU 로 경량 AI 분산 (Jetson 대체 가능성, but 성능↓)
- 연구단계, 실전 검증 부족

## 관련 문헌 (수집 2026-07-27)

- 1810.03963 DSVO: Direct Stereo Visual Odometry (경량 VIO 참고, but Cortex-M 부적합) ^[raw/articles/2018-dsvo-direct-stereo-visual-odometry.md]
- 2106.08878 Autonomous Navigation System for a Delivery Drone (임베디드 항법) ^[raw/articles/2021-autonomous-navigation-system-for-a-delivery-drone.md]
- 2005.12813 AlphaPilot: Autonomous Drone Racing (경량 자율비행) ^[raw/articles/2020-alphapilot-autonomous-drone-racing.md]
- 2103.00933 DF-VO: What Should Be Learnt for Visual Odometry (학습 기반 VIO) ^[raw/articles/2021-df-vo-what-should-be-learnt-for-visual-odometry.md]
- 2511.16144 LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM (경량 SLAM) ^[raw/articles/2025-lego-slam-language-embedded-gaussian-optimization-slam.md]

## 결론

- **STM32는 이미 핵심(FC)**. 질문은 "더 활용" 관점이 맞음 → **시나리오 B(보조 MCU로 안전보험화)** 가 자율타격 체계에 가장 적합.
- Jetson 완전 제거(시나리오 A)는 YOLO 타격/실시간 VIO 포기 → Hunter-Killer 본질 훼손. 단순 정찰/decoy용으로만 한정.
- `[[gnss-denied-autonomous-navigation]]`의 TRN/VIO는 STM32 단독 불가 → 최소 Jetson급 or 시나리오 B 분업 필요.

## 관련 페이지

- [[hunter-killer-drone-system]] — 대상 하드웨어(PRD)
- [[gnss-denied-autonomous-navigation]] — STM32 단독 불가한 항법
- [[uav-mission-approval-abort]] — STM32 보조 MCU로 Kill-Switch 로컬 강제
- [[uav-swarm-defensive-countermeasures]] — 보조 MCU 안전계층
- [[uav-autopilot-stacks]] — PX4/STM32 펌웨어
