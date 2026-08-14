#!/usr/bin/env python3
"""Extract key sections from PX4 docs body for report."""
from pathlib import Path
raw = Path('raw/articles/2026-08-11-px4-docs-main.md').read_bytes()
end = raw.find(b'\n---\n', 4)
body = raw[end+5:].decode('utf-8', 'replace')
for pattern in ['Position Mode', 'Altitude Cruise', 'Offboard', 'VTOL', 'Fixed Wing', 'EKF2', 'ROS 2', 'MAVSDK', 'Gazebo', 'Autopilot']:
    idx = body.find(pattern)
    if idx > 0:
        start = max(0, idx - 50)
        end_idx = min(len(body), idx + 200)
        print(f'[{pattern}]: ...{body[start:end_idx].strip()}...')
        print()
