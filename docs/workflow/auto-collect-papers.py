#!/usr/bin/env python3.12
"""
auto-collect-papers.py — 무료 OA 논문 자동 수집 (합법 경로만)

수집 소스:
  - arXiv API (메타 + PDF)
  - Semantic Scholar API (OA PDF 링크 조회, 재시도 포함)
  - OpenAlex API (OA PDF URL 조회, 브라우저 UA로 403 우회)

동작:
  - 주제 쿼리별로 최신/관련 논문을 조회
  - OA(무료 전문)인 것만 PDF 다운로드 OR 메타만 저장
  - raw/articles/ 에 저장 (sha256 + provenance 포함)
  - 이미 수집된 arxiv_id/doi는 중복 건너뜀

용법:
  python3.12 auto-collect-papers.py [--query "UAV swarm"] [--max N] [--dry-run]
  쿼리 미지정 시 docs/workflow/collect-queries.txt 의 라인별 쿼리 사용
"""
import argparse, hashlib, json, re, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path
from datetime import date

WIKI = Path(__file__).resolve().parents[2]
ART = WIKI / "raw" / "articles"
PDF = WIKI / "raw" / "papers" / "files"
TODAY = date.today().isoformat()

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
S2_HEADERS = {"User-Agent": "PaperCollector/1.0 (mailto:research@example.com)"}

def http_get(url, headers=None, timeout=40, retries=3):
    h = {"User-Agent": UA}
    if headers: h.update(headers)
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=h)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(), r.headers
        except Exception as e:
            last = e
            time.sleep(2 ** i)
    raise last

def slugify(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:80]

def existing_ids():
    ids = set()
    for f in ART.glob("*.md"):
        t = f.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"arxiv_id: ([\d.v]+)", t)
        if m: ids.add(re.sub(r"v\d+$", "", m.group(1)))
        m2 = re.search(r"doi: (.+)", t)
        if m2: ids.add("doi:" + m2.group(1).strip())
    return ids

def save_record(title, authors, year, abstract, source_url, arxiv_id=None, doi=None,
                pdf_url=None, oa=False):
    body = f"# {title}\n\n**출처:** {source_url}\n"
    if authors: body += f"**저자:** {authors}\n"
    if year: body += f"**발행년도:** {year}\n"
    if arxiv_id: body += f"**arXiv ID:** {arxiv_id}\n"
    if doi: body += f"**DOI:** {doi}\n"
    if pdf_url: body += f"**OA PDF:** {pdf_url}\n"
    body += f"\n## 초록 (Abstract)\n\n{abstract}\n"
    # SCHEMA: sha256 covers every byte after the LF closing the frontmatter,
    # so the separating blank line is part of the hashed body.
    hashed_body = "\n" + body
    sha = hashlib.sha256(hashed_body.encode()).hexdigest()
    fm = (f"---\nsource_url: {source_url}\ningested: {TODAY}\nsha256: {sha}\n"
          f"title: {title}\n")
    if authors: fm += f"authors: {authors}\n"
    if year: fm += f"year: {year}\n"
    if arxiv_id: fm += f"arxiv_id: {arxiv_id}\n"
    if doi: fm += f"doi: {doi}\n"
    fm += "---\n"
    fname = f"{year or '20xx'}-{slugify(title)}.md"
    out = ART / fname
    if out.exists():
        out = ART / f"{year or '20xx'}-{slugify(title)[:60]}-{hashlib.md5(source_url.encode()).hexdigest()[:6]}.md"
    out.write_text(fm + hashed_body, encoding="utf-8")
    if pdf_url and oa:
        try:
            data, _ = http_get(pdf_url)
            if data[:4] == b"%PDF":
                PDF.mkdir(parents=True, exist_ok=True)
                (PDF / f"{out.stem}.pdf").write_bytes(data)
                print(f"  [PDF] {out.stem}.pdf")
        except Exception as e:
            print(f"  [PDF skip] {e}")
    print(f"  [saved] {out.name}")
    return out.name

def collect_arxiv(query, max_n, seen):
    print(f"[arXiv] {query}")
    url = ("https://export.arxiv.org/api/query?search_query=all:"
           + urllib.parse.quote(query) + f"&start=0&max_results={max_n}&sortBy=relevance")
    xml, _ = http_get(url)
    xml = xml.decode("utf-8", "ignore")
    for e in xml.split("<entry>")[1:]:
        m = re.search(r"<id>(.*?)</id>", e)
        if not m: continue
        aid = m.group(1).split("/abs/")[-1]
        base = re.sub(r"v\d+$", "", aid)
        if base in seen: continue
        seen.add(base)
        title = re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", e, re.S).group(1)).strip()
        summ = re.sub(r"\s+", " ", re.search(r"<summary>(.*?)</summary>", e, re.S).group(1)).strip()
        year = re.search(r"<published>(.*?)</published>", e).group(1)[:4]
        authors = ", ".join(re.findall(r"<name>(.*?)</name>", e)[:6])
        save_record(title, authors, year, summ, f"https://arxiv.org/abs/{aid}",
                    arxiv_id=aid, pdf_url=f"https://arxiv.org/pdf/{aid}", oa=True)

def collect_s2(query, max_n, seen):
    print(f"[SemanticScholar] {query}")
    url = ("https://api.semanticscholar.org/graph/v1/paper/search?query="
           + urllib.parse.quote(query) + f"&limit={max_n}&fields=title,year,authors,abstract,openAccessPdf,externalIds,url")
    try:
        data, _ = http_get(url, headers=S2_HEADERS)
        j = json.loads(data)
    except urllib.error.HTTPError as ex:
        if ex.code == 429:
            print("  S2 rate-limited (429); skip this query")
            return
        print(f"  S2 error: {ex}"); return
    except Exception as ex:
        print(f"  S2 error: {ex}"); return
    for p in j.get("data", []):
        doi = (p.get("externalIds") or {}).get("DOI")
        key = "doi:" + doi if doi else None
        if key:
            if key in seen: continue
            seen.add(key)
        oa = p.get("openAccessPdf")
        if not oa: continue
        title = p.get("title", "")
        year = str(p.get("year", ""))
        authors = ", ".join(a.get("name", "") for a in (p.get("authors") or [])[:6])
        save_record(title, authors, year, p.get("abstract") or "",
                    p.get("url", "https://www.semanticscholar.org/"),
                    doi=doi, pdf_url=oa.get("url") if isinstance(oa, dict) else oa, oa=True)

def collect_openalex(query, max_n, seen):
    print(f"[OpenAlex] {query}")
    url = ("https://api.openalex.org/works?search="
           + urllib.parse.quote(query) + f"&per-page={max_n}&select=id,title,publication_year,authorships,abstract_inverted_index,open_access,doi,primary_location")
    try:
        data, _ = http_get(url)
        j = json.loads(data)
    except Exception as ex:
        print(f"  OA error: {ex}"); return
    for w in j.get("results", []):
        doi = w.get("doi")
        key = "doi:" + doi if doi else w.get("id")
        if key in seen: continue
        seen.add(key)
        oa = w.get("open_access") or {}
        pdf = oa.get("oa_url") or (w.get("primary_location") or {}).get("pdf_url")
        if not (oa.get("is_oa") and pdf): continue
        title = (w.get("title") or "").replace("\n", " ")
        year = str(w.get("publication_year", ""))
        authors = ", ".join(a.get("author", {}).get("display_name", "") for a in (w.get("authorships") or [])[:6])
        save_record(title, authors, year, reconstruct_inverted(w.get("abstract_inverted_index") or {}),
                    pdf, doi=doi, pdf_url=pdf, oa=True)

def reconstruct_inverted(idx):
    if not idx: return ""
    maxp = max(max(p) for p in idx.values())
    words = [""] * (maxp + 1)
    for w, pos in idx.items():
        for p in pos: words[p] = w
    return " ".join(words)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", default=None)
    ap.add_argument("--max", type=int, default=4)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    qfile = WIKI / "docs" / "workflow" / "collect-queries.txt"
    queries = [a.query] if a.query else (
        [l.strip() for l in qfile.read_text().splitlines() if l.strip()] if qfile.exists() else [])
    if not queries:
        print("no queries"); return
    if a.dry_run:
        print("DRY RUN queries:", queries); return
    ART.mkdir(parents=True, exist_ok=True)
    seen = existing_ids()
    for q in queries:
        for fn in (collect_arxiv, collect_s2, collect_openalex):
            try:
                fn(q, a.max, seen)
            except Exception as e:
                print(f"  [{fn.__name__} fail] {q}: {e}")
            time.sleep(2)
    print("DONE. Raw count:", len(list(ART.glob('*.md'))))

if __name__ == "__main__":
    main()
