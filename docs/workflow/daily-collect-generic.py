#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROS2 기반 드론 최신 기술 일일 수집 (parameterized)
- Usage: python3 daily-collect-generic.py <YYYY-MM-DD>
- Collects: GitHub Search API (9 queries), PX4 releases, ArduPilot releases,
  PX4 docs (docs.px4.io), ROS2 docs (docs.ros.org)
- Saves raw/articles/YYYY-MM-DD-*.md with SHA256 checksums + JSON summaries for report generation.
"""
import sys
import json
import hashlib
import os
import re
import html
import subprocess
from urllib.parse import quote_plus, urlencode

DATE = sys.argv[1]
RAW_DIR = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template/raw/articles"
REPO_ROOT = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"
REPORTS_DIR = os.path.join(REPO_ROOT, "docs", "reports")
COLLECTED_AT = f"{DATE}T08:30:00Z"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0 Safari/537.36 HermesAgent/1.0"

QUERIES = [
    ("ros2 drone detection", "ROS2 드론 객체 검출"),
    ("ros2 drone autonomous", "ROS2 드론 자윅 비행"),
    ("ros2 drone navigation", "ROS2 드론 내비게이션"),
    ("PX4 ros2 bridge", "PX4 ROS2 브리지"),
    ("YOLO ros2 drone", "YOLO ROS2 드론"),
    ("zenoh ros2 middleware", "Zenoh ROS2 미들웨어"),
    ("MediaPipe ros2", "MediaPipe ROS2"),
    ("SLAM ros2 drone", "SLAM ROS2 드론"),
    ("ArUco ros2 detection", "ArUco ROS2 검출"),
]

def gh_token():
    result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
    if result.returncode != 0 or not result.stdout.strip():
        print("  [WARN] Failed to get gh token")
        return None
    return result.stdout.strip()

_TOKEN = gh_token()

def gh_api(endpoint, params=None):
    import urllib.request
    url = f"https://api.github.com/{endpoint}"
    if params:
        url += "?" + urlencode(params)
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if _TOKEN:
        headers["Authorization"] = f"token {_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8", "replace"))

def curl_text(url):
    result = subprocess.run(["curl", "-sL", "--max-time", "30", url], capture_output=True, text=True, timeout=45)
    raw = result.stdout
    if not raw:
        return f"[ERROR: curl returned empty content for {url}]"
    raw = re.sub(r'<script[^>]*>.*?</script>', '', raw, flags=re.DOTALL | re.IGNORECASE)
    raw = re.sub(r'<style[^>]*>.*?</style>', '', raw, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', raw)
    text = html.unescape(text)
    return re.sub(r'\s+', ' ', text).strip()

def compute_sha256(body):
    return hashlib.sha256(body.encode("utf-8")).hexdigest()

def write_raw_file(filename, frontmatter_dict, body):
    sha = compute_sha256(body)
    fm_lines = ["---"]
    for k, v in frontmatter_dict.items():
        if isinstance(v, list):
            fm_lines.append(f"{k}:")
            for item in v:
                fm_lines.append(f"  - {item}")
        elif isinstance(v, bool):
            fm_lines.append(f"{k}: {'true' if v else 'false'}")
        else:
            fm_lines.append(f'{k}: {v}')
    fm_lines.append(f"sha256: {sha}")
    fm_lines.append("---")
    frontmatter = "\n".join(fm_lines) + "\n"
    content = frontmatter + body
    filepath = os.path.join(RAW_DIR, filename)
    with open(filepath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"  Written: {filepath} (sha256={sha[:16]}...)")
    return sha


# ======================================================================
# 1. GitHub Search API
# ======================================================================
print(f"\n[1/5] GitHub Search API — ROS2 drone projects ({DATE})...")
all_query_results = {}
all_repos = {}

for q, desc in QUERIES:
    try:
        data = gh_api("search/repositories", {"q": q, "sort": "stars", "order": "desc", "per_page": "10"})
        if data:
            all_query_results[q] = data
            print(f"  ✓ '{q}': {data.get('total_count', 0)} repos")
            for it in data.get("items", []):
                fn = it.get("full_name", "")
                if fn not in all_repos:
                    all_repos[fn] = it
                elif it.get("stargazers_count", 0) > all_repos[fn].get("stargazers_count", 0):
                    all_repos[fn] = it
        else:
            all_query_results[q] = {"total_count": 0, "items": []}
    except Exception as e:
        print(f"  ✗ '{q}': {e}")
        all_query_results[q] = {"total_count": 0, "items": []}

sorted_repos = sorted(all_repos.values(), key=lambda x: x.get("stargazers_count", 0), reverse=True)
top_repos = sorted_repos[:10]

# Build GitHub markdown body (same structure as existing)
lines = [
    f"# ROS2 드론 관련 GitHub 저장소 검색 결과 ({DATE})",
    f"",
    f"수집 일시: {COLLECTED_AT}",
    f"수집 방법: GitHub Search API (per_page=10, sort=stars desc, 인증)",
    f"",
    f"## 1. 검색 쿼리 목록",
    f"",
    f"| # | 검색어 | 정렬 기준 | 결과 수 |",
    f"|---|--------|-----------|---------|",
]
for i, (q, desc) in enumerate(QUERIES, 1):
    count = all_query_results.get(q, {}).get("total_count", 0)
    lines.append(f"| {i} | `{q}` | stars desc | {count}개 |")
lines.append("")
lines.append("## 2. 핵심 패키지 (GitHub ⭐ 기준 top 10)")
lines.append("")
lines.append("| 순위 | 저장소 | ⭐ | 언어 | 설명 | 최근 업데이트 |")
lines.append("|------|--------|----|------|------|---------------|")
for i, repo in enumerate(top_repos, 1):
    desc_str = (repo.get('description','') or '').replace('|', '\\|')[:140]
    lines.append(f"| {i} | {repo.get('full_name','')} | {repo.get('stargazers_count',0)} | {repo.get('language','') or '-'} | {desc_str} | {repo.get('pushed_at','')[:10]} |")
lines.append("")
lines.append("## 3. 쿼리별 상세 결과")
lines.append("")
query_titles = {
    "ros2 drone detection": "ROS2 드론 객체 검출",
    "ros2 drone autonomous": "ROS2 드론 자윅 비행",
    "ros2 drone navigation": "ROS2 드론 내비게이션",
    "PX4 ros2 bridge": "PX4 ROS2 브리지",
    "YOLO ros2 drone": "YOLO ROS2 드론",
    "zenoh ros2 middleware": "Zenoh ROS2 미들웨어",
    "MediaPipe ros2": "MediaPipe ROS2",
    "SLAM ros2 drone": "SLAM ROS2 드론",
    "ArUco ros2 detection": "ArUco ROS2 검출",
}
for idx, (q, desc) in enumerate(QUERIES, 1):
    title = query_titles.get(q, q)
    lines.append(f"### 3-{idx}. {title} (`{q}`)")
    lines.append("")
    lines.append("| 저장소 | ⭐ | 언어 | 설명 | 최근 업데이트 |")
    lines.append("|--------|----|------|------|---------------|")
    items = all_query_results.get(q, {}).get("items", [])
    for it in items[:10]:
        desc_it = (it.get('description','') or '').replace('|', '\\|')[:120]
        lines.append(f"| {it.get('full_name','')} | {it.get('stargazers_count',0)} | {it.get('language','') or '-'} | {desc_it} | {it.get('pushed_at','')[:10]} |")
    lines.append("")

lines.append("## 4. 저장소 상세 메타데이터 (Top 8)")
lines.append("")
for i, repo in enumerate(top_repos[:8], 1):
    lines.append(f"### {i}. {repo.get('full_name','')}")
    lines.append(f"- ⭐ {repo.get('stargazers_count',0)} | 생성: {repo.get('created_at','')[:10]} | 언어: {repo.get('language','') or '-'}")
    topics = repo.get("topics", [])
    if topics:
        lines.append(f"- 토픽: {', '.join(topics)}")
    lines.append(f"- 설명: {repo.get('description','') or '(none)'}")
    hp = repo.get("homepage", "") or ""
    if hp:
        lines.append(f"- 홈페이지: {hp}")
    lic = repo.get("license", {})
    if lic:
        lines.append(f"- 라이선스: {lic.get('name','None')}")
    lines.append(f"- 기본 브랜치: {repo.get('default_branch','main')}")
    lines.append(f"- URL: {repo.get('html_url','')}")
    lines.append("")

lines.append("## 5. 종합 관측사항")
lines.append("")
total_unique = len(all_repos)
desc_lower = lambda r: (r.get("description","") or "").lower()
topics_lower = lambda r: [t.lower() for t in r.get("topics", [])]
yolo_count = sum(1 for r in all_repos.values() if "yolo" in desc_lower(r) or "yolo" in topics_lower(r))
px4_count = sum(1 for r in all_repos.values() if "px4" in desc_lower(r) or "px4" in topics_lower(r))
aruco_count = sum(1 for r in all_repos.values() if "aruco" in desc_lower(r))
slam_count = sum(1 for r in all_repos.values() if "slam" in desc_lower(r) or "slam" in topics_lower(r))
zenoh_count = sum(1 for r in all_repos.values() if "zenoh" in desc_lower(r) or "zenoh" in topics_lower(r))
mediapipe_count = sum(1 for r in all_repos.values() if "mediapipe" in desc_lower(r))
swarm_count = sum(1 for r in all_repos.values() if "swarm" in desc_lower(r) or "swarm" in topics_lower(r) or "multi-agent" in topics_lower(r))

lines.append(f"- **검색 통계**: 9 쿼리, 총 {total_unique}개의 중복 제거된 저장소 발견")
lines.append(f"- **스웜/다중 드론**: {swarm_count}개 저장소에서 swarm/multi-agent 관련")
lines.append(f"- **YOLO 통합**: {yolo_count}개 저장소에서 YOLO 객체 감지 언급")
lines.append(f"- **PX4 통합**: {px4_count}개 저장소에서 PX4 관련 (공식 px4_ros_com 포함)")
lines.append(f"- **ArUco 정밀 착륙**: {aruco_count}개 저장소에서 ArUco 언급")
lines.append(f"- **SLAM**: {slam_count}개 저장소에서 SLAM 관련")
lines.append(f"- **Zenoh**: {zenoh_count}개 저장소에서 Zenoh 미들웨어 언급")
lines.append(f"- **MediaPipe**: {mediapipe_count}개 저장소에서 MediaPipe 언급")
if top_repos:
    lines.append(f"- **가장 활발한 저장소**: {top_repos[0].get('full_name','')} (⭐{top_repos[0].get('stargazers_count',0)})")

gh_body = "\n".join(lines)
gh_sha = write_raw_file(f"{DATE}-ros2-drone-github-data.md", {
    "source_url": "GitHub Search API (9 queries)",
    "ingested": DATE,
    "title": f"ROS2 드론 GitHub 검색 데이터 ({DATE})",
    "captured_via": "2nd-brain-cron",
    "search_queries": "9 queries, per_page=10, sort=stars desc",
}, gh_body)
print(f"  ✓ GitHub data saved (sha256={gh_sha[:16]}...)")

# Save JSON summary for report generation
summary = {
    "top_repos": [{
        "full_name": it.get("full_name", ""),
        "stargazers_count": it.get("stargazers_count", 0),
        "language": it.get("language", ""),
        "description": it.get("description") or "",
        "pushed_at": it.get("pushed_at", ""),
        "created_at": it.get("created_at", ""),
        "topics": it.get("topics", []),
        "homepage": it.get("homepage", ""),
        "license": (it.get("license") or {}).get("spdx_id", ""),
        "html_url": it.get("html_url", ""),
        "source_query": "",
        "source_desc": "",
    } for it in top_repos[:10]],
    "query_counts": {q: all_query_results.get(q, {}).get("total_count", 0) for q, _ in QUERIES},
    "total_unique_repos": total_unique,
    "yolo_count": yolo_count,
    "px4_count": px4_count,
    "aruco_count": aruco_count,
    "slam_count": slam_count,
    "zenoh_count": zenoh_count,
    "mediapipe_count": mediapipe_count,
    "swarm_count": swarm_count,
}
with open(os.path.join(REPO_ROOT, "docs", "workflow", f"{DATE}-github-data-summary.json"), "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

# ======================================================================
# 2. PX4 Releases
# ======================================================================
print(f"\n[2/5] PX4-Autopilot 릴리즈 노트 ({DATE})...")
results = {}
try:
    px4_releases = gh_api("repos/PX4/PX4-Autopilot/releases", {"per_page": "10"})
    lines = [f"# PX4-Autopilot 릴리즈 노트 ({DATE}", "", f"수집 일시: {COLLECTED_AT}", "출처: https://api.github.com/repos/PX4/PX4-Autopilot/releases", ""]
    if px4_releases:
        for r in px4_releases[:6]:
            tag = r.get("tag_name", "N/A")
            lines.append(f"## {tag}")
            lines.append("")
            lines.append(f"- 이름: {r.get('name','') or tag}")
            lines.append(f"- 날짜: {r.get('published_at','N/A')[:10]}")
            lines.append(f"- 프리릴리즈: {str(r.get('prerelease',False)).capitalize()}")
            lines.append(f"- 드래프트: {str(r.get('draft',False)).capitalize()}")
            lines.append("")
            body_text = (r.get("body","") or "").replace("\r\n","\n").strip()
            if len(body_text) > 5000:
                body_text = body_text[:5000] + "\n\n...(truncated)...)"
            if body_text:
                lines.append(f"```\n{body_text}\n```")
            else:
                lines.append("(본문 없음)")
            lines.append("")
    else:
        lines.append("[WARN: PX4 릴리즈 정보를 가져오지 못했습니다]")
        lines.append("")
    px4_body = "\n".join(lines)
    px4_sha = write_raw_file(f"{DATE}-px4-release-notes.md", {
        "source_url": "https://api.github.com/repos/PX4/PX4-Autopilot/releases",
        "ingested": DATE,
        "title": f"PX4 릴리즈 노트 ({DATE})",
        "captured_via": "2nd-brain-cron",
    }, px4_body)
    results["px4"] = px4_sha
except Exception as e:
    print(f"  ✗ PX4 Releases 오류: {e}")

# ======================================================================
# 3. ArduPilot Releases
# ======================================================================
print(f"\n[3/5] ArduPilot 릴리즈 노트 ({DATE})...")
try:
    ap_releases = gh_api("repos/ArduPilot/ardupilot/releases", {"per_page": "10"})
    lines = [f"# ArduPilot 릴리즈 노트 ({DATE}", "", f"수집 일시: {COLLECTED_AT}", "출처: https://api.github.com/repos/ArduPilot/ardupilot/releases", ""]
    if ap_releases:
        for r in ap_releases[:7]:
            tag = r.get("tag_name", "N/A")
            lines.append(f"## {tag}")
            lines.append("")
            lines.append(f"- 이름: {r.get('name','') or tag}")
            lines.append(f"- 날짜: {r.get('published_at','N/A')[:10]}")
            lines.append(f"- 프리릴리즈: {str(r.get('prerelease',False)).capitalize()}")
            lines.append(f"- 드래프트: {str(r.get('draft',False)).capitalize()}")
            lines.append("")
            body_text = (r.get("body","") or "").replace("\r\n","\n").strip()
            if len(body_text) > 5000:
                body_text = body_text[:5000] + "\n\n...(truncated)...)"
            if body_text:
                lines.append(f"```\n{body_text}\n```")
            else:
                lines.append("(본문 없음)")
            lines.append("")
    else:
        lines.append("[WARN: ArduPilot 릴리즈 정보를 가져오지 못했습니다]")
        lines.append("")
    ap_body = "\n".join(lines)
    ap_sha = write_raw_file(f"{DATE}-ardupilot-release-notes.md", {
        "source_url": "https://api.github.com/repos/ArduPilot/ardupilot/releases",
        "ingested": DATE,
        "title": f"ArduPilot 릴리즈 노트 ({DATE})",
        "captured_via": "2nd-brain-cron",
    }, ap_body)
    results["ardupilot"] = ap_sha
except Exception as e:
    print(f"  ✗ ArduPilot Releases 오류: {e}")

# ======================================================================
# 4. PX4 Docs
# ======================================================================
print(f"\n[4/5] PX4 공식 문서 ({DATE})...")
px4_urls = [
    ("PX4 Autopilot User Guide (Main)", "https://docs.px4.io/main/en/"),
    ("uXRCE-DDS (PX4-ROS 2/DDS Bridge)", "https://docs.px4.io/main/en/middleware/uxrce_dds.html"),
    ("Computer Vision (Optical Flow, MoCap, VIO, Avoidance)", "https://docs.px4.io/main/en/computer_vision/"),
    ("PX4 Main Release Notes", "https://docs.px4.io/main/en/releases/main.html"),
    ("ROS 2 Interface (px4_ros_com)", "https://docs.px4.io/main/en/ros2/"),
    ("Zenoh Middleware", "https://docs.px4.io/main/en/middleware/zenoh.html"),
]
px4_lines = [f"# PX4 공식 문서 수집 ({DATE}", "", f"수집 일시: {COLLECTED_AT}", "수집 방법: docs.px4.io/main/en/ (curl + HTML 텍스트 추출, 2nd-brain-cron)", ""]
for title, url in px4_urls:
    px4_lines.append(f"## {title} ({url})")
    px4_lines.append("")
    text = curl_text(url)
    if text.startswith("[ERROR:"):
        px4_lines.append(text)
    else:
        px4_lines.append(text[:5000])
    px4_lines.append("")
px4_docs_body = "\n".join(px4_lines)
px4_docs_sha = write_raw_file(f"{DATE}-px4-docs.md", {
    "source_url": "https://docs.px4.io/main/en/",
    "ingested": DATE,
    "title": f"PX4 공식 문서 수집 ({DATE})",
    "captured_via": "2nd-brain-cron",
    "pages": "main, uxrce_dds, computer_vision, releases/main, ros2, zenoh",
}, px4_docs_body)
results["px4_docs"] = px4_docs_sha

# ======================================================================
# 5. ROS2 Docs
# ======================================================================
print(f"\n[5/5] ROS2 공식 문서 ({DATE})...")
ros2_urls = [
    ("ROS 2 문서 메인 (Rolling)", "https://docs.ros.org/en/rolling/"),
    ("About ROS", "https://docs.ros.org/en/rolling/Get-Started/About-ROS/About-ROS.html"),
    ("설치 (Installation)", "https://docs.ros.org/en/rolling/Get-Started/Installation.html"),
    ("Ubuntu Debian Installation", "https://docs.ros.org/en/rolling/Installation/Installing-ROS2-From-Debr.html"),
    ("ROS 2 Concepts", "https://docs.ros.org/en/rolling/Concepts/About-ROS-2-Architecture.html"),
    ("ROS 2 Communication (QoS)", "https://docs.ros.org/en/rolling/Concepts/Basic/Quality-of-Service.html"),
    ("Navigation 2 (Nav2)", "https://docs.ros.org/en/rolling/Tutorials/Navigation-on-ROS2.html"),
]
ros2_lines = [f"# ROS2 공식 문서 수집 ({DATE}", "", f"수집 일시: {COLLECTED_AT}", "수집 방법: docs.ros.org/en/rolling/ (curl + HTML 텍스트 추출, 2nd-brain-cron)", ""]
for title, url in ros2_urls:
    ros2_lines.append(f"## {title} ({url})")
    ros2_lines.append("")
    text = curl_text(url)
    if text.startswith("[ERROR:"):
        ros2_lines.append(text)
    else:
        ros2_lines.append(text[:5000])
    ros2_lines.append("")
ros2_docs_body = "\n".join(ros2_lines)
ros2_docs_sha = write_raw_file(f"{DATE}-ros2-docs.md", {
    "source_url": "https://docs.ros.org/en/rolling/",
    "ingested": DATE,
    "title": f"ROS2 공식 문서 수집 ({DATE})",
    "captured_via": "2nd-brain-cron",
    "pages": "main, About-ROS, Installation, Concepts, QoS, Nav2",
}, ros2_docs_body)
results["ros2_docs"] = ros2_docs_sha

# Save results metadata
with open(os.path.join(REPO_ROOT, "docs", "workflow", f"{DATE}-collect-results.json"), "w", encoding="utf-8") as f:
    json.dump({k: {"sha256": v, "url": ""} for k, v in results.items()}, f, indent=2, ensure_ascii=False)

print(f"\n{'=' * 60}")
print(f"Collection complete for {DATE}!")
print(f"{'=' * 60}")
for k, v in results.items():
    print(f"  {k}: {v[:16]}...")
