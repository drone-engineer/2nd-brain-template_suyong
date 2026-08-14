---
title: An Equivariant Filter for Visual Inertial Odometry
authors: Pieter van Goor; Robert Mahony
arxiv_id: 2104.03532v1
published: 2021-04-08
source_type: arxiv
collected: 2026-07-27
sha256: 660c9894a175ea3564bb6144836e4c2c7ecb74faded1d0c936b3c491084a16c7
---

# An Equivariant Filter for Visual Inertial Odometry

## 메타데이터
- arXiv: 2104.03532v1
- 저자: Pieter van Goor; Robert Mahony
- 출판일: 2021-04-08
- 수집: 2026-07-27 (GNSS-Denied 자율항법 기술검토용)

## 초록
Visual Inertial Odometry (VIO) is of great interest due the ubiquity of devices equipped with both a monocular camera and Inertial Measurement Unit (IMU). Methods based on the extended Kalman Filter remain popular in VIO due to their low memory requirements, CPU usage, and processing time when compared to optimisation-based methods. In this paper, we analyse the VIO problem from a geometric perspective and propose a novel formulation on a smooth quotient manifold where the equivalence relationship is the well-known invariance of VIO to choice of reference frame. We propose a novel Lie group that acts transitively on this manifold and is compatible with the visual measurements. This structure allows for the application of Equivariant Filter (EqF) design leading to a novel filter for the VIO problem. Combined with a very simple vision processing front-end, the proposed filter demonstrates state-of-the-art performance on the EuRoC dataset compared to other EKF-based VIO algorithms.

---
*raw evidence — immutable. GNSS-Denied navigation (TRN/VIO/비전매칭) 참조.*
