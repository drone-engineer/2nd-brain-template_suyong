---
title: tinySLAM-based exploration with a swarm of nano-UAVs
authors: Johan Markdahl; Mattias Vikgren
arxiv_id: 2309.02834v1
published: 2023-09-06
source_type: arxiv
collected: 2026-07-26
sha256: 37b560cbc7c74ab1550a4211b66973fe5a702b791a0ddd186a3c709e87dc93b2
---

# tinySLAM-based exploration with a swarm of nano-UAVs

## 메타데이터
- arXiv: 2309.02834v1
- 저자: Johan Markdahl; Mattias Vikgren
- 출판일: 2023-09-06
- 수집: 2026-07-26 (플랫폼 실증 검토용)

## 초록
This paper concerns SLAM and exploration for a swarm of nano-UAVs. The laser range finder-based tinySLAM algorithm is used to build maps of the environment. The maps are synchronized using an iterative closest point algorithm. The UAVs then explore the map by steering to points selected by a modified dynamic coverage algorithm, for which we prove a stability result. Both algorithms inform each other, allowing the UAVs to map out new areas of the environment and move into them for exploration. Experimental findings using the nano-UAV Crazyflie 2.1 platform are presented. A key challenge is to implement all algorithms on the hardware limited experimental platform.

---
*raw evidence — immutable. 플랫폼/미들웨어/시뮬 실증 맥락에서 수집됨.*
