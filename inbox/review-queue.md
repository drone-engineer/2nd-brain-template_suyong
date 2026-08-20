# Review Queue (Human Gate)

> 파이프라인 `deliver-review` 결과. 사람이 Accepted / Contested / Deferred / Rejected를 적는다.  
> 이 파일은 `inbox/` — canonical 증거가 아니다.

---

## [2026-08-21] collect | YouTube Scout Summary

- **단계:** collect-evidence (YouTube daily scout) → Gate A → review-queue prepend
- **수집 결과:** YouTube raw 15개 (Hunter-Killer계열)
  - `raw/youtube/2026-08-21-5knSEDXDa_0.md`
  - `raw/youtube/2026-08-21-MGggtBIzvtg.md`
  - `raw/youtube/2026-08-21-al9ITeP4fUA.md`
  - `raw/youtube/2026-08-21-EKpxP2YieZw.md`
  - `raw/youtube/2026-08-21-Lr7L2t-svJQ.md`
  - `raw/youtube/2026-08-21-l2ARv6y70bw.md`
  - `raw/youtube/2026-08-21-p8frNNYQNV4.md`
  - `raw/youtube/2026-08-21-i1QRqu3Cocw.md`
  - `raw/youtube/2026-08-21-V5ZMhFyWQa8.md`
  - `raw/youtube/2026-08-21-w0z-362DkIU.md`
  - `raw/youtube/2026-08-21-w5KkbRVhqzE.md`
  - `raw/youtube/2026-08-21-sEiKDZ6pZo4.md`
  - `raw/youtube/2026-08-21-M5YyDGfKhE8.md`
  - `raw/youtube/2026-08-21-aGINGHexT7k.md`
  - `raw/youtube/2026-08-21-HMKXMaAzByU.md`
- **Gate A:** PASS (YouTube raw files with sha256, title, channel, URL)
- **canonical 변경:** 없음 (기타 비공식 컨텐츠 보강 → 필요시 기존 `concepts/`, `entities/` 등의 canonical에 연결 가능)
- **사람 조치:**
  - [ ] YouTube raw contents 재검토(제목/채널 정보) → 해당 주제가 `concept/`, `entity/`로 정리되는 경우 반영
  - [ ] `process-youtube.py` 스크립트 개선 (자막 추출 기능 없어 현재 내용 미집약 가능)
- 판정: **Accepted** (2026-08-21) — via 2nd-brain-web

## [2026-07-25] next-step: Clipper + Telegram prep

> 파이프라인 `next-step`에 해당하는 문서. `docs/workflow/second-brain-pipeline.md`

- **단계:** Hermes Gateway 설치, 설정 가이드 작성
- **완료:** `python-telegram-bot` 22.6, `docs/workflow/hermes/telegram-setup.md`, Zotero Connector 확인
- **Gate B:** 이전 PASS 유지 (그래프 `.ua/` 존재)
- **사람 조치 필요:**
  - [ ] Obsidian Web Clipper 설치 (Chrome)
  - [ ] BotFather로 봇 생성 → `hermes gateway setup`
  - [ ] `hermes gateway install` 후 Cron (telegram-setup.md C절)
- 판정: **Accepted** (2026-07-30) — via 2nd-brain-web

## [2026-07-24] install-order tooling

- **단계:** Understand Anything 플러그인 + notebooklm-py + Hermes CLI 설치
- **Gate B:** PASS (재검증)
- **사람 조치 필요:**
  - [ ] Cursor 재시작 (UA 플러그인)
  - [ ] `notebooklm login`
  - [ ] `hermes model` 또는 `hermes setup`
  - [ ] (선택) `hermes gateway install` 후 Cron
- 판정: **Accepted** (2026-07-30) — via 2nd-brain-web

## [2026-07-24] pipeline bootstrap

- **단계:** collect(기존 Zotero 9편 이미 ingest) / compile(UAV canonical 6) / graph=SKIP / review
- **Gate A:** 부분 통과 — 다수 항목 PDF 미첨부, abstract/메타 위주 (노트 명시됨)
- **Gate B:** 당시 수동 구성 (스크립트 도입 전). 이후 `python3 docs/workflow/check-gate-b.py`로 재검증 권장
- **Gate C:** SKIP — Understand Anything 미설치
- **변경 요약:** `raw/papers/` 9, UAV canonical 6, SCHEMA 태그/`raw/papers/` 등록, pipeline 문서
- **사람 조치 필요:**
  - [ ] Zotero에서 PDF `Find Full Text` / 첨부 후 본문 재ingest
  - [ ] UAV canonical 내용 검수 (Accepted 여부)
  - [ ] (선택) NotebookLM / UA / Hermes 도입 시기 결정
- 판정: **Accepted** (2026-07-30) — via 2nd-brain-web
- **메모:**