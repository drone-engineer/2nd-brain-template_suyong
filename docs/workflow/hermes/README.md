# Hermes Cron 프롬프트 스텁

Hermes Agent 설치 후 Scheduled Tasks에 붙여 넣는다.  
`workdir` = 이 저장소 루트. 비밀·API 키는 프롬프트에 넣지 않는다.

**Telegram·gateway 연결:** [telegram-setup.md](./telegram-setup.md)

현재 기본 제어면은 Cursor. gateway가 뜨면 아래 프롬프트를 Cron에 등록한다.

## collect-evidence

```text
workdir: <repo-root>
skills: llm-wiki
Read SCHEMA.md, index.md, tail of log.md.
Collect only from the user-specified allowlist / query.
Write only to inbox/ or raw/** per SCHEMA. Never edit raw bodies after capture except allowed Zotero metadata repair.
Compute sha256. Append log.md ingest entry.
Stop after Gate A checklist in docs/workflow/gate-checklist.md. Do not compile wiki in this job.
```

## compile-wiki

```text
workdir: <repo-root>
skills: llm-wiki
Confirm Gate A passed for target raw files.
Compile/update canonical pages per SCHEMA page thresholds.
Sync index.md and log.md in the same transaction.
Run: python3 docs/workflow/check-gate-b.py
On failure, do not claim success; do not start graph job.
```

## build-knowledge-graph

```text
workdir: <repo-root>
Require Gate B pass on the same revision.
Run understand-knowledge (not generic understand).
Write only under .ua/. Never overwrite canonical from graph hypotheses.
Validate Gate C checklist. On failure keep previous .ua artifacts.
```

## deliver-review

```text
workdir: <repo-root>
Summarize collect/compile/graph outcomes, gate results, and file diffs.
Prepend a block to inbox/review-queue.md asking for Accepted|Contested|Deferred|Rejected.
Do not auto-merge contested changes.
```

## 권장: 단일 second-brain-refresh

초보 운영은 네 작업을 하나로 직렬화한다: Gate A → B → C → review.  
스케줄은 느슨하게 (예: 주 1회) 시작하고, writer는 한 번에 하나만.
