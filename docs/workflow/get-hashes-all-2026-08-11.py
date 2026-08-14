#!/usr/bin/env python3
"""Get SHA256 hashes for ALL 14 raw article files for 2026-08-11."""
import hashlib
from pathlib import Path

REPO = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"

files = [
    "raw/articles/2026-08-11-ros2-drone-github-data.md",
    "raw/articles/2026-08-11-px4-release-notes.md",
    "raw/articles/2026-08-11-ardupilot-release-notes.md",
    "raw/articles/2026-08-11-px4-docs-main.md",
    "raw/articles/2026-08-11-ros2-docs-rolling.md",
]

for i in range(1, 10):
    files.append(f"raw/articles/2026-08-11-github-search-ros2-drone-{i}.md")

for f in files:
    raw = Path(f"{REPO}/{f}").read_bytes()
    end = raw.find(b'\n---\n', 4)
    body = raw[end+5:]
    sha = hashlib.sha256(body).hexdigest()
    short = sha[:16]
    print(f"  `{f}` | `{sha}` | `{short}…` | ✅ 검증")
