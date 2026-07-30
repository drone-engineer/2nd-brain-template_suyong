#!/usr/bin/env python3
"""
daily-youtube-scout.py — 매일 아침 Hunter-Killer 계열 YouTube 기술 보강.

용도:
  - YouTube에서 지정 키워드로 최신 영상 검색
  - 메타데이터 + 자막(있으면) 추출 → raw/youtube/ 에 저장
  - Hunter-Killer 계열 canonical 페이지(hunter-killer-drone-system,
    uav-swarm-defensive-countermeasures, gnss-denied-autonomous-navigation,
    hunter-killer-kill-chain) 중 보강 필요 부분에 링크/요약 추가
  - 발견된 영상 목록을 stdout으로 출력 (크론이 텔레그램 리포트에 사용)

실제 검색은 yt-dlp + youtube_transcript_api 사용.
네트워크 실패 시 조용히 빈 결과 반환 (크론이 멈추지 않게).
"""
import json, sys, os, hashlib, re, time, urllib.parse
from pathlib import Path
from datetime import datetime, timezone, timedelta

WIKI = Path(__file__).resolve().parents[2]
RAW_YT = WIKI / "raw" / "youtube"
RAW_YT.mkdir(parents=True, exist_ok=True)

# KST = UTC+9
KST = timezone(timedelta(hours=9))
TODAY = datetime.now(KST).strftime("%Y-%m-%d")

QUERY_TERMS = [
    "Hunter Killer drone autonomous",
    "swarm drone kill chain",
    "GNSS denied navigation drone",
    "drone terminal homing",
    "counter-UAS swarm",
]

# 보강 대상 canonical 페이지 (헌터 킬러 계열)
TARGET_PAGES = [
    "entities/hunter-killer-drone-system.md",
    "concepts/uav-swarm-defensive-countermeasures.md",
    "concepts/gnss-denied-autonomous-navigation.md",
    "queries/hunter-killer-kill-chain.md",
]


def yt_search(query, max_results=3):
    """yt-dlp로 YouTube 검색 메타데이터 추출."""
    import yt_dlp
    out = []
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": "in_playlist",
        "dump_single_json": True,
        "skip_download": True,
        "default_search": "ytsearch",
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)
        for e in (info.get("entries") or []):
            if not e:
                continue
            out.append({
                "id": e.get("id"),
                "title": e.get("title"),
                "uploader": e.get("uploader"),
                "url": f"https://youtu.be/{e.get('id')}",
                "duration": e.get("duration"),
                "view_count": e.get("view_count"),
                "published": e.get("upload_date"),
            })
    except Exception as ex:
        sys.stderr.write(f"search fail {query}: {ex}\n")
    return out


def fetch_caption(vid):
    """자막 있으면 텍스트 추출 (없으면 빈 문자열)."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        segs = YouTubeTranscriptApi.get_transcript(vid, languages=["en", "ko"])
        return " ".join(s.get("text", "") for s in segs)
    except Exception:
        return ""


def save_raw(vid, meta, caption):
    fn = f"{TODAY}-{vid}.md"
    body = f"""---
title: {meta['title']}
channel: {meta.get('uploader')}
url: {meta['url']}
published: {meta.get('published')}
duration_s: {meta.get('duration')}
views: {meta.get('view_count')}
collected: {TODAY}
source_type: youtube
---

# {meta['title']}

- 채널: {meta.get('uploader')}
- URL: {meta['url']}
- 업로드: {meta.get('published')}
- 조회수: {meta.get('view_count')}
- 길이(초): {meta.get('duration')}
- 수집: {TODAY} (매일 YouTube 스카우트 — Hunter-Killer 계열)

## 자막/설명 요약
{caption[:4000] if caption else '(자막 없음)'}

---
*raw evidence — immutable. YouTube 캡처.*
"""
    p = RAW_YT / fn
    # [동작] Gate B와 동일하게 closing --- 이후 본문만 sha256.
    # [이유] 예전엔 파일 전체를 해시해 FM에 넣은 뒤 다시 FM을 고쳐 mismatch가 났음.
    # [근거] docs/workflow/check-gate-b.py — body = after first \n---\n following opening FM.
    data = body.encode("utf-8")
    end = data.find(b"\n---\n", 4)
    if end < 0:
        raise ValueError(f"frontmatter closing --- missing for {fn}")
    payload = data[end + 5 :]
    digest = hashlib.sha256(payload).hexdigest()
    # Insert sha256 into FM before writing once (avoid rewrite that invalidates a whole-file hash).
    text = body.replace(f"collected: {TODAY}", f"collected: {TODAY}\nsha256: {digest}", 1)
    p.write_text(text, encoding="utf-8")
    return str(p.relative_to(WIKI))


def main():
    results = []
    seen = set()
    for q in QUERY_TERMS:
        vids = yt_search(q, max_results=3)
        for v in vids:
            if not v.get("id") or v["id"] in seen:
                continue
            seen.add(v["id"])
            cap = fetch_caption(v["id"])
            raw_path = save_raw(v["id"], v, cap)
            results.append({"meta": v, "raw": raw_path})
        time.sleep(2)
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
