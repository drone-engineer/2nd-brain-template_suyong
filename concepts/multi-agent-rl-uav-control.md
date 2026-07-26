---
title: Multi-Agent RL for UAV Control
created: 2026-07-24
updated: 2026-07-26
type: concept
tags:
  - uav
  - swarm
  - control
  - survey
sources:
  - raw/papers/2025-07-a-survey-on-uav-control-with-multi-agent-reinforcement-learning.md
  - raw/papers/2024-07-advancement-challenges-in-uav-swarm-formation-control-a-comprehensive-review.md
  - raw/articles/2023-faster-consensus-via-a-sparser-controller.md
  - raw/articles/2020-variational-policy-propagation-for-multi-agent-reinforcement-learning.md
  - raw/articles/2025-learning-bilateral-team-formation-in-cooperative-multi-agent-reinforcement-learn.md
  - raw/articles/2026-interference-aware-k-step-reachable-communication-in-multi-agent-reinforcement-l.md
confidence: medium
contested: false
contradictions: []
---

# Multi-Agent RL for UAV Control

Multi-Agent Reinforcement Learning(MARL)은 여러 UAV가 환경·서로와 상호작용하며 협력 정책을 학습하는 프레임워크다. 전통 제어가 동적·불확실·대규모 분산 의사결정에서 한계를 보일 때 대안으로 논의된다. ^[raw/papers/2025-07-a-survey-on-uav-control-with-multi-agent-reinforcement-learning.md]

## 서베이가 말하는 상태

Ekechi et al.(2025)은 UAV 제어에 적용된 MARL을 체계적으로 분류하고 경향·공백을 정리한다. 알고리즘·아키텍처·평가 지표가 도메인별로 파편화되어 있어, 협력적 공중 로봇을 위한 공통 기반이 필요하다고 본다. ^[raw/papers/2025-07-a-survey-on-uav-control-with-multi-agent-reinforcement-learning.md]

편대 제어 리뷰에서도 DRL이 고급 AI 축으로 등장하며, 전통 방법과의 결합이 과제로 남는다([[uav-formation-control]]). ^[raw/papers/2024-07-advancement-challenges-in-uav-swarm-formation-control-a-comprehensive-review.md]

상위 맥락은 [[uav-swarm-robotics]], 문헌 지도는 [[uav-swarm-survey-landscape]]를 본다.

## 합의 수렴·통신·팀 형성의 최신 진전 (2026-07-26 신규)

MARL을 군집드론에 굴릴 때 풀어야 할 세 하위 문제가 최신 논문에서 구체화된다.

- **빠른 합의(Faster Consensus, 2023):** 단일 적분자动力学 합의에서 수렴 속도를 최대화하는 최적 제어기를 찾은 결과, 통신 지연이 홉 수에 비례할 때 **최적 제어기는 희소 연결(sparser) 구조**를 갖는다. → "모두와 연결"보다 "전략적 희소 연결"이 빠름. ^[raw/articles/2023-faster-consensus-via-a-sparser-controller.md]
- **변분 정책 전파(VPP, 2020):** MARL에서 결합 정책을 마르코프 랜덤필드(MRF)로 보고 변분 추론을 미분 가능 레이어로 삽입. 정책 공간을 효과적으로 축소하며 샘플링 효율을 높인다. ^[raw/articles/2020-variational-policy-propagation-for-multi-agent-reinforcement-learning.md]
- **양측 팀 형성(Bilateral Team Formation, 2025):** 기존이 고정/편측 팀이었던 것을 동적 집단에서의 **양측 팀 형성 학습**으로 확장. 인구가 변하는 환경에서 알고리즘적 그룹핑 선택 효과를 실증. ^[raw/articles/2025-learning-bilateral-team-formation-in-cooperative-multi-agent-reinforcement-learn.md]
- **간섭 인지 K-스텝 통신(IARCoM, 2026):** 제한된 대역폭·동적 위상에서 "통신할 가치 있는 파트너"를 K-스텝 도달 가능성 + 간섭으로 판단. 불확실한 환경에서 고가치 협력자를 선별. ^[raw/articles/2026-interference-aware-k-step-reachable-communication-in-multi-agent-reinforcement-l.md]

시사점: MARL 군집드론은 **통신 토폴로지 설계(희소화·간섭 인지)** 와 **정책 표현(MRF·팀 형성)** 두 축이 병목. 합의 속도·학습 효율·통신 비용을 동시에 다루는 통합 프레임워크가 부족하다.
