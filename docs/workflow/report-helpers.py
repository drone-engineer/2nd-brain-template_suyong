#!/usr/bin/env python3
"""report-helpers.py — 크론 리포트 개선 헬퍼.

용도:
  1. raw/articles/INDEX.md 자동 갱신 (파일명↔제목 매핑) → 깃허브에서 파일 찾기 쉬움
  2. 수집된 논문 목록을 Telegram 리포트용 텍스트로 포맷 (한글 요약은 에이전트가 채움)

실제 한글 번역 요약은 Hermes Agent(LLM)가 초록을 읽고 생성한다. 이 스크립트는
인덱스 생성과 리포트 템플릿 조립만 담당한다.
"""
from __future__ import annotations
import re, glob, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "raw" / "articles"


def rebuild_index() -> int:
    """raw/articles/INDEX.md 재생성. 반환값: 총 편수."""
    rows = []
    for f in sorted(ART.glob("*.md")):
        if f.name == "INDEX.md":
            continue
        t = f.read_text(encoding="utf-8", errors="ignore")
        title = re.search(r"^title:\s*(.+)$", t, re.M)
        m = re.match(r"^(\d{4})-", f.name)
        rows.append((m.group(1) if m else "????", f.name,
                     title.group(1).strip() if title else "(no title)"))
    d = defaultdict(list)
    for y, f, ti in rows:
        d[y].append((f, ti))
    out = ["# Raw Articles Index", "",
           f"> 자동 생성(수집 시 갱신). 파일명 ↔ 제목 매핑. 총 {len(rows)}편\n\n"]
    for y in sorted(d.keys()):
        out.append(f"## {y} ({len(d[y])}편)\n")
        for f, ti in d[y]:
            out.append(f"- `{f}` — {ti}")
        out.append("")
    (ROOT / "docs" / "workflow" / "raw-articles-index.md").write_text("\n".join(out), encoding="utf-8")
    return len(rows)


def format_report_collected(items: list[dict]) -> str:
    """Telegram 보고서용 텍스트 생성."""
    lines = []
    for it in items:
        lines.append(f"## [{it['name']}]({it.get('url', '?')})")
        lines.append(f"   설명: {it.get('desc', '?')}")
        lines.append(f"   언어: {it.get('lang', '?')}")
        lines.append(f"   푸시: {it.get('pushed_at', '?')}")
        lines.append(f"   이슈: {it.get('issues', '?')}")
        lines.append(f"   생성: {it.get('created_at', '?')}")
        lines.append(f"   └ 파일: `raw/articles/{it.get('file','?')}`")
        lines.append("")
    lines.append("👉 판정: review-queue.md에서 Accepted/Rejected 선택")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "index":
        n = rebuild_index()
        print(f"INDEX rebuilt: {n} entries")
    else:
        print("usage: report-helpers.py index")
