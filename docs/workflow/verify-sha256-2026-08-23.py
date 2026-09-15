#!/usr/bin/env python3
"""Verify SHA256 checksums of collected raw articles for 2026-08-23 (Gate B validation)."""
import re, hashlib, os, json

REPO = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"
RAW_DIR = os.path.join(REPO, "raw", "articles")
date = "2026-08-23"
files = [
    f"{date}-ros2-drone-github-data.md",
    f"{date}-px4-release-notes.md",
    f"{date}-ardupilot-release-notes.md",
    f"{date}-px4-docs.md",
    f"{date}-ros2-docs.md",
]

results = []
all_pass = True
for fname in files:
    fpath = os.path.join(RAW_DIR, fname)
    if not os.path.exists(fpath):
        print(f"  {fname}: FILE NOT FOUND")
        results.append({"file": fname, "match": False, "error": "not found"})
        all_pass = False
        continue
    with open(fpath, "r", encoding="utf-8") as fh:
        content = fh.read()
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        body = fm_match.group(2)
        sha_match = re.search(r'sha256:\s*([a-f0-9]{64})', fm)
        if sha_match:
            declared = sha_match.group(1)
            actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
            ends_nl = body.endswith('\n')
            match = declared == actual
            status = "PASS" if match else "FAIL"
            if not match:
                all_pass = False
            print(f"  {fname}: {status} (declared={declared[:24]}..., actual={actual[:24]}..., ends_nl={ends_nl}, body_len={len(body)})")
            results.append({"file": fname, "sha256": declared, "match": match, "ends_nl": ends_nl, "body_len": len(body)})
        else:
            print(f"  {fname}: no sha256 in frontmatter")
            results.append({"file": fname, "match": False, "error": "no sha256 field"})
            all_pass = False
    else:
        print(f"  {fname}: FRONTMATTER PARSE FAILED")
        results.append({"file": fname, "match": False, "error": "frontmatter parse failed"})
        all_pass = False

with open(os.path.join(REPO, "docs", "workflow", f"{date}-sha256-verification.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\nGate B: {'ALL PASS' if all_pass else 'FAILURES DETECTED'}")
print(f"Verification saved: docs/workflow/{date}-sha256-verification.json")

# Exit code for script chaining
import sys
sys.exit(0 if all_pass else 1)
