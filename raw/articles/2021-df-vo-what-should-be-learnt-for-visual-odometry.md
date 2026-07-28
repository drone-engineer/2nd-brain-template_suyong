---
title: DF-VO What Should Be Learnt for Visual Odometry
authors: Huangying Zhan; Chamara Saroj Weerasekera; Jia-Wang Bian; Ravi Garg; Ian Reid
arxiv_id: 2103.00933v1
published: 2021-03-01
source_type: arxiv
collected: 2026-07-27
sha256: 6ea09d7ceefd6c401217d551f7c5a8964ce159a1b14746a344accfd1491c69c0
---

# DF-VO What Should Be Learnt for Visual Odometry

## 메타데이터
- arXiv: 2103.00933v1
- 저자: Huangying Zhan; Chamara Saroj Weerasekera; Jia-Wang Bian; Ravi Garg; Ian Reid
- 출판일: 2021-03-01
- 수집: 2026-07-27 (STM32 활용검토 관련 임베디드 항법/SLAM 참고)

## 초록
Multi-view geometry-based methods dominate the last few decades in monocular Visual Odometry for their superior performance, while they have been vulnerable to dynamic and low-texture scenes. More importantly, monocular methods suffer from scale-drift issue, i.e., errors accumulate over time. Recent studies show that deep neural networks can learn scene depths and relative camera in a self-supervised manner without acquiring ground truth labels. More surprisingly, they show that the well-trained networks enable scale-consistent predictions over long videos, while the accuracy is still inferior to traditional methods because of ignoring geometric information. Building on top of recent progress in computer vision, we design a simple yet robust VO system by integrating multi-view geometry and deep learning on Depth and optical Flow, namely DF-VO. In this work, a) we propose a method to carefully sample high-quality correspondences from deep flows and recover accurate camera poses with a geometric module; b) we address the scale-drift issue by aligning geometrically triangulated depths to the scale-consistent deep depths, where the dynamic scenes are taken into account. Comprehensive ablation studies show the effectiveness of the proposed method, and extensive evaluation results show the state-of-the-art performance of our system, e.g., Ours (1.652%) v.s. ORB-SLAM (3.247%}) in terms of translation error in KITTI Odometry benchmark. Source code is publicly available at: \href{https://github.com/Huangying-Zhan/DF-VO}{DF-VO}.

---
*raw evidence — immutable.*
