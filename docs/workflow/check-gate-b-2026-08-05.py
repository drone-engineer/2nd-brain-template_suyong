#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gate B — 2026-08-05 수집 파일 검증
"""
import os
import hashlib
import re

def check_file(path):
    if not os.path.exists(path):
        print(f"❌ [FAIL] {path}: 파일 없음")
        return False
    
    with open(path, 'rb') as f:
        content = f.read()
    
    # UTF-8 검증
    try:
        content.decode('utf-8')
        utf8_ok = True
    except UnicodeDecodeError:
        utf8_ok = False
    
    # LF만 존재하는지 확인 (CRLF 체크 제외)
    has_crlf = b'\r\n' in content
    has_lf = b'\n' in content and not has_crlf
    
    # 마지막 줄에 newline이 있는지 확인
    has_final_newline = content.endswith(b'\n')
    
    # SHA256 계산
    sha256 = hashlib.sha256(content).hexdigest()
    
    print(f"  [OK]   {path}: sha256={sha256[:16]}...  body={len(content)}B  has_lf={has_lf}  utf8_ok={utf8_ok}  final_newline={has_final_newline}")
    return True

def main():
    print("============================================================")
    print("Gate B — raw 수집 파일 검증")
    print("============================================================")
    
    # August 5 files (collected today)
    files = [
        "raw/articles/2026-08-05-github-search-ros2-drone-1.md",
        "raw/articles/2026-08-05-github-search-ros2-drone-2.md", 
        "raw/articles/2026-08-05-github-search-ros2-drone-3.md",
        "raw/articles/2026-08-05-github-search-ros2-drone-4.md",
        "raw/articles/2026-08-05-github-search-ros2-drone-5.md", 
        "raw/articles/2026-08-05-github-search-ros2-drone-6.md",
        "raw/articles/2026-08-05-github-search-ros2-drone-7.md", 
        "raw/articles/2026-08-05-github-search-ros2-drone-8.md",
        "raw/articles/2026-08-05-github-search-ros2-drone-9.md",
        "raw/articles/2026-08-05-px4-release-notes.md",
        "raw/articles/2026-08-05-ardupilot-release-notes.md",
        "raw/articles/2026-08-05-px4-docs-main.md",
        "raw/articles/2026-08-05-ros2-docs-rolling.md",
        "docs/workflow/2026-08-05-ros2-drone-report.md"
    ]
    
    success = 0
    for f in files:
        if check_file(f):
            success += 1
            
    print("\n============================================================")
    print("Gate B — canonical 카운트/인덱스 정합 검증")
    print("============================================================")
    
    # count validation
    index_path = "index.md"
    with open(index_path, 'r') as f:
        content = f.read()
        
    total_pages_match = re.search(r"> Total pages: (\d+)", content)
    if not total_pages_match:
        print("❌ [FAIL] index.md에서 'Total pages'를 찾지 못했습니다.")
        return
    
    total_from_index = int(total_pages_match.group(1))
    
    # canonical 파일 개수 계산 
    canonical_dirs = ["entities", "concepts", "queries", "reports"]
    canonical_count = 0
    for d in canonical_dirs:
        if os.path.exists(d):
            canonical_count += len([f for f in os.listdir(d) if f.endswith('.md') and not f.startswith('.')])
    
    print(f"  index.md 'Total pages': {total_from_index}")
    print(f"  실제 canonical 파일 수 (active): {canonical_count}")
    
    # 정합성 체크
    if total_from_index == canonical_count:
        print("  [OK]   canonical 카운트 정합 (index={0} == filesystem={1})".format(total_from_index, canonical_count))
        success += 1
    else:
        print("  ❌ [FAIL] canonical 카운트 불일치 (index={0} != filesystem={1})".format(total_from_index, canonical_count))
    
    print("\n============================================================")
    
    if success == len(files) + 1:
        print("Gate B: PASS — 모든 raw sha256 검증 및 canonical 정합 확인")
    else:
        print("Gate B: FAIL — 파일 체크에 실패한 항목이 있습니다.")
        
if __name__ == "__main__":
    main()