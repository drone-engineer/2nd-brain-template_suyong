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

## 관련 페이지

- [[uav-swarm-middleware]] — MAVLink/ROS 2 토픽이 펌웨어와 상위 로직을 어떻게 잇는지
- [[uav-swarm-simulation]] — PX4/ArduPilot이 어떤 시뮬과 붙는지
- [[combat-swarm-drone-operations]] — 보안 계층(블록체인 인증)이 펌웨어 메시지와 만나는 지점