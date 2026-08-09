#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROS2 기반 드론 최신 기술 일일 수집 (2026-08-10)
- GitHub Search API (9 쿼리, per_page=5, sort=stars)
- PX4 / ArduPilot 릴리즈 노트 (GitHub Releases API)
- PX4 공식 문서 (docs.px4.io)
- ROS2 공식 문서 (docs.ros.org)

각 raw/articles/2026-08-10-*.md 파일에 frontmatter + sha256(body) 기록.
수집 후 docs/workflow/2026-08-10-ros2-drone-report.md 보고서 자동 생성.
"""
import json
import hashlib
import re
import urllib.request
import urllib.parse
import ssl
from datetime import datetime, timezone

TODAY = "2026-08-10"
NOW_ISO = f"{TODAY}T08:30:00Z"
RAW_DIR = "raw/articles"
REPO = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0 Safari/537.36 HermesAgent/1.0"
CTX = ssl.create_default_context()

QUERIES = [
    ("ros2 drone detection", "ROS2 드론 객체 검출"),
    ("ros2 drone autonomous", "ROS2 드론 자율 비행"),
    ("ros2 drone navigation", "ROS2 드론 내비게이션"),
    ("PX4 ros2 bridge", "PX4 ROS2 브리지"),
    ("YOLO ros2 drone", "YOLO ROS2 드론"),
    ("zenoh ros2 middleware", "Zenoh ROS2 미들웨어"),
    ("MediaPipe ros2", "MediaPipe ROS2"),
    ("SLAM ros2 drone", "SLAM ROS2 드론"),
    ("ArUco ros2 detection", "ArUco ROS2 검출"),
]


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def fetch_html(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"})
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return r.read().decode("utf-8", "replace")


def strip_html(html):
    """HTML에서 의미 있는 텍스트만 추출 (스크립트/스타일/noscript 제거)."""
    html = re.sub(r"<script.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<noscript.*?</noscript>", "", html, flags=re.DOTALL | re.IGNORECASE)
    # 링크 텍스트 보존 — href 속성의 이스케이프된 따옴표 처리
    html = re.sub(r'<a[^>]*href=\\"([^\\"]+)\\"[^>]*>', r' [링크: \1] ', html)
    html = re.sub(r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>', r' [링크: \1] ', html)
    html = re.sub(r"<[^>]+>", " ", html)
    text = urllib.parse.unquote(html)
    return re.sub(r"\s+", " ", text).strip()


def save_article(filename, body, url):
    """Article 저장: frontmatter(sha256 포함) + body. SCHEMA-compliant."""
    sha256 = hashlib.sha256(body.encode("utf-8")).hexdigest()
    frontmatter = f"""---
title: (no title)
created: {TODAY}
updated: {TODAY}
type: article
tags:
  - drone
  - swarm
  - ros2
sources:
  - {url}
fetched: {NOW_ISO}
sha256: {sha256}
---
"""
    content = frontmatter + body
    path = f"{RAW_DIR}/{filename}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return sha256


def main():
    print(f"=== ROS2 드론 기술 수집 ({TODAY}) ===")

    results = {}
    all_github_items = []

    # 1. GitHub Search API (9 queries)
    print("\n[1] GitHub Search API - ROS2 drone projects...")
    for i, (query, desc) in enumerate(QUERIES):
        try:
            api_url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(query)}&sort=stars&order=desc&per_page=5"
            result = fetch_json(api_url)
            body = json.dumps(result, indent=2, ensure_ascii=False)
            filename = f"{TODAY}-github-search-ros2-drone-{i+1}.md"
            sha256 = save_article(filename, body, api_url)
            print(f"  ✓ {filename} (sha256: {sha256[:16]}…)")
            results[filename] = {"sha256": sha256, "url": api_url, "data": result, "desc": desc}
            # Collect items for the consolidated github-data file
            if isinstance(result, dict) and "items" in result:
                for item in result["items"]:
                    item["_source_query"] = query
                    item["_source_desc"] = desc
                    all_github_items.append(item)
        except Exception as e:
            print(f"  ✗ GitHub Search 쿼리 실패 {query}: {e}")

    # Save consolidated github-data file
    if all_github_items:
        consolidated = {
            "total_query_results": len(QUERIES),
            "total_items": len(all_github_items),
            "queries": [q[0] for q in QUERIES],
            "items": all_github_items,
        }
        body = json.dumps(consolidated, indent=2, ensure_ascii=False)
        filename = f"{TODAY}-ros2-drone-github-data.md"
        sha256 = save_article(filename, body, "GitHub Search API (9 queries)")
        print(f"  ✓ {filename} (sha256: {sha256[:16]}…) — {len(all_github_items)} total items")
        results[filename] = {"sha256": sha256, "data": consolidated}

    # 2. PX4 Releases
    print("\n[2] PX4-Autopilot 최신 릴리즈...")
    try:
        api_url = "https://api.github.com/repos/PX4/PX4-Autopilot/releases"
        result = fetch_json(api_url)
        body = json.dumps(result[:6], indent=2, ensure_ascii=False)
        filename = f"{TODAY}-px4-release-notes.md"
        sha256 = save_article(filename, body, api_url)
        print(f"  ✓ {filename} (sha256: {sha256[:16]}…)")
        results[filename] = {"sha256": sha256, "data": result[:6]}
    except Exception as e:
        print(f"  ✗ PX4 Releases API 오류: {e}")

    # 3. ArduPilot Releases
    print("\n[3] ArduPilot 최신 릴리즈...")
    try:
        api_url = "https://api.github.com/repos/ArduPilot/ardupilot/releases"
        result = fetch_json(api_url)
        body = json.dumps(result[:7], indent=2, ensure_ascii=False)
        filename = f"{TODAY}-ardupilot-release-notes.md"
        sha256 = save_article(filename, body, api_url)
        print(f"  ✓ {filename} (sha256: {sha256[:16]}…)")
        results[filename] = {"sha256": sha256, "data": result[:7]}
    except Exception as e:
        print(f"  ✗ ArduPilot Releases API 오류: {e}")

    # 4. PX4 Main Docs
    print("\n[4] PX4 공식 문서...")
    try:
        docs_url = "https://docs.px4.io/main/en/"
        html = fetch_html(docs_url)
        body = strip_html(html)
        filename = f"{TODAY}-px4-docs-main.md"
        sha256 = save_article(filename, body, docs_url)
        print(f"  ✓ {filename} (sha256: {sha256[:16]}…)")
        results[filename] = {"sha256": sha256, "body": body, "url": docs_url}
    except Exception as e:
        print(f"  ✗ PX4 Docs 오류: {e}")

    # 5. ROS2 Rolling Docs
    print("\n[5] ROS2 공식 문서...")
    try:
        docs_url = "https://docs.ros.org/en/rolling/"
        html = fetch_html(docs_url)
        body = strip_html(html)
        filename = f"{TODAY}-ros2-docs-rolling.md"
        sha256 = save_article(filename, body, docs_url)
        print(f"  ✓ {filename} (sha256: {sha256[:16]}…)")
        results[filename] = {"sha256": sha256, "body": body, "url": docs_url}
    except Exception as e:
        print(f"  ✗ ROS2 Docs 오류: {e}")

    print("\n=== 수집 완료 ===")

    # Save results metadata for report generation
    with open(f"{REPO}/docs/workflow/2026-08-10-collect-results.json", "w", encoding="utf-8") as f:
        json.dump({k: {"sha256": v.get("sha256"), "url": v.get("url")} for k, v in results.items()}, f, indent=2, ensure_ascii=False)
    print(f"결과 메타데이터: docs/workflow/2026-08-10-collect-results.json")

    return results


if __name__ == "__main__":
    main()
