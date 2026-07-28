---
title: Banshee: Target Switch Attacks on Gimbal-Stabilized Visual Tracking Systems via Acoustic Injection
authors: Jiarui Li; Joseph Brewington; Qingzhao Zhang; Z. Morley Mao
arxiv_id: 2607.09930v1
published: 2026-07-10
source_type: arxiv
collected: 2026-07-27
sha256: 1faca3a3808e5f7a38ccc1155fcf3f2488e79897da1713ba6f4ca93d2cad8085
---

# Banshee: Target Switch Attacks on Gimbal-Stabilized Visual Tracking Systems via Acoustic Injection

## 메타데이터
- arXiv: 2607.09930v1
- 저자: Jiarui Li; Joseph Brewington; Qingzhao Zhang; Z. Morley Mao
- 출판일: 2026-07-10
- 수집: 2026-07-27 (Hunter-Killer PRD 관련 기술 검토용)

## 초록
Gimbal-stabilized visual tracking is critical for modern autonomous systems such as Unmanned Aerial Vehicles (UAVs). While prior work shows acoustic signals can disturb gimbal internals, the impact of such attacks on real-world applications like UAV tracking and following remains underexplored. Existing demonstrations largely overlook practical challenges for real-world attacks, such as object-motion uncertainty and runtime latency. To bridge this gap, we present Banshee, the first physically realizable attack that induces target switching in UAV visual tracking systems by exploiting acoustic vulnerabilities in gimbal-camera systems. Banshee generates carefully crafted acoustic waveforms that induce optimized adversarial gimbal oscillations, causing directionally biased camera-view drifts that break inter-frame target associations. Consequently, the onboard tracker is driven to switch from the original target to an attacker-selected object with high probability, with occasional target loss. Banshee achieves a 93.6% success rate in simulation across two commercial gimbal systems and five trackers. Real-world benchtop and in-flight black-box attacks against a commercial drone across varied scenarios show an overall 95.5% attack success rate. Our results reveal a practical cross-domain vulnerability between acoustics and vision, highlighting the need for robust designs of gimbal systems and applications. Our code is available at: https://github.com/U1ltra/Banshee.

---
*raw evidence — immutable.*
