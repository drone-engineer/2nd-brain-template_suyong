---
title: UAV Swarm Survey Landscape
created: 2026-08-24
updated: 2026-08-24
type: concept
tags:
  - uav
  - swarm
  - survey
  - research
sources:
  - raw/papers/2018-08-a-survey-on-aerial-swarm-robotics.md
  - raw/papers/2025-01-uav-swarms-research-challenges-and-future-directions.md
  - raw/papers/2024-08-from-pid-to-swarms-a-decade-of-advancements-in-drone-control-and-path-planning-a.md
  - raw/papers/2025-07-systematic-review-of-multi-objective-uav-swarm-mission-planning-systems-from-reg.md
  - raw/articles/2013-evolution-of-swarm-robotics-systems-with-novelty-search.md
  - raw/articles/2012-exploiting-particle-swarm-optimization-in-multiple-faults-fuzzy-detection.md
confidence: high
contested: false
contradictions: []
---

# UAV Swarm Survey Landscape

UAV swarm research covers a wide range of topics and approaches. A survey of the field reveals several key areas of focus.

## Key Research Areas

Recent surveys have consistently organized the field around several core axes:

- Formation Control → [[uav-formation-control]]
- Path Planning and Clustering → [[uav-swarm-path-planning]]
- Multi-Agent Reinforcement Learning Control → [[multi-agent-rl-uav-control]]
- Infrastructure, Security, Regulation, and Mission Planning → [[uav-swarm-survey-landscape]]

Alqudsi & Makaraci (2025) provide a comprehensive review organizing the research challenges and future directions of UAV swarms.^[raw/papers/2025-01-uav-swarms-research-challenges-and-future-directions.md]

## Research Challenges Table (from Alqudsi, 2025)

Based on Table 6 in the Zotero attachment `H89MMR98`, the following are key challenges and future directions:

- Heterogeneous swarms and surveillance ethics → blockchain/IoT and responsible deployment
- Energy efficiency and large-scale control algorithms → energy-aware AI/ML/DL
- Autonomous control and task allocation → collaborative assignment + AI/ML decision-making
- Communication and coordination (as scale increases, communication overhead grows) → 5G/6G, distributed, robust protocols
- Robustness and scalability → dynamic environment assignment, routing, motion coordination
- Synchronization and environmental interference → adaptive control
- Security and safety → threat detection and mitigation, policy and ethics framework

## Barriers to Field Adoption

The technical performance alone may not be sufficient for industry adoption. Checker et al. (2025) argue that the gap between mission planning features and legal/regulatory requirements represents a major barrier to field deployment.^[raw/papers/2025-07-systematic-review-of-multi-objective-uav-swarm-mission-planning-systems-from-reg.md]

Low-cost research platforms such as [[airswarm]] with COTS drone-based approaches are emerging.

## Software Stack (as of 2026-08-24)

The underlying platforms and tools supporting algorithmic research:

- **Firmware/Flight Stacks** → [[uav-autopilot-stacks]] (PX4 vs ArduPilot, Offboard/Companion structure)
- **Communication/Middleware** → [[uav-swarm-middleware]] (MAVLink/ROS 2/DDS; connected to consensus and Comm-MADRL)
- **Simulation** → [[uav-swarm-simulation]] (Gazebo/AirSim/Webots; reproducibility and sim-to-real)

## Foundational Methodologies (as of 2026-08-24)

The core algorithmic foundations for swarm intelligence:

- **Novelty Search (2013):** Using "novelty" as a reward to prevent premature convergence in evolutionary algorithms. Combined with NEAT neural networks for evolving control systems for homogeneous swarms. This approach provides a way to avoid deceptive fitness functions in evolutionary approaches. ^[raw/articles/2013-evolution-of-swarm-robotics-systems-with-novelty-search.md]
- **PSO Fault Detection (2012):** Using Particle Swarm Optimization (PSO) for optimal design of fuzzy detectors' membership functions. Applied to online detection of multiple faults using residue-based bonded graphs. This shows PSO's application in controller tuning and fault detection, which is used in collision avoidance frameworks like E2CoPre. ^[raw/articles/2012-exploiting-particle-swarm-optimization-in-multiple-faults-fuzzy-detection.md]

Insight: The foundation of swarm intelligence draws from **evolutionary computation (novelty search)** and **swarm optimization (PSO)**. State-of-the-art MARL and collision avoidance methods build upon these foundational approaches.

## Limitations

Some publications in IEEE/Elsevier/MDPI have only abstracts or metadata available locally, with full PDFs missing from Zotero. Only Alqudsi and AirSwarm have confirmed PDF access (`docs/workflow/zotero-pdf-status.md`).