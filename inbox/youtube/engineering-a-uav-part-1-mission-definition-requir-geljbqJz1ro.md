---
title: "Engineering a UAV - Part 1: Mission Definition, Requirements, & Design Point"
created: 2026-07-29
updated: 2026-07-29
type: inbox-note
tags:
  - youtube
  - learning
  - inbox
sources:
  - "raw/youtube/geljbqJz1ro.md"
video_id: "geljbqJz1ro"
channel: "GabeFPV"
url: "https://www.youtube.com/watch?v=geljbqJz1ro"
status: draft
---

# Engineering a UAV - Part 1: Mission Definition, Requirements, & Design Point

> 출처: [GabeFPV](https://www.youtube.com/watch?v=geljbqJz1ro) · 수집: 2026-07-29 · [[raw/youtube/geljbqJz1ro|원본 Evidence]]

## 이 영상에서 배울 것
- Intro
- Design
- Conceptual
- Preliminary

## 학습 목표
1. 영상에서 다루는 핵심 기술/도구의 역할을 한 문장으로 설명할 수 있다.
2. 챕터(또는 키워드) 기준으로 따라갈 실습·복습 항목을 정리한다.
3. 원본 Evidence와 연결해 나중에 [[concepts]] 승격 후보를 고른다.

## 목차 · 챕터
- `0:00` Intro
- `01:50` What is Design?
- `05:25` Conceptual Design
- `07:31` Preliminary Design
- `08:57` Detailed Design
- `10:16` Sizing & Synthesis
- `12:00` Who's the Customer?
- `14:10` Requirements
- `19:49` Conceptual Sizing
- `25:18` Electric Propulsion Fundamentals
- `27:09` Thrust Lapse
- `30:36` Summary

## 핵심 개념 (초안)
### 1. Intro
- 한 줄 정의: Intro — 이 영상에서 다루는 핵심 키워드(원문에서 역할 확인).
- 영상 맥락: `0:00` Intro

### 2. Design
- 한 줄 정의: 영상/설명 맥락: Engineering a UAV - Part 1: Mission Definition, Requirements, & Design Point
- 영상 맥락: `01:50` What is Design?

### 3. Conceptual
- 한 줄 정의: 영상/설명 맥락: , Aircraft Design: A Conceptual Approach, 6th ed
- 영상 맥락: `05:25` Conceptual Design

### 4. Preliminary
- 한 줄 정의: 영상/설명 맥락: So, once conceptual design has converged onto a viable configuration, we then move into what we call preliminary design
- 영상 맥락: `07:31` Preliminary Design

## 실습 체크리스트
- [ ] Intro 구간 복습
- [ ] What is Design? 구간 복습
- [ ] Conceptual Design 구간 복습
- [ ] Preliminary Design 구간 복습
- [ ] Detailed Design 구간 복습

## 확장 검색 (관련 지식)

> 핵심 부품명을 설명·제목에서 찾지 못했습니다. 원문 설명을 확인하세요.

**추출 키워드:** _(추출 실패)_

아래 쿼리로 논문 검색(`/search`)을 열어 관련 지식을 확장하세요.

- _(쿼리 없음)_

- [ ] 관심 논문은 `raw/` 저장 후 Human Gate에서 concepts 후보 검토

## 명령·링크 메모
```
In Part 1, we begin a series of videos diving into all aspects of aircraft design, at a small scale. This video covers Mission Definition, Requirements, and Design Points, also touching on how thrust changes throughout flight and a few other small, but important, topics for the design process. 

I make these videos to help people learn about aircraft design, I hate the institutional paywall. Between full-time engineering and grad school, making these takes nearly 100% of my free time. If you've found these helpful, let me know and we can share a coffee/beer over it!: 
https://buymeacoffee.com/gabefpv

(BTW, if you want black borders on the video instead of gray, click on the gear icon on the bottom right of the video and turn off 'Ambient Mode')

Important Sources:
AIAA: Raymer, D. P., Aircraft Design: A Conceptual Approach, 6th ed., American Institute of Aeronautics and Astronautics, Reston, VA, 2018.
Keane, A. J., Sóbester, A., and Scanlan, J. P., Small Unmanned Fixed-wing Aircraft Design: A Practical Approach, Wiley, Hoboken, NJ, 2017.
Finger, D. F., "Comparative Performance and Benefit Assessment of VTOL and CTOL UAVs," Proceedings of the International Micro Air Vehicle Conference and Flight Competition (IMAV), 2017.
Sztajnbok, I., et al., "Drag Characterization of a Fixed-Wing Unmanned Aerial Vehicle (UAV) with COTS Avionics through Flight Testing," 2025.
Finger, D. F., Bil, C., and Braun, C., "Drag Estimation of Small Fixed-Wing UAVs," The Aeronautical Journal, Vol. 122, No. 1248, 2018.
"Flight Testing Small Electric Powered Unmanned Aerial Vehicles," Technical Report/Paper.
Mattingly, J. D., Heiser, W. H., and Pratt, D. T., Aircraft Engine Design, 2nd ed., American Institute of Aeronautics and Astronautics, Reston, VA, 2002.

Timestamps:

0:00 Intro
01:50 What is Design?
05:25 Conceptual Design
07:31 Preliminary Design
08:57 Detailed Design
10:16 Sizing & Synthesis
12:00 Who's the Customer?
14:10 Requirements
19:49 Conceptual Sizing
25:18 Electric Propulsion 
```

## 자막 발췌 (한글)

> 양질 자막을 한글로 번역한 발췌입니다. 전체·원문은 원본 Evidence를 참고하세요.

저는 우리가 함께 고정익 UAV에 대한 완전한 준전문 엔지니어링 사이클을 수행할 7부작 비디오 시리즈를 시작하겠습니다.

이는 첫 번째 백지 개념부터 최종 비행 테스트 데이터 상관 관계까지의 의미입니다. 일반적인 취미 작업 흐름을 살펴보면 일반적으로 특정 성능을 달성할 수 있다고 생각하는 대략적인 아이디어나 종이에 그린 멋진 그림으로 시작됩니다. 그런 다음 아이디어는 곧장 CAD로 옮겨져

실제로 엔지니어링이 거의 또는 전혀 수행되지 않았습니다. 그리고 그것은 대부분 우연히 작동하는 비행 테스트로 끝납니다. 우리는 그렇게 하지 않습니다. 저는 고정익 UAV 규모까지 축소된 항공기 설계 프로그램의 실제 단계를 안내해 드리겠습니다.

단순히 드론을 만드는 것이 아닙니다.

이는 UAV가 왜 그렇게 보이는지, 왜 그렇게 비행하는지, 적어도 비생산량에서 왜 그렇게 제작되는지에 대한 실제 엔지니어링 프로세스를 배우는 것입니다. 그리고 우리는 이러한 모든 프로세스를 진행하는 방법, 특히

실제로 설계된 일부 임무를 성공적으로 비행하는 하나의 완성된 비행 가능한 UAV를 만들기 위해 점을 찍습니다.

<details><summary>영문 원문 발췌</summary>

I'm kicking off a seven-part video series where we are together going to perform a complete semi-professional engineering cycle for a fixed-wing UAV.

That meaning from the first blank sheet concepts to the final flight test data correlation. If you look at a typical hobbyist workflow, it usually starts with a rough idea or a cool drawing on paper that they think will achieve some specific performance. And the idea then moves straight to CAD and building with

little to no engineering actually performed. And that ends with a flight test that works mostly by accident. We are not doing that. I'm going to walk us all the way through the real phases of an aircraft design program scaled all the way down to the scale of a fixed-wing UAV.

This isn't about just building a drone.

This is about learning the actual engineering process behind why UAVs look the way they do, why they fly the way they do, and why they're built the way they are, at least at non-production volumes. And we'll be focusing on how to walk through every one of these processes, especially connecting the

dots along the way to result in one finished flyable UAV that successfully flies some mission designed in the really…

</details>

## 원본 Evidence
- 경로: `raw/youtube/geljbqJz1ro.md`
- 위키링크: [[raw/youtube/geljbqJz1ro]]
- 자막 품질: good

## 다음에 연결할 키워드
- Intro
- Design
- Conceptual
- Preliminary

## Human Gate
- [ ] 내용 검토 후 필요 시 `concepts/` 로 승격
- [ ] 승격 시 `sources` 에 raw 경로 유지
