#!/usr/bin/env python3
"""List all 45 GitHub items for 2026-08-11."""
import json
from pathlib import Path
raw = Path('raw/articles/2026-08-11-ros2-drone-github-data.md').read_bytes()
end = raw.find(b'\n---\n', 4)
body = raw[end+5:].decode('utf-8', 'replace')
gh = json.loads(body)
print(f'Total items: {gh["total_items"]}')
print(f'Queries: {gh["queries"]}')
print()
items = sorted(gh['items'], key=lambda x: x.get('stargazers_count', 0), reverse=True)
for i, it in enumerate(items):
    print(f'{i+1:2d}. ⭐{it.get("stargazers_count",0):>5} | {it["full_name"]} | {it.get("language","N/A")} | pushed={it.get("pushed_at","N/A")[:10]} | query={it.get("_source_query","")}')
    desc = it.get("description","(none)")
    if desc:
        print(f'   desc: {desc[:120]}')
    print(f'   topics: {it.get("topics",[])}')
    print()
