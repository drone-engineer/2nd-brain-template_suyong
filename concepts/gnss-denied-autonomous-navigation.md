---
title: GNSS-Denied 자율 항법 (UAV)
created: 2026-07-27
updated: 2026-08-05
type: concept
tags:
  - uav
  - swarm
  - control
  - firmware
  - security
sources:
  - raw/articles/2026-enhancing-graph-based-slam-in-gnss-denied-environments-by-leveraging-l.md
  - raw/articles/2023-long-range-uav-thermal-geo-localization-with-satellite-imagery.md
  - raw/articles/2021-an-equivariant-filter-for-visual-inertial-odometry.md
  - raw/articles/2011-vision-based-navigation-ii-error-analysis-for-a-navigation-algorithm-b.md
  - raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md
  - raw/youtube/2026-07-29-p8frNNYQNV4.md
  - raw/youtube/2026-07-29-i1QRqu3Cocw.md
  - raw/youtube/2026-07-29-V5ZMhFyWQa8.md
  - raw/youtube/2026-07-31-p8frNNYQNV4.md
  - raw/youtube/2026-07-31-i1QRqu3Cocw.md
  - raw/youtube/2026-07-31-V5ZMhFyWQa8.md
  - raw/youtube/2026-07-31-sEiKDZ6pZo4.md
  - raw/youtube/2026-07-31-w0z-362DkIU.md
- raw/youtube/2026-08-01-p8frNNYQNV4.md
- raw/youtube/2026-08-01-i1QRqu3Cocw.md
- raw/youtube/2026-08-01-V5ZMhFyWQa8.md
- raw/youtube/2026-08-01-sEiKDZ6pZo4.md
- raw/youtube/2026-08-01-w0z-362DkIU.md
- raw/youtube/2026-08-02-V5ZMhFyWQa8.md
- raw/youtube/2026-08-02-i1QRqu3Cocw.md
- raw/youtube/2026-08-02-p8frNNYQNV4.md
- raw/youtube/2026-08-04-p8frNNYQNV4.md
- raw/youtube/2026-08-04-i1QRqu3Cocw.md
- raw/youtube/2026-08-04-V5ZMhFyWQa8.md
- raw/youtube/2026-08-05-p8frNNYQNV4.md
- raw/youtube/2026-08-05-i1QRqu3Cocw.md
- raw/youtube/2026-08-05-V5ZMhFyWQa8.md
confidence: medium
contested: false
contradictions: []

---

# GNSS-Denied 자율 항법 (UAV)

GPS 마비·무선 교란(Jamming/Spoofing)으로 위성항법이 불능인 위급 상황에서, 사전 입력 경로·지형정보만으로 지정 위치까지 복귀하는 기술. 핵심 질문: **"GPS 없이 내 위치를 어떻게 알고, 어떻게 길을 찾는가?"**

## 핵심 기술 3가지

### ① TRN (Terrain Referenced Navigation, 지형 참조 항법)
하부 고도계(LiDAR/레이저)로 지형 높낮이 프로파일 측정 → 사전 DTED 지도와 대조(Matching)해 현재 좌표 역산. (토마호크 순항미사일 방식과 유사)

### ② DSM/Orthophoto Visual Matching (정방형 위성사진 비전 매칭)
하부 카메라 실시간 촬영 → 사전 저장 위성/항공사진과 AI 특징점(도로망·강·교차로·건물) 대조 → 수 미터 오차 내 글로벌 위경도 산출.

### ③ Optical Flow & VIO (Visual Inertial Odometry)
카메라 픽셀 흐름 + IMU(가속도/자이로) 결합 → TRN 결과 사이 짧은 이동 거리·방향 연속 계산으로 위치 오차 누적 방지.

## 위급 상황 Fail-Safe 제어 루틴

통신 두절·GPS 교란 감지 시 온보드 컴패니언 컴퓨터(Jetson)가 실행:
1. GNSS 손실 탐지 → TRN/VIO로 전환
2. 사전 입력 경로 + 지형정보로 지정 복귀점(RTB) 항법
3. VIO로 구간 오도메트리 보정 (Dead-reckoning 누적 오차 억제)

## 우리 위키와의 연결

- **PACNav** (`[[uav-swarm-middleware]]` 원천): 통신두절 환경에서 지역관측으로 집단 항법 — GNSS-Denied와 동일 맥락의 복원력. ^[raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md]
- **Hunter-Killer PRD** (`[[hunter-killer-drone-system]]`): Wi-Fi Mesh jamming 취약 → GNSS-Denied 항법이 생존성 필수.
- **소프트웨어 스택** (`[[uav-autopilot-stacks]]`/`[[uav-swarm-middleware]]`): TRN/VIO는 PX4+Jetson 위에서 도는 상위 로직.

## 관련 논문 (수집 2026-07-27)

- 2605.20484 Enhancing Graph-Based SLAM in GNSS-Denied environments (학습 특징 활용 SLAM) ^[raw/articles/2026-enhancing-graph-based-slam-in-gnss-denied-environments-by-leveraging-l.md]
- 2306.02994 Long-range UAV Thermal Geo-localization with Satellite Imagery (위성사진 비전 매칭) ^[raw/articles/2023-long-range-uav-thermal-geo-localization-with-satellite-imagery.md]
- 2104.03532 Equivariant Filter for Visual Inertial Odometry (VIO 필터) ^[raw/articles/2021-an-equivariant-filter-for-visual-inertial-odometry.md]
- 1107.1470 Vision-Based Navigation II: Error Analysis (비전항법 오차 분석) ^[raw/articles/2011-vision-based-navigation-ii-error-analysis-for-a-navigation-algorithm-b.md]

## 관련 페이지

- [[uav-autopilot-stacks]] — PX4/Jetson 플랫폼
- [[uav-swarm-middleware]] — PACNav 통신두절 복원력
- [[hunter-killer-drone-system]] — jamming 취약 → GNSS-Denied 생존성
- [[combat-swarm-drone-operations]] — 5대 과제 중 통신보안/복원력
- [[uav-mission-approval-abort]] — abort 후 복귀/중단
- 구현 가이드: `docs/workflow/px4-ekf2-vio-prototype.md` (EKF2+VIO+TRN+Kill-Switch)

## 관련 영상 (YouTube 보강 2026-07-29)

실전 항법 보강: Nicholas Rehm의 안티재밍 자율 DIY 드론, Ian Laffey(Theseus)의 군용 드론 GPS 없는 비행, Beyond Vision의 쉬운 설명 영상으로 GNSS-Denied 항법의 구현·설명 사례가 추가됨.

- [Nicholas Rehm — GPS-Denied, Anti-Jam Autonomous DIY Drone](https://youtu.be/p8frNNYQNV4) — GPS 불능·재밍 대항 자율 DIY 드론 작동 원리, 안티재밍 항법 구현.
- [First Principles — Military Drones Without GPS (Ian Laffey, Theseus)](https://youtu.be/i1QRqu3Cocw) — 군용 드론의 GPS 없는 비행 원리, GNSS-Denied 항법 설명.
- [Beyond Vision — How Drones Navigate Without GPS](https://youtu.be/V5ZMhFyWQa8) — GPS 없이 드론이 항법하는 원리 쉬운 설명, 비전/관성 항법 개요.

## 관련 영상 (YouTube 보강 2026-07-31)

실전 항법·자율 운용 보강: Nicholas Rehm GPS 불능·재밍 대항 DIY 드론, Ian Laffey 군용 드론 GPS 없는 비행, Beyond Vision 비전/관성 항법 개요, GPO FPV 오토호밍·500m 표적 록온(No GPS)으로 GNSS-Denied 환경 자율 운용 사례 추가.

- [Nicholas Rehm — GPS-Denied, Anti-Jam Autonomous DIY Drone](https://youtu.be/p8frNNYQNV4) — GPS 불능·재밍 대항 자율 DIY 드론 작동 원리, 안티재밍 항법 구현 (재캡처).
- [First Principles — Military Drones Without GPS (Ian Laffey, Theseus)](https://youtu.be/i1QRqu3Cocw) — 군용 드론의 GPS 없는 비행 원리, GNSS-Denied 항법 설명 (재캡처).
- [Beyond Vision — How Drones Navigate Without GPS](https://youtu.be/V5ZMhFyWQa8) — GPS 없이 드론이 항법하는 원리 쉬운 설명, 비전/관성 항법 개요 (재캡처).
- [GPO Technologies — FPV Autohoming -12°C 야외 시험](https://youtu.be/sEiKDZ6pZo4) — 엣지 AI 자율 인간추적·오토호밍 FPV, GPS 없이 -12°C 극한 환경 운용.
- [GPO Technologies — Edge AI Autohoming 500m Target Lock to Impact (No GPS)](https://youtu.be/w0z-362DkIU) — GPS·클라우드·신호 없이 500m 표적 록온→타격, GNSS-Denied 환경 킬러 유도.

## 관련 영상 (YouTube 보강 2026-08-01)

GNSS-Denied 자율 항법 재캡처 확인: Nicholas Rehm 안티재밍 DIY 드론, Ian Laffey 군용 드론 GPS 없는 비행, Beyond Vision 비전/관성 항법 개요, GPO FPV 오토호밍·500m 표적 록온(No GPS)으로 GNSS-Denied 환경 자율 운용 사례 재확인.

- [Nicholas Rehm — GPS-Denied, Anti-Jam Autonomous DIY Drone](https://youtu.be/p8frNNYQNV4) — GPS 불능·재밍 대항 자율 DIY 드론 작동 원리, 안티재밍 항법 구현 (재캡처).
- [First Principles — Military Drones Without GPS (Ian Laffey, Theseus)](https://youtu.be/i1QRqu3Cocw) — 군용 드론의 GPS 없는 비행 원리, GNSS-Denied 항법 설명 (재캡처).
- [Beyond Vision — How Drones Navigate Without GPS](https://youtu.be/V5ZMhFyWQa8) — GPS 없이 드론이 항법하는 원리 쉬운 설명, 비전/관성 항법 개요 (재캡처).
- [GPO Technologies — FPV Autohoming -12°C 야외 시험](https://youtu.be/sEiKDZ6pZo4) — 엣지 AI 자율 인간추적·오토호밍 FPV, GPS 없이 -12°C 극한 환경 운용 (재캡처).
- [GPO Technologies — Edge AI Autohoming 500m Target Lock to Impact (No GPS)](https://youtu.be/w0z-362DkIU) — GPS·클라우드·신호 없이 500m 표적 록온→타격, GNSS-Denied 환경 킬러 유도 (재캡처).

## 관련 영상 (YouTube 보강 2026-08-02)

- [GPS-Denied, Anti-Jam Autonomous DIY Drone: How It Works](https://youtu.be/p8frNNYQNV4) — GPS 불능/재밍 대항 자율 DIY 드론 작동 원리, 안티재밍 항법 구현.
- [How Do Military Drones Fly Without GPS? | Ian Laffey, Theseus](https://youtu.be/i1QRqu3Cocw) — 군용 드론의 GPS 없는 비행 원리, GNSS-Denied 항법 설명.
- [How Drones Navigate Without GPS: Explained Simply](https://youtu.be/V5ZMhFyWQa8) — GPS 없이 드론이 항법하는 원리 쉬운 설명, 비전/관성 항법 개요.

## 관련 영상 (YouTube 보강 2026-08-03)

- [GPS-Denied, Anti-Jam Autonomous DIY Drone: How It Works](https://youtu.be/p8frNNYQNV4) — GPS 불능/재밍 대항 자율 DIY 드론 작동 원리, 안티재밍 항법 구현.
- [How Do Military Drones Fly Without GPS? | Ian Laffey, Theseus](https://youtu.be/i1QRqu3Cocw) — 군용 드론의 GPS 없는 비행 원리, GNSS-Denied 항법 설명.
- [How Drones Navigate Without GPS: Explained Simply](https://youtu.be/V5ZMhFyWQa8) — GPS 없이 드론이 항법하는 원리 쉬운 설명, 비전/관성 항법 개요.
- [Edge AI Autohoming for FPV Drones — 500m Target Lock to Impact | No GPS, No Cloud, No Signal](https://youtu.be/w0z-362DkIU) — GPS/클라우드/신호 없이 500m 표적 록온→타격, GNSS 불능 환경 킬러 유도.

## 관련 영상 (YouTube 보강 2026-08-05)

- [GPS-Denied, Anti-Jam Autonomous DIY Drone: How It Works](https://youtu.be/p8frNNYQNV4) — GPS 불능·재밍 대항 자율 DIY 드론 작동 원리, 안티재밍 항법 구현 재확인.
- [How Do Military Drones Fly Without GPS? | Ian Laffey, Theseus](https://youtu.be/i1QRqu3Cocw) — 군용 드론의 GPS 없는 비행 원리, GNSS-Denied 항법 설명 재확인.
- [How Drones Navigate Without GPS: Explained Simply](https://youtu.be/V5ZMhFyWQa8) — GPS 없이 드론이 항법하는 원리 쉬운 설명, 비전/관성 항법 개요 재확인.
