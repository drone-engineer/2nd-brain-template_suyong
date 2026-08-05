#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gate B 검증 (2026-08-04 신규 raw 수집 파일)
- UTF-8, LF-only, no BOM, final newline
- frontmatter sha256 재계산 검증 (post-frontmatter body bytes)
- canonical 카운트/index 정합 (보고서 커밋 전 canonical 검증)
"""
import hashlib
import os
import re

REPO = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"
RAW_DIR = os.path.join(REPO, "raw/articles")
TODAY = "2026-08-04"

FILES = [
    f"raw/articles/{TODAY}-ros2-drone-github-data.md",
    f"raw/articles/{TODAY}-px4-release-notes.md",
    f"raw/articles/{TODAY}-ardupilot-release-notes.md",
    f"raw/articles/{TODAY}-px4-docs-main.md",
    f"raw/articles/{TODAY}-ros2-docs-rolling.md",
]

def check_raw(relpath):
    path = os.path.join(REPO, relpath)
    if not os.path.exists(path):
        print(f"  [FAIL] {relpath}: 파일 없음")
        return False
    with open(path, "rb") as f:
        data = f.read()
    ok = True
    # BOM 검사
    if data.startswith(b"\xef\xbb\xbf"):
        print(f"  [FAIL] {relpath}: BOM 존재"); ok = False
    # LF-only 검사 (CRLF 금지)
    if b"\r\n" in data:
        print(f"  [WARN] {relpath}: CRLF 발견 (raw body 보존 정책 참고)"); # raw body immutable이므로 경고만. 새 파일이라면 문제.
        ok = False
    # final newline
    if not data.endswith(b"\n"):
        print(f"  [FAIL] {relpath}: final newline 없음"); ok = False
    # frontmatter at byte 0
    if not data.startswith(b"---\n"):
        print(f"  [FAIL] {relpath}: frontmatter가 byte 0에 없음"); ok = False
        return False
    # frontmatter 파싱
    rest = data[len(b"---\n"):]
    fm_end = rest.find(b"\n---\n")
    if fm_end == -1:
        print(f"  [FAIL] {relpath}: closing frontmatter 없음"); ok = False
        return False
    fm_text = rest[:fm_end].decode("utf-8")
    body = rest[fm_end + len(b"\n---\n"):]
    fm = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    recorded = fm.get("sha256", "")
    actual = hashlib.sha256(body).hexdigest()
    if recorded != actual:
        print(f"  [FAIL] {relpath}: sha256 mismatch (recorded={recorded[:16]}... actual={actual[:16]}...)"); ok = False
    else:
        has_lf = b"\n" in body
        print(f"  [OK]   {relpath}: sha256 match={actual[:16]}...  body={len(body)}B  has_lf={has_lf}  source_url={fm.get('source_url','')[:40]}  fetched={fm.get('fetched','')}")
    return ok

print("=" * 60)
print("Gate B — raw 수집 파일 검증")
print("=" * 60)
all_ok = True
for rel in FILES:
    if not check_raw(rel):
        all_ok = False

# canonical 카운트/인덱스 정합 (보고서 작성 전 상태 — canonical 추가 없음)
print("\n" + "=" * 60)
print("Gate B — canonical 카운트/인덱스 정합 검증")
print("=" * 60)
# index.md canonical 수 세기
index_path = os.path.join(REPO, "index.md")
with open(index_path, "r", encoding="utf-8") as f:
    idx = f.read()
# "Total pages:" 카운트
import re
m = re.search(r"Total pages:\s*(\d+)", idx)
index_count = int(m.group(1)) if m else -1
# 실제 canonical 파일 수 (entities/concepts/comparisons/queries, active)
canon_dirs = ["entities", "concepts", "comparisons", "queries"]
fs_count = 0
for d in canon_dirs:
    dp = os.path.join(REPO, d)
    if os.path.isdir(dp):
        for fn in os.listdir(dp):
            if fn.endswith(".md") and os.path.isfile(os.path.join(dp, fn)) and not fn.startswith("."):
                fs_count += 1
print(f"  index.md 'Total pages': {index_count}")
print(f"  실제 canonical 파일 수 (active): {fs_count}")
if index_count == fs_count:
    print(f"  [OK]   canonical 카운트 정합 (index={index_count} == filesystem={fs_count})")
else:
    print(f"  [FAIL] canonical 카운트 불일치 (index={index_count} != filesystem={fs_count})")
    all_ok = False

print("\n" + "=" * 60)
if all_ok:
    print("Gate B: PASS — 모든 raw sha256 검증 및 canonical 정합 확인")
else:
    print("Gate B: FAIL — 문제 항목 있음 (log.md에 기록)")
print("=" * 60)
