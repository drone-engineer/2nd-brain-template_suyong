---
source_url: https://arxiv.org/abs/2010.07068v1
ingested: 2026-07-26
sha256: 9d7d3f82c946744a92760d8e7504d512fb5cbbeffefc2c219faad9b9d6cf9fd9
title: UAV Trajectory and Communication Co-design: Flexible Path Discretization and Path Compression
authors: Yijun Guo, Changsheng You, Changchuan Yin, Rui Zhang
year: 2020
arxiv_id: 2010.07068v1
---

# UAV Trajectory and Communication Co-design: Flexible Path Discretization and Path Compression

**출처:** arXiv — https://arxiv.org/abs/2010.07068v1
**저자:** Yijun Guo, Changsheng You, Changchuan Yin, Rui Zhang
**발행년도:** 2020
**arXiv ID:** 2010.07068v1

## 초록 (Abstract)

The performance optimization of UAV communication systems requires the joint design of UAV trajectory and communication efficiently. To tackle the challenge of infinite design variables arising from the continuous-time UAV trajectory optimization, a commonly adopted approach is by approximating the UAV trajectory with piecewise-linear path segments in three-dimensional (3D) space. However, this approach may still incur prohibitive computational complexity in practice when the UAV flight period/distance becomes long, as the distance between consecutive waypoints needs to be kept sufficiently small to retain high approximation accuracy. To resolve this fundamental issue, we propose in this paper a new and general framework for UAV trajectory and communication co-design. First, we propose a flexible path discretization scheme that optimizes only a number of selected waypoints (designable waypoints) along the UAV path for complexity reduction, while all the designable and non-designable waypoints are used in calculating the approximated communication utility along the UAV trajectory for ensuring high trajectory discretization accuracy. Next, given any number of designable waypoints, we propose a novel path compression scheme where the UAV 3D path is first decomposed into three one-dimensional (1D) sub-paths and each sub-path is then approximated by superimposing a number of selected basis paths weighted by their corresponding path coefficients, thus further reducing the path design complexity. Finally, we provide a case study on UAV trajectory design for aerial data harvesting from distributed ground sensors, and numerically show that the proposed schemes can significantly reduce the UAV trajectory design complexity yet achieve favorable rate performance as compared to conventional path/time discretization schemes.
