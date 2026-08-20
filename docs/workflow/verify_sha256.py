#!/usr/bin/env python3
"""Verify SHA256 checksums of collected raw articles (Gate B validation)."""
import re, hashlib, os, json

REPO = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"
RAW_DIR = os.path.join(REPO, "raw", "articles")

date = "2026-08-21"
files = [
    f"{date}-ros2-drone-github-data.md",
    f"{date}-px4-release-notes.md",
    f"{date}-ardupilot-release-notes.md",
    f"{date}-px4-docs.md",
    f"{date}-ros2-docs.md",
]

results = []
for fname in files:
    fpath = os.path.join(RAW_DIR, fname)
    if not os.path.exists(fpath):
        print(f"  {fname}: FILE NOT FOUND")
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
            status = "✅ PASS" if match else "❌ FAIL"
            print(f"  {fname}: {status} (declared={declared[:24]}..., actual={actual[:24]}..., ends_nl={ends_nl}, body_len={len(body)})")
            results.append({"file": fname, "sha256": declared, "match": match, "ends_nl": ends_nl, "body_len": len(body)})
    else:
        print(f"  {fname}: FRONTMATTER PARSE FAILED")
        results.append({"file": fname, "match": False, "error": "frontmatter parse failed"})

# Save verification results for report use
with open(os.path.join(REPO, "docs", "workflow", f"{date}-sha256-verification.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print(f"\nSaved: docs/workflow/{date}-sha256-verification.json")
