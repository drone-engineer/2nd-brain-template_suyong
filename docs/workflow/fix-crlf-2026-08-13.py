#!/usr/bin/env python3
"""Fix CRLF in 2026-08-13 raw articles, recompute SHA256, update collect-results.json."""
import hashlib
import re
import json
from pathlib import Path

REPO = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"

raw_files = [
    "raw/articles/2026-08-13-ros2-drone-github-data.md",
    "raw/articles/2026-08-13-px4-release-notes.md",
    "raw/articles/2026-08-13-ardupilot-release-notes.md",
    "raw/articles/2026-08-13-px4-docs.md",
    "raw/articles/2026-08-13-ros2-docs.md",
]

SHA_RE = re.compile(rb'(?m)^sha256:\s*"([0-9a-fA-F]{64})"')

for rel in raw_files:
    path = Path(REPO) / rel
    raw = path.read_bytes()
    fm_end = raw.find(b'\n---\n', 4)
    if fm_end < 0:
        print(f"ERROR: {rel}: no frontmatter close")
        continue
    fm = raw[:fm_end]
    body = raw[fm_end+5:]

    crlf_count = body.count(b'\r\n')
    if crlf_count == 0:
        print(f"  OK (no CRLF): {rel}")
        continue

    body_fixed = body.replace(b'\r\n', b'\n')
    new_sha = hashlib.sha256(body_fixed).hexdigest()
    old_sha = hashlib.sha256(body).hexdigest()
    fm_fixed = SHA_RE.sub(b'sha256: "' + new_sha.encode() + b'"', fm)
    new_content = fm_fixed + b'\n---\n' + body_fixed
    path.write_bytes(new_content)
    print(f"  FIXED ({crlf_count} CRLF→LF): {rel} | old={old_sha[:16]}… new={new_sha[:16]}…")

# Update collect-results.json
results_path = Path(REPO) / "docs/workflow/2026-08-13-collect-results.json"
orig = json.loads(results_path.read_text())
results = {}
for rel in raw_files:
    fname = Path(rel).name
    path = Path(REPO) / rel
    raw = path.read_bytes()
    fm_end = raw.find(b'\n---\n', 4)
    fm = raw[:fm_end]
    body = raw[fm_end+5:]
    m = re.search(rb'(?m)^sha256:\s*"([0-9a-fA-F]{64})"', fm)
    if m:
        sha = m.group(1).decode()
    else:
        m2 = re.search(rb'(?m)^sha256:\s*([0-9a-fA-F]{64})', fm)
        sha = m2.group(1).decode() if m2 else ""
    url = orig.get(fname, {}).get("url", "")
    results[fname] = {"sha256": sha, "url": url}

results_path.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"\nUpdated collect-results.json")

# Verify
print("\n=== Verification ===")
for rel in raw_files:
    path = Path(REPO) / rel
    raw = path.read_bytes()
    fm_end = raw.find(b'\n---\n', 4)
    fm = raw[:fm_end]
    body = raw[fm_end+5:]
    crlf = body.count(b'\r\n')
    m = re.search(rb'(?m)^sha256:\s*"([0-9a-fA-F]{64})"', fm)
    if m:
        recorded = m.group(1).decode()
    else:
        m = re.search(rb'(?m)^sha256:\s*([0-9a-fA-F]{64})', fm)
        recorded = m.group(1).decode() if m else "NOT FOUND"
    actual = hashlib.sha256(body).hexdigest()
    match = recorded == actual
    print(f"  {rel}: CRLF={crlf}, sha256_match={match} {actual[:16]}…")
