---
source_url: https://arxiv.org/abs/2605.22709v1
ingested: 2026-07-26
sha256: df25dfe9c6cbe8959186c0bdf41bade0b3d590fce787e02a2e40631fb6f6eb46
title: TriSweep: A Four-Drone Swarm Framework for Electromagnetic Side-Channel Analysis
authors: Eric Yocam, Varghese Vaidyan
year: 2026
arxiv_id: 2605.22709v1
---

# TriSweep: A Four-Drone Swarm Framework for Electromagnetic Side-Channel Analysis

**출처:** arXiv — https://arxiv.org/abs/2605.22709v1
**저자:** Eric Yocam, Varghese Vaidyan
**발행년도:** 2026
**arXiv ID:** 2605.22709v1

## 초록 (Abstract)

Electromagnetic (EM) side-channel analysis traditionally assumes a stationary, close-proximity probe - a threat model that underestimates aerial adversaries. TriSweep is a simulation framework that designs and evaluates a four-drone swarm architecture for autonomous standoff EM-SCA of embedded microcontrollers at 0.25-1.5 m. Three spatially specialized collector drones - Anchor (full-spectrum), Mask Probe (mask-register loading leakage), and Cipher Probe (masked SubBytes output leakage) - feed a stationary Accumulator drone that performs coherent combining (+4.8 dB SNR gain) and second-order mask cancellation via a centered product of the two spatially separated leakage streams. Evaluated against three real ANSSI ASCAD datasets (ATmega8515 masked AES-128 and 50/100-sample desynchronized variants), the framework achieves a simulated key rank of 18 +/- 1.7 (five-seed) at 0.25 m on the primary masked dataset. Profiling-trace cross-correlation alignment reduces single-drone rank from 89 to 21 on the 100-sample-jitter variant, demonstrating compensation for drone hover vibration. A two-channel CNN in the Accumulator converges to a loss of 0.454 (vs. random baseline 5.545) and improves rank on desynchronized datasets. No physical hardware has been fabricated; prototype construction is the planned next step.
