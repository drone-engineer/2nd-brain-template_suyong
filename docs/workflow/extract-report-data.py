#!/usr/bin/env python3
"""Extract key data from 2026-08-10 raw articles for report generation."""
import json
from pathlib import Path

REPO = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"

def read_body(path):
    raw = Path(path).read_bytes()
    end = raw.find(b'\n---\n', 4)
    body = raw[end+5:].decode('utf-8', 'replace')
    return body

def read_frontmatter(path):
    raw = Path(path).read_bytes()
    end = raw.find(b'\n---\n', 4)
    fm_raw = raw[4:end].decode('utf-8', 'replace')
    return fm_raw

# 1. GitHub Data
gh = json.loads(read_body(f'{REPO}/raw/articles/2026-08-10-ros2-drone-github-data.md'))
print(f'=== GitHub Search Results ===')
print(f'Total items: {gh["total_items"]}')
items_sorted = sorted(gh['items'], key=lambda x: x.get('stargazers_count', 0), reverse=True)
for it in items_sorted[:12]:
    print(f'  STAR:{it["stargazers_count"]:>5} | {it["full_name"]} | lang={it.get("language","N/A")} | pushed={it.get("pushed_at","N/A")[:10]}')
    print(f'  desc: {it.get("description","(none)")[:140]}')
    print(f'  topics: {it.get("topics",[])}')
    print(f'  query: {it.get("_source_query","")}')
    print()

# 2. PX4 Release Notes
px4_releases = json.loads(read_body(f'{REPO}/raw/articles/2026-08-10-px4-release-notes.md'))
print(f'\n=== PX4 Releases (top 6) ===')
for r in px4_releases[:6]:
    print(f'  {r.get("tag_name","?")} | prerelease={r.get("prerelease",False)} | draft={r.get("draft",False)} | date={r.get("published_at","N/A")[:10]}')
    print(f'  name: {r.get("name","")}')
    print(f'  body: {r.get("body","(no body)")[:200]}')
    print()

# 3. ArduPilot Release Notes
ap_releases = json.loads(read_body(f'{REPO}/raw/articles/2026-08-10-ardupilot-release-notes.md'))
print(f'\n=== ArduPilot Releases (top 7) ===')
for r in ap_releases[:7]:
    print(f'  {r.get("tag_name","?")} | prerelease={r.get("prerelease",False)} | draft={r.get("draft",False)} | date={r.get("published_at","N/A")[:10]}')
    print(f'  name: {r.get("name","")}')
    print(f'  body: {r.get("body","(no body)")[:200]}')
    print()

# 4. PX4 Docs
px4_docs = read_body(f'{REPO}/raw/articles/2026-08-10-px4-docs-main.md')
print(f'\n=== PX4 Docs (first 500 chars) ===')
print(px4_docs[:500])

# 5. ROS2 Docs
ros2_docs = read_body(f'{REPO}/raw/articles/2026-08-10-ros2-docs-rolling.md')
print(f'\n=== ROS2 Docs (first 500 chars) ===')
print(ros2_docs[:500])
