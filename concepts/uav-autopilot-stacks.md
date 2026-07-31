---
title: UAV Autopilot Stacks (PX4 vs ArduPilot)
created: 2026-07-26
updated: 2026-07-26
type: concept
tags:
  - uav
  - swarm
  - software
  - firmware
sources:
  - raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md
  - raw/articles/2021-advanced-drone-swarm-security-blockchain-governance.md
  - raw/articles/2025-a-learning-framework-for-cooperative-collision-avoidance-of-uav-swarms-leveragin.md
  - raw/articles/2025-a-modular-and-scalable-system-architecture-for-heterogeneous-uav-swarm.md
  - raw/articles/2023-tinyslam-based-exploration-with-a-swarm-of-nano-uavs.md
confidence: high
contested: false
contradictions: []
---

# UAV Autopilot Stacks (PX4 vs ArduPilot)

군집드론 소프트웨어 스택의 **L1(펌웨어/비행 스택)** 계층. 개별 기체의 자세·위치 제어, 모터 믹싱, 상태추정, 안전 모드를 담당하는 온보드 소프트웨어다. 위키에 수집된 알고리즘 연구(합의, MARL, 충돌회피)는 사실상 이 비행 스택 위에서 돌아가는 상위 로직이다.

## 두 개의 지배적 오픈소스 스택

| 항목 | PX4 (PX4 Autopilot) | ArduPilot |
| --- | --- | --- |
| 언어/구조 | C++ / 모듈형 uORB 메시지버스 | C++ / 태스크 루프 |
| 생태계 | ROS 2 연동 표준(MAVLink), 상용 드론 많음 | 범용성(비행기/로버/보트), 커뮤니티 방대 |
| 군집 지원 | Offboard 모드 + MAVLink로 다기체 지령 | 스왐/대형비행 스크립트 지원 |
| 시뮬 | Gazebo/Ignition, jMAVSim, AirSim | SITL + Gazebo/Webots |

두 스택 모두 **MAVLink**를 기본 통신 프로토콜로 쓰며, 외부 컴퓨터(지상국 또는 온보드 Companion Computer)에서 상위 제어를 내리는 **Offboard/Companion** 구조를 표준으로 삼는다. [PACNav, 2024] 같은 통신두절 복원력 연구나 [Advanced Drone Swarm Security(BGG), 2021] 같은 보안 연구는 이 분산 기체 전제 위에서 성립한다.

## 왜 중요한가 (위키 관점)

- 수집된 32편 중 알고리즘/제어 논문은 많지만, **어떤 펌웨어 위에서 검증됐는지 명시한 실증이 없다**. 대개 "시뮬 또는 하드웨어 추상화"로 끝남 → 재현성 공백.
- 완전 자율화 5대 과제(보안/윤리/복원력 등) 중 **보안**은 펌웨어 메시지(MEXLink 평문) 취약점과 직결 → `combat-swarm-drone-operations`의 블록체인 인증([BGG, 2021])과 연결.

## 일반 지식 한계 명시

이 페이지의 스택 비교는 **제조사 문서 기반 일반 지식**이며, 위키 수집 논문이 직접 벤치마크한 결과는 아니다. 실증 비중을 높이려면 `raw/articles/`에 "PX4 swarm" / "ArduPilot swarm" 실측 논문을 추가 수집해야 한다 (→ `uav-swarm-middleware`, `uav-swarm-simulation` 참조).

## 핵심 파라미터 기능별 비교 (2026-07-27 기준)

> 📎 전체 149개 파라미터 수집: `docs/tech-stack/px4-ardupilot-parameters.csv` (엑셀 가능)

| 기능 영역 | PX4 파라미터 | ArduPilot 파라미터 | 비고 |
|-----------|-------------|-------------------|------|
| **통신 손실 타임아웃** | `COM_DL_LOSS_T` (5~300s, 기본 10s) | `FS_THR_ENABLE` + `FS_GCS_ENABLE` | PX4는 단일 타임아웃, Ardu는 Enable/Timeout 분리 |
| **GNSS 손실 대응** | `COM_GNSSLOSS_ACT` (0~2, RTL/Hold/Land) | `FS_GPS_ENABLE` + `GPS_AUTO_SWITCH` | PX4는 즉시 행동 선택, Ardu는 자동 스위치 |
| **안장(Arming) 검증** | `COM_ARM_WO_GPS` (0~1), `COM_ARM_IMU_ACC` (0.1~1.0) | `ARMING_CHECK` (0~7), `ARMING_RTLKEYS` | PX4는 세부 IMU/Cali 검증, Ardu는 비트마스크 |
| **배터리 실패** | `COM_LOW_BAT_ACT` (0~3), `COM_BAT_ACT_T` | `BATT_LOW_MAH`, `BATT_LOW_VOLT` | PX4는 액션 선택, Ardu는 임계치 기반 |
| **항법 상태추정** | `EKF2_AID_MASK` (0~255), `EKF2_HGT_MODE` (0~2) | `EK3_SRC1_POSZ` (0~4), `EK3_GYRO_CAL` | PX4는 AID_MASK 비트마스크, Ardu는 소스 인덱스 |
| **속도 제한** | `MPC_XY_VEL_MAX` (0~50 m/s), `MPC_Z_VEL_MAX_DN` | `WHEEL_SPEED_MAX`, `CRUISE_THROTTLE` | PX4는 멀티콥터 최적화, Ardu는 범용 |
| **긴급 RTL** | `RTL_RETURN_ALT` (0~1000m), `RTL_DETECTOR` | `RTL_ALT` (cm), `RTL_RADIUS` | PX4는 고도 우선, Ardu는 반경 기반 |
| **Kill-Switch** | `COM_KILL` (0~1) | `ARMING_KILLSWITCH` | 두 스택 모두 물리적 스위치 지원 |

### 📌 사용 시나리오 예시

- **GNSS-Denied 환경**: `EKF2_AID_MASK`에서 비전/레이더 비트(2+8) 활성화 → `COM_GNSSLOSS_ACT=2`(Hold)로 설정
- **초경량 드론**: `ARMING_CHECK=0`으로 안장 검증 완화 → `SYS_AUTOSTART`로 프레임 빠르게 전환
- **군집 비행**: `COM_RC_LOSS_T` 짧게(3s) → 빠른 실패 감지 + `FS_GCS_ENABLE=2`(RTL) 조합

> 💡 **세팅 팁**: QGroundControl(Master/Param) 또는 Mission Planner(Config/Tuning)에서 실시간 파라미터 편집 후 `.params` 파일로 export → Git에 버전 관리

## 경고 메시지 기능별 비교 (53개 수집)

> 📎 전체 83개 경고 메시지 수집: `docs/tech-stack/px4-ardupilot-warnings.csv` (엑셀 가능)

| 기능 영역 | PX4 경고 | ArduPilot 경고 | 주치상 | 비고 |
|-----------|----------|----------------|--------|------|
| **통신 손실** | `COM_DL_LOSS_T` (GCS 연결 손실) | `FS_GCS_ENABLE` + `FS_THR_ENABLE` | 안테나/배선 점검, 타임아웃 늘리기 | PX4는 단일 파라미터, Ardu는 Enable/Timeout 분리 |
| **GNSS 손실** | `COM_GNSSLOSS_ACT` (GNSS 손실 실패 안전) | `FS_GPS_ENABLE` + `GPS_AUTO_SWITCH` | EKF2_AID_MASK에서 비전/레이더 활성화 | 실내 비행 시 반드시 GNSS-Denied 모드 전환 필요 |
| **EKF2 상태추정** | `angular_velocity_invalid`, `global_position_invalid` | `EK3_SRC1_POSZ` (EKF3 위치 추정 실패) | EKF2 파라미터 재설정, 센서 교체 | PX4는 failsafe_flags 비트마스크, Ardu는 소스 인덱스 |
| **센서 캘리브레이션** | `EKF2_MAG_CAL` (자력계 캘리브레이션 필요) | `COMPASS_CHECK`, `BARO_CHECK`, `INS_CHECK` | 캘리브레이션 재수행, 금속/전자파 제거 | Ardu는 개별 센서별 검증, PX4는 EKF2 통합 검증 |
| **배터리 실패** | `COM_LOW_BAT_ACT` (배터리 실패 안전 모드) | `BATT_LOW_MAH`, `BATT_LOW_VOLT` | 배터리 교체, 저전 임계치 재설정 | 두 스택 모두 임계치 기반 |
| **안장 검증 실패** | `COM_ARM_WO_GPS`, `COM_ARM_IMU_ACC` | `ARMING_CHECK` (0~7 비트마스크) | 전체 캘리브레이션 재수행 | Ardu는 비트마스크로 세부 제어 가능 |
| **지오펜스 위반** | `NAV_DLL_ACT` (자동 RTL 실패) | `FENCE_ENABLE` + `FENCE_ALT_MAX` | FENCE 비활성화 또는 반경 늘리기 | PX4는 RTL 고도 우선, Ardu는 반경 기반 |
| **조종기 손실** | `COM_RC_LOSS_T` (조종기 연결 손실) | `RC_CHECK` | RC 캘리브레이션, 배터리 충전 | 두 스택 모두 조종기 신호 검증 |
| **Kill-Switch** | `COM_KILL` (0~1) | `ARMING_KILLSWITCH` | 스위치 누르기 또는 파라미터 재설정 | 인간 승인 게이트의 핵심 |
| **지형 데이터** | `PREFLIGHT_FAIL` | `PREARM_TERRAIN` (PreArm: Waiting for Terrain Data) | TERRAIN_FOLLOW 대신 RTL_ALT_TYPE 사용 | 실내 비행 시 지형 추적 비활성화 |
| **거리 센서** | `SENS_RNG_RESERVE` | `RANGEFINDER_NO_DATA` (Rangefinder 1: No Data) | RNGFND1_TYPE 설정, 케이블 점검 | 라이다/초음파 장착 시 |
| **LIDAR** | `SENS_EN_SAL` | `BAD_LIDAR` (Pre Arm Bad LIDAR) | LIDAR 캘리브레이션, 센서 교체 | 고도 유지 보조용 |
| **전원 버튼** | `POWER_BUTTON_ERR` | - | 전원 버튼 교체 또는 펌웨어 업데이트 | 하드웨어 오류 |
| **GPS 신호** | - | `GPS_SIGNAL_WEAK` (Unhealthy GPS Signal Error) | GPS 안테나 위치 변경, 장애물 제거 | 도심/실내 비행 시 |
| **배터리 건강** | - | `BATT_UNHEALTHY` (Battery 1 unhealthy warning) | 배터리 교체, 저전 임계치 재설정 | 배터리 모니터링 경고 |
| **GPS 없이 시동** | - | `ARM_PIXHawk6C_NOGPS` (Cannot arm without GPS) | ARMING_CHECK에서 GPS 검증 건너뛰기 | 실내 비행 시 |
| **LUA 스크립트** | - | `LUA_SCRIPT_ERROR` (LUA script Pre arm error) | 스크립트 문법/논리 검증 | 사용자 정의 스크립트 사용 시 |
| **프리플라이트 검증** | `PREFLIGHT_CHECK_FAIL` | `PREARM_POSITION_EST` (Prearm: Need Position Estimate) | 전체 캘리브레이션 재수행 | 시동 전 자동 검증 단계에서 실패 |
| **사전 시동 안전** | `PREARM_SAFETY_FAIL` | `CHECK_FS_THR_VALUE` (Pre Arm: Check_FS_THR_VALUE) | 스로틀 failsafe 값 재설정 | 수동 시동 전 안전 검증 단계 |
| **실패 안전 모드** | `FAILSAFE_TRIGGERED` | `RC_FAILSAFE_LOST` | 통신 링크 확인, RTL 모드 전환 | 통신 손실/센서 오류 시 자동 발동 |
| **MAVLink 명령 손실** | `CMD_LOST` (vehicle_command lost) | `ERROR_SUBSYSTEM_EKF_PRIMARY` | GCS 재연결, EKF2 파라미터 재설정 | 오프보드/자동 비행 시 |
| **로깅 실패** | - | `PREARM_LOGGING_FAIL` (PreArm: Logging not started) | SD 카드 확인/포맷 | 데이터 기록 실패 시 |
| **조종기 스틱** | - | `PREARM_RC_NEUTRAL` (PreArm: Roll is not neutral) | 스틱 중립 위치 재조정 | 시동 전 조종기 점검 시 |
| **GPS 위치 오류** | - | `BAD_GPS_POS` (Bad GPS Pos) | GPS 안테나 위치 변경 | GPS 신호 약화 시 |
| **EKF 주축 전환** | - | `EKF_PRIMARY_SWITCH` (EKF primary changed) | IMU/센서 교체 | EKF2 상태 추정 불안정 시 |
| **크래시 덤프** | - | `CRASHDUMP_DETECT` (CrashDump data detected) | 펌웨어 재플래시 | 이전 비행 중 크래시 발생 후 |

### 📌 사용 시나리오별 주치상

- **GNSS-Denied 비행 (실내/도심)**:
  - PX4: `EKF2_AID_MASK=2+8`(비전/레이더), `COM_GNSSLOSS_ACT=2`(Hold)
  - Ardu: `FS_GPS_ENABLE=0`, `EK3_SRC1_POSZ=3`(BARO)

- **진동이 심한 환경 (헬리컥터/중량 드론)**:
  - PX4: `EKF2_ACC_NOISE` 경고 → IMU_FILTER 조정, 진동 패드 설치
  - Ardu: `INS_CHECK` 실패 → IMU 캘리브레이션 재수행, 진동 완화

- **통신 장애 (장거리 비행)**:
  - PX4: `COM_DL_LOSS_T=30`(30초로 늘리기), GCS 안테나 고급화
  - Ardu: `FS_GCS_ENABLE=2`(RTL), `FS_THR_ENABLE=1`(안전 스위치)

- **배터리 부족**:
  - PX4: `COM_LOW_BAT_ACT=3`(RTL), `COM_BAT_ACT_T=30`(30초 전 알림)
  - Ardu: `BATT_LOW_MAH` 값 늘리기, 스팬톤 배터리 사용

> 💡 **핵심 원칙**: 경고 메시지는 **사전 예방**을 위한 것 → 실제 비행 전에 반드시 점검!

## 관련 페이지

- [[uav-swarm-middleware]] — MAVLink/ROS 2 토픽이 펌웨어와 상위 로직을 어떻게 잇는지
- [[uav-swarm-simulation]] — PX4/ArduPilot이 어떤 시뮬과 붙는지
- [[combat-swarm-drone-operations]] — 보안 계층(블록체인 인증)이 펌웨어 메시지와 만나는 지점