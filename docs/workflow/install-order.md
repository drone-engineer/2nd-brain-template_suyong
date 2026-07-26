# 설치 순서 (에러 최소화)

아키텍처·README 권장 순서를 따른다. **한 단계 검증 후** 다음으로 간다.

| # | 단계 | 상태 (2026-07-24) | 검증 |
| --- | --- | --- | --- |
| 0 | Obsidian vault = 저장소 root | 기존 | vault 열림 |
| 1 | Zotero + Local API | 완료 | Zotero.app, localhost:23119 |
| 2 | uv | 완료 | `uv --version` |
| 3 | zotero-mcp + Cursor mcp.json | 완료 | MCP Connected |
| 4 | llm-wiki 스킬 | 완료 | `.agents/skills/llm-wiki` |
| 5 | Gate B 스크립트 | 완료 | `python3 docs/workflow/check-gate-b.py` |
| 6 | Understand Anything (Cursor 플러그인) | 완료 | `~/.cursor/plugins/Understand-Anything` + 프로젝트 스킬 심볼릭 |
| 7 | notebooklm-py CLI | 완료 | Auth pass (`notebooklm doctor`) |
| 8 | Hermes Agent CLI | 완료 | Nous + free 모델 — **gateway/Telegram 남음** |
| 9 | understand-knowledge → `.ua/` | 완료 | 92 nodes / 95 edges, `kind: knowledge` |
| 10 | Connector / Web Clipper | 부분 | Connector ✅ / Clipper ❌ — [browser-capture-extensions.md](./browser-capture-extensions.md) |
| 11 | Hermes Telegram SDK | 완료 | `python-telegram-bot` 22.6 — **봇 토큰·gateway는 사용자** |
| 12 | Telegram 가이드 | 작성 | [hermes/telegram-setup.md](./hermes/telegram-setup.md) |

## 사용자가 아직 할 일

1. ~~Chrome에 Obsidian Web Clipper~~ ✅  
2. ~~Telegram BotFather + `hermes gateway setup`~~ ✅  
3. ~~Cron 등록~~ ✅ (`second-brain-collect-review`, 월 09:00)  
4. (일상) Telegram 알림/`inbox/review-queue` 판정 → Cursor에서 Accepted만 확정  
5. (선택) `/understand-dashboard` 로 그래프 UI 열기

## 일부러 뒤로 미룬 것

- Hermes Playwright/Chromium: `--skip-browser`로 설치해 의존성 충돌 감소. 필요 시 수동 설치.
