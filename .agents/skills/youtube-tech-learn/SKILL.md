---
name: youtube-tech-learn
description: >-
  Ingest a YouTube URL into technical learning notes using Google YouTube Data API
  metadata, captions (TranscriptAPI or youtube-transcript), and optional Whisper
  fallback. Use when the user pastes a YouTube link, asks to learn from a video,
  extract tech concepts, or save to raw/youtube for the 2nd Brain vault.
---

# YouTube Tech Learn

유튜브 링크 하나로 **기술 습득용 Evidence**를 만든다.  
Google Data API + 자막 API + Whisper 폴백을 순서대로 쓰고, 결과를 `raw/youtube/`와 학습 노트 템플릿으로 정리한다.

## When to use

- 사용자가 YouTube URL을 붙였을 때
- “이 영상에서 기술 정리해줘”, “학습 노트 만들어줘”, “raw에 저장해줘”
- OpenIPC / FPV / 드론 / 임베디드 등 기술 영상 수집

## Required environment

| 변수 | 필수 | 용도 |
|------|------|------|
| `YOUTUBE_API_KEY` | **권장** | Google YouTube Data API v3 — 제목·설명·채널·태그 |
| `TRANSCRIPT_API_KEY` | 선택 | TranscriptAPI (youtube-full 계열) — 안정적 자막 |
| `WIKI_ROOT` | 선택 | 기본: 현재 vault / `2nd_Brain_Template` |

Whisper 폴백(선택): `yt-dlp`, `ffmpeg`, `whisper` 또는 `whisper.cpp`가 PATH에 있어야 함.

## Pipeline (반드시 이 순서)

```
URL
 → ① Google Data API (메타 + description)     [공식]
 → ② 자막: TranscriptAPI → 실패 시 youtube-transcript
 → ③ 자막 품질 검사 (Music/OSD/너무 짧음 = poor)
 → ④ poor/none 이고 사용자가 Whisper 허용 시 → Whisper
 → ⑤ 학습 노트 작성 (아래 템플릿)
 → ⑥ raw/youtube/{videoId}.md 저장 + log.md ingest
```

**원칙**
- description(업로더 설명)이 기술 정보의 1순위인 경우가 많다. 자막만 믿지 말 것.
- 저품질 자막은 본문에 크게 싣지 말고 `<details>` 또는 경고만.
- 정식 concepts/ 승격은 **하지 않는다** (Human Gate). Evidence(`raw/`)만 작성.

## Agent steps

1. URL에서 videoId 추출 (`watch?v=`, `youtu.be/`, `shorts/`).
2. 스킬 디렉터리의 스크립트 실행:

```bash
# 메타 + 자막 수집 (JSON stdout)
node "$SKILL_DIR/scripts/fetch-evidence.mjs" "YOUTUBE_URL"

# Whisper 폴백 (자막 poor/none일 때만, 시간 소요)
bash "$SKILL_DIR/scripts/whisper-fallback.sh" "VIDEO_ID"
```

`$SKILL_DIR` = 이 `SKILL.md`가 있는 폴더.

3. 스크립트 JSON을 읽고 [references/learning-note-template.md](references/learning-note-template.md) 형식으로 **학습 노트**를 작성한다.
4. vault가 있으면 `raw/youtube/{videoId}.md`에 Evidence 원본을 쓴다 (frontmatter + 설명 + 양질 자막 + 학습 요약).
5. 사용자에게 보여줄 것:
   - 이 영상에서 배울 **핵심 기술 3~7개**
   - **학습 목표** / **개념 정리** / **따라할 체크리스트**
   - 원본 파일 경로
   - 다음에 볼 관련 키워드 (검색용)

## Quality gates

- [ ] Google API 또는 oEmbed로 제목·채널 확보
- [ ] description이 있으면 「영상 설명」섹션에 전문 포함
- [ ] 자막 quality=good일 때만 「자막 · 본문」에 본문급으로 포함
- [ ] 학습 노트에 “무엇을 배웠는지”가 추상어만이 아닌지 (구체 도구/명령/하드웨어명)
- [ ] raw 저장 시 `status: raw`, `source: youtube`

## Do NOT

- Google 키 없이 “공식 API 사용 중”이라고 거짓말하지 말 것
- 저품질 `[Music]` 자막을 기술 요약의 근거로 쓰지 말 것
- concepts/entities 자동 승격 금지

## Related

- vault의 `llm-wiki-ains` 스킬과 함께 쓰면 Evidence → Review 흐름에 맞춤
- 웹 UI: `2nd-brain-web`의 `/youtube` 수집 메뉴와 동일 파이프라인 지향
