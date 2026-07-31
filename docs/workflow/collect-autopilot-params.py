#!/usr/bin/env python3
"""
collect-autopilot-params.py — PX4/ArduPilot 파라미터 수집기

수집 대상:
- PX4: GitHub PX4/PX4-Autopilot → src/modules/*/params.yaml (핵심 23개)
- ArduPilot: GitHub ArduPilot/ardupilot → ArduCopter/ArduPlane/Parameters.cpp

출력:
- docs/tech-stack/px4-ardupilot-parameters.csv
  컬럼: system, param_name, description, usage_scenario, setting_range, source

사용법:
  python3 docs/workflow/collect-autopilot-params.py
"""
import urllib.request, json, re, csv, os, hashlib, socket, time
from pathlib import Path

socket.setdefaulttimeout(30)
WIKI = Path(__file__).resolve().parents[2]
OUT_CSV = WIKI / "docs" / "tech-stack" / "px4-ardupilot-parameters.csv"

# --- PX4 파라미터 수집 ---
PX4_PARAM_FILES = [
    "src/modules/commander/commander_params.yaml",
    "src/modules/ekf2/ekf2_params.yaml",
    "src/modules/mc_att_control/mc_att_control_params.yaml",
    "src/modules/mc_pos_control/multicopter_position_control_params.yaml",
    "src/modules/navigator/navigator_params.yaml",
    "src/modules/navigator/mission_params.yaml",
    "src/modules/navigator/rtl_params.yaml",
]

def fetch_px4_params():
    base = "https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/"
    results = []
    for pf in PX4_PARAM_FILES:
        try:
            req = urllib.request.Request(base + pf, headers={"User-Agent": "Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
            # YAML params: "PARAM_NAME:" 형식 (nested under definitions:)
            # Pattern: PARAM_NAME: followed by description block
            for m in re.finditer(r'^    ([A-Z][A-Z0-9_]{3,40}):\s*\n(?:      description:\n        short:\s*([^\n]+)\n)?(?:        long:\s*([^\n]+))?', data, re.M):
                name = m.group(1)
                short_desc = m.group(2) or ""
                long_desc = m.group(3) or ""
                desc = f"{short_desc} {long_desc}".strip()
                # Setting range 추출
                min_m = re.search(rf'    {re.escape(name)}:.*?min:\s*([^\n]+)', data, re.S)
                max_m = re.search(rf'    {re.escape(name)}:.*?max:\s*([^\n]+)', data, re.S)
                setting_range = f"min={min_m.group(1).strip()}, max={max_m.group(1).strip()}" if min_m and max_m else ""
                results.append({
                    "system": "PX4",
                    "param_name": name,
                    "description": desc,
                    "usage_scenario": "",  # 추후 보강
                    "setting_range": setting_range,
                    "source": pf
                })
            time.sleep(2)
        except Exception as e:
            print(f"ERR PX4 {pf}: {str(e)[:50]}")
    return results

# --- ArduPilot 파라미터 수집 ---
def fetch_ardupilot_params():
    """ArduPilot 파라미터는 .param 파일에서 추출."""
    base = "https://raw.githubusercontent.com/ArduPilot/ardupilot/Copter-4.7.0/"
    results = []
    # 기본 파라미터 파일 다운로드
    param_files = [
        "Tools/Frame_params/3DR_Iris+.param",
        "ArduCopter/Parameters.cpp",
        "libraries/AP_Param/AP_Param.h",
    ]
    for pf in param_files:
        try:
            req = urllib.request.Request(base + pf, headers={"User-Agent": "Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
            # .param 파일: PARAM_NAME,VALUE,TYPE,DESCRIPTION
            if pf.endswith(".param"):
                for line in data.split("\n"):
                    m = re.match(r'^([A-Z][A-Z0-9_]{3,40}),', line)
                    if m:
                        name = m.group(1)
                        # 설명 추출 (일반적으로 줄 끝에 주석)
                        desc = line.split(",")[-1].strip() if "," in line else ""
                        results.append({
                            "system": "ArduPilot",
                            "param_name": name,
                            "description": desc,
                            "usage_scenario": "",
                            "setting_range": "",
                            "source": pf
                        })
            # C++ 소스: AP_Param<> 정의 추출
            elif pf.endswith(".cpp"):
                for m in re.finditer(r'AP_Param<\w+>\s+\w+\s*\(\s*"([A-Z][A-Z0-9_]+)"\s*,\s*"([^"]+)"', data):
                    results.append({
                        "system": "ArduPilot",
                        "param_name": m.group(1),
                        "description": m.group(2),
                        "usage_scenario": "",
                        "setting_range": "",
                        "source": pf
                    })
        except Exception as e:
            print(f"ERR ArduPilot {pf}: {str(e)[:50]}")
    return results

def main():
    print("Collecting PX4 params...")
    px4 = fetch_px4_params()
    print(f"  Found {len(px4)} PX4 params")

    print("Collecting ArduPilot params...")
    ardu = fetch_ardupilot_params()
    print(f"  Found {len(ardu)} ArduPilot params")

    all_params = px4 + ardu
    print(f"Total: {len(all_params)} params")

    # CSV 저장
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["system", "param_name", "description", "usage_scenario", "setting_range", "source"])
        writer.writeheader()
        writer.writerows(all_params)
    print(f"Saved to {OUT_CSV}")

if __name__ == "__main__":
    main()
