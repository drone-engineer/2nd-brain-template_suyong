---
title: Hunter-Killer Drone System (PRD v2 참조)
created: 2026-07-27
updated: 2026-07-27
type: entity
tags:
  - uav
  - swarm
  - software
  - firmware
sources:
  - raw/articles/2026-hunter-killer-drone-prd-v2.md
confidence: medium
contested: false
contradictions: []
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
- [[uav-swarm-defensive-countermeasures]] — 본 시스템 취약점(Banshee/교란) 대응 방어 체계
