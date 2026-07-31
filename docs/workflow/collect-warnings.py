#!/usr/bin/env python3
"""
collect-warnings.py — PX4/ArduPilot 경고 메시지 + 주치상 수집기

수집 대상:
- PX4: GitHub PX4/PX4-Autopilot → src/modules/commander/, src/modules/ekf2/
  - failsafe_flags 구조
  - preflight check 메시지
  - MAVLink status enums
- ArduPilot: GitHub ArduPilot/ardupilot → ArduCopter/AP_Arming_Copter.cpp
  - pre_arm_checks() 메시지
  - arming_checks() 실패 메시지

출력:
- docs/tech-stack/px4-ardupilot-warnings.csv
  컬럼: system, warning_code, message, cause, remedy, scenario, source

사용법:
  python3 docs/workflow/collect-warnings.py
"""
import urllib.request, re, csv, socket, time
from pathlib import Path

socket.setdefaulttimeout(30)
WIKI = Path(__file__).resolve().parents[2]
OUT_CSV = WIKI / "docs" / "tech-stack" / "px4-ardupilot-warnings.csv"

# ============================================================
# PX4 경고 메시지 수집
# ============================================================
def fetch_px4_warnings():
    """PX4의 failsafe_flags와 preflight check 메시지 수집."""
    results = []
    
    # 1. failsafe_flags 구조에서 플래그 추출
    try:
        url = "https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/src/modules/commander/HealthAndArmingChecks/HealthAndArmingChecks.cpp"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
        
        # failsafe_flags.XXX = true 패턴 추출
        for m in re.finditer(r'failsafe_flags\.(\w+)\s*=\s*true', data):
            flag = m.group(1)
            # 의미 추정 (플래그명 기반)
            cause_map = {
                "angular_velocity_invalid": "IMU 각속도 데이터 손상",
                "attitude_invalid": "자세 데이터(roll/pitch/yaw) 오류",
                "local_altitude_invalid": "로컬 고도 측정 오류",
                "local_position_invalid": "로컬 위치 추정 실패",
                "local_velocity_invalid": "로컬 속도 추정 실패",
                "global_position_invalid": "글로벌 위치(GPS) 추정 실패",
                "auto_mission_missing": "자동 미션 없음",
                "offboard_control_signal_lost": "오프보드 제어 신호 손실",
            }
            results.append({
                "system": "PX4",
                "warning_code": flag,
                "message": f"failsafe_flags.{flag} = true",
                "cause": cause_map.get(flag, flag.replace("_", " ")),
                "remedy": "",
                "scenario": "",
                "source": "HealthAndArmingChecks.cpp"
            })
    except Exception as e:
        print(f"ERR PX4 HealthAndArmingChecks: {str(e)[:50]}")
    
    # 2. VehicleStatus.msg에서 enum 값 추출
    try:
        url = "https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/msg/VehicleStatus.msg"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
        
        # enum 추출
        for m in re.finditer(r'^\w+\s+\#\s*(.+)$', data, re.M):
            results.append({
                "system": "PX4",
                "warning_code": m.group(0).split()[0],
                "message": m.group(1).strip(),
                "cause": "",
                "remedy": "",
                "scenario": "",
                "source": "VehicleStatus.msg"
            })
    except Exception as e:
        print(f"ERR PX4 VehicleStatus.msg: {str(e)[:50]}")
    
    # 3. 수동으로 정의된 핵심 PX4 경고 메시지
    px4_manual = [
        {"code": "COM_DL_LOSS_T", "msg": "GCS 연결 손실", "cause": "텔레메트리/Datamavlink 신호 끊김", "remedy": "COM_DL_LOSS_T 값을 늘리거나, 안테나/배선 점검", "scenario": "GCS와 통신 장애 시", "src": "commander_params.yaml"},
        {"code": "COM_GNSSLOSS_ACT", "msg": "GNSS 손실 실패 안전 모드", "cause": "GPS 신호 손실/위성 수 부족", "remedy": "실내 비행 시 EKF2_AID_MASK에서 비전/레이더 활성화", "scenario": "실내/도심 비행 시 GNSS 차단", "src": "commander_params.yaml"},
        {"code": "EKF2_GPS_POS", "msg": "EKF2 GPS 위치 추정 실패", "cause": "GPS 신호 약화 또는 EKF2 innovation 초과", "remedy": "EKF2_GPS_POS_DEV 파라미터 확인, GPS 안테나 교체", "scenario": "GNSS-Denied 환경에서 위치 추정 실패", "src": "ekf2_params.yaml"},
        {"code": "EKF2_MAG_CAL", "msg": "자력계 캘리브레이션 필요", "cause": "자기장 왜곡 또는 캘리브레이션 안됨", "remedy": "MAG 캘리브레이션 재수행 (자기장 환경 확인)", "scenario": "자기장이 강하게 왜곡된 환경(금속, 전자파)", "src": "ekf2_params.yaml"},
        {"code": "EKF2_ACC_NOISE", "msg": "가속도계 노이즈 과다", "cause": "진동/충격으로 인한 센서 데이터 오염", "remedy": "진동 완화(패드/다이슈킨), IMU 필터(IMU_FILTER) 조정", "scenario": "진동이 심한 엔진/모터 장착 시", "src": "ekf2_params.yaml"},
        {"code": "EKF2_VEL_IMBAL", "msg": "속도 추정 불안정", "cause": "IMU와 GPS 속도 불일치", "remedy": "EKF2_GYRO_NOISE 및 EKF2_ACCEL_NOISE 증가, 센서 교체", "scenario": "고속 회전 또는 급가속 시", "src": "ekf2_params.yaml"},
        {"code": "NAV_DLL_ACT", "msg": "드론 자동 RTL(귀환) 실패", "cause": "RTL 시 경로 계획 실패 또는 충돌 위험", "remedy": "RTL_RETURN_ALT 늘리기, 장애물 회피 활성화", "scenario": "배터리 부족 또는 통신 손실 시 자동 귀환", "src": "navigator_params.yaml"},
    ]
    for item in px4_manual:
        results.append({
            "system": "PX4",
            "warning_code": item["code"],
            "message": item["msg"],
            "cause": item["cause"],
            "remedy": item["remedy"],
            "scenario": item["scenario"],
            "source": item["src"]
        })
    
    return results

# ============================================================
# ArduPilot 경고 메시지 수집
# ============================================================
def fetch_ardupilot_warnings():
    """ArduPilot의 Arming 검증 실패 메시지 수집."""
    results = []
    
    # AP_Arming_Copter.cpp에서 pre_arm_checks() 메시지 추출
    try:
        url = "https://raw.githubusercontent.com/ArduPilot/ardupilot/Copter-4.7.0/ArduCopter/AP_Arming_Copter.cpp"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
        
        # check_failed(display_failure, "message") 패턴 추출
        for m in re.finditer(r'check_failed\([^,]+,\s*"([^"]+)"', data):
            msg = m.group(1)
            results.append({
                "system": "ArduPilot",
                "warning_code": msg,
                "message": msg,
                "cause": "",
                "remedy": "",
                "scenario": "",
                "source": "AP_Arming_Copter.cpp"
            })
    except Exception as e:
        print(f"ERR ArduCopter AP_Arming: {str(e)[:50]}")
    
    # 수동으로 정의된 핵심 ArduPilot 경고 메시지
    ardu_manual = [
        {"code": "ARMING_CHECK", "msg": "Arming 검증 실패", "cause": "센서 캘리브레이션 누락 또는 하드웨어 오류", "remedy": "Mission Planner에서 전체 캘리브레이션 수행(Accel, Compass, Radio)", "scenario": "시동 전 센서 검증 단계에서 실패", "src": "AP_Arming.cpp"},
        {"code": "FS_GCS_ENABLE", "msg": "GCS 연결 손실 실패 안전 모드", "cause": "지상국과의 통신 끊김", "remedy": "FS_GCS_ENABLE=2(RTL) 또는 FS_GCS_ENABLE=3(Land)로 설정", "scenario": "장거리 비행 시 통신 범위를 벗어날 때", "src": "AP_Arming.cpp"},
        {"code": "FS_THR_ENABLE", "msg": "스로틀 신호 손실", "cause": "조종기 신호 손실 또는 스로틀 입력 없음", "remedy": "FS_THR_ENABLE=1 활성화, 안전 스위치 사용", "scenario": "조종기 배터리 방전 또는 신호 간섭 시", "src": "AP_Arming.cpp"},
        {"code": "FS_GPS_ENABLE", "msg": "GPS 손실 실패 안전 모드", "cause": "GPS 신호 손실 또는 위성 수 부족", "remedy": "FS_GPS_ENABLE=1, RTL_ALT 늘리기", "scenario": "실내 또는 GPS 차단 환경에서 비행 시", "src": "AP_Arming.cpp"},
        {"code": "EK3_SRC1_POSZ", "msg": "EKF3 위치 추정 실패", "cause": "GPS/바로미터/레이더 데이터 불일치", "remedy": "EK3_SRC1_POSZ=1(Altitude) 또는 EK3_SRC1_POSZ=3(BARO)로 변경", "scenario": "고도 유지 실패 시 EKF3 재설정 필요", "src": "AP_Arming.cpp"},
        {"code": "COMPASS_CHECK", "msg": "나침반 검증 실패", "cause": "자기장 왜곡 또는 캘리브레이션 안됨", "remedy": "나침반 캘리브레이션 재수행, 금속/전자파 근처 피하기", "scenario": "도시/금속 구조물 근처 비행 시", "src": "AP_Arming.cpp"},
        {"code": "BARO_CHECK", "msg": "바로미터 검증 실패", "cause": "기압 센서 오류 또는 기류 변화", "remedy": "BARO_PROBING 파라미터 조정, 센서 교체", "scenario": "날씨 변화가 심한 날씨에 비행 시", "src": "AP_Arming.cpp"},
        {"code": "GPS_CHECK", "msg": "GPS 검증 실패", "cause": "GPS 위성 수 부족 또는 신호 약화", "remedy": "GPS 안테나 위치 변경, 외부 장애물 제거", "scenario": "실내/도심/숲속 등 GPS 차단 환경", "src": "AP_Arming.cpp"},
        {"code": "INS_CHECK", "msg": "IMU 검증 실패", "cause": "가속도계/자이로 센서 불일치", "remedy": "IMU 캘리브레이션 재수행, 진동 완화", "scenario": "진동이 심한 환경에서 시동 시", "src": "AP_Arming.cpp"},
        {"code": "RC_CHECK", "msg": "조종기 검증 실패", "cause": "조종기 신호 없음 또는 채널 오류", "remedy": "RC 캘리브레이션, 배터리 충전, 안테나 점검", "scenario": "조종기 배터리 방전 시", "src": "AP_Arming.cpp"},
        {"code": "COMPASS_DEV_OPTION", "msg": "자기장 왜곡 감지", "cause": "주변 금속/전자파로 인한 자기장 변화", "remedy": "COMPASS_DEV_OPTION=0으로 설정하거나, 자기장 캘리브레이션", "scenario": "금속 구조물/전선타워 근처 비행 시", "src": "AP_Arming.cpp"},
        {"code": "FENCE_ENABLE", "msg": "지오펜스 위반", "cause": "프리셋된 비행 영역을 벗어남", "remedy": "FENCE_ENABLE=0(비활성화) 또는 FENCE_ALT_MAX 늘리기", "scenario": "지정된 비행 반경/고도를 벗어날 때", "src": "AP_Arming.cpp"},
        {"code": "RTL_ALT", "msg": "RTL 고도 설정 오류", "cause": "귀환 고도가 지면보다 낮음 또는 설정 오류", "remedy": "RTL_ALT=10000(10m) 이상으로 설정", "scenario": "자동 귀환 시 고도 유지 실패 시", "src": "AP_Arming.cpp"},
        {"code": "BATT_LOW_MAH", "msg": "배터리 잔량 부족", "cause": "배터리 방전 또는 소비량 과다", "remedy": "BATT_LOW_MAH 값을 늘리거나 배터리 교체", "scenario": "장시간 비행 후 배터리 저하 시", "src": "AP_Arming.cpp"},
        {"code": "SERIAL1_PROTOCOL", "msg": "직렬 통신 프로토콜 오류", "cause": "MAVLink/UART 설정 불일치", "remedy": "SERIAL1_PROTOCOL=2(MAVLink2)로 설정", "scenario": "지상국/컴패니언 컴퓨터와 통신 설정 시", "src": "AP_Arming.cpp"},
        {"code": "BRD_SAFETY", "msg": "안전 스위치 활성화됨", "cause": "안전 스위치가 켜져 있어 시동 불가", "remedy": "BRD_SAFETY=0(비활성화) 또는 스위치 누르기", "scenario": "안전 스위치를 통한 인간 승인 게이트", "src": "AP_Arming.cpp"},
    ]
    for item in ardu_manual:
        results.append({
            "system": "ArduPilot",
            "warning_code": item["code"],
            "message": item["msg"],
            "cause": item["cause"],
            "remedy": item["remedy"],
            "scenario": item["scenario"],
            "source": item["src"]
        })
    
    return results

def main():
    print("Collecting PX4 warnings...")
    px4 = fetch_px4_warnings()
    print(f"  Found {len(px4)} PX4 warnings")

    print("Collecting ArduPilot warnings...")
    ardu = fetch_ardupilot_warnings()
    print(f"  Found {len(ardu)} ArduPilot warnings")

    all_warnings = px4 + ardu
    print(f"Total: {len(all_warnings)} warnings")

    # CSV 저장
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["system", "warning_code", "message", "cause", "remedy", "scenario", "source"])
        writer.writeheader()
        writer.writerows(all_warnings)
    print(f"Saved to {OUT_CSV}")

if __name__ == "__main__":
    main()
