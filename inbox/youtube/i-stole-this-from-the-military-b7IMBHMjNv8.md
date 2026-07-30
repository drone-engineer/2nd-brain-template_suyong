---
title: "I Stole This from the Military"
created: 2026-07-29
updated: 2026-07-29
type: inbox-note
tags:
  - youtube
  - learning
  - inbox
sources:
  - "raw/youtube/b7IMBHMjNv8.md"
video_id: "b7IMBHMjNv8"
channel: "Data Slayer"
url: "https://www.youtube.com/watch?v=b7IMBHMjNv8"
status: draft
---

# I Stole This from the Military

> 출처: [Data Slayer](https://www.youtube.com/watch?v=b7IMBHMjNv8) · 수집: 2026-07-29 · [[raw/youtube/b7IMBHMjNv8|원본 Evidence]]

## 이 영상에서 배울 것
- LoRa
- Raspberry Pi
- OpenWRT
- IP mesh
- mesh

## 학습 목표
1. 영상에서 다루는 핵심 기술/도구의 역할을 한 문장으로 설명할 수 있다.
2. 챕터(또는 키워드) 기준으로 따라갈 실습·복습 항목을 정리한다.
3. 원본 Evidence와 연결해 나중에 [[concepts]] 승격 후보를 고른다.

## 목차 · 챕터
- (챕터 없음)

## 핵심 개념 (초안)
### 1. LoRa
- 한 줄 정의: 저전력·장거리 무선 통신 방식. Wi-Fi/Bluetooth보다 멀리 보내지만 데이터 속도는 낮다.
- 영상 맥락: Same neighborhood spectrum as projects like LoRa and Meshtastic in the US, which is why it carries signals like those builds do

### 2. Raspberry Pi
- 한 줄 정의: 리눅스가 돌아가는 SBC(싱글보드 컴퓨터). 게이트웨이·메시·영상 처리에 자주 쓴다.
- 영상 맥락: I put the newest long-range radio chip on a Raspberry Pi 5 — a $246 build that does what $20,000 military mesh radios do

### 3. OpenWRT
- 한 줄 정의: 임베디드용 오픈소스 리눅스 라우터 OS. 커스텀 무선/메시 스택을 올리기 좋다.
- 영상 맥락: 05 out of an OpenWRT '24 tree and using Claude to debug every incompatibility error that was thrown at build time for several days until …

### 4. IP mesh
- 한 줄 정의: 다수 노드가 서로 중계해 인터넷 없이도 통신망을 유지하는 메시 네트워킹.
- 영상 맥락: One of them is a military-grade IP mesh radio

## 실습 체크리스트
- [ ] LoRa 정의·역할을 내 말로 다시 쓰기
- [ ] Raspberry Pi 정의·역할을 내 말로 다시 쓰기
- [ ] OpenWRT 정의·역할을 내 말로 다시 쓰기
- [ ] IP mesh 정의·역할을 내 말로 다시 쓰기

## 확장 검색 (관련 지식)

> LoRa 기반 센싱·무선 전송 시스템

**추출 키워드:** `LoRa` · `Raspberry Pi` · `OpenWRT` · `IP mesh` · `mesh`

아래 쿼리로 논문 검색(`/search`)을 열어 관련 지식을 확장하세요.

- **종합**: [`LoRa`](/search?q=LoRa)
- **키워드**: [`LoRa Raspberry Pi OpenWRT IP mesh mesh`](/search?q=LoRa%20Raspberry%20Pi%20OpenWRT%20IP%20mesh%20mesh)

- [ ] 관심 논문은 `raw/` 저장 후 Human Gate에서 concepts 후보 검토

## 명령·링크 메모
```
Built with $240 and zero remorse...

I put the newest long-range radio chip on a Raspberry Pi 5 — a $246 build that does what $20,000 military mesh radios do. I'll show you how I built it, how it compares spec-for-spec, and a live field test that proves it works. No subscriptions, no closed firmware, fully open-source.

Build your own $20,000 MANET for $97 👉 https://buildwithparallel.com/products/haven

New OpenWRT/MorseMicro Raspberry Pi 5 Image 👉 https://github.com/buildwithparallel/openwrt-morse-rpi5

MM8108 Halow Chip 👉 https://www.digikey.com/en/products/detail/gateworks-corporation/GW16167/28244003

Watch these next:

I Built a $20,000 Military Router for $106.23
https://www.youtube.com/watch?v=ofR7GFNZzJY

I Built a $40,000 Military Drone for $120.07
https://www.youtube.com/watch?v=bmLE9BT76Pc



🎥 NEW: Unlock MEMBERS-ONLY videos and behind-the-scenes drops 👉 https://bit.ly/4iyBm4I
🛠️ The exact tools and gear I trust (and actually use) 👉 https://amzn.to/44fKDv4
📡 Join the r/ModernRadio community for LoRa, Meshtastic, and off-grid tech builds  👉 https://reddit.com/r/ModernRadio
💬 Get real-time help and connect with other builders on Discord  👉 https://discord.gg/g7h8Jc7Agt
📚 Step-by-step setup guides, templates, and insider resources 👉 https://bit.ly/4ivZDID
🛒 Grab custom gear and tools designed by me 👉 https://etsy.me/4isKwjb
📩 For sponsorships or business inquiries, reach out: macgyvertechnology@gmail.com
🧠 Need expert help fast? Book a 1:1 session and get unstuck today 👉 https://bit.ly/42I10y5
```

## 자막 발췌 (한글)

> 양질 자막을 한글로 번역한 발췌입니다. 전체·원문은 원본 Evidence를 참고하세요.

비용은 $20,000이고 비용은 $246.04에 불과합니다.

그 중 하나는 군용 IP 메시 라디오입니다. 다른 하나는 내 책상 위에 놓여 있는 Raspberry Pi 5입니다. 하지만 그들은 똑같은 일을 합니다. 알았어, 알았어. 나는 포트 브래그에 밧줄을 묶고 펠리칸 케이스에서 하나를 꺼내지 않았다. 하지만 저는 장거리에 걸쳐 통신망을 분리하여 라우팅하는 IP 메시라는 아이디어를 차용했습니다.

인터넷 없이도 그것을 Raspberry Pi 5에 탑재했습니다. 시중에서 판매되는 최신 장거리 무선 칩과 사상 최초로 함께 작동하는 가장 강력한 Pi를 탑재했습니다. 나는 지금까지 이 일에 대해 아무에게도 말하지 않았습니다.

이것이 Haven 2입니다. 차고에 3D 프린터와 GitHub 계정이 있는 사람이 이제 대부분의 사람들이 기성품으로 구매하는 것보다 성능이 뛰어나고 DoD가 메쉬 라디오 공간에서 공급업체에 지불하는 가격과 겹치는 라우터를 구축할 수 있습니다. 이제 Haven 1이 올해 초에 출시되어 신경이 쓰였습니다.

매주 내 피드에 수백 개의 빌드, 사진, 내 급여 등급보다 훨씬 높은 사람들의 봉사 활동이 있습니다. 하지만 해당 설정은 Pi 4에서만 실행되었습니다. 그래서 "Pi 5에서는 언제 작동할까요?"라는 같은 질문을 계속 받았습니다. 그리고 그 질문에 답하기 위해 저는 Halo 칩 제조업체인 Morris Micr에게 이메일을 보냈습니다.

<details><summary>영문 원문 발췌</summary>

This costs $20,000, and this costs only $246.04.

One of them is a military-grade IP mesh radio. The other is a Raspberry Pi 5 sitting on my desk. But, they do the same thing. Okay, okay, I didn't fast rope into Fort Bragg and pry one out of a Pelican case. But, I did borrow the idea, which is an IP mesh that routes your comms off-grid over long distances

without internet, and I put that on a Raspberry Pi 5. The newest long-range radio chip on the market plus the most powerful Pi ever made working together for the first time ever. I've told absolutely no one about this until now.

This is Haven 2. Cuz here's the thing, a guy in his garage with a 3D printer and a GitHub account can now build a router that outperforms what most people buy off the shelf and overlaps with what the DoD pays vendor rates for in the mesh radio space. Now, Haven 1 shipped earlier this year, and it hit a nerve.

Hundreds of builds, photos in my feed every week, and outreach from people way above my pay grade. But, that setup only ran on the Pi 4. So, I kept getting the same question, "When will this work on a Pi 5?" And in an effort to answer that question, I emailed the Halo chip manufacturer, Morris Micr…

</details>

## 원본 Evidence
- 경로: `raw/youtube/b7IMBHMjNv8.md`
- 위키링크: [[raw/youtube/b7IMBHMjNv8]]
- 자막 품질: good

## 다음에 연결할 키워드
- LoRa
- Raspberry Pi
- OpenWRT
- IP mesh
- mesh

## Human Gate
- [ ] 내용 검토 후 필요 시 `concepts/` 로 승격
- [ ] 승격 시 `sources` 에 raw 경로 유지
