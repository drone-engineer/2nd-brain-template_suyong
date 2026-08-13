#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROS2 기반 드론 최신 기술 일일 수집 (2026-08-13)
- GitHub Search API (9 쿼리, per_page=10, sort=stars)
- PX4 공식 문서 (docs.px4.io/main/en/ + uXRCE-DDS + computer_vision + releases/main)
- ROS2 공식 문서 (docs.ros.org/en/rolling/ + About-ROS + Installation)
- PX4 / ArduPilot 릴리즈 노트 (GitHub Releases API)
수집 후 docs/reports/2026-08-13-ros2-drone-report.md 보고서 자동 생성용 메타데이터 저장.
"""
import json
import hashlib
import re
import urllib.request
import urllib.parse
import ssl
import subprocess
from pathlib import Path

TODAY = "2026-08-13"
NOW_ISO = f"{TODAY}T08:30:00Z"
RAW_DIR = "raw/articles"
REPO = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0 Safari/537.36 HermesAgent/1.0"
CTX = ssl.create_default_context()

# GitHub 토큰 (gh CLI에서 가져오기)
try:
    GH_TOKEN = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
except Exception:
    GH_TOKEN = None

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
    headers = {"User-Agent": UA, "Accept": "application/vnd.github+json"}
    if GH_TOKEN:
        headers["Authorization"] = f"Bearer {GH_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def fetch_html(url):
    headers = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"}
    if GH_TOKEN and "api.github.com" in url:
        headers["Authorization"] = f"Bearer {GH_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return r.read().decode("utf-8", "replace")


def strip_html(html):
    """HTML에서 의미 있는 텍스트만 추출 (스크립트/스타일/noscript 제거)."""
    html = re.sub(r"<script.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<noscript.*?</noscript>", "", html, flags=re.DOTALL | re.IGNORECASE)
    # 링크 텍스트 보존
    html = re.sub(r'<a[^>]*href="([^"]+)"[^>]*>', r' [링크: \\1] ', html)
    html = re.sub(r"<a[^>]*href=[\'\"]?([^\s\'\">]+)[\'\"]?[^>]*>", r' [링크: \\1] ', html)
    html = re.sub(r"<[^>]+>", " ", html)
    text = urllib.parse.unquote(html)
    return re.sub(r"\s+", " ", text).strip()


def save_article(filename, body, url, title, extra_fields=""):
    """Article 저장: frontmatter(sha256 포함) + body. GATE B 호환."""
    sha256 = hashlib.sha256(body.encode("utf-8")).hexdigest()
    fm_parts = [
        'source_url: "%s"' % url,
        'ingested: %s' % TODAY,
        'sha256: %s' % sha256,
        'title: "%s"' % title,
        'captured_via: 2nd-brain-cron',
    ]
    if extra_fields:
        fm_parts.append(extra_fields)
    frontmatter = "---\n" + "\n".join(fm_parts) + "\n---\n"
    content = frontmatter + body
    path = f"{REPO}/{RAW_DIR}/{filename}"
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return sha256


def main():
    print(f"=== ROS2 드론 기술 수집 ({TODAY}) ===")
    if GH_TOKEN:
        print(f"  (GitHub token available: {GH_TOKEN[:8]}…)")
    else:
        print("  (GitHub token NOT available - using unauthenticated API)")

    results = {}
    all_github_items = []
    all_repos_meta = {}

    # ── 1. GitHub Search API (9 queries) ──
    print("\n[1] GitHub Search API - ROS2 drone projects...")
    gh_header = "# ROS2 드론 관련 GitHub 저장소 검색 결과 (%s)\n\n" % TODAY
    gh_header += f"수집 일시: {NOW_ISO}\n"
    gh_header += f"수집 방법: GitHub Search API (per_page=10, sort=stars desc, {'인증' if GH_TOKEN else '비인증'}) \n\n"
    gh_header += "## 1. 검색 쿼리 목록\n\n"
    gh_header += "| # | 검색어 | 정렬 기준 | 결과 수 |\n|---|--------|-----------|---------|\n"

    query_results = []
    for i, (query, desc) in enumerate(QUERIES):
        try:
            api_url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(query)}&sort=stars&order=desc&per_page=10"
            result = fetch_json(api_url)
            items = result.get("items", [])
            total = result.get("total_count", len(items))
            print(f"  ✓ 쿼리 {i+1}: '{query}' → {total} results, {len(items)} returned")
            query_results.append((query, desc, items, total, api_url))
            for it in items:
                it["_source_query"] = query
                it["_source_desc"] = desc
                it["_query_index"] = i + 1
                all_github_items.append(it)
                # Collect repo metadata for dedup
                full_name = it.get("full_name", "")
                if full_name and full_name not in all_repos_meta:
                    all_repos_meta[full_name] = it
        except Exception as e:
            print(f"  ✗ GitHub Search 쿼리 실패 '{query}': {e}")
            query_results.append((query, desc, [], 0, api_url))

    # Build GitHub data Markdown body
    gh_body = gh_header
    for i, (query, desc, items, total, api_url) in enumerate(query_results):
        gh_body += f"| {i+1} | `{query}` | stars desc | {total}개 |\n"
    gh_body += "\n## 2. 핵심 패키지 (GitHub ⭐ 기준 top 10)\n\n"

    # Sort all items by stars, deduplicate by full_name
    unique_items = sorted(
        all_repos_meta.values(),
        key=lambda x: x.get("stargazers_count", 0),
        reverse=True,
    )

    gh_body += "| 순위 | 저장소 | ⭐ | 언어 | 설명 | 최근 업데이트 |\n"
    gh_body += "|------|--------|----|------|------|---------------|\n"
    for rank, it in enumerate(unique_items[:10], 1):
        name = it.get("full_name", "N/A")
        star = it.get("stargazers_count", 0)
        lang = it.get("language", "N/A")
        desc_item = it.get("description", "") or "(none)"
        desc_item = desc_item[:140]
        pushed = it.get("pushed_at", "N/A")[:10]
        gh_body += f"| {rank} | {name} | {star} | {lang} | {desc_item} | {pushed} |\n"

    gh_body += "\n## 3. 쿼리별 상세 결과\n\n"
    for i, (query, desc, items, total, api_url) in enumerate(query_results):
        gh_body += f"### 3-{i+1}. {desc} (`{query}`)\n\n"
        if not items:
            gh_body += "  - (결과 없음)\n\n"
            continue
        gh_body += "| 저장소 | ⭐ | 언어 | 설명 | 최근 업데이트 |\n"
        gh_body += "|--------|----|------|------|---------------|\n"
        for it in sorted(items, key=lambda x: x.get("stargazers_count", 0), reverse=True)[:10]:
            name = it.get("full_name", "N/A")
            star = it.get("stargazers_count", 0)
            lang = it.get("language", "N/A")
            d = (it.get("description", "") or "(none)")[:120]
            pushed = it.get("pushed_at", "N/A")[:10]
            gh_body += f"| {name} | {star} | {lang} | {d} | {pushed} |\n"
        gh_body += "\n"

    # Section 4: Top repo detailed metadata
    gh_body += "## 4. 저장소 상세 메타데이터 (Top 8)\n\n"
    for rank, it in enumerate(unique_items[:8], 1):
        full_name = it.get("full_name", "N/A")
        star = it.get("stargazers_count", 0)
        created = it.get("created_at", "N/A")[:10]
        lang = it.get("language", "N/A")
        topics = it.get("topics", [])
        gh_body += f"### {rank}. {full_name}\n"
        gh_body += f"- ⭐ {star} | 생성: {created} | 언어: {lang}\n"
        if topics:
            gh_body += f"- 토픽: {', '.join(topics)}\n"
        desc_item = it.get("description", "") or "(none)"
        gh_body += f"- 설명: {desc_item}\n"
        homepage = it.get("homepage", "")
        if homepage:
            gh_body += f"- 홈페이지: {homepage}\n"
        license_info = it.get("license", {})
        if license_info and license_info.get("spdx_id"):
            gh_body += f"- 라이선스: {license_info['spdx_id']}\n"
        default_branch = it.get("default_branch", "")
        if default_branch:
            gh_body += f"- 기본 브랜치: {default_branch}\n"
        # README or repo URL
        html_url = it.get("html_url", "")
        if html_url:
            gh_body += f"- URL: {html_url}\n"
        gh_body += "\n"

    # Section 5: 종합 관측사항
    gh_body += "## 5. 종합 관측사항\n\n"
    # Key observations based on collected data
    swarm_count = sum(1 for it in unique_items if any(t in it.get("topics", []) for t in ["swarm", "multi-agent", "multirotor"]))
    yolo_count = sum(1 for it in unique_items if "yolo" in (it.get("topics", []) + [(it.get("description") or "").lower()]))
    px4_count = sum(1 for it in unique_items if "px4" in (it.get("topics", []) + [(it.get("description") or "").lower()]))
    aruco_count = sum(1 for it in unique_items if "aruco" in ((it.get("description") or "").lower()))
    slam_count = sum(1 for it in unique_items if "slam" in (it.get("topics", []) + [(it.get("description") or "").lower()]))
    zenoh_count = sum(1 for it in unique_items if "zenoh" in ((it.get("description") or "").lower() + ",".join(it.get("topics", []))))
    mediapipe_count = sum(1 for it in unique_items if "mediapipe" in ((it.get("description") or "").lower()))

    gh_body += f"- **검색 통계**: 9 쿼리, 총 {len(unique_items)}개의 중복 제거된 저장소 발견\n"
    gh_body += f"- **스웜/다중 드론**: {swarm_count}개 저장소에서 swarm/multi-agent 관련\n"
    gh_body += f"- **YOLO 통합**: {yolo_count}개 저장소에서 YOLO 객체 감지 언급\n"
    gh_body += f"- **PX4 통합**: {px4_count}개 저장소에서 PX4 관련 (공식 px4_ros_com 포함)\n"
    gh_body += f"- **ArUco 정밀 착륙**: {aruco_count}개 저장소에서 ArUco 언급\n"
    gh_body += f"- **SLAM**: {slam_count}개 저장소에서 SLAM 관련\n"
    gh_body += f"- **Zenoh**: {zenoh_count}개 저장소에서 Zenoh 미들웨어 언급\n"
    gh_body += f"- **MediaPipe**: {mediapipe_count}개 저장소에서 MediaPipe 언급\n"
    gh_body += f"- **가장 활발한 저장소**: {unique_items[0]['full_name'] if unique_items else 'N/A'} (⭐{unique_items[0]['stargazers_count'] if unique_items else 0})\n"

    # Save GitHub data
    filename = f"{TODAY}-ros2-drone-github-data.md"
    sha256 = save_article(filename, gh_body, "GitHub Search API (9 queries)", f"ROS2 드론 GitHub 검색 데이터 ({TODAY})", f'search_queries: "9 queries, per_page=10, sort=stars desc"')
    print(f"\n  ✓ {filename} (sha256: {sha256[:16]}…) — {len(unique_items)} unique repos")
    results[filename] = {"sha256": sha256, "url": "GitHub Search API (9 queries)"}

    # ── 2. PX4 Releases ──
    print("\n[2] PX4-Autopilot 최신 릴리즈...")
    try:
        api_url = "https://api.github.com/repos/PX4/PX4-Autopilot/releases"
        result = fetch_json(api_url)
        releases = result[:6] if isinstance(result, list) else []
        # Build Markdown body
        px4_rel_body = f"# PX4-Autopilot 릴리즈 노트 ({TODAY})\n\n"
        px4_rel_body += f"수집 일시: {NOW_ISO}\n"
        px4_rel_body += f"출처: {api_url}\n\n"
        for r in releases:
            tag = r.get("tag_name", "N/A")
            name = r.get("name", "")
            prerelease = r.get("prerelease", False)
            draft = r.get("draft", False)
            pub_date = r.get("published_at", "N/A")[:10]
            body_text = r.get("body", "(no body)")
            # Truncate very large bodies
            if len(body_text) > 5000:
                body_text = body_text[:5000] + "\n\n...(truncated)..."
            px4_rel_body += f"## {tag}\n\n"
            px4_rel_body += f"- 이름: {name}\n"
            px4_rel_body += f"- 날짜: {pub_date}\n"
            px4_rel_body += f"- 프리릴리즈: {prerelease}\n"
            px4_rel_body += f"- 드래프트: {draft}\n"
            if body_text:
                px4_rel_body += f"\n```\n{body_text}\n```\n\n"
            else:
                px4_rel_body += "\n\n"
        filename = f"{TODAY}-px4-release-notes.md"
        sha256 = save_article(filename, px4_rel_body, api_url, f"PX4 릴리즈 노트 ({TODAY})", "")
        print(f"  ✓ {filename} (sha256: {sha256[:16]}…)")
        results[filename] = {"sha256": sha256, "url": api_url}
    except Exception as e:
        print(f"  ✗ PX4 Releases API 오류: {e}")

    # ── 3. ArduPilot Releases ──
    print("\n[3] ArduPilot 최신 릴리즈...")
    try:
        api_url = "https://api.github.com/repos/ArduPilot/ardupilot/releases"
        result = fetch_json(api_url)
        releases = result[:7] if isinstance(result, list) else []
        ap_rel_body = f"# ArduPilot 릴리즈 노트 ({TODAY})\n\n"
        ap_rel_body += f"수집 일시: {NOW_ISO}\n"
        ap_rel_body += f"출처: {api_url}\n\n"
        for r in releases:
            tag = r.get("tag_name", "N/A")
            name = r.get("name", "")
            prerelease = r.get("prerelease", False)
            draft = r.get("draft", False)
            pub_date = r.get("published_at", "N/A")[:10]
            body_text = r.get("body", "(no body)")
            if len(body_text) > 5000:
                body_text = body_text[:5000] + "\n\n...(truncated)..."
            ap_rel_body += f"## {tag}\n\n"
            ap_rel_body += f"- 이름: {name}\n"
            ap_rel_body += f"- 날짜: {pub_date}\n"
            ap_rel_body += f"- 프리릴리즈: {prerelease}\n"
            ap_rel_body += f"- 드래프트: {draft}\n"
            if body_text:
                ap_rel_body += f"\n```\n{body_text}\n```\n\n"
            else:
                ap_rel_body += "\n\n"
        filename = f"{TODAY}-ardupilot-release-notes.md"
        sha256 = save_article(filename, ap_rel_body, api_url, f"ArduPilot 릴리즈 노트 ({TODAY})", "")
        print(f"  ✓ {filename} (sha256: {sha256[:16]}…)")
        results[filename] = {"sha256": sha256, "url": api_url}
    except Exception as e:
        print(f"  ✗ ArduPilot Releases API 오류: {e}")

    # ── 4. PX4 공식 문서 ──
    print("\n[4] PX4 공식 문서...")
    px4_pages = [
        ("https://docs.px4.io/main/en/", "PX4 Autopilot User Guide (Main)"),
        ("https://docs.px4.io/main/en/middleware/uxrce_dds.html", "uXRCE-DDS (PX4-ROS 2/DDS Bridge)"),
        ("https://docs.px4.io/main/en/computer_vision/", "Computer Vision"),
        ("https://docs.px4.io/main/en/releases/main.html", "PX4 Main Release Notes"),
    ]
    px4_docs_parts = []
    for url, label in px4_pages:
        try:
            html = fetch_html(url)
            text = strip_html(html)
            px4_docs_parts.append(f"## {label} ({url})\n\n{text[:3000]}\n\n")
            print(f"  ✓ {label}")
        except Exception as e:
            px4_docs_parts.append(f"## {label} ({url})\n\n(수집 실패: {e})\n\n")
            print(f"  ✗ {label}: {e}")
    px4_docs_body = f"# PX4 공식 문서 수집 ({TODAY})\n\n"
    px4_docs_body += f"수집 일시: {NOW_ISO}\n"
    px4_docs_body += f"수집 방법: docs.px4.io/main/en/ (curl + HTML 텍스트 추출, 2nd-brain-cron)\n\n"
    px4_docs_body += "".join(px4_docs_parts)
    filename = f"{TODAY}-px4-docs.md"
    sha256 = save_article(filename, px4_docs_body, "https://docs.px4.io/main/en/", f"PX4 공식 문서 수집 ({TODAY})", 'pages: "main, uxrce_dds, computer_vision, releases/main"')
    print(f"  ✓ {filename} (sha256: {sha256[:16]}…)")
    results[filename] = {"sha256": sha256, "url": "https://docs.px4.io/main/en/"}

    # ── 5. ROS2 공식 문서 ──
    print("\n[5] ROS2 공식 문서...")
    ros2_pages = [
        ("https://docs.ros.org/en/rolling/", "ROS 2 문서 메인 (Rolling)"),
        ("https://docs.ros.org/en/rolling/Get-Started/About-ROS/About-ROS.html", "About ROS"),
        ("https://docs.ros.org/en/rolling/Get-Started/Installation.html", "설치 (Installation)"),
        ("https://docs.ros.org/en/rolling/Installation/Installing-ROS2-From-Debr.html", "Ubuntu Debian Installation"),
    ]
    ros2_docs_parts = []
    for url, label in ros2_pages:
        try:
            html = fetch_html(url)
            text = strip_html(html)
            ros2_docs_parts.append(f"## {label} ({url})\n\n{text[:3000]}\n\n")
            print(f"  ✓ {label}")
        except Exception as e:
            ros2_docs_parts.append(f"## {label} ({url})\n\n(수집 실패: {e})\n\n")
            print(f"  ✗ {label}: {e}")
    ros2_docs_body = f"# ROS2 공식 문서 수집 ({TODAY})\n\n"
    ros2_docs_body += f"수집 일시: {NOW_ISO}\n"
    ros2_docs_body += f"수집 방법: docs.ros.org/en/rolling/ (curl + HTML 텍스트 추출, 2nd-brain-cron)\n\n"
    ros2_docs_body += "".join(ros2_docs_parts)
    filename = f"{TODAY}-ros2-docs.md"
    sha256 = save_article(filename, ros2_docs_body, "https://docs.ros.org/en/rolling/", f"ROS2 공식 문서 수집 ({TODAY})", 'pages: "main, About-ROS, Installation"')
    print(f"  ✓ {filename} (sha256: {sha256[:16]}…)")
    results[filename] = {"sha256": sha256, "url": "https://docs.ros.org/en/rolling/"}

    print("\n=== 수집 완료 ===")

    # Save results metadata for report generation
    with open(f"{REPO}/docs/workflow/{TODAY}-collect-results.json", "w", encoding="utf-8") as f:
        json.dump({k: {"sha256": v.get("sha256"), "url": v.get("url")} for k, v in results.items()}, f, indent=2, ensure_ascii=False)
    print(f"결과 메타데이터: docs/workflow/{TODAY}-collect-results.json")

    # Also save the GitHub data for report generation
    with open(f"{REPO}/docs/workflow/{TODAY}-github-data-summary.json", "w", encoding="utf-8") as f:
        summary = {
            "top_repos": [
                {
                    "full_name": it.get("full_name", ""),
                    "stargazers_count": it.get("stargazers_count", 0),
                    "language": it.get("language", ""),
                    "description": it.get("description", "") or "",
                    "pushed_at": it.get("pushed_at", ""),
                    "created_at": it.get("created_at", ""),
                    "topics": it.get("topics", []),
                    "homepage": it.get("homepage", ""),
                    "license": (it.get("license") or {}).get("spdx_id", ""),
                    "html_url": it.get("html_url", ""),
                    "source_query": it.get("_source_query", ""),
                    "source_desc": it.get("_source_desc", ""),
                }
                for it in unique_items[:10]
            ],
            "query_counts": {
                q[0]: q[3] for q in query_results
            },
            "total_unique_repos": len(unique_items),
        }
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"GitHub 요약: docs/workflow/{TODAY}-github-data-summary.json")

    return results


if __name__ == "__main__":
    main()
