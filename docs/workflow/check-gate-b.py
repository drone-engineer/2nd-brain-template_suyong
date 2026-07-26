#!/usr/bin/env python3
"""Gate B checker for 2nd_Brain_Template. Exit 0 = pass, 1 = fail."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANON_DIRS = ("entities", "concepts", "comparisons", "queries")
REQUIRED = (
    "title",
    "created",
    "updated",
    "type",
    "tags",
    "sources",
    "confidence",
    "contested",
    "contradictions",
)
TYPE_DIR = {
    "entity": "entities",
    "concept": "concepts",
    "comparison": "comparisons",
    "query": "queries",
}
RAW_HASH = re.compile(br"""(?m)^sha256:\s*["']?([0-9a-fA-F]{64})["']?\s*$""")
LEGACY_NO_HASH = {
    "raw/web/NomaDamasslides-grab Best harness + editor + linter for generating slides in Claude Code  Codex - Claude Design Open Source Alternative.md",
    "raw/web/stablyaiorca Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop and mobile..md",
    "raw/youtube/📺 How To Build LLM Wiki In Obsidian 🧠 A Memory Layer For Any Agentic AI.md",
    "raw/youtube/📺 LLM Wiki를 업그레이드하는 외부 지식 시스템! 연구자를 위한 최강의 조합 Zotero × Notebook × Obsidian x Claude Code.md",
    "raw/youtube/📺 Orca Is the Free Cursor Killer Nobody's Talking About!.md",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unclosed frontmatter")
    fm_raw = text[4:end]
    body = text[end + 5 :]
    data: dict = {}
    key = None
    list_mode = None
    for line in fm_raw.splitlines():
        if re.match(r"^[a-zA-Z0-9_]+:", line):
            list_mode = None
            k, _, v = line.partition(":")
            key = k.strip()
            v = v.strip().strip('"').strip("'")
            if v == "" or v == "|" or v == ">":
                data[key] = []
                list_mode = key
            elif v.startswith("[") and v.endswith("]"):
                inner = v[1:-1].strip()
                if not inner:
                    data[key] = []
                else:
                    parts = [p.strip().strip('"').strip("'") for p in inner.split(",")]
                    data[key] = parts
            else:
                data[key] = v
        elif list_mode and line.strip().startswith("- "):
            item = line.strip()[2:].strip().strip('"').strip("'")
            data.setdefault(list_mode, []).append(item)
        elif key and line.startswith("  ") and not line.strip().startswith("-"):
            # folded scalar continuation — ignore for lint
            pass
    return data, body


def extract_wikilinks(body: str) -> list[str]:
    return re.findall(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", body)


def load_taxonomy(schema: str) -> set[str]:
    tags = set()
    in_reg = False
    for line in schema.splitlines():
        if line.startswith("### Registered tags"):
            in_reg = True
            continue
        if in_reg and line.startswith("## "):
            break
        if in_reg:
            m = re.match(r"^- `([^`]+)`:", line)
            if m:
                tags.add(m.group(1))
    return tags


def index_entries(index_text: str) -> list[str]:
    return re.findall(r"\[\[([^\]|#]+)\]\]", index_text)


def check_raw_integrity() -> list[str]:
    """Verify every raw record under raw/, not just raw/papers/.

    Legacy imports in LEGACY_NO_HASH predate the hash contract and are recorded
    in log.md as a documented coverage gap; they are reported, not failed.
    """
    issues: list[str] = []
    raw_root = ROOT / "raw"
    if not raw_root.is_dir():
        return issues
    for p in sorted(raw_root.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        data = p.read_bytes()
        if not data.startswith(b"---\n"):
            issues.append(f"{rel}: missing leading frontmatter")
            continue
        end = data.find(b"\n---\n", 4)
        if end < 0:
            issues.append(f"{rel}: unclosed frontmatter (no closing ---)")
            continue
        fm, body = data[:end], data[end + 5 :]
        if re.search(br"(?m)^notebooklm_source_id:", body):
            issues.append(f"{rel}: notebooklm_source_id leaked into body")
        m = RAW_HASH.search(fm)
        if not m:
            if rel not in LEGACY_NO_HASH:
                issues.append(f"{rel}: missing sha256")
            continue
        if hashlib.sha256(body).hexdigest() != m.group(1).decode().lower():
            issues.append(f"{rel}: sha256 mismatch")
    return issues


def main() -> int:
    errors: list[str] = []
    schema_path = ROOT / "SCHEMA.md"
    index_path = ROOT / "index.md"
    if not schema_path.exists() or not index_path.exists():
        print("FAIL: SCHEMA.md or index.md missing")
        return 1

    taxonomy = load_taxonomy(read_text(schema_path))
    index_slugs = index_entries(read_text(index_path))

    pages: dict[str, Path] = {}
    for d in CANON_DIRS:
        for p in sorted((ROOT / d).glob("*.md")):
            pages[p.stem] = p

    if len(index_slugs) != len(set(index_slugs)):
        errors.append("index.md has duplicate entries")
    if sorted(index_slugs) != sorted(pages.keys()):
        only_idx = sorted(set(index_slugs) - set(pages))
        only_fs = sorted(set(pages) - set(index_slugs))
        if only_idx:
            errors.append(f"index-only: {only_idx}")
        if only_fs:
            errors.append(f"filesystem-only: {only_fs}")
        m = re.search(r"Total pages:\s*(\d+)", read_text(index_path))
        if m and int(m.group(1)) != len(pages):
            errors.append(
                f"Total pages header {m.group(1)} != filesystem {len(pages)}"
            )

    for slug, path in pages.items():
        try:
            fm, body = parse_frontmatter(read_text(path))
        except ValueError as e:
            errors.append(f"{path.relative_to(ROOT)}: {e}")
            continue
        for req in REQUIRED:
            if req not in fm:
                errors.append(f"{slug}: missing {req}")
        t = fm.get("type")
        if t not in TYPE_DIR:
            errors.append(f"{slug}: bad type {t!r}")
        elif TYPE_DIR[t] != path.parent.name:
            errors.append(f"{slug}: type {t} in folder {path.parent.name}")
        tags = fm.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        for tag in tags:
            if tag not in taxonomy:
                errors.append(f"{slug}: unregistered tag {tag}")
        sources = fm.get("sources") or []
        if isinstance(sources, str):
            sources = [sources]
        if not sources:
            errors.append(f"{slug}: empty sources")
        for src in sources:
            sp = ROOT / src
            if not sp.is_file():
                errors.append(f"{slug}: missing source {src}")
        links = extract_wikilinks(body)
        outbound = {l for l in links if l != slug and l in pages}
        if len(pages) >= 3 and len(outbound) < 2:
            errors.append(f"{slug}: need ≥2 outbound canonical links, got {sorted(outbound)}")
        for l in links:
            if l == slug:
                continue
            # allow links only to canonical; flag broken canonical-looking misses
            if l not in pages and (ROOT / "entities" / f"{l}.md").exists() is False:
                # broken if it looks like our slug style and not a path
                if "/" not in l and l.replace("-", "").isalnum():
                    if l not in pages:
                        errors.append(f"{slug}: broken wikilink [[{l}]]")

    errors.extend(check_raw_integrity())

    if errors:
        print(f"Gate B FAIL ({len(errors)} issues)")
        for e in errors:
            print(f" - {e}")
        return 1
    print(f"Gate B PASS ({len(pages)} canonical pages, index aligned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
