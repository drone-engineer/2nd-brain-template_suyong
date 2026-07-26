# Pipeline Status

> 도구·단계 가용성. 비밀·API 키는 적지 않는다.  
> 갱신: 2026-07-25

| 구성 요소 | 상태 | 비고 |
| --- | --- | --- |
| SCHEMA / index / log | OK | 계약 활성 |
| llm-wiki-ains 스킬 | OK | `.agents/skills/llm-wiki/` (`name: llm-wiki-ains`, Hermes 기본 `llm-wiki`와 분리) |
| Zotero MCP (Cursor) | OK | hybrid 읽기+쓰기 |
| Obsidian vault | OK | 저장소 root |
| Gate B 스크립트 | OK | `docs/workflow/check-gate-b.py` → PASS. canonical + **`raw/` 전체 무결성** 검사 (해시·frontmatter·본문 유출) |
| raw 무결성 | OK | 54건 중 49건 해시 검증 통과, 불일치 0. `raw/web`·`raw/youtube` 5건은 문서화된 legacy gap |
| Understand Anything (Cursor 플러그인) | 설치됨 | `~/.cursor/plugins/Understand-Anything` |
| understand-knowledge 스킬 | 설치됨 | `.agents/skills/understand-knowledge` → 플러그인 심볼릭 |
| NotebookLM CLI (`notebooklm-py`) | OK | Auth pass + UAV 노트북 1회 질의 완료 |
| Zotero PDF 첨부 | 부분 | 2/9 — Alqudsi·AirSwarm 메타 repair·canonical 보강 완료. [zotero-pdf-status.md](./zotero-pdf-status.md) |
| Cursor Tavily MCP | OK | `tavily_search` 응답 확인 (Hermes 배선은 별도) |
| `.ua/` 지식그래프 | OK | 2026-07-25 refresh — 85 nodes / 77 edges (`kind=knowledge`) |
| Hermes Agent | CLI OK | primary=`tencent/hy3:free` (Nous) |
| Hermes fallback | OK | 1) `poolside/laguna-s-2.1:free` 2) local Ollama `qwen2.5:14b` |
| Hermes ← llm-wiki-ains / understand-knowledge | 링크됨 | `~/.hermes/skills/custom/llm-wiki-ains` → vault 스킬 |
| Hermes Cron gateway | OK | launchd 실행 중 + Telegram 연결 |
| Hermes Cron job | OK | `second-brain-collect-review` pinned to hy3 — 수동 run **성공** (2026-07-25) |
| Obsidian Web Clipper | OK | vault=`2nd_Brain_Template`, 경로=`inbox` — 테스트 클립 확인 |

## 현재 실행 모드

**Hermes Cron + Telegram** (수집·리뷰 알림) + **Cursor** (canonical 확정·Gate B).  
주간 자동: `second-brain-collect-review` (월 09:00). 모델 폴백으로 503 대비.  
상세: [hermes/telegram-setup.md](./hermes/telegram-setup.md) · [hermes/telegram-daily.md](./hermes/telegram-daily.md)

상세 설치 이력: [install-order.md](./install-order.md)
