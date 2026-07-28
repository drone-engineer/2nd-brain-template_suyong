---
title: Enhancing Graph-Based SLAM in GNSS-Denied environments by leveraging learned features
authors: Léon Perruchot-Triboulet; Luc Jaulin; Kai Xiao
arxiv_id: 2605.20484v1
published: 2026-05-19
source_type: arxiv
collected: 2026-07-27
sha256: 83f8430be0e7a313712dbe03c56f253aa769aa6b36dabfdf7f23a4f0fb1df365
---

# Enhancing Graph-Based SLAM in GNSS-Denied environments by leveraging learned features

## 메타데이터
- arXiv: 2605.20484v1
- 저자: Léon Perruchot-Triboulet; Luc Jaulin; Kai Xiao
- 출판일: 2026-05-19
- 수집: 2026-07-27 (GNSS-Denied 자율항법 기술검토용)

## 초록
Autonomous navigation in GNSS-denied environments remains a core challenge for legged robots, where exteroceptive sensors such as LiDAR are prone to elevation drift in geometrically sparse or repetitive scenes. We present a factor graph architecture that augments the LIO-SAM framework with a parallel kinematic lane driven by proprioceptive leg odometry, coupled to the main LiDAR-inertial lane via an identity relative pose constraint with a selective noise model. Applied to a Linxai D50 quadruped platform across two outdoor loops totaling over one kilometer, our approach reduces elevation drift from over 30m to under 30cm and enables convergence in a scene where the baseline pipeline fails entirely. These results suggest that proprioceptive data, already computed onboard for gait control, constitutes a lightweight and effective vertical anchor for SLAM in GNSS-denied settings.

---
*raw evidence — immutable. GNSS-Denied navigation (TRN/VIO/비전매칭) 참조.*
