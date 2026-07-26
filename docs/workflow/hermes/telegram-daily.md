# Telegram으로 2nd-Brain 쓰기 (일상)

Hermes 봇 `2nd_Brain_Template`을 **메인 창구**로 쓴다.  
품질이 중요한 canonical 확정만 Cursor에서 한다.

> vault 루트: `/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template`  
> 모델: Nous free — 복잡한 SCHEMA 편집은 보수적으로.

## 시작 습관

1. 봇 채팅을 즐겨찾기/고정  
2. 첫 메시지에 vault를 박아 두기 (세션마다 한 번):

```text
작업 디렉터리는 /Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template 야.
SCHEMA.md와 llm-wiki 규칙을 지켜. canonical은 내 승인 없이 만들지 마.
```

3. `/help` — 명령 목록  
4. Home channel은 이미 본인 DM으로 설정됨 (Cron 알림 여기로 옴)

## 자주 쓰는 말 (복붙)

### 상태 보기
```text
지금 gateway/cron 상태와 inbox/에 뭐가 있는지 짧게 요약해줘.
canonical은 건드리지 마.
```

### 웹/메모 수집 (임시)
```text
아래를 inbox/에만 메모로 남겨줘. raw/나 canonical은 건드리지 마.
제목: …
링크/요약: …
```

### Zotero/논문 수집 지시
```text
workdir는 이 vault야. Zotero에서 DOI … 를 찾아 메타만 확인하고,
ingest가 필요하면 무엇을 raw/papers에 넣을지 계획만 제안해.
실제 파일 쓰기는 내가 OK 한 뒤에만.
```

### 주간 리뷰 강제 실행 (테스트)
```text
second-brain-collect-review 작업을 지금 한 번 실행해줘.
canonical은 수정하지 말고 review-queue만 갱신한 뒤 요약해줘.
```

또는 PC 터미널:
```bash
hermes cron run 31830320217b
```

### 판정 반영 요청 (Accepted만)
```text
inbox/review-queue.md의 최신 블록을 읽어줘.
내가 Accepted라고 한 항목만 정리 계획을 제안하고,
실제 canonical 수정은 제안만 하고 실행은 물어봐.
```

## 역할 나누기 (Telegram 중심)

| 할 일 | Telegram (Hermes) | Cursor |
| --- | --- | --- |
| 수집 지시·알림 | ✅ 메인 | 보조 |
| inbox / review-queue | ✅ | 검수 |
| Cron 주간 리포트 | ✅ 자동 | — |
| SCHEMA 맞춘 canonical | 제안만 | ✅ 확정 |
| Gate B·복잡 lint | 요약 | ✅ 실행 |
| Clipper 웹 저장 | 브라우저 Clipper | Obsidian |

## 주의

- free 모델이 `entities/`·`concepts/`를 마음대로 고치면 SCHEMA가 깨질 수 있다 → **“승인 전 쓰기 금지”**를 매번 상기  
- 비밀·API 키·Zotero 키는 텔레그램에 보내지 않는다  
- OpenClaw 봇과 헷갈리지 말고 **Hermes `2nd_Brain_Template` 봇**만 이 vault용으로 쓴다

## 월요일 루틴

1. 봇이 Cron 요약 보냄  
2. `inbox/review-queue.md` 열기 (Obsidian 또는 봇에게 읽어 달라고 함)  
3. 판정 적기  
4. Accepted만 Cursor에서 “이건 Accepted야, compile 해줘”
