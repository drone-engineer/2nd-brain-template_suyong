---
source_url: https://arxiv.org/abs/1612.00480v1
ingested: 2026-08-03
sha256: 2f3f03b57608977a402b96b4b41e8d5f529a2c91acd4e76e453a8573022c6234
title: A Scalable and Adaptable Multiple-Place Foraging Algorithm for Ant-Inspired Robot Swarms
authors: Qi Lu, Melanie E. Moses, Joshua P. Hecker
year: 2016
arxiv_id: 1612.00480v1
---

# A Scalable and Adaptable Multiple-Place Foraging Algorithm for Ant-Inspired Robot Swarms

**출처:** https://arxiv.org/abs/1612.00480v1
**저자:** Qi Lu, Melanie E. Moses, Joshua P. Hecker
**발행년도:** 2016
**arXiv ID:** 1612.00480v1
**OA PDF:** https://arxiv.org/pdf/1612.00480v1

## 초록 (Abstract)

Individual robots are not effective at exploring large unmapped areas. An alternate approach is to use a swarm of simple robots that work together, rather than a single highly capable robot. The central-place foraging algorithm (CPFA) is effective for coordinating robot swarm search and collection tasks. Robots start at a centrally placed location (nest), explore potential targets in the area without global localization or central control, and return the targets to the nest. The scalability of the CPFA is limited because large numbers of robots produce more inter-robot collisions and large search areas result in substantial travel costs. We address these problems with the multiple-place foraging algorithm (MPFA), which uses multiple nests distributed throughout the search area. Robots start from a randomly assigned home nest but return to the closest nest with found targets. We simulate the foraging behavior of robot swarms in the robot simulator ARGoS and employ a genetic algorithm to discover different optimized foraging strategies as swarm sizes and the number of targets are scaled up. In our experiments, the MPFA always produces higher foraging rates, fewer collisions, and lower travel and search time compared to the CPFA for the partially clustered targets distribution. The main contribution of this paper is that we systematically quantify the advantages of the MPFA (reduced travel time and collisions), the potential disadvantages (less communication among robots), and the ability of a genetic algorithm to tune MPFA parameters to mitigate search inefficiency due to less communication.
