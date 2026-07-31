---
title: "PX4 v1.17 + ArduPilot 4.7.0 종합 릴리즈 비교 보고서"
created: 2026-07-31
updated: 2026-07-31
type: report
tags: [uav, firmware, release, comparison]
sources:
  - raw/articles/2026-07-31-px4-v1.17-release-notes.md
  - raw/articles/2026-07-31-ardupilot-4.7-release-notes.md
confidence: high
contested: false
contradictions: []
---

# PX4 v1.17 + ArduPilot 4.7.0 종합 릴리즈 비교 보고서

## 1. 개요

| 항목 | PX4 v1.17.0 | ArduPilot 4.7.0 |
|------|-------------|-----------------|
| **릴리즈일** | 2026-05-13 | 2026-07-21 (Copter), 2026-07-27 (Plane) |
| **지원 드론 종류** | 멀티콥터, Fixed-Wing, VTOL, Rover | Copter, Plane, Rover, Sub, Tracker, Periph |
| **주요 강조점** | Altitude Cruise, ROS 2 통합, Zenoh | EKF3 개선, CAN 페리펄티, 보안 강화 |

## 2. PX4 v1.17.0 주요 변경사항

### 2.1 신규 기능
| 기능 | 설명 | 적용 파라미터/모듈 |
|------|------|-------------------|
| **Altitude Cruise** | 멀티콥터 새 비행 모드. Tilt과 Heading 유지 | `MPC_ZOOM_RC_VALUE`, `MPC_RA_ZOOM_SP` |
| **Fixed Wing 자동 이착륙** | GNSS 손실 시 자동 클라임 + 레벨 윙 | `FW_THR_MAX`, `FW_THR_SCL` |
| **ROS 2 고수준 제어** | `FwLateralLongitudinalSetpointType` | ROS 2 Control Interface |
| **MC Neural Network Control** | TensorFlow Lite Micro 통합 | `MC_NN_EN` (실험적) |
| **Zenoh 미들웨어** | `rmw_zenoh` 호환, FMU-v6xRT 내장 | `SER_TEL1_CFG`, `SER_TEL2_CFG` |

### 2.2 하드웨어 지원 추가
| 하드웨어 | 유형 | 비고 |
|----------|------|------|
| **Radiolink PIX6** | 새 FC | PX4-Autopilot#25562 |
| **CUAV X25-Evo** | 새 FC | PX4-Autopilot#25176 |
| **Accton Godwit GA1** | 새 FC | PX4-Autopilot#25411 |
| **CUAV Pixhawk V6X** | 빌드 타겟 | 기존 하드웨어 지원 강화 |

### 2.3 주요 파라미터 변경
| 파라미터 | 변경 내용 | 업그레이드 시 주의사항 |
|----------|----------|-------------------|
| `SENS_BAR_AUTOCAL` | 바로미터 자동 캘리브레이션 | GNSS 높이 기준 |
| `EKF2_MIN_RNG` | 최소 거리 임계값 조정 | 라이다/초음파 센서 |
| `MAN_DEADZONE` | 조종채널 데드존 | RC 입력 민감도 |
| `MAV_PROTO_VER` | MAVLink 프로토콜 버전 | GCS 호환성 |

## 3. ArduPilot 4.7.0 주요 변경사항

### 3.1 신규 기능
| 기능 | 설명 | 적용 파라미터/모듈 |
|------|------|-------------------|
| **EKF3 멀티-센서 융합** | GNSS/비전/IMU 자동 스위칭 | `EK3_SRC1_POSZ`, `EK3_GYRO_CAL` |
| **CAN 페리펄티 확장** | UAVCAN 2.0 지원 강화 | `CAN_D1_PROTOCOL`, `CAN_P1_AUTOSTART` |
| **보안 강화** | MAVLink 암호화 (실험적) | `MAV_ENC_KEY`, `MAV_AUTH_EN` |
| **배터리 관리 개선** | 잔여 시간 계산 정확도 향상 | `BATT_LOW_MAH`, `BATT_LOW_VOLT` |
| **VTOL 전환 최적화** | 고속 VTOL 전환 시 자동 보정 | `VT_ARSP_TRANS`, `VT_THR_TRANS` |

### 3.2 하드웨어 지원 추가
| 하드웨어 | 유형 | 비고 |
|----------|------|------|
| **Holybro Kakute H7** | 새 FC | ArduPilot#26052 |
| **Matek F405-WING** | Fixed-Wing | ArduPilot#25149 |
| **Cube Orange+** | 개선된 버전 | 기존 Cube Orange 하위 호환 |

### 3.3 주요 파라미터 변경
| 파라미터 | 변경 내용 | 업그레이드 시 주의사항 |
|----------|----------|-------------------|
| `EK3_SRC1_POSZ` | 위치 추정 소스 변경 | 비전/레이더/바로미터 선택 |
| `FS_GPS_ENABLE` | GPS 실패 안전 모드 | GNSS-Denied 환경 시 비활성화 필요 |
| `BATT_LOW_MAH` | 배터리 임계치 재계산 | 사용 패턴에 따라 재설정 |
| `ARMING_CHECK` | 안장 검증 비트마스크 | 비행 전 재검증 필수 |

## 4. 핵심 비교 및 차이점

### 4.1 GNSS-Denied 항법
| 항목 | PX4 v1.17 | ArduPilot 4.7 |
|------|-----------|---------------|
| **VIO 지원** | `EKF2_AID_MASK` 비트 2,8 (Vision, Flow) | `EK3_SRC1_VISION_POS` |
| **Optical Flow** | `EKF_USES_GPS_NOT_FLOW` 경고 | `FLOW_*` 파라미터 |
| **TRN 지원** | DTED + LRF (커스텀) | `EK3_SRC1_TERRAIN` |

### 4.2 안전/방어 메커니즘
| 항목 | PX4 v1.17 | ArduPilot 4.7 |
|------|-----------|---------------|
| **인간 승인 게이트** | `COM_PREARM` (0~1) | `ARMING_CHECK` (0~7 비트마스크) |
| **Kill-Switch** | `COM_KILL` (0~1) | `ARMING_KILLSWITCH` |
| **통신 손실** | `COM_DL_LOSS_T` (5~300s) | `FS_GCS_ENABLE` + `FS_THR_ENABLE` |
| **배터리 실패** | `BAT_CRIT_THR`, `COM_LOW_BAT_ACT` | `BATT_LOW_MAH`, `BATT_LOW_VOLT` |

### 4.3 ROS 2 / 미들웨어
| 항목 | PX4 v1.17 | ArduPilot 4.7 |
|------|-----------|---------------|
| **ROS 2 통합** | 공식 지원 (rmw_zenoh) | MAVROS + DDS (서드파티) |
| **Zenoh** | 내장 (experimental) | 미지원 |
| **MAVLink** | MAVLink 2/3 지원 | MAVLink 2 (MAVLink 3 실험적) |

## 5. 헌터킬러 applications 적용 가이드

### 5.1 GNSS-Denied 비행
```bash
# PX4: VIO + Optical Flow 활성화
param set EKF2_AID_MASK 10  # Vision + Flow
param set COM_GNSSLOSS_ACT 2  # GNSS 손실 시 Hold

# ArduPilot: EKF3 소스 변경
param set EK3_SRC1_POSZ 6  # Vision
param set FS_GPS_ENABLE 0  # GNSS 손실 시 안전 비활성화
```

### 5.2 안전/방어 메커니즘
```bash
# PX4: 인간 승인 게이트
param set COM_PREARM 1  # PreArm 승인 필수
param set COM_KILL 1  # Kill-Switch 활성화

# ArduPilot: 안장 검증
param set ARMING_CHECK 7  # 전체 검증
param set ARMING_KILLSWITCH 1  # Kill-Switch 활성화
```

## 6. 결론

PX4 v1.17은 **ROS 2/Zenoh 미들웨어**와 **Neural Network 제어**로 미래지향적인 기능을 제공합니다.
ArduPilot 4.7은 **EKF3 멀티-센서 융합**과 **CAN 페리펄티**로 하드웨어 호환성을 강화했습니다.
두 스택 모두 **GNSS-Denied 항법**과 **안전 메커니즘**을 강화했으나, PX4는 ROS 2 생태계에,
ArduPilot는 하드웨어 호환성에 중점을 둔 것을 확인했습니다.
