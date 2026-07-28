---
title: A Decision-theoretic Approach to Detection-based Target Search with a UAV
authors: Aayush Gupta; Daniel Bessonov; Patrick Li
arxiv_id: 1801.01228v1
published: 2018-01-04
source_type: arxiv
collected: 2026-07-27
sha256: 00b45861939544cd6e54b558caf88ce6956393ad4b03144277ca4cae223f4a26
---

# A Decision-theoretic Approach to Detection-based Target Search with a UAV

## 메타데이터
- arXiv: 1801.01228v1
- 저자: Aayush Gupta; Daniel Bessonov; Patrick Li
- 출판일: 2018-01-04
- 수집: 2026-07-27 (Hunter-Killer PRD 관련 기술 검토용)

## 초록
Search and rescue missions and surveillance require finding targets in a large area. These tasks often use unmanned aerial vehicles (UAVs) with cameras to detect and move towards a target. However, common UAV approaches make two simplifying assumptions. First, they assume that observations made from different heights are deterministically correct. In practice, observations are noisy, with the noise increasing as the height used for observations increases. Second, they assume that a motion command executes correctly, which may not happen due to wind and other environmental factors. To address these, we propose a sequential algorithm that determines actions in real time based on observations, using partially observable Markov decision processes (POMDPs). Our formulation handles both observations and motion uncertainty and errors. We run offline simulations and learn a policy. This policy is run on a UAV to find the target efficiently. We employ a novel compact formulation to represent the coordinates of the drone relative to the target coordinates. Our POMDP policy finds the target up to 3.4 times faster when compared to a heuristic policy.

---
*raw evidence — immutable.*
