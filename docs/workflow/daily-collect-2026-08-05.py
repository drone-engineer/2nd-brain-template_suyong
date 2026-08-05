#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROS2 기반 드론 최신 기술 일일 수집 (2026-08-05)
- GitHub Search API (9 쿼리)
- PX4 / ArduPilot 릴리즈 노트 (GitHub Releases API)
- PX4 공식 문서 (docs.px4.io main + releases + ros2)
- ROS2 공식 문서 (docs.ros.org rolling)
각 raw/articles/YYYY-MM-DD-*.md 파일에 frontmatter + sha256(body) 저장.
"""
import json
import hashlib
import re
import urllib.request
import urllib.parse
import urllib.error
import ssl
from datetime import datetime, timezone

TODAY = "2026-08-05"
NOW_ISO = f"{TODAY}T08:30:00Z"
RAW_DIR = "raw/articles"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0 Safari/537.36 HermesAgent/1.0"
CTX = ssl.create_default_context()

REPO = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def fetch_html(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return r.read().decode("utf-8", "replace")


def strip_html(html):
    """HTML에서 의미 있는 텍스트만 추출 (스크립트/스타일 제거)."""
    html = re.sub(r"<script.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<noscript.*?</noscript>", "", html, flags=re.DOTALL | re.IGNORECASE)
    # 링크 텍스트 보존
    html = re.sub(r"<a[^>]*href=\"([^\\\"]+)\"[^>]*>", r"<a href=\"\1\">", html)
    html = re.sub(r"<[^>]+>", " ", html)
    text = urllib.parse.unquote(html)
    return re.sub(r"\s+", " ", text).strip()


def save_article(filename, body, url):
    """Article 저장. frontmatter + body."""
    content = f"""---
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
---
{body}
"""
    with open(f"{RAW_DIR}/{filename}", "w", encoding="utf-8") as f:
        f.write(content)
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def main():
    print(f"=== ROS2 드론 기술 수집 ({TODAY}) ===")

    # 1. GitHub Search API (9 queries) for ROS2 drone projects
    print("\n[1] GitHub Search API - ROS2 drone projects...")
    search_queries = [
        "topic:ros2 language:python drone swarm",
        "topic:drone-swarm language:python ros2",
        "uav swarm ros2",
        "px4 ros2 drone",
        "ardupilot ros2",
        "ros2 drone simulation",
        "mavros ros2",
        "multi-robot ros2",
        "swarm robotics ros2"
    ]

    for i, query in enumerate(search_queries):
        try:
            api_url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(query)}&sort=stars&order=desc&per_page=5"
            result = fetch_json(api_url)
            body = json.dumps(result, indent=2, ensure_ascii=False)  # JSON으로 저장
            filename = f"2026-08-05-github-search-ros2-drone-{i+1}.md"
            sha256 = save_article(filename, body, api_url)
            print(f"  ✓ {filename} (sha256: {sha256})")
        except Exception as e:
            print(f"  ✗ GitHub Search 쿼리 실패 {query}: {e}")

    # 2. PX4 Releases
    print("\n[2] PX4-Autopilot 최신 릴리즈...")
    try:
        api_url = "https://api.github.com/repos/PX4/PX4-Autopilot/releases"
        result = fetch_json(api_url)
        # 6개의 가장 최근 릴리즈만
        body = json.dumps(result[:6], indent=2, ensure_ascii=False)  
        filename = f"2026-08-05-px4-release-notes.md"
        sha256 = save_article(filename, body, api_url)
        print(f"  ✓ {filename} (sha256: {sha256})")
    except Exception as e:
        print(f"  ✗ PX4 Releases API 오류: {e}")

    # 3. ArduPilot Releases 
    print("\n[3] ArduPilot 최신 릴리즈...")
    try:
        api_url = "https://api.github.com/repos/ArduPilot/ardupilot/releases"
        result = fetch_json(api_url)
        # 7개의 가장 최근 릴리즈만
        body = json.dumps(result[:7], indent=2, ensure_ascii=False)  
        filename = f"2026-08-05-ardupilot-release-notes.md"
        sha256 = save_article(filename, body, api_url)
        print(f"  ✓ {filename} (sha256: {sha256})")
    except Exception as e:
        print(f"  ✗ ArduPilot Releases API 오류: {e}")

    # 4. PX4 Main Docs
    print("\n[4] PX4 공식 문서...")
    try:
        docs_url = "https://docs.px4.io/main/en/"
        html = fetch_html(docs_url)
        body = strip_html(html)  
        filename = f"2026-08-05-px4-docs-main.md"
        sha256 = save_article(filename, body, docs_url)
        print(f"  ✓ {filename} (sha256: {sha256})")
    except Exception as e:
        print(f"  ✗ PX4 Docs 오류: {e}")

    # 5. ROS2 Rolling Docs
    print("\n[5] ROS2 공식 문서...")
    try:
        docs_url = "https://docs.ros.org/en/rolling/"
        html = fetch_html(docs_url)
        body = strip_html(html) 
        filename = f"2026-08-05-ros2-docs-rolling.md"
        sha256 = save_article(filename, body, docs_url)
        print(f"  ✓ {filename} (sha256: {sha256})")
    except Exception as e:
        print(f"  ✗ ROS2 Docs 오류: {e}")

    print("\n=== 수집 완료 ===")


if __name__ == "__main__":
    main()