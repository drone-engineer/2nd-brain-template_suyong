---
source_url: https://www.semanticscholar.org/paper/3814a43640439f3d38da5165a0486b3178afceac
ingested: 2026-08-17
sha256: ba0f8271296c255da03078118f0b62fb17db249e7679bc85fb64b095c90f2a49
title: A Unified Risk-Aware and Explainable Dual-Critic MAPPO Framework for Safe UAV Swarm Navigation in GPS-Denied Environments
authors: Aswin Karkadakattil
year: 2026
doi: 10.13111/2066-8201.2026.18.2.5
---

# A Unified Risk-Aware and Explainable Dual-Critic MAPPO Framework for Safe UAV Swarm Navigation in GPS-Denied Environments

**출처:** https://www.semanticscholar.org/paper/3814a43640439f3d38da5165a0486b3178afceac
**저자:** Aswin Karkadakattil
**발행년도:** 2026
**DOI:** 10.13111/2066-8201.2026.18.2.5
**OA PDF:** https://doi.org/10.13111/2066-8201.2026.18.2.5

## 초록 (Abstract)

Autonomous UAV swarms operating in GPS-denied environments must achieve coordinated navigation, collision avoidance, and interpretable decision-making under partial observability and strong inter-agent coupling. While multi-agent reinforcement learning (MARL) has demonstrated promising capabilities for decentralized swarm control, existing approaches largely entangle task performance and safety within a single reward formulation, often leading to unstable policies, unsafe interactions, and limited transparency in safety-critical deployments. This work proposes a unified risk-decomposed and explainable MARL framework based on a dual-critic Multi-Agent Proximal Policy Optimization (MAPPO) architecture, in which task reward and collision risk are explicitly modelled using separate value functions during centralized training. This structural decomposition enables stable policy optimization by preventing safety signals from being overshadowed by reward-driven updates, resulting in improved coordination robustness and consistent collision mitigation. To address the interpretability limitations of cooperative MARL, an action-level explainability framework using Kernel SHAP is integrated to quantify the contribution of individual UAV states to collective decision-making. In addition, a direction-wise SHAP difference (ΔSHAP) analysis is introduced to systematically reveal how explicit risk modelling reshapes feature relevance and induces structured coordination patterns across action dimensions. The proposed framework is evaluated through multi-seed statistical experiments and controlled ablation studies against PPO and a reward-only MAPPO baseline. Results demonstrate simultaneous improvements in reward stability, collision reduction, and explanation consistency, while ablation analysis confirms that explicit risk decomposition is essential for achieving safe and interpretable swarm behavior. Overall, this work establishes a novel and unified paradigm for integrating safety and explainability in multi-agent reinforcement learning, with direct implications for reliable deployment of UAV swarms in safety-critical and GPS-denied environments.
