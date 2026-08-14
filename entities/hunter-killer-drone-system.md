---
title: Hunter-Killer Drone System (PRD v2 참조)
created: 2026-07-27
updated: 2026-08-09
type: entity
tags:
  - uav
  - swarm
  - software
  - firmware
sources:
  - raw/articles/2026-hunter-killer-drone-prd-v2.md
  - raw/articles/2026-banshee-target-switch-attacks-on-gimbal-stabilized-visual-tracking-sys.md
  - raw/articles/2026-enhancing-graph-based-slam-in-gnss-denied-environments-by-leveraging-l.md
  - raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md
  - raw/youtube/2026-07-29-M5YyDGfKhE8.md
  - raw/youtube/2026-07-29-HMKXMaAzByU.md
  - raw/youtube/2026-07-29-a5kumlJqkQQ.md
  - raw/youtube/2026-07-31-M5YyDGfKhE8.md
  - raw/youtube/2026-07-31-unraT22a4zY.md
  - raw/youtube/2026-07-31-a5kumlJqkQQ.md
  - raw/youtube/2026-08-01-M5YyDGfKhE8.md
  - raw/youtube/2026-08-01-unraT22a4zY.md
  - raw/youtube/2026-08-01-QpWl1EmtWNs.md
  - raw/youtube/2026-08-01-al9ITeP4fUA.md
  - raw/youtube/2026-08-02-HMKXMaAzByU.md
  - raw/youtube/2026-08-02-M5YyDGfKhE8.md
  - raw/youtube/2026-08-02-l2ARv6y70bw.md
  - raw/youtube/2026-08-02-unraT22a4zY.md
  - raw/youtube/2026-08-09-M5YyDGfKhE8.md
  - raw/youtube/2026-08-09-HMKXMaAzByU.md
  - raw/youtube/2026-08-09-unraT22a4zY.md
  - raw/youtube/2026-08-09-l2ARv6y70bw.md
  - raw/youtube/2026-08-04-M5YyDGfKhE8.md
  - raw/youtube/2026-08-04-HMKXMaAzByU.md
  - raw/youtube/2026-08-04-unraT22a4zY.md
  - raw/youtube/2026-08-04-l2ARv6y70bw.md
  - raw/youtube/2026-08-05-M5YyDGfKhE8.md
  - raw/youtube/2026-08-05-HMKXMaAzByU.md
  - raw/youtube/2026-08-05-l2ARv6y70bw.md
  - raw/youtube/2026-08-06-M5YyDGfKhE8.md
  - raw/youtube/2026-08-06-HMKXMaAzByU.md
  - raw/youtube/2026-08-06-l2ARv6y70bw.md
  - raw/youtube/2026-08-11-MGggtBIzvtg.md
  - raw/youtube/2026-08-11-b3lrvZ8MA5E.md
  - raw/youtube/2026-08-11-al9ITeP4fUA.md
  - raw/youtube/2026-08-11-EKpxP2YieZw.md
confidence: medium
contested: false
contradictions: []

raw/youtube/2026-08-06-MGggtBIzvtg.md
raw/youtube/2026-08-06-sriVQXreqG8.md
raw/youtube/2026-08-06-hp4ySL2xzV8.md
raw/youtube/2026-08-06-sEiKDZ6pZo4.md
raw/youtube/2026-08-06-w0z-362DkIU.md
---

# Hunter-Killer Drone System (PRD v2 참조)

군집드론 **킬체인(kill chain)** 하드웨어 참조 구현. 정찰(Hunter) → 타격(Killer) 2계층 구조로, 우리 위키 `combat-swarm-drone-operations`의 "공격용 군집드론 5대 과제" 중 **C2/임무재할당·보안** 과제와 직접 맞닿는 실증 사례.

## 하드웨어 스택 (PRD v2 명세)

| 컴포넌트 | 역할 | 비고 |
| --- | --- | --- |
| Pixhawk Jetson Baseboard | 통합 캐리어 보드 | Pixhawk 6X FC + Jetson Orin Nano 일체형 |
| Pixhawk 6X | 비행 제어기(FC) | PX4 Autopilot, 모터 4개 제어 |
| NVIDIA Jetson Orin Nano | 온보드 AI 컴퓨터 | YOLO 영상분석·비전유도 |
| Skydroid C13 | 짐벌 카메라 | 2K 광학 + 640 열화상 + 1km LRF |
| H-RTK F9P | RTK GPS | 센티미터급(1~2cm) 항법 |
| 4S~6S LiPo | 전원 | PDB→Baseboard POWER |

→ 우리 `uav-autopilot-stacks`(PX4)·`uav-swarm-middleware`(ROS2/DDS) 페이지가 다루는 L1/L2 스택과 **정확히 일치하는 검증된 플랫폼**.

## 소프트웨어 흐름

```
[Hunter] C13+LRF → 목표 위경도 계산 (target_localizer, ROS2)
   │  Wi-Fi Mesh
   ▼
[Killer] 수신 위경도 → 비행 (terminal_homing) → YOLO 락온 → 직충돌
```

- 통신: **MicroXRCE-DDS Agent** (`udp4 -p 8888`)로 PX4↔Jetson 브리지
- 좌표계: `Azimuth = (Heading_drone + Yaw_gimbal) mod 360` 등 변환 모델

## 보안 취약점 (PRD 미언급, 위키 연결)

- **적대적 추적 기만**: Banshee(arXiv 2607.09930)처럼 짐벌 안정화 비전추적을 속이는 공격이 YOLO 락온을 우회 가능 → `combat-swarm-drone-operations`의 "보안" 과제와 직결.
- **Wi-Fi Mesh 교란**: 전파 jamming에 취약. 통신두절 시 `uav-swarm-middleware`/PACNav 계열 복원력 필요.
- **GNSS 교란**: GPS spoofing/jamming 시 TRN/VIO 기반 `gnss-denied-autonomous-navigation` 항법 없이는 복귀 불가 → 생존성 필수.
- **인간 게이트 부재**: 자율타격이나 우리 `text-to-uav-mission`의 "자동계획→인간승인" 원칙이 빠짐 — 운용 윤리 측면에서 검토 필요.

## 관련 페이지

- [[combat-swarm-drone-operations]] — 공격용 군집드론 5대 과제, 킬체인 매핑
- [[uav-autopilot-stacks]] — PX4/Jetson 통합 보드
- [[uav-swarm-middleware]] — ROS2/DDS/MicroXRCE 통신
- [[text-to-uav-mission]] — 자율타격에도 인간승인 게이트 필요
- [[gnss-denied-autonomous-navigation]] — jamming/spoofing 시 TRN/VIO 복귀 항법
- [[uav-mission-approval-abort]] — 사전승인 + 긴급취소(Kill-Switch) 설계
- [[uav-swarm-defensive-countermeasures]] — 본 시스템 취약점(Banshee/교란) 대응 방어 체계

## 관련 영상 (YouTube 보강 2026-07-29)

실전 데모 보강: 러시아 게란(Geran) 드론의 수동 레이더 호밍 탐색두 장착, GPO Technologies의 엣지 AI 오토호밍 FPV 야외 시험 등으로 Killer 단말 유도(terminal_homing)의 실증 사례가 추가됨.

- [러시아 게란 드론 수동 레이더 호밍 탐색두 장착 (DEEP WEAPONS)](https://youtu.be/hp4ySL2xzV8) — 게란(Geran) 드론에 수동 레이더 호밍 seeker 탑재, HK 표적 유도 생존성 강화 사례.
- [GPO FPV 자율인간추적/오토호밍 -12°C 야외 시험](https://youtu.be/sEiKDZ6pZo4) — 엣지 AI 자율 인간추적·오토호밍 FPV, Killer terminal_homing 실증.
- [GPO 엣지 AI 오토호밍 500m 표적 록온→타격 (No GPS)](https://youtu.be/w0z-362DkIU) — GPS·클라우드·신호 없이 500m 표적 록온→타격, GNSS 불능 환경 킬러 유도.

## 관련 영상 (YouTube 보강 2026-07-31)

추가 HK 시스템 실증 사례 보강: Spectrum UV·Data Engineering Edge 자율 살상 드론 개요, DEEP WEAPONS 러시아 게란 수동 레이더 호밍, GPO Technologies FPV 오토호밍 -12°C 야외 시험, GPO 500m 표적 록온→타격, News Direct US Sea Hunter 해양 자율 드론 실증.

- [Spectrum UV — Autonomous killer drones](https://youtu.be/MGggtBIzvtg) — 자율 살상 드론 기본 개요, HK 시스템 정의.
- [Data Engineering Edge — Autonomous killer drones](https://youtu.be/DK6IGG5zRU8) — 자율 살상 드론 대중적 설명 (조회 45만+).
- [DEEP WEAPONS — Silent Hunters: Russian Geran with Passive Radar Homing](https://youtu.be/hp4ySL2xzV8) — 게란 드론 수동 레이더 호밍 탐색두 장착, HK 표적 유도 생존성 강화.
- [GPO Technologies — FPV Autohoming -12°C 야외 시험](https://youtu.be/sEiKDZ6pZo4) — 엣지 AI 자율 인간추적·오토호밍 FPV, 극한 환경 Killer 단말 실증.
- [GPO Technologies — Edge AI Autohoming 500m Target Lock to Impact (No GPS)](https://youtu.be/w0z-362DkIU) — GPS·클라우드·신호 없이 500m 표적 록온→타격, GNSS 불능 환경 킬러 유도.
- [News Direct — US Testing Autonomous Sea Hunter Ocean Drone](https://youtu.be/sriVQXreqG8) — 미국 Sea Hunter 자율 해양 정찰 드론 실증, HK Hunter 플랫폼 사례.

## 관련 영상 (YouTube 보강 2026-08-01)

새로운 날짜의 재캡처로 HK 시스템 정의·실전 유도 사례 확인.

- [Spectrum UV — Autonomous killer drones](https://youtu.be/MGggtBIzvtg) — 자율 살상 드론 기본 개요, HK 시스템 정의.
- [DEEP WEAPONS — Silent Hunters: Russian Geran with Passive Radar Homing](https://youtu.be/hp4ySL2xzV8) — 게란 드론 수동 레이더 호밍 탐색두 장착, HK 표적 유도 생존성 강화.
- [GPO Technologies — FPV Autohoming -12°C 야외 시험](https://youtu.be/sEiKDZ6pZo4) — 엣지 AI 자율 인간추적·오토호밍 FPV, 극한 환경 Killer 단말 실증.
- [GPO Technologies — Edge AI Autohoming 500m Target Lock to Impact (No GPS)](https://youtu.be/w0z-362DkIU) — GPS·클라우드·신호 없이 500m 표적 록온→타격, GNSS 불능 환경 킬러 유도.

## 관련 영상 (YouTube 보강 2026-08-02)

ESPIRIDI C-UAS Kill Chain 영상은 탐지->추적->식별->타격의 전체 교전 과정을 보여주어, HK 시스템의 terminal_homing 단계가 실전 교전 체계에서 어떤 위치를 차지하는지 맥락을 제공한다.

- [Autonomous killer drones](https://youtu.be/MGggtBIzvtg) — 자율 살상 드론 기본 개요, HK 시스템 정의.
- [U.S. testing autonomous Sea Hunter ocean drone](https://youtu.be/sriVQXreqG8) — 미국 Sea Hunter 자율 해양 정찰 드론 실증, HK Hunter 플랫폼 사례.
- [Hunter-Killer drones - Terminator 1/2](https://youtu.be/5knSEDXDa_0) — 영화 터미네이터 속 헌터-킬러 드론 개념, HK 체계 상상.
- [The Ultimate Drone War Simulation | DEWs, Missiles & EW Kill Chain](https://youtu.be/EKpxP2YieZw) — DEW/미사일/전자전 킬체인 포함 무인전 시뮬레이션, HK 교전 맥락.
- [Breaking the Drone Threat: Inside the C-UAS Kill Chain](https://youtu.be/l2ARv6y70bw) — C-UAS 킬체인 전체 교전 과정을 상세 분석, 실전 방어 관점의 새로운 시각.
- [How China's new 'kill chain' swarm system changes everything](https://youtu.be/5k9F7QK66Ws) — 중국 신형 킬체인 군집 체계가 바꿀 전장 변화, HK 시스템 운용 맥락.
- [Silent Hunters: Russian Military Equips Geran Drones with Cutting-Edge Passive Radar Homing](https://youtu.be/hp4ySL2xzV8) — 게란 드론 수동 레이더 호밍 탐색두 장착, HK 표적 유도 생존성 강화.
- [FPV Drone Autonomous Human Tracking Test | Edge AI Autohoming System | -12C Field Test](https://youtu.be/sEiKDZ6pZo4) — 엣지 AI 자율 인간추적/오토호밍 FPV, 극한 환경 Killer 단말 실증.
- [Edge AI Autohoming for FPV Drones - 500m Target Lock to Impact | No GPS, No Cloud, No Signal](https://youtu.be/w0z-362DkIU) — GPS/클라우드/신호 없이 500m 표적 록온->타격, GNSS 불능 환경 킬러 유도.

## 관련 영상 (YouTube 보강 2026-08-03)

- [Autonomous killer drones](https://youtu.be/MGggtBIzvtg) — 자율 살상 드론 기본 개요, HK 시스템 정의.
- [Awesome Hunter Killer Drone Multi-Kill](https://youtu.be/RVFbk787cl8) — 헌터-킬러 드론 다중 살상 시연, HK 시스템 개념.
- [Hunter-Killer drones - Terminator 1/2](https://youtu.be/5knSEDXDa_0) — 영화 터미네이터 속 헌터-킬러 드론 개념, HK 체계 상상.
- [The Ultimate Drone War Simulation | DEWs, Missiles & EW Kill Chain](https://youtu.be/EKpxP2YieZw) — DEW/미사일/전자전 킬체인 포함 무인전 시뮬레이션, HK 교전 맥락.
- [Silent Hunters: Russian Military Equips Geran Drones with Cutting-Edge Passive Radar Homing](https://youtu.be/hp4ySL2xzV8) — 게란 드론 수동 레이더 호밍 탐색두 장착, HK 표적 유도 생존성 강화.
- [FPV Drone Autonomous Human Tracking Test | Edge AI Autohoming System | -12°C Field Test](https://youtu.be/sEiKDZ6pZo4) — 엣지 AI 자율 인간추적/오토호밍 FPV, 극한 환경 Killer 단말 실증.
- [Edge AI Autohoming for FPV Drones — 500m Target Lock to Impact | No GPS, No Cloud, No Signal](https://youtu.be/w0z-362DkIU) — GPS/클라우드/신호 없이 500m 표적 록온→타격, GNSS 불능 환경 킬러 유도.

## 관련 영상 (YouTube 보강 2026-08-04)

- [Autonomous killer drones](https://youtu.be/MGggtBIzvtg) — 자율 살상 드론의 기본 개요, HK 시스템 정의 확인.
- [Autonomous killer drones](https://youtu.be/DK6IGG5zRU8) — 자율 살상 드론 대중적 설명, HK 시스템 운용 개념 재확인.
- [Silent Hunters: Russian Military Equips Geran Drones with Cutting-Edge Passive Radar Homing](https://youtu.be/hp4ySL2xzV8) — 러시아 게란 드론에 수동 레이더 호밍 탐색두 장착, HK 표적 유도 생존성 강화 사례.
- [FPV Drone Autonomous Human Tracking Test | Edge AI Autohoming System | -12°C Field Test](https://youtu.be/sEiKDZ6pZo4) — 엣지 AI 자율 인간추적·오토호밍 FPV, 극한 환경(-12°C)에서 Killer 단말 실증.
- [Edge AI Autohoming for FPV Drones — 500m Target Lock to Impact | No GPS, No Cloud, No Signal](https://youtu.be/w0z-362DkIU) — GPS·클라우드·신호 없이 500m 표적 록온→타격, GNSS 불능 환경 킬러 유도.

## 관련 영상 (YouTube 보강 2026-08-05)

- [Autonomous killer drones](https://youtu.be/MGggtBIzvtg) — 자율 살상 드론 기본 개요, HK 시스템 정의 재확인.
- [U.S. testing autonomous Sea Hunter ocean drone](https://youtu.be/sriVQXreqG8) — 미국 Sea Hunter 자율 해양 정찰 드론 실증, HK Hunter 플랫폼 사례.
- [Silent Hunters: Russian Military Equips Geran Drones with Cutting-Edge Passive Radar Homing](https://youtu.be/hp4ySL2xzV8) — 러시아 게란 드론에 수동 레이더 호밍 탐색두 장착, HK 표적 유도 생존성 강화 사례.
- [FPV Drone Autonomous Human Tracking Test | Edge AI Autohoming System | -12°C Field Test](https://youtu.be/sEiKDZ6pZo4) — 엣지 AI 자율 인간추적·오토호밍 FPV, 극한 환경(-12°C)에서 Killer 단말 실증 재확인.
- [Edge AI Autohoming for FPV Drones — 500m Target Lock to Impact | No GPS, No Cloud, No Signal](https://youtu.be/w0z-362DkIU) — GPS·클라우드·신호 없이 500m 표적 록온→타격, GNSS 불능 환경 킬러 유도 재확인.

## 관련 영상 (YouTube 보강 2026-08-06)

2026-08-06 영상 보강을 통해 러시아 게란 드론의 수동 레이더 호밍 탐색두 장착, GPO Technologies의 극한 환경(-12°C) 오토호밍 실증, 그리고 GPS·클라우드·신호 없이 500m 표적 록온→타격하는 엣지 AI 시스템이 확인되어, HK 시스템의 terminal_homing 유도 기술이 실전 환경에서도 작동 가능함을 재확인했다.

- [Autonomous killer drones](https://youtu.be/MGggtBIzvtg) — Autonomous killer drones — 자율 살상 드론 기본 개요, HK 시스템 정의 확인
- [U.S. testing autonomous Sea Hunter ocean drone](https://youtu.be/sriVQXreqG8) — U.S. testing autonomous Sea Hunter ocean drone — 미국 Sea Hunter 자율 해양 정찰 드론 실증, HK Hunter 플랫폼 사례
- [Silent Hunters: Russian Military Equips Geran Drones with Cutting-Edge Passive Radar Homing](https://youtu.be/hp4ySL2xzV8) — Silent Hunters: Russian Geran with Passive Radar Homing — 게란 드론 수동 레이더 호밍 탐색두 장착, HK 표적 유도 생존성 강화
- [FPV Drone Autonomous Human Tracking Test | Edge AI Autohoming System | -12°C Field Test](https://youtu.be/sEiKDZ6pZo4) — FPV Drone Autonomous Human Tracking Test | Edge AI Autohoming -12C — 엣지 AI 자율 인간추적/오토호밍 FPV, 극한 환경에서 Killer 단말 실증
- [Edge AI Autohoming for FPV Drones — 500m Target Lock to Impact | No GPS, No Cloud, No Signal](https://youtu.be/w0z-362DkIU) — Edge AI Autohoming for FPV Drones 500m Target Lock to Impact No GPS — GPS/클라우드/신호 없이 500m 표적 록온→타격, GNSS 불능 환경 킬러 유도

## 관련 영상 (YouTube 보강 2026-08-07)

새로 수집된 자료를 통해 HK 체계에 대한 실제 시연/구현 및 방어 체계가 추가됨.

- [Autonomous killer drones](https://youtu.be/MGggtBIzvtg) — 자율 살상 드론 기본 개요, HK 시스템 정의
- [U.S. testing autonomous Sea Hunter ocean drone](https://youtu.be/sriVQXreqG8) — 미국 Sea Hunter 자율 해양 정찰 드론 실증, HK Hunter 플랫폼 사례
- [Anduril Unveils Roadrunner & Roadrunner-M](https://youtu.be/al9ITeP4fUA) — Anduril 로드러너/로드러너-M 대응 시스템 공개, 킬체인 방어 차원
- [Breaking the Drone Threat: Inside the C-UAS Kill Chain](https://youtu.be/l2ARv6y70bw) — C-UAS 킬체인 전체 교전 과정 상세 분석, 실전 방어 관점의 새로운 시각

## 관련 영상 (YouTube 보강 2026-08-15)

새로 수집된 자료를 통해 타겟 잠금 및 항법 기술이 갱신됨.

- [Real-Time Object Tracking on FPV UAV Drone | DIY AI Target Lock System Test](https://youtu.be/w5KkbRVhqzE) — FPV 드론 실시간 목표추적, 자율 락온 시스템 실험
