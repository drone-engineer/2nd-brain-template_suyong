---
title: LEGO-SLAM Language-Embedded Gaussian Optimization SLAM
authors: Sibaek Lee; Seongbo Ha; Kyeongsu Kang; Joonyeol Choi; Seungjun Tak; Hyeonwoo Yu
arxiv_id: 2511.16144v2
published: 2025-11-20
source_type: arxiv
collected: 2026-07-27
sha256: 755f118fdf88fe37c521e6ea3121fcd2fc216b51ae571e72dbab665fbc8ae82b
---

# LEGO-SLAM Language-Embedded Gaussian Optimization SLAM

## 메타데이터
- arXiv: 2511.16144v2
- 저자: Sibaek Lee; Seongbo Ha; Kyeongsu Kang; Joonyeol Choi; Seungjun Tak; Hyeonwoo Yu
- 출판일: 2025-11-20
- 수집: 2026-07-27 (STM32 활용검토 관련 임베디드 항법/SLAM 참고)

## 초록
Recent advances in 3D Gaussian Splatting (3DGS) have enabled Simultaneous Localization and Mapping (SLAM) systems to build photorealistic maps. However, these maps lack the open-vocabulary semantic understanding required for robotic interaction. Integrating language features into SLAM remains a significant challenge, as storing high-dimensional features incurs excessive memory and rendering overhead, while existing methods with static models lack adaptability for novel environments. We propose LEGO-SLAM (Language-Embedded Gaussian Optimization SLAM), a framework that achieves real-time, open-vocabulary mapping within a 3DGS-based SLAM system. At the core of our method is a scene-adaptive autoencoder that distills high-dimensional language embeddings into a compact 16-dimensional feature space, reducing the memory per Gaussian and accelerating rendering. Unlike static approaches, our encoder adapts online to unseen scenes. These compact features also enable a language-guided pruning strategy that identifies semantic redundancy, reducing the map's Gaussian count by up to 58% while maintaining rendering quality. Furthermore, we introduce a language-based loop detection approach that reuses the language features already extracted for mapping, eliminating the need for a separate detection model. Experiments demonstrate that LEGO-SLAM achieves competitive mapping quality and tracking accuracy, all while providing open-vocabulary capabilities at 15 FPS. Our project page is available at https://lab-of-ai-and-robotics.github.io/LEGO-SLAM/

---
*raw evidence — immutable.*
