# 학습 노트 템플릿 (YouTube Tech Learn)

에이전트는 수집 JSON을 바탕으로 아래 형식으로 작성한다.

```markdown
# {title}

> 출처: [{channel}]({url}) · 수집: {date} · video_id: `{videoId}`

## 이 영상에서 배울 것
- (구체적 기술/도구/개념 3~7개)

## 학습 목표
1. …
2. …

## 핵심 개념
### {개념1}
- 한 줄 정의
- 영상에서 나온 맥락 / 명령 / 하드웨어

### {개념2}
…

## 실습 체크리스트
- [ ] …
- [ ] …

## 명령·링크 메모
(업로더 description / 자막에서 뽑은 명령어, 레포, 구매 링크)

## 원본 Evidence
- 경로: `raw/youtube/{videoId}.md`
- 자막 품질: good | poor | none | whisper
- 설명 확보: yes | no

## 다음에 연결할 키워드
(논문 검색 / 웹 수집용 쿼리)
```

## Evidence 파일 (`raw/youtube/{videoId}.md`) frontmatter

```yaml
---
title: "..."
channel: "..."
video_id: "..."
url: "https://www.youtube.com/watch?v=..."
thumbnail: "..."
captured_at: "ISO-8601"
source: youtube
has_description: true
has_transcript: true
transcript_quality: good
transcript_source: google-caption | transcriptapi | youtube-transcript | whisper
status: raw
tags: [openipc, fpv, ...]
---
```
