# Hermes + Telegram 설정 (자동수집·알림)

> 갱신: 2026-07-25  
> 목표: 텔레그램으로 수집 지시·Cron 결과 수신. **canonical 확정은 Cursor/사람 게이트**.

토큰·유저 ID는 이 문서·Git에 넣지 않는다. `~/.hermes/.env`에만 둔다.

## 사전 상태

| 항목 | 상태 |
| --- | --- |
| Hermes CLI | 설치됨 |
| Nous 로그인 + 기본 모델 | 됨 (free 모델 — 품질 제한 있음) |
| `python-telegram-bot` | 설치함 (gateway용) |
| `TELEGRAM_BOT_TOKEN` | **미설정** ← 사용자 |
| gateway 서비스 | **미실행** |

## A. Telegram 봇 (사용자, 5분)

1. Telegram에서 [@BotFather](https://t.me/BotFather) 열기  
2. `/newbot` → display name → username(`…bot`)  
3. 받은 **API token** 복사 (채팅/Git에 붙이지 말 것)  
4. [@userinfobot](https://t.me/userinfobot) 에 메시지 → **숫자 user ID** 복사  

선택: `/setcommands`에

```text
help - Show help
new - New conversation
sethome - Set home channel for cron
```

## B. Hermes에 연결

터미널에서:

```bash
source ~/.zshrc
hermes gateway setup
```

- Telegram 선택  
- bot token / allowed user ID 입력  

또는 수동 (`~/.hermes/.env`):

```bash
TELEGRAM_BOT_TOKEN=<BotFather토큰>
TELEGRAM_ALLOWED_USERS=<내숫자ID>
```

검증:

```bash
hermes gateway run
```

텔레그램에서 봇에게 `ping` 또는 `안녕하세요` → 응답 오면 OK.  
Ctrl+C로 종료한 뒤 백그라운드 설치:

```bash
hermes gateway install
hermes gateway start
hermes gateway status
```

## C. 이 vault용 Cron (gateway 뜬 뒤)

프롬프트 본문은 [README.md](./README.md) 참고.  
`hermes cron create` 형식: `schedule` 다음에 `prompt` (위치 인자).

권장 첫 작업 (매주 월요일 09:00, 수집·리뷰만 — canonical 자동 확정 금지):

```bash
REPO="/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"

hermes cron create \
  --name "second-brain-collect-review" \
  --deliver telegram \
  --workdir "$REPO" \
  --skill llm-wiki-ains \
  "0 9 * * 1" \
  "$(cat <<'EOF'
Read SCHEMA.md, index.md, tail of log.md.
If the user gave an allowlist/query in recent Telegram context, collect only that into inbox/ or raw/ per SCHEMA.
Otherwise summarize inbox/ into a new review block only.
Do NOT create or update canonical pages.
Do NOT edit raw/ bodies after capture.
Prepend a block to inbox/review-queue.md asking Accepted|Contested|Deferred|Rejected.
Reply with a short summary and changed paths.
EOF
)"
```

## D. 운영 원칙 (하이브리드)

| 채널 | 역할 |
| --- | --- |
| Telegram + Hermes | 트리거, 스케줄, inbox/리뷰 알림 |
| Cursor (Claude) | SCHEMA 준수 canonical, Gate B, 사람 확정 |

free 모델이 위키를 직접 많이 고치면 SCHEMA 위반 위험이 크다.  
처음엔 **수집·알림만** Telegram에 두고, 정리는 Cursor에서 한다.

## E. Clipper (병행)

Chrome에 [Obsidian Web Clipper](https://chromewebstore.google.com/detail/obsidian-web-clipper/cnjifjpddelmedmihgiseonhbbhnpjmi) 설치.  
Vault = 이 저장소, 저장 위치 `inbox/` 또는 `raw/web/`.  
상세: [../browser-capture-extensions.md](../browser-capture-extensions.md)
