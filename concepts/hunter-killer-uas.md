---
title: Hunter-Killer 무인헬기 자율 타격 체계
created: 2026-07-31
updated: 2026-07-31
type: concept
tags: [security, uav, control, swarm]
sources:
  - raw/youtube/2026-07-31-unraT22a4zY.md
  - raw/youtube/2026-07-31-M5YyDGfKhE8.md
  - raw/youtube/2026-07-31-a5kumlJqkQQ.md
  - raw/youtube/2026-07-31-w0z-362DkIU.md
  - raw/youtube/2026-07-31-sEiKDZ6pZo4.md
  - raw/youtube/2026-07-31-hp4ySL2xzV8.md
  - raw/youtube/2026-07-31-V5ZMhFyWQa8.md
  - raw/youtube/2026-07-31-i1QRqu3Cocw.md
  - raw/youtube/2026-07-31-p8frNNYQNV4.md
  - raw/youtube/2026-07-31-EKpxP2YieZw.md
  - raw/youtube/2026-07-31-hGakXrt1EFo.md
  - raw/youtube/2026-07-31-sriVQXreqG8.md
  - raw/youtube/2026-07-31-DK6IGG5zRU8.md
  - raw/youtube/2026-07-31-MGggtBIzvtg.md
confidence: medium
contested: true
contradictions: []
---

# Hunter-Killer 무인헬기 자윆 타격 체계 (Hunter-Killer UAS)

## 개요

> "Drone Swarms Are Here. This Technology Could Stop Them." — Sam Eckholm (YouTube)

**Hunter-Killer**(사냥-살해) 무인헬기는 자율적으로 적을 탐지, 추적, 타격하는 무인항공체계이다. 특히 **스웜 드론**에 대한 대응과 **GNSS-Denied 환경**에서의 생존항법이 핵심 과제로 대두되고 있다.

## 1. 킬체인 (Kill Chain)

| 단계 | 설명 | 기술 |
|------|------|------|
| **탐지 (Detect)** | 적 드론/스웜 탐지 | 레이다, 전파 스팩트럼, IR/시각 카메라 |
| **인식 (Classify)** | 적 유형 판별 | 컴퓨터 비전 + YOLOv8 |
| **추적 (Track)** | 지속적 위치 추적 | EKF2 + VIO (PX4) 또는 EKF3 (ArduPilot) |
| **타격 (Engage)** | 실제 타격 | 유도 무장 또는 전파 교란 |
| **평가 (Assess)** | 타격 결과 확인 | 사진/영상 재획득 |

## 2. GNSS-Denied 생존항법

GNSS가 차단된 환경에서 VIO + TRN(Terrain Referenced Navigation) 결합:

- **VIO**: [[uav-autopilot-stacks]] (docs/workflow/px4-ekf2-vio-prototype.md)
- **TRN**: DTED 지형 데이터 + LRF (Laser rangefinder)
- **융합**: EKF2 `EKF2_AID_MASK`에서 비전/레이더/VIO 활성화

> 📎 TRN용 DTED 다운로드 스크립트: `docs/workflow/download-dted.py`

## 3. 안전/방어 메커니즘

### 인간 승인 게이트 (Human-in-the-Loop)
- **ARMING_CHECK** (ArduPilot) / **COM_PREARM** (PX4): 시동 전 인간 승인 필수
- **BRD_SAFETY** (ArduPilot): 안전 스위치를 통한 물리적 승인
- **Kill-Switch**: 실시간 긴급 취소 메커니즘

### 자동 취소 조건
| 조건 | PX4 파라미터 | ArduPilot 파라미터 |
|------|-------------|-------------------|
| 통신 손실 | `COM_DL_LOSS_T` | `FS_GCS_ENABLE` |
| 배터리 부족 | `BAT_CRIT_THR` | `BATT_LOW_MAH` |
| GNSS 손실 | `COM_GNSSLOSS_ACT` | `FS_GPS_ENABLE` |

> 📎 전체 경고 메시지: `docs/tech-stack/px4-ardupilot-warnings.csv` (83개)

## 4. Counter-UAS (대항-드론) 기술

### 탐지 기술
- **Sanctum™** (Lockheed Martin): 전파 스팩트럼 분석 + 머신러닝
- **Divyania Defence**: 스웜 드론 탐지 및 위협 관리

### 대응 기술
- **전파 교란**: GPS/GNSS 신호 교란
- **사이버 공격**: 드론 제어 프로토콜 해킹
- **물리적 타격**: 유도 무장 또는 레이저

## 5. 관련 개념

- [[uav-autopilot-stacks]] — PX4 vs ArduPilot 비교
- [[uav-swarm-middleware]] — MAVLink/ROS 2/DDS 미들웨어 (드론-지상국 통신)

## 6. 참고 자료

### YouTube
- [Drone Swarms Are Here. This Technology Could Stop Them.](https://youtu.be/unraT22a4zY) (Sam Eckholm)
- [Sanctum™ vs. the Swarm: Next-Gen Counter-UAS in Action](https://youtu.be/M5YyDGfKhE8) (Lockheed Martin)
- [Swarm Counter Drone System](https://youtu.be/a5kumlJqkQQ) (Divyania Defence)
