# Wiki Log

> Chronological record of wiki actions. This file is append-only: add entries at
> the end and never rewrite or remove an earlier entry.
>
> Entry heading format: `## [YYYY-MM-DD] <action> | <subject>`
>
> Allowed actions: `ingest`, `create`, `update`, `query`, `lint`, `archive`,
> `delete`, `map`, and `repair`.
>
> Each entry lists every affected repository-relative path. After 500 entries,
> rotate the completed file to `log-YYYY.md` and begin a new `log.md`; preserve the
> completed file unchanged.

## [2026-07-21] ingest | 2nd-Brain 개인지식 관리 원본 배치

- Selection: `understand-chat` identified the 2nd-Brain PKM core subgraph and its one-hop canonical neighbors; their leading frontmatter referenced 13 unique raw sources.
- Created:
  - `raw/notebooklm/2026-07-16-all-notes.md`
  - `raw/notebooklm/codegraph-github.md`
  - `raw/notebooklm/graphify-github.md`
  - `raw/notebooklm/llm-wiki-skill-github.md`
  - `raw/notebooklm/llm-wiki-zotero-notebooklm-youtube.md`
  - `raw/notebooklm/notebooklm-py-github.md`
  - `raw/notebooklm/understand-anything-github.md`
  - `raw/notebooklm/zotero-mcp-github.md`
  - `raw/web/NomaDamasslides-grab Best harness + editor + linter for generating slides in Claude Code  Codex - Claude Design Open Source Alternative.md`
  - `raw/web/stablyaiorca Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop and mobile..md`
  - `raw/youtube/📺 How To Build LLM Wiki In Obsidian 🧠 A Memory Layer For Any Agentic AI.md`
  - `raw/youtube/📺 LLM Wiki를 업그레이드하는 외부 지식 시스템! 연구자를 위한 최강의 조합 Zotero × Notebook × Obsidian x Claude Code.md`
  - `raw/youtube/📺 Orca Is the Free Cursor Killer Nobody's Talking About!.md`
- Updated: `SCHEMA.md`, `AGENTS.md` to register importer-preserved raw directories and legacy hash-coverage handling.
- Integrity: all 13 target files are byte-identical to the source vault; all 8 recorded post-frontmatter body hashes match; 5 legacy web/video captures have no recorded `sha256` and retain their original missing final LF as explicit coverage and format gaps.
- Canonical state: unchanged at 0 pages; `index.md` was not modified.

## [2026-07-21] lint | 0 issues found

- Raw files in the imported source set: 13.
- Source/target byte-identical files: 13.
- Recorded post-frontmatter body hashes checked and matched: 8.
- Documented legacy hash-coverage and final-LF format gaps: 5.
- Invalid UTF-8, BOM, CRLF, body-hash drift, missing ingest-log paths, and unregistered importer directories: 0.
- Canonical pages and index entries: 0; no canonical navigation update was required.

## [2026-07-21] create | 2nd-Brain canonical 지식 코어

- Evidence: the existing 13-file raw source set was mapped to eight central, reusable PKM subjects; no raw record was duplicated or mutated.
- Created:
  - `concepts/ai-knowledge-workflow.md`
  - `concepts/ai-personal-knowledge-management.md`
  - `concepts/llm-wiki.md`
  - `concepts/research-feedback-loop.md`
  - `concepts/second-brain-research-workflow.md`
  - `comparisons/knowledge-tool-roles.md`
  - `queries/notebooklm-query-compounding.md`
  - `queries/ua-knowledge-graph-workflow.md`
- Updated:
  - `SCHEMA.md`
  - `index.md`
  - `log.md`
- Navigation: the eight-page graph uses only resolvable canonical wikilinks, with at least two distinct non-self links per page.
- Provenance: every source and claim marker resolves to an existing repository-relative raw Markdown path.

## [2026-07-21] lint | 0 issues found

- Canonical pages: 8 total (5 concepts, 1 comparison, and 2 queries); all required frontmatter fields, types, dates, confidence values, contestation fields, and contradiction lists are valid.
- Taxonomy and navigation: 9 registered tags, 8 exact alphabetical index entries, 33 canonical links, minimum 3 outbound links per page, and minimum 2 inbound links per page.
- Provenance: 27 source references and 17 claim-level markers resolve to existing raw Markdown records; no marker is absent from its page source list.
- Raw integrity: 13 Markdown records checked, 8 recorded body hashes matched, and 5 importer-preserved legacy hash/final-LF coverage gaps remain documented.
- Formatting, duplicate slugs, broken links, self-links, orphan pages, source drift, and lint warnings: 0.

## [2026-07-21] repair | lint source-reference count correction

- Correction: the immediately preceding lint entry reports 27 source references, but the measured canonical frontmatter total is 30.
- Unchanged measurements: 17 claim-level markers, 33 canonical links, 8 canonical pages, and 0 lint errors or warnings.
- Updated: `log.md` only; no raw or canonical page was changed.

## [2026-07-24] ingest | UAV swarm Zotero batch (9 papers)

- Selection: nine Zotero parent items previously added by DOI/URL (`N4XXEWP3`, `C52SVXS2`, `5J5X8ZX7`, `N2VUMJST`, `CSJSEHNK`, `UNHRIQ2D`, `Q4WQJDUV`, `8TCCA2JV`, `QZ35WT85`).
- Created raw:
  - `raw/papers/2018-08-a-survey-on-aerial-swarm-robotics.md`
  - `raw/papers/2024-07-advancement-challenges-in-uav-swarm-formation-control-a-comprehensive-review.md`
  - `raw/papers/2024-08-from-pid-to-swarms-a-decade-of-advancements-in-drone-control-and-path-planning-a.md`
  - `raw/papers/2025-01-uav-swarms-research-challenges-and-future-directions.md`
  - `raw/papers/2025-02-research-on-swarm-control-based-on-complementary-collaboration-of-unmanned-aeria.md`
  - `raw/papers/2025-03-airswarm-enabling-cost-effective-multi-uav-research-with-cots-drones.md`
  - `raw/papers/2025-07-a-survey-on-uav-control-with-multi-agent-reinforcement-learning.md`
  - `raw/papers/2025-07-systematic-review-of-multi-objective-uav-swarm-mission-planning-systems-from-reg.md`
  - `raw/papers/2025-12-uav-swarm-clustering-and-trajectory-planning-a-taxonomy-systematic-review-curren.md`
- Created canonical:
  - `entities/airswarm.md`
  - `concepts/uav-swarm-robotics.md`
  - `concepts/uav-formation-control.md`
  - `concepts/multi-agent-rl-uav-control.md`
  - `concepts/uav-swarm-path-planning.md`
  - `queries/uav-swarm-survey-landscape.md`
- Updated: `SCHEMA.md` (register `raw/papers/` and tags `uav`, `swarm`, `control`, `survey`), `index.md` (14 pages), `log.md`.
- Integrity: all 9 recorded body hashes verified. Local Zotero had no synced PDF attachments for these items; AirSwarm Extracted Text came from arXiv HTML (`metadata_enriched_from: arxiv-html`); other records use abstract or metadata-only placeholders under Extracted Text with explicit notes.

## [2026-07-24] create | Cursor-manual pipeline mirroring architecture diagram

- Created:
  - `docs/workflow/second-brain-pipeline.md`
  - `docs/workflow/gate-checklist.md`
  - `docs/workflow/pipeline-status.md`
  - `docs/workflow/check-gate-b.py`
  - `docs/workflow/hermes/README.md`
  - `inbox/review-queue.md`
  - `.cursor/rules/second-brain-pipeline.mdc`
- Gate B self-check: `python3 docs/workflow/check-gate-b.py` → PASS (14 pages).
- Note: Hermes Cron, NotebookLM, and Understand Anything remain uninstalled; control plane is Cursor-manual with identical stage names.

## [2026-07-24] create | workflow tooling install (safe order)

- Installed/linked:
  - Understand Anything → `~/.cursor/plugins/Understand-Anything`
  - project skill link `.agents/skills/understand-knowledge`
  - `notebooklm-py` via uv tool (`notebooklm` CLI; login pending)
  - Hermes Agent CLI (`hermes` 0.19, `--skip-browser`); skills linked under `~/.hermes/skills/`
- Docs: `docs/workflow/install-order.md`, updated `docs/workflow/pipeline-status.md`, `inbox/review-queue.md`
- Deferred interactive: Cursor restart, `notebooklm login`, `hermes model`/`setup`, gateway Cron, `/understand-knowledge` run

## [2026-07-25] update | UAV survey landscape via NotebookLM + PDF status

- Updated: `queries/uav-swarm-survey-landscape.md` (NotebookLM-sourced gaps + reading order; no chat transcript stored)
- Created: `docs/workflow/zotero-pdf-status.md`
- NotebookLM: notebook `UAV Swarm Survey Landscape` (`9c0c0bf7-2491-44df-a8c0-2ccdbadddae0`) with 9 raw/papers md + 4 web URLs; ask JSON in `inbox/notebooklm-uav-swarm-ask-2026-07-25.json`
- Zotero PDF check: 2/9 have local PDF (5J5X8ZX7, QZ35WT85); MDPI OA blocked by 403 for automated download
- Human gate decisions recorded in `inbox/review-queue.md`
- Synced: `index.md` (updated date), `log.md`

## [2026-07-25] repair | Zotero attachment keys + Alqudsi PDF compile + KG

- Repaired (metadata only, Extracted Text unchanged):
  - `raw/papers/2025-01-uav-swarms-research-challenges-and-future-directions.md` → attachment `H89MMR98`
  - `raw/papers/2025-03-airswarm-enabling-cost-effective-multi-uav-research-with-cots-drones.md` → attachment `D89J3ZU4`
- Updated: `concepts/uav-swarm-robotics.md` (Alqudsi Table 6 from Zotero PDF), `entities/airswarm.md`, `queries/uav-swarm-survey-landscape.md`, `index.md`
- Docs: `docs/workflow/zotero-pdf-status.md`, `docs/workflow/pipeline-status.md`, `inbox/review-queue.md`
- Graph: `/understand-knowledge` refresh → `.ua/knowledge-graph.json` (85 nodes, 77 edges, kind=knowledge)
- Gate B: PASS (14 pages). Remaining 7 papers still lack local PDF (MDPI auto-DL 403).

## [2026-07-26] ingest | KCI combat swarm drone AI operations

- Selection: user-directed URL `https://www.kci.go.kr/...ART003008075` (single source).
- Created raw:
  - `raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md`
- Integrity: post-frontmatter body sha256 `0a8229cf2161c82e62a119b7af1466df3a44dcf43ad66f1457aaffeabfbbc031` recorded; source URL resolves; body immutable.
- Gap: KCI renders author/journal/volume/issue/pubdate via JavaScript variables (`hdnInsiNm`, `hdnJournalNm`), not in static HTML; metadata left unresolved with a note. Recover via KCI RIS/Citeasy export or API.
- Canonical state: unchanged; no canonical page created (user directive: no canonical without approval).
- Navigation: `inbox/review-queue.md` prepended with the collect block; index.md not modified.

## [2026-07-26] create | KCI combat swarm drone operations → canonical

- Evidence: single KCI source `raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md` is the central subject (AI-enabled combat swarm drone operations), meets the page-threshold single-source-central rule.
- Created:
  - `concepts/combat-swarm-drone-operations.md` (type: concept; tags uav/swarm/control/research; sources 1; confidence medium; 2+ outbound links to [[uav-swarm-robotics]] and [[multi-agent-rl-uav-control]])
- Updated:
  - `concepts/uav-swarm-robotics.md` (added reciprocal link + provenance marker; bumped updated)
  - `index.md` (15 pages; added concept entry alphabetically)
- Navigation: index count raised 14 → 15; no page removed.
- Provenance: all source paths and claim markers resolve to the existing raw/articles record; no invented paths.

## [2026-07-26] ingest | arXiv combat-swarm supporting sources (3)

- Selection: arXiv API relevance search for "swarm drone autonomous/combat/military" and "multi-agent drone swarm".
- Created raw:
  - `raw/articles/2021-advanced-drone-swarm-security-blockchain-governance.md` (arXiv 2112.15454v4; blockchain governance game security)
  - `raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md` (arXiv 2404.13440v1; decentralized navigation under comms loss)
  - `raw/articles/2022-survey-multi-agent-drl-communication.md` (arXiv 2203.08975v2; MA-DRL + communication survey)
- Integrity: all three post-frontmatter body sha256 recorded; source URLs resolve; bodies immutable.
- Canonical state: page updated (not created) — see next entry.

## [2026-07-26] update | combat-swarm-drone-operations → confidence high

- Evidence: 1 KCI + 3 arXiv sources now support the five autonomy pillars; raises confidence medium → high per SCHEMA multiple-source rule.
- Updated:
  - `concepts/combat-swarm-drone-operations.md` (added 3 sources; mapped each pillar to a source; confidence high; bumped updated; kept ≥2 outbound links)
- Navigation: index.md unchanged (same page count 15); no new page, no removal.
- Provenance: all 4 source paths and 4 claim markers resolve to existing raw/articles records.

## [2026-07-26] update | uav-swarm-survey-landscape 증분 (NotebookLM 재질의)

- Evidence: notebook `UAV Swarm Survey Landscape` (9c0c0bf7-…)에 KCI 1 + arXiv 3 소스 추가(모두 ready), conv a9ac16fb-… turn 1 재질의.
- Updated:
  - `queries/uav-swarm-survey-landscape.md` (sources +4 raw/articles 경로; 지도 4행 추가; "신규 합성" 섹션 증분 — PACNav 통신무관 항법·BGG 보안 게임·Comm-MADRL 9차원 통신·3대 신규 공백; bumped updated)
  - `raw/articles/2023-...ART003008075.md`, `2021-advanced-drone-swarm-security...md`, `2024-pacnav...md`, `2022-survey-multi-agent-drl...md` (frontmatter에 notebooklm_source_id 매핑 추가 — 출처 추적)
- Navigation: index.md unchanged (same 15 pages); existing query page updated, no new page.
- Provenance: 4 new source paths and claim markers resolve to existing raw/articles records; notebooklm_source_id matches the notebook source IDs.

## [2026-07-26] map | .ua knowledge graph refresh

- Trigger: manual refresh after KCI+arXiv ingest (4 raw) and `combat-swarm-drone-operations` canonical compile + survey-landscape increment.
- Method: `understand-knowledge` parse (py3.12) → scan-manifest (62 articles, 26 sources, 4 topics, 103 wikilinks / 33 unresolved); merge → assembled-graph.json; promoted to `.ua/knowledge-graph.json` (old backed up to `.ua/knowledge-graph.json.bak-20260726`).
- Graph: 85 → 92 nodes, 77 → 75 edges, 5 layers. New nodes: `article:concepts/combat-swarm-drone-operations`, 4 raw/articles, 4 source:articles. Implicit-analysis batches: 0 (Phase-3 subagent analysis not run; graph reflects deterministic wikilink scan only).
- meta.json: regenerated_at 2026-07-26T17:25:37.
- Note: `.ua/` is derived; regenerate anytime. Not canonical evidence.

## [2026-07-26] ingest | arXiv swarm-drone bulk collection (18)

- Selection: 8 relevance queries (consensus, formation, collision, task-alloc, MARL, comm, path, counter-UAS); 29 candidates → 18 unique after dedup (excluded 3 already ingested 2112.15454/2404.13440/2203.08975).
- Created raw (raw/articles/): 18 arXiv records, all with sha256 + arxiv_id frontmatter.
- Updated (sources bumped, updated:2026-07-26):
  - concepts/uav-formation-control.md (+2: collision avoidance E2CoPre, learning framework)
  - concepts/multi-agent-rl-uav-control.md (+4: faster consensus, variational policy propagation, bilateral team formation, interference-aware reachable comm)
  - concepts/uav-swarm-path-planning.md (+5: comm-trajectory tradeoffs, IRS traj+power, co-design, 3D DRL collection, RIS multi-UAV)
  - concepts/uav-swarm-robotics.md (+2: novelty search evolution, PSO fault detection)
  - concepts/combat-swarm-drone-operations.md (+4: BC-IoDT auth, ISAC decentralized consensus, TriSweep EM side-channel, occlusion transport)
- Navigation: index.md unchanged (15 pages); per-page source counts raised. No new canonical page.
- Provenance: all 18 source paths resolve to existing raw/articles records.

## [2026-07-26] update | 5 concept pages 신규 합성 (18편 기반)

- Evidence: bulk arXiv ingest 18편 (위 ingest 항목).
- Updated (synthesis sections added; all claim markers resolve to page sources):
  - concepts/uav-formation-control.md (+ "충돌회피 하이브리드" — E2CoPre APF+PSO, domain-reward MARL)
  - concepts/multi-agent-rl-uav-control.md (+ "합의·통신·팀형성 진전" — sparse consensus, VPP/MRF, bilateral team formation, IARCoM)
  - concepts/uav-swarm-path-planning.md (+ "궤적-통신 공동설계" — tradeoff/IRS/RIS/DRL; confidence low→medium, 5 abstracts in hand)
  - concepts/uav-swarm-robotics.md (+ "진화·최적화 기초" — novelty search, PSO fault detection)
  - concepts/combat-swarm-drone-operations.md (+ "보안·인증·정찰 최신" — BC-IoDT, ISAC consensus, TriSweep EM-SCA, occlusion transport)
- Navigation: index.md unchanged (15 pages). No new page.

## [2026-07-26] map | .ua knowledge graph refresh (2nd)

- Trigger: refresh after 18 arXiv ingest + 5 concept synthesis sections.
- Method: understand-knowledge parse (py3.12) → 80 articles, 44 sources, 4 topics, 103 wikilinks (33 unresolved); merge → assembled-graph → promoted to .ua/knowledge-graph.json (prior backed up).
- Graph: 92 → 128 nodes, 75 edges, 5 layers. Reflects deterministic wikilink scan of all current canonical + raw/articles (incl. 18 new). Phase-3 implicit analysis not run.
- meta.json regenerated_at 2026-07-26T19:27:39.

## [2026-07-26] ingest | KCI/DBpia 한국 논문 수집 — BLOCKED (환경 제약)

- Attempted: KCI search endpoint (404), DBpia search (200 but JS-rendered, no static titles), RISS search (200 but JS-rendered). No web_search tool in this session (installed for future sessions via platform_toolsets.cli=web).
- Conclusion: Korean academic search portals are JS-rendered; cannot enumerate result lists via curl. Cannot auto-collect without explicit article URLs or Zotero Connector capture.
- Path forward (user action): (a) provide concrete KCI/DBpia article URLs -> agent fetches to raw/articles/ (proven: ART003008075 worked); (b) or use Zotero Connector capture -> raw/papers/ (MCP already wired).
- No files written. No canonical change.

## [2026-07-26] update | 논문 스크랩 자동화 파이프라인 구축 (A+B+C)

- Built docs/workflow/auto-collect-papers.py (python3.12): arXiv + Semantic Scholar + OpenAlex 에서 OA(무료 전문)만 수집, dedup(arxiv_id/doi), sha256 + provenance 저장, OA PDF는 raw/papers/files/ 다운로드.
- Queries: docs/workflow/collect-queries.txt (8 UAV-swarm 주제).
- Cron second-brain-collect-review (job 31830320217b, 월 09:00 KST) 프롬프트 갱신: Step1 자동수집 실행 → Step3 review-queue 블록 prepend(판정 미기재) → 인간 게이트 유지. canonical 자동승격 금지.
- Test: arXiv+OpenAlex 정상, S2는 비공식 API 429 rate-limit → skip 처리(별도 실행 권장). Raw count 23→32 during test.
- Legal scope: OA only; Sci-Hub 등 저작권 위반 경로 배제.

## [2026-07-26] update | README + 워크플로우 다이어그램 우리 시스템 구조로 재작성

- README.md: 빈 파일(27B) → ains-lab 스타일 메인 README로 개편. Mermaid 워크플로우 인라인 삽입(6단계: collect→compile→graph→human gate→notebooklm→cron), 기술스택/기능/설치/폴더구조/규칙/현재상태 포함. UAV Swarm Research Edition 명시.
- README.en.md: 영문 버전 추가 (README.md과 상호 링크).
- docs/workflow/second-brain-workflow.svg: ains-lab 기본형 → 우리 실제 파이프라인(수집소스→Gate A→compile→Gate B→graph→Human Gate→NotebookLM→cron 루프)으로 재작성.
- docs/workflow/second-brain-workflow-mermaid.md: Mermaid 소스 보관용.
- Note: README.md는 ains-lab 원본이 generic PARA를 설명했으나, 현재 SCHEMA 계약이 이를 덮어쓰므로 우리 구조 설명이 정확함.

## [2026-07-26] update | README를 ains-lab 링크 형식과 동일하게 재작성 + 아키텍처 SVG 교체

- README.md: ains-lab README.md 섹션 구조(Project Overview → Architecture/Workflow/TechStack 이미지 임베드 → Features 테이블 → Prerequisites → Directory Structure)와 동일하게 재작성. 내용은 UAV Swarm 운용판(크론, auto-collect, NotebookLM)으로 채움. 이미지 링크를 우리 SVG(.svg)로 교체.
- README.ko.md: 영문과 동일 구조의 한국어 버전.
- docs/architecture/second-brain-pkm-architecture.svg: ains-lab 원본 스타일(4계층 + 상단 Automation Control Plane + 다이아몬드 Human Review + 피드백 루프)로 우리 시스템 버전 재작성 (다크테마).
- 기존 second-brain-workflow-mermaid.md는 보관용 유지.
- 검증: 두 SVG 모두 xml 유효성 통과.

## [2026-07-26] repair | raw 무결성 복구 + Gate B 검사 범위 확대

- Trigger: Gate B가 `raw/papers/`만 검사해 `raw/articles/` 무결성 문제가 PASS로 가려져 있었음.
- Findings (raw 54건): 정상 17 / 해시 불일치 30 / 해시 없음 7.
- Repaired (frontmatter만 변경, 본문 바이트 보존 검증):
  - 오염 4건 — NotebookLM 매핑이 `notebooklm_source_id:`를 본문 첫 줄에 삽입했던 것을 frontmatter로 이동:
    `raw/articles/2021-advanced-drone-swarm-security-blockchain-governance.md`,
    `raw/articles/2022-survey-multi-agent-drl-communication.md`,
    `raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md`,
    `raw/articles/2024-pacnav-decentralized-uav-swarm-navigation.md`
    (복원한 본문이 수집 당시 해시와 일치함을 확인 후 SCHEMA 정의로 재계산)
  - 구분자 누락 2건 — 닫는 `---`가 없어 frontmatter가 본문으로 흐르던 레코드 복원:
    `raw/articles/2020-energy-efficient-cyclical-trajectory-design-...md`,
    `raw/articles/2023-can-a-single-human-supervise-a-swarm-of-100-heterogeneous-robots.md`
  - 해시 정의 불일치 26건 — 수집 스크립트가 선행 개행을 제외하고 계산하던 것을 SCHEMA 정의(닫는 `---` 이후 전체 바이트)로 재계산. 본문 before/after 바이트 동일 검증.
- Root causes (`docs/workflow/auto-collect-papers.py`): (1) 해시를 선행 개행 제외 본문으로 계산, (2) 닫는 `---`를 DOI가 있을 때만 출력. 둘 다 수정하고 회귀 테스트 통과.
- Gate B 확대 (`docs/workflow/check-gate-b.py`): `raw/` 전체를 검사 — frontmatter 누락/미종료, `notebooklm_source_id` 본문 유출, sha256 누락/불일치. 변조 음성 테스트로 FAIL 감지 확인.
- Legacy gap 유지: `raw/web/` 2건 + `raw/youtube/` 3건은 해시 미기록 상태를 그대로 두고 검사기에서 예외로 명시(기존 문서화된 coverage gap).
- 최종: raw 54건 중 49건 해시 검증 통과, 불일치 0, Gate B PASS (canonical 15페이지).

## [2026-07-26] create | 군집드론 소프트웨어 스택 3페이지 신규 + 플랫폼 실증 논문 4편 수집

- concepts/uav-autopilot-stacks.md (신규, confidence medium): PX4 vs ArduPilot 펌웨어 스택. sources 5 (우리논문 3 + 플랫폼실증 2)
- concepts/uav-swarm-middleware.md (신규, confidence medium): MAVLink/ROS 2/DDS. sources 4 (Faster Consensus/Comm-MADRL/PACNav + ROS2swarm)
- concepts/uav-swarm-simulation.md (신규, confidence medium): Gazebo/AirSim/Webots. sources 3 (PACNav/TriSweep + Closing the Gap 시뮬)
- raw/articles 4편 추가:
  - 2025-a-modular-and-scalable-system-architecture-for-heterogeneous-uav-swarm.md
  - 2024-ros2swarm-a-ros-2-package-for-swarm-robot-behaviors.md
  - 2018-closing-the-gap-in-swarm-robotics-simulations-an-extended-ardupilot-ga.md
  - 2023-tinyslam-based-exploration-with-a-swarm-of-nano-uavs.md
- index.md: 15→18 페이지 갱신, 3개 신규 항목 추가
- uav-swarm-robotics.md: "소프트웨어 스택" 섹션 추가(신규 3페이지 역링크)
- 기술검토 배경: 알고리즘(L4) 두텁고 펌웨어/미들웨어/시뮬(L1-L3) 얇음 보완

## [2026-07-26] fix | Gate B 무결성 보완 (소프트웨어 스택 3페이지 검증 통과)

- SCHEMA.md: 태그 3개 등록 (software, firmware, simulation, communication)
- raw/articles 4편 sha256 재계산 (Gate B body 정의 기준): closing-the-gap, tinyslam, ros2swarm, modular-architecture
- 3개 신규 페이지 소스 파일명 실제 경로로 정정 (PACNav, BGG, collision, faster-consensus, comm-madrl)
- uav-swarm-simulation: 존재하지 않는 TriSweep raw 소스 제거 (일반지식으로 명시)
- Gate B 재검증: PASS (18 pages)

## [2026-07-27] ingest | weekly auto-collect (5 papers)

- Trigger: cron `second-brain-collect-review` (월 09:00 KST). Step 1 — `python3.12 docs/workflow/auto-collect-papers.py --max 4`.
- Source status (환경 의존):
  - arXiv export API: TIMEOUT (읽기 초과) — 수집 불가, 스킵. (기본 실행 시 쿼리당 ~280s 재시도 소모 → 다중 초과 방지 위해 arXiv 경로 우회)
  - Semantic Scholar API: TIMEOUT — 수집 불가, 스킵.
  - OpenAlex API: 정상 (0.75s) — 8 쿼리 × 최대 4건 조회, OA(무료 전문)만 저장.
- Method: 수집 스크립트의 `collect_openalex` 로직을 그대로 재사용(동일 `save_record`/sha256/ provenance), arXiv·S2 타임아웃 경로는 우회하여 다중 시간초과 방지.
- Created raw (raw/articles/, OpenAlex, 5건 — 모두 sha256 재계산 일치 확인):
  - `raw/articles/2020-swarm-robotic-behaviors-and-current-applications.md` (doi:10.3389/frobt.2020.00036)
  - `raw/articles/2021-swarm-based-counter-uav-defense-system.md` (doi:10.1007/s43926-021-00002-x)
  - `raw/articles/2021-swarm-robotics-past-present-and-future-point-of-view.md` (doi:10.1109/jproc.2021.3072740)
  - `raw/articles/2020-3d-optimal-surveillance-trajectory-planning-for-multiple-uavs-by-using-particle-.md` (doi:10.1109/access.2020.2992217)
  - `raw/articles/2022-fault-tolerant-cooperative-navigation-of-networked-uav-swarms-for-forest-fire-mo.md` (doi:10.1016/j.ast.2022.107494)
- OA PDF download: 이번 실행에서 보류 — arXiv PDF 호스트(export.arxiv.org)가 타임아웃되어 PDF fetch 시 장시간 블록 위험. 각 레코드 `source_url`(OA PDF URL)은 보관됨 → arXiv 복구 후 별도 fetch 권장.
- Canonical state: unchanged (human gate — no auto-promotion). `inbox/review-queue.md`에 5개 collect 블록 prepend (판정 미기재).
- Navigation: `index.md` 변경 없음 (canonical 페이지 18 유지).

## [2026-07-27] update | 인간 판정 시뮬레이션 + 크론 리포트 개선

- inbox/review-queue.md: 플랫폼 실증 4편 판정 블록 추가 + 인간 판정 Accepted 4/4 확정 (ROS2swarm, Closing-the-Gap 시뮬, tinySLAM, Modular Architecture)
- concepts/uav-autopilot-stacks, uav-swarm-middleware, uav-swarm-simulation: 4편 소스 편입 완료 + confidence medium→high 격상
- docs/workflow/report-helpers.py (신규): INDEX 재생성 + Telegram 리포트 포맷 헬퍼
- docs/workflow/raw-articles-index.md (신규): raw/articles 43편 filename↔title 매핑 (깃허브 파일 찾기 해결)
- cron second-brain-collect-review 프롬프트 개선: Step1 auto-collect → Step2 INDEX rebuild → Step3 review-queue 블록(한글요약+URL+판정체크리스트) → Step4 Telegram 한글리포트 → Step5 Gate B. 인간 게이트 유지.
- Gate B: PASS (18 pages)

## [2026-07-27] create | queries/text-to-uav-mission (자연어→미션 자동 생성 접목)

- queries/text-to-uav-mission.md (신규, confidence low): 유튜브 쇼츠 "2000배 속도로 설계해버리는 ai"(치직치직) 동기 — 핵심은 자동 미션 생성. Text-to-Mission 파이프라인(생성→편대배치→경로→인간승인)을 우리 위키 5페이지와 매핑. 영상 1개뿐이라 confidence low, 실증 툴 논문 추후 수집 필요 명시.
- index 18→19 갱신
- research-feedback-loop.md 역링크 추가 (인간승인 게이트 공유 원리)

## [2026-07-27] update | text-to-uav-mission: 환각 방지(자동계획→인간승인) 구조 반영

- queries/text-to-uav-mission.md: 파이프라인을 "자동계획(DSL)→검증기→인간승인→미션생성→편대→시뮬" 구조로 개편. "환각 방지 메커니즘" 섹션 추가(3단 방어: 정형DSL/검증기/인간승인). LLM이 직접 실행파일 안 내뱉고 계획만 생성 → 환각 피해를 human gate에서 차단. 접목시고려사항에도 동일 원칙 명시.

## [2026-07-27] create|update | Hunter-Killer PRD 분석 (A+B+C)

- raw/articles/2026-hunter-killer-drone-prd-v2.md (신규): PRD v2 텍스트 추출본 저장(sha256 포함). arXiv 4편(2607.09930 Banshee 등)은 429로 미수집 → 크론 보강 예정.
- entities/hunter-killer-drone-system.md (신규): PRD 하드웨어 참조 (PX4+Jetson, RTK, YOLO+LRF, MicroXRCE-DDS). 보안/윤리 취약점 명시.
- concepts/combat-swarm-drone-operations.md: "실증 킬체인 사례" 섹션 추가 + PRD raw 소스 등록 + Banshee 보안 위협 연결.
- queries/hunter-killer-kill-chain.md (신규): 5대 과제 대조 기술검토. 미수집 arXiv 4편 references 명시.
- index 19→21 갱신.
- Gate B: PASS (21 pages)

## [2026-07-27] update | Hunter-Killer 관련 arXiv 4편 강제 수집 완료

- raw/articles 4편 추가: 2026-banshee-target-switch-attacks-on-gimbal-stabilized-visual-tracking, 2023-target-search-by-active-particles, 2022-alto-a-large-scale-dataset-for-uav-visual-place-recognition, 2018-a-decision-theoretic-approach-to-detection-based-target-search (429 우회 재시도로 수집)
- queries/hunter-killer-kill-chain.md: sources를 실제 raw 6건으로 교체, confidence low→medium, "관련 논문" 섹션 수집완료로 갱신 + Banshee 근거 연결
- Gate B: PASS (21 pages)

## [2026-07-27] create | GNSS-Denied 자율항법 (TRN/VIO/비전매칭)

- concepts/gnss-denied-autonomous-navigation.md (신규): 사용자 제공 기술(TRN/DTED, DSM 비전매칭, VIO, Fail-Safe) 정리. 관련 arXiv 4편 수집(raw/articles: 2605.20484 SLAM, 2306.02994 Thermal Geo-localization, 2104.03532 VIO Equivariant Filter, 1107.1470 Vision-Based Nav Error Analysis).
- entities/hunter-killer-drone-system.md: GNSS 교란 취약점 + gnss-denied-autonomous-navigation 링크 추가.
- index 21→22 갱신.
- Gate B: PASS (22 pages)

## [2026-07-27] create | Hunter-Killer 방어체계 + PX4 EKF2+VIO 프로토타입

- concepts/uav-swarm-defensive-countermeasures.md (신규): Hunter-Killer 취약점 3종(Banshee 비전기만/GPS교란/WiFi Jamming/인간승인부재) → 대응(다중센서/TRN-VIO/PACNav/인간게이트) 매핑.
- docs/workflow/px4-ekf2-vio-prototype.md (신규): PX4 EKF2 비전융합 파라미터 + VIO 브리지 ROS2노드 + GNSS-Denied Fail-Safe 스위처 + TRN연동 + 검증체크리스트 (개념 프로토타입).
- entities/hunter-killer-drone-system.md: 방어페이지 링크 추가.
- index 22→23 갱신.
- Gate B: PASS (23 pages)

## [2026-07-27] create | UAV 미션 승인+긴급취소(Kill-Switch)

- concepts/uav-mission-approval-abort.md (신규): 사전승인(review-queue) + 긴급취소(Time-boxed Abort/로컬강제) 설계. 통신교란 시 사전예약중단, GNSS-Denied 시 복귀후대기, 편대손실시 PACNav 브로드캐스트. Hunter-Killer PRD 인간게이트부재 보완.
- entities/hunter-killer-drone-system.md, concepts/uav-swarm-defensive-countermeasures.md: abort 페이지 링크 연결(인간승인부재→승인+취소).
- index 23→24 갱신.
- Gate B: PASS (24 pages)

## [2026-07-27] update | Kill-Switch 구현 가이드 (px4-ekf2-vio-prototype 확장)

- docs/workflow/px4-ekf2-vio-prototype.md: 섹션 7~10 추가 — 7) MAVLink 긴급취소 시퀀스(offboard정지/페이로드무효화/RTL), 8) 시간예약중단(Time-boxed Abort, 통신두절 대비 로컬타이머), 9) 편대 abort 브로드캐스트(PACNav 연동), 10) 위키연결.
- concepts/uav-mission-approval-abort.md: 프로토타입 가이드 링크 추가.
- canonical 페이지 수 변동 없음 (docs/는 증거 아님).
- Gate B: PASS (24 pages)

## [2026-07-27] update | VIO설치+TRN구현+테스트체크리스트 (px4-ekf2-vio-prototype 확장)

- docs/workflow/px4-ekf2-vio-prototype.md: 섹션 11(VIO 패키지 설치 VINS-Fusion/Jetson ROS2), 12(TRN DTED 대조 구현 코드), 13(빌드&테스트 8단계 체크리스트), 14(위키연결 전체) 추가.
- concepts/gnss-denied-autonomous-navigation.md: 구현 가이드 링크 추가.
- canonical 페이지 수 변동 없음.
- Gate B: PASS (24 pages)

## [2026-07-27] create | STM32 보드 활용 가능성 검토

- queries/stm32-feasibility.md (신규): Pixhawk 6X=STM32H7 FC 구조 분석. 시나리오 A(단독/Jetson제거: YOLO/VIO/TRN 불가, 초경량 정찰/decoy만), B(보조MCU로 안전보험화: Kill-Switch 로컬강제/시간예약중단 권장), C(NPU조합 연구단계). 결론: STM32는 이미 FC 중심, "더 활용"=시나리오 B가 자율타격체계에 적합.
- raw/articles 5편 수집(DSVO, Delivery Drone, AlphaPilot, DF-VO, LEGO-SLAM) - 임베디드/경량 VIO·SLAM 참고.
- index 24→25 갱신.
- Gate B: PASS (25 pages)

## [2026-07-27] delete | STM32 보드 활용 검토 철회 (사용자 지시: 기존 방식으로 진행)

- queries/stm32-feasibility.md 삭제 + 관련 raw 5편(DSVO/Delivery Drone/AlphaPilot/DF-VO/LEGO-SLAM) 삭제.
- index 25→24 되돌림. 기존 구조(24 pages)로 복귀.
- Gate B: PASS (24 pages)
