#!/usr/bin/env python3
"""Daily ROS2 Drone Technology Collector — cron job for 2026-08-15.
Collects from: GitHub Search API, PX4 releases, ArduPilot releases, PX4 docs, ROS2 docs.
Saves raw/articles/YYYY-MM-DD-*.md with SHA256 checksums."""

import subprocess
import json as _json
import hashlib
import os
import re
import html
from datetime import datetime, timezone

DATE = "2026-08-15"
RAW_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "raw", "articles",
)
# Fix: use known repo root
REPO_ROOT = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"
RAW_DIR = os.path.join(REPO_ROOT, "raw", "articles")

os.makedirs(RAW_DIR, exist_ok=True)

COLLECTED_AT = f"{DATE}T08:30:00Z"


def gh_token():
    """Get GitHub auth token from gh CLI."""
    result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
    if result.returncode != 0 or not result.stdout.strip():
        print(f"  [WARN] Failed to get gh token: {result.stderr[:200]}")
        return None
    return result.stdout.strip()


_TOKEN = gh_token()


def gh_api(endpoint, extra_params=None):
    """Call GitHub API via curl with gh token, return parsed JSON."""
    base_url = "https://api.github.com"
    url = f"{base_url}/{endpoint}"
    if extra_params:
        param_str = "&".join(f"{k}={v}" for k, v in extra_params.items())
        url = f"{url}?{param_str}"

    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if _TOKEN:
        headers["Authorization"] = f"token {_TOKEN}"

    cmd = ["curl", "-sL", "--max-time", "45", "-H", f"Accept: {headers['Accept']}",
           "-H", f"X-GitHub-Api-Version: {headers['X-GitHub-Api-Version']}"]
    if _TOKEN:
        cmd.extend(["-H", f"Authorization: token {_TOKEN}"])
    cmd.append(url)

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0 or not result.stdout:
        print(f"  [WARN] curl {endpoint} failed: {result.stderr[:200]}")
        return None
    try:
        return _json.loads(result.stdout)
    except Exception as e:
        print(f"  [WARN] JSON parse error for {endpoint}: {e}")
        return None


def curl_text(url):
    """Fetch URL text via curl, strip tags, return clean text."""
    result = subprocess.run(
        ["curl", "-sL", "--max-time", "30", url],
        capture_output=True, text=True, timeout=45
    )
    raw = result.stdout
    if not raw:
        return f"[ERROR: curl returned empty content for {url}]"
    # Strip script/style blocks
    raw = re.sub(r'<script[^>]*>.*?</script>', '', raw, flags=re.DOTALL | re.IGNORECASE)
    raw = re.sub(r'<style[^>]*>.*?</style>', '', raw, flags=re.DOTALL | re.IGNORECASE)
    # Replace html entity &#39; etc and strip tags
    text = re.sub(r'<[^>]+>', ' ', raw)
    text = html.unescape(text)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def compute_sha256(body):
    """Compute SHA256 of the post-frontmatter body bytes (UTF-8, LF, final newline)."""
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def write_raw_file(filename, frontmatter_dict, body):
    """Write a raw Markdown file with frontmatter, body, and correct sha256 in frontmatter.
    Returns the computed sha256."""
    # First build frontmatter without sha256
    fm_lines = ["---"]
    for k, v in frontmatter_dict.items():
        if isinstance(v, list):
            fm_lines.append(f"{k}:")
            for item in v:
                fm_lines.append(f"  - {item}")
        elif isinstance(v, bool):
            fm_lines.append(f"{k}: {'true' if v else 'false'}")
        else:
            # Quote strings that contain special chars
            if isinstance(v, str) and any(c in v for c in [':', '#', '"', "'"]) and not v.startswith('"'):
                v = f'"{v}"'
            fm_lines.append(f"{k}: {v}")
    # Add sha256 placeholder
    fm_lines.append("sha256: PLACEHOLDER")
    fm_lines.append("---")
    frontmatter = "\n".join(fm_lines) + "\n"

    # Body should end with newline
    body_text = body
    if not body_text.endswith("\n"):
        body_text += "\n"

    # Compute sha256 over the post-frontmatter body
    sha = compute_sha256(body_text)

    # Replace placeholder
    frontmatter = frontmatter.replace("sha256: PLACEHOLDER", f"sha256: {sha}")

    full_content = frontmatter + body_text
    filepath = os.path.join(RAW_DIR, filename)
    with open(filepath, "w", encoding="utf-8", newline="\n") as f:
        f.write(full_content)

    print(f"  Written: {filepath} (sha256={sha[:16]}...)")
    return sha


# ======================================================================
# 1. GITHUB SEARCH API — ROS2 Drone repos (9 queries)
# ======================================================================
print("=" * 60)
print("[1/5] Collecting GitHub Search API data...")
print("=" * 60)

SEARCH_QUERIES = [
    "ros2 drone detection",
    "ros2 drone autonomous",
    "ros2 drone navigation",
    "PX4 ros2 bridge",
    "YOLO ros2 drone",
    "zenoh ros2 middleware",
    "MediaPipe ros2",
    "SLAM ros2 drone",
    "ArUco ros2 detection",
]

# Aggregate search results
all_query_results = {}
for q in SEARCH_QUERIES:
    encoded = q.replace(" ", "+")
    data = gh_api("search/repositories", {"q": encoded, "sort": "stars", "order": "desc", "per_page": "10"})
    if data:
        all_query_results[q] = data
        print(f"  Query '{q}': {data.get('total_count', 0)} repos found")
    else:
        all_query_results[q] = {"total_count": 0, "items": []}

# Build aggregated markdown (following 2026-08-14 format)
lines = []
lines.append(f"# ROS2 드론 관련 GitHub 저장소 검색 결과 ({DATE})")
lines.append("")
lines.append(f"수집 일시: {COLLECTED_AT}")
lines.append("수집 방법: GitHub Search API (per_page=10, sort=stars desc, 인증)")
lines.append("")
lines.append("## 1. 검색 쿼리 목록")
lines.append("")
lines.append("| # | 검색어 | 정렬 기준 | 결과 수 |")
lines.append("|---|--------|-----------|---------|")
for i, q in enumerate(SEARCH_QUERIES, 1):
    count = all_query_results.get(q, {}).get("total_count", 0)
    lines.append(f"| {i} | `{q}` | stars desc | {count}개 |")
lines.append("")

# Collect all repos for top-10 ranking (with dedup, keeping highest star count)
all_repos = {}
for q in SEARCH_QUERIES:
    items = all_query_results.get(q, {}).get("items", [])
    for item in items:
        full_name = item.get("full_name", "")
        if full_name and full_name not in all_repos:
            all_repos[full_name] = item
        elif full_name in all_repos:
            # Keep the one with more stars
            if item.get("stargazers_count", 0) > all_repos[full_name].get("stargazers_count", 0):
                all_repos[full_name] = item

# Sort by stars desc
sorted_repos = sorted(all_repos.values(), key=lambda x: x.get("stargazers_count", 0), reverse=True)
top_repos = sorted_repos[:10]

lines.append("## 2. 핵심 패키지 (GitHub ⭐ 기준 top 10)")
lines.append("")
lines.append("| 순위 | 저장소 | ⭐ | 언어 | 설명 | 최근 업데이트 |")
lines.append("|------|--------|----|------|------|---------------|")
for i, repo in enumerate(top_repos, 1):
    name = repo.get("full_name", "")
    stars = repo.get("stargazers_count", 0)
    lang = repo.get("language", "") or ""
    desc = (repo.get("description", "") or "").replace("|", "\\|").replace("\n", " ")
    updated = repo.get("pushed_at", "")[:10]
    lines.append(f"| {i} | {name} | {stars} | {lang} | {desc} | {updated} |")
lines.append("")

# Per-query detail
lines.append("## 3. 쿼리별 상세 결과")
lines.append("")

# Map queries to Korean section titles
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

for idx, q in enumerate(SEARCH_QUERIES, 1):
    title = query_titles.get(q, q)
    lines.append(f"### 3-{idx}. {title} (`{q}`)")
    lines.append("")
    lines.append("| 저장소 | ⭐ | 언어 | 설명 | 최근 업데이트 |")
    lines.append("|--------|----|------|------|---------------|")
    items = all_query_results.get(q, {}).get("items", [])
    for item in items[:10]:
        name = item.get("full_name", "")
        stars = item.get("stargazers_count", 0)
        lang = item.get("language", "") or ""
        desc = (item.get("description", "") or "").replace("|", "\\|").replace("\n", " ")
        updated = item.get("pushed_at", "")[:10]
        lines.append(f"| {name} | {stars} | {lang} | {desc} | {updated} |")
    lines.append("")

# Repository metadata for top 8
lines.append("## 4. 저장소 상세 메타데이터 (Top 8)")
lines.append("")
for i, repo in enumerate(top_repos[:8], 1):
    name = repo.get("full_name", "")
    owner = repo.get("owner", {}).get("login", "")
    stars = repo.get("stargazers_count", 0)
    created = repo.get("created_at", "")[:10]
    lang = repo.get("language", "") or ""
    topics = repo.get("topics", [])
    desc = repo.get("description", "") or ""
    homepage = repo.get("homepage", "") or ""
    license_info = repo.get("license", {})
    license_name = license_info.get("name", "None") if license_info else "None"
    default_branch = repo.get("default_branch", "main")
    html_url = repo.get("html_url", "")

    lines.append(f"### {i}. {name}")
    lines.append(f"- ⭐ {stars} | 생성: {created} | 언어: {lang}")
    if topics:
        lines.append(f"- 토픽: {', '.join(topics)}")
    lines.append(f"- 설명: {desc}")
    if homepage:
        lines.append(f"- 홈페이지: {homepage}")
    lines.append(f"- 라이선스: {license_name}")
    lines.append(f"- 기본 브랜치: {default_branch}")
    lines.append(f"- URL: {html_url}")
    lines.append("")

# Summary observations
lines.append("## 5. 종합 관측사항")
lines.append("")
total_unique = len(all_repos)
yolo_count = sum(1 for r in all_repos.values() if (r.get("description","") or "").lower().find("yolo") != -1 or any("yolo" in (t or "").lower() for t in r.get("topics",[])))
px4_count = sum(1 for r in all_repos.values() if (r.get("description","") or "").lower().find("px4") != -1 or any("px4" in (t or "").lower() for t in r.get("topics",[])))
aruco_count = sum(1 for r in all_repos.values() if (r.get("description","") or "").lower().find("aruco") != -1 or any("aruco" in (t or "").lower() for t in r.get("topics",[])))
slam_count = sum(1 for r in all_repos.values() if (r.get("description","") or "").lower().find("slam") != -1 or any("slam" in (t or "").lower() for t in r.get("topics",[])))
zenoh_count = sum(1 for r in all_repos.values() if (r.get("description","") or "").lower().find("zenoh") != -1 or any("zenoh" in (t or "").lower() for t in r.get("topics",[])))
mediapipe_count = sum(1 for r in all_repos.values() if (r.get("description","") or "").lower().find("mediapipe") != -1 or any("mediapipe" in (t or "").lower() for t in r.get("topics",[])))
swarm_count = sum(1 for r in all_repos.values() if (r.get("description","") or "").lower().find("swarm") != -1 or any("swarm" in (t or "").lower() for t in r.get("topics",[])))

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

body = "\n".join(lines)

frontmatter = {
    "source_url": "GitHub Search API (9 queries)",
    "ingested": DATE,
    "title": f"ROS2 드론 GitHub 검색 데이터 ({DATE})",
    "captured_via": "2nd-brain-cron",
    "search_queries": "9 queries, per_page=10, sort=stars desc",
}
write_raw_file(f"{DATE}-ros2-drone-github-data.md", frontmatter, body)


# ======================================================================
# 2. PX4 RELEASE NOTES (GitHub Releases API)
# ======================================================================
print("\n" + "=" * 60)
print("[2/5] Collecting PX4 release notes...")
print("=" * 60)

px4_releases = gh_api("repos/PX4/PX4-Autopilot/releases", {"per_page": "10"})

lines = []
lines.append(f"# PX4-Autopilot 릴리즈 노트 ({DATE})")
lines.append("")
lines.append(f"수집 일시: {COLLECTED_AT}")
lines.append("출처: https://api.github.com/repos/PX4/PX4-Autopilot/releases")
lines.append("")

if px4_releases:
    for release in px4_releases:
        name = release.get("name", "")
        tag = release.get("tag_name", "")
        date = release.get("published_at", "")[:10]
        prerelease = release.get("prerelease", False)
        draft = release.get("draft", False)
        body_text = release.get("body", "") or ""

        lines.append(f"## {tag}")
        lines.append("")
        lines.append(f"- 이름: {name or tag}")
        lines.append(f"- 날짜: {date}")
        lines.append(f"- 프리릴리즈: {str(prerelease).capitalize()}")
        lines.append(f"- 드래프트: {str(draft).capitalize()}")
        lines.append("")
        # Escape any pipe chars in body for markdown table safety; here it's block
        cleaned = body_text.replace("\r\n", "\n").strip()
        if cleaned:
            lines.append("```")
            lines.append(cleaned)
            lines.append("```")
        else:
            lines.append("(본문 없음)")
        lines.append("")
else:
    lines.append("[WARN: PX4 릴리즈 정보를 가져오지 못했습니다]")
    lines.append("")

body = "\n".join(lines)
frontmatter = {
    "source_url": "https://api.github.com/repos/PX4/PX4-Autopilot/releases",
    "ingested": DATE,
    "title": f"PX4 릴리즈 노트 ({DATE})",
    "captured_via": "2nd-brain-cron",
}
write_raw_file(f"{DATE}-px4-release-notes.md", frontmatter, body)


# ======================================================================
# 3. ARDUPILOT RELEASE NOTES (GitHub Releases API)
# ======================================================================
print("\n" + "=" * 60)
print("[3/5] Collecting ArduPilot release notes...")
print("=" * 60)

ardupilot_releases = gh_api("repos/ArduPilot/ardupilot/releases", {"per_page": "10"})

lines = []
lines.append(f"# ArduPilot 릴리즈 노트 ({DATE})")
lines.append("")
lines.append(f"수집 일시: {COLLECTED_AT}")
lines.append("출처: https://api.github.com/repos/ArduPilot/ardupilot/releases")
lines.append("")

if ardupilot_releases:
    for release in ardupilot_releases:
        name = release.get("name", "")
        tag = release.get("tag_name", "")
        date = release.get("published_at", "")[:10]
        prerelease = release.get("prerelease", False)
        draft = release.get("draft", False)
        body_text = release.get("body", "") or ""

        lines.append(f"## {tag}")
        lines.append("")
        lines.append(f"- 이름: {name or tag}")
        lines.append(f"- 날짜: {date}")
        lines.append(f"- 프리릴리즈: {str(prerelease).capitalize()}")
        lines.append(f"- 드래프트: {str(draft).capitalize()}")
        lines.append("")
        cleaned = body_text.replace("\r\n", "\n").strip()
        if cleaned:
            lines.append("```")
            lines.append(cleaned)
            lines.append("```")
        else:
            lines.append("(본문 없음)")
        lines.append("")
else:
    lines.append("[WARN: ArduPilot 릴리즈 정보를 가져오지 못했습니다]")
    lines.append("")

body = "\n".join(lines)
frontmatter = {
    "source_url": "https://api.github.com/repos/ArduPilot/ardupilot/releases",
    "ingested": DATE,
    "title": f"ArduPilot 릴리즈 노트 ({DATE})",
    "captured_via": "2nd-brain-cron",
}
write_raw_file(f"{DATE}-ardupilot-release-notes.md", frontmatter, body)


# ======================================================================
# 4. PX4 DOCS (docs.px4.io)
# ======================================================================
print("\n" + "=" * 60)
print("[4/5] Collecting PX4 docs...")
print("=" * 60)

px4_urls = [
    ("PX4 Autopilot User Guide (Main)", "https://docs.px4.io/main/en/"),
    ("uXRCE-DDS (PX4-ROS 2/DDS Bridge)", "https://docs.px4.io/main/en/middleware/uxrce_dds.html"),
    ("Computer Vision (Optical Flow, MoCap, VIO, Avoidance)", "https://docs.px4.io/main/en/computer_vision/"),
    ("PX4 Main Release Notes", "https://docs.px4.io/main/en/releases/main.html"),
    ("ROS 2 Interface (px4_ros_com)", "https://docs.px4.io/main/en/ros2/"),
    ("Zenoh Middleware", "https://docs.px4.io/main/en/middleware/zenoh.html"),
    ("Computer Vision Overview", "https://docs.px4.io/main/en/computer_vision/overview.html"),
]

lines = []
lines.append(f"# PX4 공식 문서 수집 ({DATE})")
lines.append("")
lines.append(f"수집 일시: {COLLECTED_AT}")
lines.append("수집 방법: docs.px4.io/main/en/ (curl + HTML 텍스트 추출, 2nd-brain-cron)")
lines.append("")

for title, url in px4_urls:
    lines.append(f"## {title} ({url})")
    lines.append("")
    text = curl_text(url)
    if text.startswith("[ERROR:"):
        lines.append(text)
    else:
        lines.append(text[:5000])
    lines.append("")

body = "\n".join(lines)
frontmatter = {
    "source_url": "https://docs.px4.io/main/en/",
    "ingested": DATE,
    "title": f"PX4 공식 문서 수집 ({DATE})",
    "captured_via": "2nd-brain-cron",
    "pages": "main, uxrce_dds, computer_vision, releases/main, ros2, zenoh",
}
write_raw_file(f"{DATE}-px4-docs.md", frontmatter, body)


# ======================================================================
# 5. ROS2 DOCS (docs.ros.org)
# ======================================================================
print("\n" + "=" * 60)
print("[5/5] Collecting ROS2 docs...")
print("=" * 60)

ros2_urls = [
    ("ROS 2 문서 메인 (Rolling)", "https://docs.ros.org/en/rolling/"),
    ("About ROS", "https://docs.ros.org/en/rolling/Get-Started/About-ROS/About-ROS.html"),
    ("설치 (Installation)", "https://docs.ros.org/en/rolling/Get-Started/Installation.html"),
    ("Ubuntu Debian Installation", "https://docs.ros.org/en/rolling/Installation/Installing-ROS2-From-Debr.html"),
    ("ROS 2 Concepts", "https://docs.ros.org/en/rolling/Concepts/About-ROS-2-Architecture.html"),
    ("ROS 2 Communication (QoS)", "https://docs.ros.org/en/rolling/Concepts/Basic/Quality-of-Service.html"),
    ("Navigation 2 (Nav2)", "https://docs.ros.org/en/rolling/Tutorials/Navigation-on-ROS2.html"),
]

lines = []
lines.append(f"# ROS2 공식 문서 수집 ({DATE})")
lines.append("")
lines.append(f"수집 일시: {COLLECTED_AT}")
lines.append("수집 방법: docs.ros.org/en/rolling/ (curl + HTML 텍스트 추출, 2nd-brain-cron)")
lines.append("")

for title, url in ros2_urls:
    lines.append(f"## {title} ({url})")
    lines.append("")
    text = curl_text(url)
    if text.startswith("[ERROR:"):
        lines.append(text)
    else:
        lines.append(text[:5000])
    lines.append("")

body = "\n".join(lines)
frontmatter = {
    "source_url": "https://docs.ros.org/en/rolling/",
    "ingested": DATE,
    "title": f"ROS2 공식 문서 수집 ({DATE})",
    "captured_via": "2nd-brain-cron",
    "pages": "main, About-ROS, Installation, Concepts, QoS, Nav2",
}
write_raw_file(f"{DATE}-ros2-docs.md", frontmatter, body)

print("\n" + "=" * 60)
print("Collection complete!")
print("=" * 60)
print(f"Files saved to: {RAW_DIR}")
print(f"Date: {DATE}")
