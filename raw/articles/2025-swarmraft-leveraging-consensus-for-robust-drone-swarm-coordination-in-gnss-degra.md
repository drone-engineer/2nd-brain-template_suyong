---
source_url: https://www.semanticscholar.org/paper/a97810f737efe5f0ee78072d1ce026dff22e2ebe
ingested: 2026-08-10
sha256: 5ebec0bfb0745082bcee83f25ce983c69faebee6a0ce4c7c71c2ea6c0dd5594c
title: SwarmRaft: Leveraging Consensus for Robust Drone Swarm Coordination in GNSS-Degraded Environments
authors: Kapel Dev, Yash Madhwal, Sofia Shevelo, Pavel Osinenko, Yury Yanovich
year: 2025
doi: 10.1109/JIOT.2025.3645453
---

# SwarmRaft: Leveraging Consensus for Robust Drone Swarm Coordination in GNSS-Degraded Environments

**출처:** https://www.semanticscholar.org/paper/a97810f737efe5f0ee78072d1ce026dff22e2ebe
**저자:** Kapel Dev, Yash Madhwal, Sofia Shevelo, Pavel Osinenko, Yury Yanovich
**발행년도:** 2025
**DOI:** 10.1109/JIOT.2025.3645453

## 초록 (Abstract)

Uncrewed aerial vehicle (UAV) swarms are increasingly used in critical applications such as aerial mapping, environmental monitoring, and autonomous delivery. However, the reliability of these systems is highly dependent on uninterrupted access to the Global Navigation Satellite Systems (GNSS) signals, which can be disrupted in real-world scenarios due to interference, environmental conditions, or adversarial attacks, causing disorientation, collision risks, and mission failure. This article proposes SwarmRaft, a blockchain-inspired positioning and consensus framework for maintaining coordination and data integrity in UAV swarms operating under GNSS-denied conditions. SwarmRaft leverages the Raft consensus algorithm to enable distributed drones (nodes) to agree on state updates such as location and heading, even in the absence of GNSS signals for one or more nodes. In our prototype, each node uses GNSS and local sensing, and communicates over WiFi in a simulated swarm. Upon signal loss, consensus is used to reconstruct or verify the position of the failed node based on its last known state and trajectory. Our system demonstrates robustness in maintaining swarm coherence and fault tolerance through a lightweight, scalable communication model. This work provides a practical and secure approach for decentralized drone operation in unpredictable environments.
