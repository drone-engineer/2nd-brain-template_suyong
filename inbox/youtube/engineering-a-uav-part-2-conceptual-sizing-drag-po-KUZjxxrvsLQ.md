---
title: "Engineering a UAV - Part 2: Conceptual Sizing, Drag Polars, & Constraint Analysis"
created: 2026-07-29
updated: 2026-07-29
type: inbox-note
tags:
  - youtube
  - learning
  - inbox
sources:
  - "raw/youtube/KUZjxxrvsLQ.md"
video_id: "KUZjxxrvsLQ"
channel: "GabeFPV"
url: "https://www.youtube.com/watch?v=KUZjxxrvsLQ"
status: draft
---

# Engineering a UAV - Part 2: Conceptual Sizing, Drag Polars, & Constraint Analysis

> 출처: [GabeFPV](https://www.youtube.com/watch?v=KUZjxxrvsLQ) · 수집: 2026-07-29 · [[raw/youtube/KUZjxxrvsLQ|원본 Evidence]]

## 이 영상에서 배울 것
- Intro
- Drag
- Polar
- Overview
- Wetted

## 학습 목표
1. 영상에서 다루는 핵심 기술/도구의 역할을 한 문장으로 설명할 수 있다.
2. 챕터(또는 키워드) 기준으로 따라갈 실습·복습 항목을 정리한다.
3. 원본 Evidence와 연결해 나중에 [[concepts]] 승격 후보를 고른다.

## 목차 · 챕터
- `00:00` Intro
- `01:31` Drag Polar Overview
- `02:20` Wetted Aspect Ratio
- `06:09` Drag Polar Buildup
- `10:01` Important Airspeeds
- `14:01` Turning/Loitering
- `15:52` Empty Weight Methods
- `17:29` Empty Weight Estimation
- `19:37` Conceptual Sizing Loop
- `21:25` Constraint Analysis
- `26:16` Design Point Selection
- `30:47` Summary

## 핵심 개념 (초안)
### 1. Intro
- 한 줄 정의: Intro — 이 영상에서 다루는 핵심 키워드(원문에서 역할 확인).
- 영상 맥락: `00:00` Intro

### 2. Drag
- 한 줄 정의: 영상/설명 맥락: Engineering a UAV - Part 2: Conceptual Sizing, Drag Polars, & Constraint Analysis
- 영상 맥락: `01:31` Drag Polar Overview

### 3. Polar
- 한 줄 정의: 영상/설명 맥락: Engineering a UAV - Part 2: Conceptual Sizing, Drag Polars, & Constraint Analysis
- 영상 맥락: `01:31` Drag Polar Overview

### 4. Overview
- 한 줄 정의: 영상/설명 맥락: 01:31 Drag Polar Overview
- 영상 맥락: `01:31` Drag Polar Overview

## 실습 체크리스트
- [ ] Intro 구간 복습
- [ ] Drag Polar Overview 구간 복습
- [ ] Wetted Aspect Ratio 구간 복습
- [ ] Drag Polar Buildup 구간 복습
- [ ] Important Airspeeds 구간 복습

## 확장 검색 (관련 지식)

> 핵심 부품명을 설명·제목에서 찾지 못했습니다. 원문 설명을 확인하세요.

**추출 키워드:** _(추출 실패)_

아래 쿼리로 논문 검색(`/search`)을 열어 관련 지식을 확장하세요.

- _(쿼리 없음)_

- [ ] 관심 논문은 `raw/` 저장 후 Human Gate에서 concepts 후보 검토

## 명령·링크 메모
```
In Part 2, we continue a series of videos diving into all aspects of aircraft design, at a small scale. This video covers Conceptual Sizing, Drag Polars, and Energy-Based Constraint Analysis (all at very basic levels), also touching on the differences between propeller-driven and jet driven performance and how each differs when performing constraint analysis and power sizing. Remember, the target at this stage is the derivation of the design point: Thrust/Weight Ratio, Wingloading, and Design/Takeoff Weight

I also realize that I totally forgot to cover the lift curve in this video, so I'll discuss it in part 3!

I work super hard to take down the paywall to deliver this information in the most digestible manner possible; I make these videos to help people learn about aircraft design, and I hate the institutional paywall. Between full-time engineering and grad school, making these takes nearly 100% of my free time. If you've found these helpful, let me know and we can share a coffee/beer over it!: 
https://buymeacoffee.com/gabefpv

(BTW, if you want black borders on the video instead of gray, click on the gear icon on the bottom right of the video and turn off 'Ambient Mode')

Important Sources:
AIAA: Raymer, D. P., Aircraft Design: A Conceptual Approach, 6th ed., American Institute of Aeronautics and Astronautics, Reston, VA, 2018.
Keane, A. J., Sóbester, A., and Scanlan, J. P., Small Unmanned Fixed-wing Aircraft Design: A Practical Approach, Wiley, Hoboken, NJ, 2017.
Finger, D. F., "Comparative Performance and Benefit Assessment of VTOL and CTOL UAVs," Proceedings of the International Micro Air Vehicle Conference and Flight Competition (IMAV), 2017.
Sztajnbok, I., et al., "Drag Characterization of a Fixed-Wing Unmanned Aerial Vehicle (UAV) with COTS Avionics through Flight Testing," 2025.
Finger, D. F., Bil, C., and Braun, C., "Drag Estimation of Small Fixed-Wing UAVs," The Aeronautical Journal, Vol. 122, No. 1248, 2018.
"Flight Testing Small Electric Powered Unma
```

## 자막 발췌 (한글)

> 양질 자막을 한글로 번역한 발췌입니다. 전체·원문은 원본 Evidence를 참고하세요.

이것은 첫 번째 백지 개념부터 최종 비행 테스트 데이터 상관 관계까지 고정익 UAV에 대한 전체 엔지니어링 주기를 함께 실행하는 7부작 비디오 시리즈 중 2부입니다.

단순히 드론을 만드는 것이 아닙니다.

이는 실제 엔지니어링 프로세스와 UAV가 이렇게 보이는 이유, 왜 그렇게 비행하는지, 왜 그렇게 설계되었는지, 그리고 각 엔지니어링 프로세스를 진행하는 방법을 학습하고 그 과정에서 점들을 연결하여 비행 가능한 UAV를 완성하는 방법을 학습하는 것입니다.

초기 단계에서 정의된 일부 임무를 성공적으로 수행합니다.

지난 비디오에서는 임무 정의, 요구 사항, 설계 포인트, 그리고 제트 구동 항공기와 프로펠러 구동 항공기 간의 성능 차이에 대해 이해해야 할 몇 가지 핵심 사항과 연료 연소에 대한 가장 기본적인 임무 분석 방정식을 다뤘습니다.

그리고 전기 항공기.

이번 비디오에서는 드래그 극성, 무게 비율 추정, 제약 조건 분석 등을 사용하여 설계 지점에 도달하는 방법을 포함하여 개념적 크기 조정에 대해 좀 더 기술적으로 이야기하겠습니다.

알았어, 그렇게 말하면 시간 낭비는 충분해. 허락하다'…

<details><summary>영문 원문 발췌</summary>

This is part two of my seven-part video series where we are together executing a complete engineering cycle for a fixed-wing UAV from the first blank sheet concept to the final flight test data correlation.

This isn't about just building a drone.

This is about learning the actual engineering process and reasons behind why UAVs look the way they do, why they fly the way they do, and why they're designed the way they are, and how to walk through each of the engineering processes, connecting the dots along the way to result in a finished flyable UAV

that successfully flies some mission defined in the early stages.

Last video, I covered mission definitions, requirements, design points, and a few key things to understand about the performative differences between jet-driven aircraft and propeller-driven aircraft, as well as some of the most basic mission analysis equations for both fuel burning

and electric aircraft.

This video, we'll be talking more technically this time about conceptual sizing, including how to arrive at a design point using things like drag polars, weight fraction estimations, and constraint analysis.

All right, with that said, that's enough wasting time. Let'…

</details>

## 원본 Evidence
- 경로: `raw/youtube/KUZjxxrvsLQ.md`
- 위키링크: [[raw/youtube/KUZjxxrvsLQ]]
- 자막 품질: good

## 다음에 연결할 키워드
- Intro
- Drag
- Polar
- Overview
- Wetted

## Human Gate
- [ ] 내용 검토 후 필요 시 `concepts/` 로 승격
- [ ] 승격 시 `sources` 에 raw 경로 유지
