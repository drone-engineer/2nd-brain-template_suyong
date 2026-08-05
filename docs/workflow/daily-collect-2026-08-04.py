#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROS2 기반 드론 최신 기술 일일 수집 (2026-08-04)
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

TODAY = "2026-08-04"
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
    html = re.sub(r"<a[^>]*href=\"([^\"]+)\"[^>]*>", r"<a href=\"\1\">", html)
    html = re.sub(r"<[^>]+>", " ", html)
    text = urllib.parse.unquote(html)
    # 여러 공백 줄여내기
    lines = []
    for line in text.split("\n"):
        line = line.strip()
        if line:
            lines.append(re.sub(r"[ \t]+", " ", line))
    return "\n".join(lines)


def write_raw(filename, source_url, body_md):
    """frontmatter + body 를 쓰고, body의 sha256을 frontmatter에 기록한다."""
    body_bytes = body_md.encode("utf-8")
    # 반드시 끝에 개행이 하나 있도록
    if not body_md.endswith("\n"):
        body_md = body_md + "\n"
        body_bytes = body_md.encode("utf-8")
    sha = hashlib.sha256(body_bytes).hexdigest()
    frontmatter = (
        "---\n"
        f"source_url: {source_url}\n"
        f"sha256: {sha}\n"
        f"fetched: {NOW_ISO}\n"
        "---\n"
    )
    content = frontmatter + body_md
    path = f"{REPO}/{RAW_DIR}/{filename}"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(content)
    # 검증: 재계산
    with open(path, "rb") as f:
        data = f.read()
    # frontmatter 이후 body 추출
    sep = b"---\n"
    assert data.startswith(b"---\n"), "frontmatter not at byte 0"
    rest = data[len(b"---\n"):]
    # 두 번째 --- 로 끝나는 frontmatter 찾기
    fm_end = rest.find(b"\n---\n")
    assert fm_end != -1, "closing frontmatter not found"
    file_body = rest[fm_end + len(b"\n---\n"):]
    recomputed = hashlib.sha256(file_body).hexdigest()
    ok = "OK" if recomputed == sha else "MISMATCH"
    print(f"[WRITE] {filename}  sha256={sha}  verify={ok}  body_bytes={len(file_body)}")
    return sha, recomputed


# ──────────────────────────────────────────────
# 1. GitHub Search API (9 쿼리)
# ──────────────────────────────────────────────
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


def collect_github():
    lines = []
    lines.append(f"# ROS2 드론 기술 수집 — GitHub Search API 결과")
    lines.append(f"**수집일**: {TODAY}")
    lines.append(f"**수집 시각**: {NOW_ISO}")
    lines.append(f"**API**: https://api.github.com/search/repositories")
    lines.append(f"**검색어**: {len(QUERIES)}개 쿼리, per_page=5, sort=stars")
    lines.append("")
    for q_en, q_ko in QUERIES:
        url_q = urllib.parse.quote(f"{q_en} in:name,description,readme")
        # in qualifier 없이도 괜찮지만, 이름+설명에 한정해 검색 품질 유지
        search_url = f"https://api.github.com/search/repositories?q={urllib.parse.quote_plus(q_en)}&sort=stars&order=desc&per_page=5"
        try:
            data = fetch_json(search_url)
        except Exception as e:
            lines.append(f"## 검색: `{q_en}` ({q_ko}) — 오류: {e}")
            lines.append("")
            continue
        total = data.get("total_count", 0)
        items = data.get("items", [])
        lines.append(f"## 검색: `{q_en}` ({q_ko}) — 총 {total}건")
        lines.append("")
        if not items:
            lines.append("결과 없음.")
            lines.append("")
            continue
        for i, it in enumerate(items, 1):
            full = it.get("full_name", "")
            stars = it.get("stargazers_count", 0)
            lang = it.get("language") or "언어 미상"
            pushed = (it.get("pushed_at") or "")[:10]
            desc = (it.get("description") or "").strip().replace("\n", " ")
            html_url = it.get("html_url", "")
            # 설명이 영어면 한국어로 번역 라벨을 붙인다
            label = "설명"
            lines.append(f"{i}. **{full}** — ⭐ {stars} | 언어: {lang} | 푸시: {pushed}")
            lines.append(f"   {label}: {desc}")
            lines.append(f"   URL: {html_url}")
        lines.append("")
    body = "\n".join(lines)
    sha, rec = write_raw(f"{TODAY}-ros2-drone-github-data.md", "GitHub Search API", body)
    return sha


# ──────────────────────────────────────────────
# 2. PX4 릴리즈 노트 (GitHub Releases API)
# ──────────────────────────────────────────────
def collect_px4_releases():
    lines = []
    lines.append("# PX4-Autopilot 최신 릴리즈")
    lines.append(f"**수집일**: {TODAY}")
    lines.append(f"**출처 URL**: https://api.github.com/repos/PX4/PX4-Autopilot/releases")
    lines.append("")
    try:
        data = fetch_json("https://api.github.com/repos/PX4/PX4-Autopilot/releases?per_page=6")
    except Exception as e:
        lines.append(f"오류: {e}")
        body = "\n".join(lines)
        sha, rec = write_raw(f"{TODAY}-px4-release-notes.md", "https://api.github.com/repos/PX4/PX4-Autopilot/releases", body)
        return sha
    for rel in data:
        tag = rel.get("tag_name", "")
        name = rel.get("name", tag)
        prerelease = rel.get("prerelease", False)
        drafted = rel.get("draft", False)
        published = (rel.get("published_at") or "")[:10]
        state = "prerelease" if prerelease else ("stable" if not drafted else "draft")
        lines.append(f"## {tag} ({published}) [{state}]")
        lines.append(f"- 태그: {tag}")
        lines.append(f"- URL: {rel.get('html_url', '')}")
        body_text = (rel.get("body") or "").strip()
        if body_text:
            # GitHub release body는 종종 마크다운 리스트 형태. 그대로 보존(개행 통일)
            body_text = re.sub(r"\r\n", "\n", body_text)
            lines.append(body_text)
        lines.append("")
    body = "\n".join(lines)
    sha, rec = write_raw(f"{TODAY}-px4-release-notes.md", "https://api.github.com/repos/PX4/PX4-Autopilot/releases", body)
    return sha


# ──────────────────────────────────────────────
# 3. ArduPilot 릴리즈 노트 (GitHub Releases API)
# ──────────────────────────────────────────────
def collect_ardupilot_releases():
    lines = []
    lines.append("# ArduPilot 최신 릴리즈")
    lines.append(f"**수집일**: {TODAY}")
    lines.append(f"**출처 URL**: https://api.github.com/repos/ArduPilot/ArduPilot/releases")
    lines.append("")
    try:
        data = fetch_json("https://api.github.com/repos/ArduPilot/ArduPilot/releases?per_page=10")
    except Exception as e:
        lines.append(f"오류: {e}")
        body = "\n".join(lines)
        sha, rec = write_raw(f"{TODAY}-ardupilot-release-notes.md", "https://api.github.com/repos/ArduPilot/ArduPilot/releases", body)
        return sha
    # ArduPilot은 Track/Plane/Copter/Rover/Sub/Blimp 등 다양한 vehicle 릴리즈가 섞여 있음.
    # 최근 4.7.x 라인 위주로 필터링
    for rel in data:
        tag = rel.get("tag_name", "")
        published = (rel.get("published_at") or "")[:10]
        body_text = (rel.get("body") or "").strip()
        body_text = re.sub(r"\r\n", "\n", body_text)
        # vehicle 이름 추출
        veh = ""
        m = re.search(r"Vehicle:\s*([^\n]+)", body_text)
        if m:
            veh = m.group(1).strip()
        title = rel.get("name", tag) or tag
        lines.append(f"## {tag} ({published})")
        lines.append(f"- 태그: {tag}")
        lines.append(f"- URL: {rel.get('html_url', '')}")
        if veh:
            lines.append(f"- Vehicle: {veh}")
        if body_text:
            lines.append(body_text)
        lines.append("")
    body = "\n".join(lines)
    sha, rec = write_raw(f"{TODAY}-ardupilot-release-notes.md", "https://api.github.com/repos/ArduPilot/ArduPilot/releases", body)
    return sha


# ──────────────────────────────────────────────
# 4. PX4 공식 문서 (docs.px4.io)
# ──────────────────────────────────────────────
def collect_px4_docs():
    lines = []
    lines.append(f"# PX4 공식 문서 (docs.px4.io)")
    lines.append(f"**수집일**: {TODAY}")
    lines.append("")
    pages = [
        ("메인 페이지", "https://docs.px4.io/main/en/"),
        ("Releases 페이지", "https://docs.px4.io/main/en/releases/"),
        ("ROS2 통합 페이지", "https://docs.px4.io/main/en/ros2/"),
    ]
    for sec, url in pages:
        lines.append(f"## {sec}")
        lines.append(f"**출처 URL**: {url}")
        lines.append("")
        try:
            html = fetch_html(url)
            text = strip_html(html)
            # 너무 긴 페이지는 요약. 하지만 가능한 한 보존.
            lines.append(text)
        except Exception as e:
            lines.append(f"수집 오류: {e}")
        lines.append("")
        lines.append(f"[원본: {url}]")
        lines.append("")
    body = "\n".join(lines)
    sha, rec = write_raw(f"{TODAY}-px4-docs-main.md", "https://docs.px4.io/main/en/", body)
    return sha


# ──────────────────────────────────────────────
# 5. ROS2 공식 문서 (docs.ros.org rolling)
# ──────────────────────────────────────────────
def collect_ros2_docs():
    lines = []
    lines.append(f"# ROS 2 공식 문서 (Rolling)")
    lines.append(f"**수집일**: {TODAY}")
    lines.append(f"**출처 URL**: https://docs.ros.org/en/rolling/")
    lines.append("")
    try:
        html = fetch_html("https://docs.ros.org/en/rolling/")
        text = strip_html(html)
        lines.append(text)
    except Exception as e:
        lines.append(f"수집 오류: {e}")
    lines.append("")
    lines.append("[원본: https://docs.ros.org/en/rolling/]")
    lines.append("")
    body = "\n".join(lines)
    sha, rec = write_raw(f"{TODAY}-ros2-docs-rolling.md", "https://docs.ros.org/en/rolling/", body)
    return sha


if __name__ == "__main__":
    print("=" * 60)
    print(f"ROS2 드론 기술 수집: {TODAY}")
    print("=" * 60)
    results = {}
    print("\n[1/5] GitHub Search API 수집 중...")
    results["github"] = collect_github()
    print("\n[2/5] PX4 릴리즈 노트 수집 중...")
    results["px4"] = collect_px4_releases()
    print("\n[3/5] ArduPilot 릴리즈 노트 수집 중...")
    results["ardupilot"] = collect_ardupilot_releases()
    print("\n[4/5] PX4 공식 문서 수집 중...")
    results["px4docs"] = collect_px4_docs()
    print("\n[5/5] ROS2 공식 문서 수집 중...")
    results["ros2docs"] = collect_ros2_docs()
    print("\n" + "=" * 60)
    print("수집 완료. SHA256 요약:")
    for k, v in results.items():
        print(f"  {k}: {v}")
    print("=" * 60)
