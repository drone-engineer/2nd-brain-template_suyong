# 2nd-Brain 운영 파이프라인 (그림 ↔ 실행)

> 작성일: 2026-07-24  
> 기준 그림: Automation Control Plane · Evidence → Canonical → Discovery → Decision  
> 현재 제어면: **Cursor + llm-wiki** (Hermes Cron은 미설치 → 동일 단계를 수동/채팅으로 실행)

이 문서는 아키텍처 그림을 **지금 바로 따라 하는 순서**로 바꾼 것이다.  
Hermes·NotebookLM·Understand Anything이 생기면 같은 단계 이름 그대로 도구만 갈아끼운다.

## 한눈에

```text
1 collect-evidence   Zotero/URL → raw/     → Gate A
2 compile-wiki       llm-wiki → canonical  → Gate B
3 build-knowledge-graph  UA → .ua/         → Gate C   (도구 없으면 SKIP + 기록)
4 deliver-review     diff·lint·조치 목록   → Human Gate
5 (승인분만) canonical 확정 → 필요 시 3 재실행
```

채팅에서 한 줄로 시키기:

```text
파이프라인 돌려줘: collect | compile | graph | review | full
```

에이전트는 아래 단계 계약과 [gate-checklist.md](./gate-checklist.md)를 따른다.

---

## 1) collect-evidence (Evidence)

**담당:** 사람 + Cursor(+ Zotero MCP)  
**쓰기 허용:** `inbox/`, `raw/**` (본문 불변 규칙 준수), `log.md`  
**금지:** canonical 승격, `.ua/` 생성

### 할 일
1. 소스 범위 확인 (URL / Zotero item / PDF 첨부 여부)
2. 중복 확인 (`index.md`, `raw/`, DOI·URL)
3. 미분류면 `inbox/`, 확정이면 `raw/articles|papers|…`
4. Zotero면 parent 메타 → children → fulltext 순 ([zotero-mcp-cursor-setup.md](./zotero-mcp-cursor-setup.md), llm-wiki zotero-ingest)
5. `sha256` 기록, ingest를 `log.md`에 append

### Gate A
[gate-checklist.md](./gate-checklist.md) § Gate A. 실패 시 compile로 가지 않는다.

---

## 2) compile-wiki (Canonical Memory)

**담당:** Cursor + `.agents/skills/llm-wiki`  
**쓰기 허용:** `entities|concepts|comparisons|queries/`, `index.md`, `log.md`, 필요 시 `SCHEMA.md` 태그 등록  
**선행:** Gate A 통과 raw

### 할 일
1. `SCHEMA.md` · `index.md` · 최근 `log.md` 읽기
2. 기존 페이지 검색 후 갱신 우선 (동의어 페이지 금지)
3. 페이지 임계값: 중심 주제 또는 2+ 소스
4. 출처 경로·wikilink≥2·confidence·contested 규칙
5. `index.md` + `log.md` 같은 트랜잭션

### Gate B
체크리스트 또는:

```bash
python3 docs/workflow/check-gate-b.py
```

실패 시 graph로 가지 않는다.

---

## 3) build-knowledge-graph (Discovery · UA)

**담당:** Understand Anything `understand-knowledge`  
**쓰기 허용:** `.ua/` 만 (canonical 덮어쓰기 금지)  
**선행:** Gate B 통과

### 도구 있을 때
1. lint 통과 revision에서 `understand-knowledge`
2. Gate C 검증 ([gate-checklist.md](./gate-checklist.md))
3. dashboard/chat 후보는 **가설** — 원문 대조 전 canonical 반영 금지

### 도구 없을 때 (현재 기본)
1. `docs/workflow/pipeline-status.md`에 `graph: skipped (UA not installed)` 기록
2. Discovery 대안: Obsidian 그래프 보기 + 채팅 질의
3. NotebookLM은 선택 — 결과 환류는 [notebooklm-query-compounding](../../queries/notebooklm-query-compounding.md) 절차

---

## 4) deliver-review (보고) → Human Gate (Decision)

**담당:** 에이전트가 보고, **사람이 판정**

### deliver-review 산출물
`inbox/review-queue.md`에 이번 실행 요약 추가:

- 변경 파일 목록
- Gate A/B/C 결과
- 사람 조치 (Accepted / Contested / Deferred / Rejected)

### Human Gate 판정

| 판정 | 의미 | 다음 |
| --- | --- | --- |
| Accepted | 재사용·출처 OK | canonical 유지/병합, 필요 시 graph 재실행 |
| Contested | 충돌 미해결 | `contested: true` + 양측 출처 |
| Deferred | 가치 있으나 근거 부족 | inbox/query 보류 |
| Rejected | 중복·저품질 | canonical 미편입·되돌리기 |

개인 메모·판단은 canonical 사실과 섞지 않는다.

---

## Automation Control Plane 대응표

| 그림 블록 | Hermes (목표) | 지금 (Cursor) |
| --- | --- | --- |
| collect-evidence | Hermes + MCP | 채팅 `ingest` + Zotero MCP |
| compile-wiki | Cron + llm-wiki | 채팅 + llm-wiki 스킬 |
| build-knowledge-graph | Cron + UA | UA 설치 전 SKIP |
| deliver-review | Hermes 전달 | `inbox/review-queue.md` + 채팅 요약 |
| Cron 스케줄 | Hermes Scheduled Tasks | 사람이 `full` 요청 시 직렬 실행 |

Hermes 설치 후 붙일 프롬프트: [hermes/](./hermes/).

---

## full 실행 순서 (직렬)

1. collect (요청된 소스만; 없으면 “수집 없음”으로 Gate A N/A)
2. compile
3. Gate B 스크립트
4. graph 또는 SKIP
5. review-queue 갱신 + 사용자에게 판정 요청

실패 격리: 이전 단계 실패 시 다음 단계 쓰지 않는다. raw 실패가 canonical을, lint 실패가 `.ua/`를 오염시키지 않는다.
