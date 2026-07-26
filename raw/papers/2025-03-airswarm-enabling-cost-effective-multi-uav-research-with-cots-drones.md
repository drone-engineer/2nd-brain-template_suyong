---
source_type: zotero
zotero_item_key: QZ35WT85
zotero_attachment_keys: [D89J3ZU4]
item_type: preprint
title: "AirSwarm: Enabling Cost-Effective Multi-UAV Research with COTS drones"
authors:
  - "Li, Xiaowei"
  - "Xu, Kuan"
  - "Liu, Fen"
  - "Bai, Ruofei"
  - "Yuan, Shenghai"
  - "Xie, Lihua"
published: "2025-03-10"
url: "https://arxiv.org/abs/2503.06890"
citation_key: Li2025_QZ35WT85
zotero_tags: ["uav-swarm"]
zotero_collections: []
ingested: 2026-07-24
metadata_status: complete
metadata_enriched_from: [arxiv-html]
sha256: e37311c602150027c0f9db4a00722cf995ed9bd5ae712d30ac2cf8f20253fb15
---
# AirSwarm: Enabling Cost-Effective Multi-UAV Research with COTS drones

## Zotero Metadata

- Zotero Item Key: QZ35WT85
- Item Type: preprint
- Citation Key: Li2025_QZ35WT85
- Authors: Li, Xiaowei; Xu, Kuan; Liu, Fen; Bai, Ruofei; Yuan, Shenghai; Xie, Lihua
- Published: 2025-03-10
- URL: https://arxiv.org/abs/2503.06890
- Extra: arXiv:2503.06890
- Collections: (none)
- Attachment Keys: D89J3ZU4
- Tags: uav-swarm

## Abstract

Traditional unmanned aerial vehicle (UAV) swarm missions rely heavily on expensive custom-made drones with onboard perception or external positioning systems, limiting their widespread adoption in research and education. To address this issue, we propose AirSwarm. AirSwarm democratizes multi-drone coordination using low-cost commercially available drones such as Tello or Anafi, enabling affordable swarm aerial robotics research and education. Key innovations include a hierarchical control architecture for reliable multi-UAV coordination, an infrastructure-free visual SLAM system for precise localization without external motion capture, and a ROS-based software framework for simplified swarm development. Experiments demonstrate cm-level tracking accuracy, low-latency control, communication failure resistance, formation flight, and trajectory tracking. By reducing financial and technical barriers, AirSwarm makes multi-robot education and research more accessible. The complete instructions and open source code will be available at

## Extracted Text

AirSwarm: Enabling Cost-Effective Multi-UAV Research with COTS drones

# AirSwarm: Enabling Cost-Effective Multi-UAV Research with COTS drones

Xiaowei Li∼, Kuan Xu∼, Fen Liu, Ruofei Bai, Shenghai Yuan∗, and Lihua Xie ∼ Equal Contribution. ∗ Corresponding Author.This work is supported by the National Research Foundation of Singapore under its Medium-Sized Center for Advanced Robotics Technology Innovation.All authors are with the Centre for Advanced Robotics Technology Innovation (CARTIN), School of Electrical and Electronic Engineering, Nanyang Technological University, 50 Nanyang Avenue, Singapore 639798, {shyuan,elhxie}@ntu.edu.sg.

###### Abstract

Traditional unmanned aerial vehicle (UAV) swarm missions rely heavily on expensive custom-made drones with onboard perception or external positioning systems, limiting their widespread adoption in research and education. To address this issue, we propose AirSwarm. AirSwarm democratizes multi-drone coordination using low-cost commercially available drones such as Tello or Anafi, enabling affordable swarm aerial robotics research and education. Key innovations include a hierarchical control architecture for reliable multi-UAV coordination, an infrastructure-free visual SLAM system for precise localization without external motion capture, and a ROS-based software framework for simplified swarm development. Experiments demonstrate cm-level tracking accuracy, low-latency control, communication failure resistance, formation flight, and trajectory tracking. By reducing financial and technical barriers, AirSwarm makes multi-robot education and research more accessible. The complete instructions and open source code will be available at https://github.com/vvEverett/tello_ros.

Index Terms — Drone Swarms, Multi-Robot Systems, SLAM, Low-Cost Robotics

## I Introduction

Unmanned Aerial Vehicle (UAV) swarm systems have shown great potential in applications such as collaborative inspection [1, 2, 3, 4], goods delivery [5, 6, 7], and field surveys [8, 9]. They offer better scalability and resilience, ensuring redundancy and fault tolerance in dynamic environments. However, their adoption in research and education is severely limited by high hardware costs and system complexity [10]. Worse still, regulations often work against academic and research efforts, making swarm research on UAVs extremely difficult to advance.

Existing swarm research [2, 6, 11, 8, 5, 10, 12] is heavily biased toward custom-built drones [13, 14, 15, 16, 17] that rely on DIY hardware and firmware, often requiring hundreds of hours for development, integration, and procurement. Although these drones demonstrate impressive capabilities, their implementation is highly resource-intensive and demands expertise across multiple domains, including aerodynamics, embedded systems, computer vision, and networking. The fragmented nature of development [18] not only slows progress but also creates a high barrier to entry for researchers and educators who lack specialized knowledge in all these areas. In contrast, commercial off-the-shelf (COTS) drones like the DJI Mavic series offer limited API support, while options like the DJI Tello and Anafi lack robust perception, restricting their use in scalable swarm applications. A balance between accessibility, modularity, and computational capability is crucial for advancing UAV swarm research.

A key challenge in expanding UAV swarm research is enabling precise state estimation and real-time coordination on affordable COTS drones by effectively integrating sensor feedback with control systems [19, 20, 21]. Traditional methods rely on costly external localization, such as motion capture systems [22, 23] or RTKGPS/UWB-based solutions [24], which, while effective, significantly limit accessibility and scalability. High-precision platforms like the Flying Machine Arena [25] and Crazyswarm [26] have demonstrated impressive swarm control, but their reliance on expensive infrastructure restricts their use to well-funded research institutions, preventing broader adoption in real-world applications.

Figure 1: Comparison of Swarm systems by cost and complexity, highlighting the proposed approach.

Figure 2: AirSwarm System Architecture. The diagram shows the complete workflow from environmental sensing to drone control, including: multi-session mapping, hardware communication architecture, and the integrated control interface.

To address external sensing issues, onboard alternatives, such as LIO [5] or VIO [8], have a higher chance of enabling a COTS drone swarm with onboard autonomy. However, they come with their own challenges, including intermittent communication, drift accumulation, sensor calibration complexities, and susceptibility to environmental factors such as lighting conditions and electromagnetic interference. Overall, a swarm, in a nutshell, presents a complex set of challenges that need to be balanced.

To address these challenges, we present AirSwarm, a novel swarm architecture designed for low-cost, scalable UAV research using commercial off-the-shelf (COTS) drones, such as DJI Tello or Parrot Anafi. The system incorporates Raspberry Pi units to manage IP address conflicts and compress video streams for efficient data handling. Each UAV localizes independently using visual SLAM-based prior mapping, without associating with past observations, ensuring robustness against intermittent network connectivity. A PD controller is implemented for precise UAV control, alongside a dedicated interface for streamlined swarm management. We demonstrate that AirSwarm enhances the success rate of existing control and planning algorithms, making it a practical and accessible solution for swarm robotics research. Our contributions can be summarized as follows:

•

Resilient Multi-UAV Control with Noisy and Conflicting Networks: We propose a network-adaptive communication framework that mitigates IP-conflict of the COTS drones, ensuring robust swarm coordination in real-world wireless conditions with intermittent noises.

•

Low-Cost, Scalable Swarm Research Platform with COTS Drones: Introduces a cost-effective, infrastructure-free swarm system utilizing commercial off-the-shelf (COTS) drones, such as DJI Tello or Parrot Anafi, combined with lightweight localization and hierarchical control architecture, lowering the barrier for swarm robotics research.

•

Open-Source, Reproducible Swarm Research Platform: Provides a ROS-based, open-source framework with detailed deployment instructions, hardware integration guidelines, and real-world experimental validation, making swarm research more accessible, scalable, and reproducible for academia and industry https://github.com/vvEverett/tello_ros.

The significance of this work lies in democratizing UAV swarm research by reducing cost and complexity barriers, enabling broader institutional participation in robotics research while advancing practical, infrastructure-independent swarm operations.

## II Related Works

UAV swarm research has made significant progress, yet key challenges persist in achieving scalable, cost-effective, and flexible deployments [27]. One major limitation is the reliance on expensive external localization systems [28, 29, 30, 31, 32], restricting accessibility and real-world applicability. Traditional approaches such as motion capture [22, 23] and RTK-GPS/UWB solutions [24] provide high-precision tracking but entail substantial financial and infrastructural costs. Advanced swarm control has been demonstrated in systems like FMA [25] and Crazyswarm [26], but their dependence on costly VICON motion capture and other external positioning systems restricts use to well-funded institutions. Alternative solutions like ICARUS [33] attempt to lower costs through optical tracking but remain confined to controlled indoor environments [34]. Overcoming these limitations is essential for expanding UAV swarm accessibility and real-world deployment.

Many UAV swarm studies focus on custom-built drones [2, 6, 11, 8, 5, 10, 12], which, while capable, require extensive development and specialized expertise. This fragmented approach [18] slows progress and creates high entry barriers for researchers lacking expertise in aerodynamics, embedded systems, and networking. In contrast, commercial off-the-shelf (COTS) drones offer a more accessible alternative but suffer from limited API support and weak onboard perception, constraining their scalability in swarm applications. A balance between accessibility, modularity, and computational capability is crucial for progress.

A promising solution for enabling swarm applications on COTS drones is robust onboard state estimation [35, 36], where Visual Simultaneous Localization and Mapping (SLAM) is vital [37]. Traditional SLAM methods such as ORB-SLAM3 [38] and PL-SLAM [39] improved localization robustness, while learning-based methods like DROID-SLAM [40, 41, 42, 43, 44, 45, 46] offer resilience but demand high computational resources. Moreover, multi-UAV SLAM [47] [48] systems often struggle with calibration and intermittent data streaming, making deployment challenging.

Hybrid SLAM architectures [49, 50, 51, 52] have emerged as an optimal solution. AirVO [49] combines learning-based feature detection with classical optimization, improving illumination robustness while maintaining efficiency. Its successor, AirSLAM [53], further enhances loop closure detection and map reuse through a unified point-line feature network, making it particularly suitable for UAVs with limited onboard processing power.

## III AirSwarm System

### III-A System Overview

The AirSwarm system employs a hierarchical architecture that integrates perception and control capabilities within a tiered framework, as illustrated in Fig 2. The system comprises three primary functional layers:

•

Mapping Subsystem: Implements multi-session mapping using stereo cameras, integrating stereo visual-inertial odometry for initial pose estimation and local mapping with point-line features. The process includes loop detection, global bundle adjustment, and offline optimization to generate an optimized environmental model.

•

Communication Architecture: Establishes a centralized network topology where COTS drones with onboard monocular cameras and IMUs communicate via WiFi to Raspberry Pi units. These units serve as bridges, utilizing a fixed-to-reconfigurable IP architecture that interfaces with ROS Topics through Ethernet connections to the central processor.

•

Control Framework: It implements a versatile control stack compatible with various COTS drones equipped with video feedback for planning and control functions with lightweight relocalization. The relocalization pipeline processes monocular image streams for 2D-to-3D localization against the pre-built map, supporting both direct user interface control and programmatic access through multiple computing platforms.

The NVIDIA Jetson AGX Orin functions as the computational nexus, executing mapping and localization algorithms while coordinating the drone network through a centralized architecture. This design enables infrastructure-independent operation via visual SLAM localization while maintaining efficient command distribution through hierarchical communication. This approach optimizes computational resource utilization while providing the unified coordination necessary for precise multi-UAV formation control.

### III-B ROS-Based Universal COTS Framework

Based on ROS and COTS SDK, we implemented a drone control system with carefully designed architecture for simplicity and usability. Our key design considerations include:

1.

A unified architecture that enables seamless transition between single and multiple drone operations;

2.

Thread-safe implementations for video stream processing to ensure reliable real-time performance;

3.

A comprehensive yet minimalist API that encapsulates complex flight control functionalities through simple ROS topics;

4.

A streamlined configuration approach where users only need to specify basic parameters like drone ID and IP address.

These design choices significantly lower the technical barrier for robotics research and education, particularly in multi-drone applications. The system’s modular architecture also facilitates straightforward integration with SLAM algorithms, making it a versatile platform for both research exploration and educational practices in swarm robotics.

### III-C Drift-Free Visual Localization

To achieve drift-free localization [54] for multiple UAVs using only low-cost cameras, we first build an accurate point-line map using a stereo camera based on AirSLAM [53], and then perform relocalization within this map using onboard monocular cameras . Our relocalization consists of four steps. First, line and point features are extracted using a unified convolutional neural network (CNN). Then, a bag-of-words (BoW) vocabulary is utilized to retrieve keyframes within the map. Subsequently, feature matching between retrieved keyframes and the query frame is performed using a graph neural network (GNN). Finally, the Perspective-n-Point (PnP) algorithm is applied to estimate the camera pose.

To fully utilize the computational resources of the Jetson platform, we use both GPU and CPU to perform relocalization . Our feature detection and matching are executed on the GPU, while similar keyframe retrieval and pose estimation are performed on the CPU. This design enables our visual-only localization to achieve both the robustness and accuracy of learning-based methods while maintaining near real-time efficiency on embedded platforms.

### III-D Unified Multi-UAV Architecture

To facilitate research and educational applications, we developed a comprehensive control system that manages both single-drone operation and multi-drone fleet coordination. Let $n\in\mathbb{N^{+}}$ denote the number of drones in the system, where $n=1$ represents single-drone operation and $n>1$ indicates fleet configuration. For each drone $i\in\{1,2,\ldots,n\}$ . Let $\mathbf{p}_{i}=[x_{i},y_{i},z_{i},\psi_{i}]^{T}\in\mathbb{R}^{4}$ denote the 3D position and yaw angle, $\mathbf{v}_{i}=[v_{x,i}^{b},v_{y,i}^{b},v_{z,i}^{b},\omega_{\psi,i}]^{T}\in% \mathbb{R}^{4}$ represent the body-frame velocity command, and $\mathbf{p}^{d}_{i}=[x^{d}_{i},y^{d}_{i},z^{d}_{i},\psi^{d}_{i}]^{T}\in\mathbb{% R}^{4}$ indicate the desired state. The error vector $\mathbf{e}_{i}=[e_{x,i},e_{y,i},e_{z,i},e_{\psi,i}]^{T}\in\mathbb{R}^{4}$ contains position errors, yaw error in world-frame, while $\eta_{i}\in\mathbb{R}$ represents the battery status. The system state matrices are:

| $\displaystyle\mathbf{P}$ | $\displaystyle=[\mathbf{p}_{1},\mathbf{p}_{2},\ldots,\mathbf{p}_{n}]^{T}\in% \mathbb{R}^{n\times 4},$ | (1) |
| --- | --- | --- |
| $\displaystyle\mathbf{V}$ | $\displaystyle=[\mathbf{v}_{1},\mathbf{v}_{2},\ldots,\mathbf{v}_{n}]^{T}\in% \mathbb{R}^{n\times 4},$ | (2) |
| $\displaystyle\mathbf{P}^{d}$ | $\displaystyle=[\mathbf{p}^{d}_{1},\mathbf{p}^{d}_{2},\ldots,\mathbf{p}^{d}_{n}% ]^{T}\in\mathbb{R}^{n\times 4},$ | (3) |
| $\displaystyle\mathbf{E}$ | $\displaystyle=[\mathbf{e}_{1},\mathbf{e}_{2},\ldots,\mathbf{e}_{n}]^{T}\in% \mathbb{R}^{n\times 4},$ | (4) |
| $\displaystyle\boldsymbol{\eta}$ | $\displaystyle=[\eta_{1},\eta_{2},\ldots,\eta_{n}]^{T}\in\mathbb{R}^{n}.$ | (5) |

The control mapping $\mathcal{C}(\cdot)$ transforms state observations into control commands:

| $\displaystyle\mathbf{V}=\mathcal{C}(\mathcal{S})\triangleq\mathcal{C}(\mathbf{% P},\mathbf{P}^{d},\mathbf{E},\boldsymbol{\eta},t),$ | (6) |
| --- | --- |

where $\mathcal{S}=(\mathbf{P},\mathbf{P}^{d},\mathbf{E},\boldsymbol{\eta},t)$ represents the system state tuple at time $t$ .

### III-E Position-Based Control System

SDKs of COTS UAV platforms only accept body-frame velocity commands, therefore, to complement our visual-only localization system, we implement a practical position control solution. Our approach adapts established control principles to bridge this interface constraint. The controller applies a fundamental coordinate transformation method that converts desired world-frame positions to compatible body-frame velocity commands. The position and yaw errors for each drone $i$ can be calculated as:

| $$\mathbf{e}_{i}=\begin{bmatrix}e_{x,i}\\ e_{y,i}\\ e_{z,i}\\ e_{\psi,i}\end{bmatrix}=\begin{bmatrix}x^{d}_{i}-x_{i}\\ y^{d}_{i}-y_{i}\\ z^{d}_{i}-z_{i}\\ \arg\min_{k\in\{-1,0,1\}}|\psi^{d}_{i}-\psi_{i}+360k|\end{bmatrix}.$$ | (7) |
| --- | --- |

To mitigate measurement noise, we implemented first-order filtering on velocity error estimates:

| $$\dot{\mathbf{e}}^{f}_{i}(t)=\alpha\dot{\mathbf{e}}^{f}_{i}(t-1)+\beta\dot{% \mathbf{e}}_{i}(t),$$ | (8) |
| --- | --- |

where $\alpha$ and $\beta$ are two hyperparameters. Then the complete control law is:

| $$\mathbf{v}_{i}=\begin{bmatrix}v^{b}_{x,i}\\ v^{b}_{y,i}\\ v^{b}_{z,i}\\ \omega_{\psi,i}\end{bmatrix}=\begin{bmatrix}\mathbf{R}(\psi_{i})&\mathbf{0}\\ \mathbf{0}&\mathbf{I}\end{bmatrix}\begin{bmatrix}K_{x}^{p}e^{f}_{x,i}+K_{x}^{d% }\dot{e}^{f}_{x,i}\\ K_{y}^{p}e^{f}_{y,i}+K_{y}^{d}\dot{e}^{f}_{y,i}\\ K_{z}^{p}e^{f}_{z,i}+K_{z}^{d}\dot{e}^{f}_{z,i}\\ K_{\psi}^{p}e^{f}_{\psi,i}+K_{\psi}^{d}\dot{e}^{f}_{\psi,i}\end{bmatrix},$$ | (9) |
| --- | --- |

where $\mathbf{K}^{p}=[K_{x}^{p},K_{y}^{p},K_{z}^{p},K_{\psi}^{p}]$ represents proportional gains for position errors along the x, y, and z axes and the yaw angle error, while $\mathbf{K}^{d}=[K_{x}^{d},K_{y}^{d},K_{z}^{d},K_{\psi}^{d}]$ represents derivative gains for the corresponding velocity errors. The yaw angle $\psi_{i}$ quantifies the angular deviation between the drone’s longitudinal axis and the principal reference axis of the SLAM coordinate frame, measured in the horizontal plane. This orientation parameter is directly extractable from our state estimation module of the localization system. $\mathbf{R}(\psi_{i})$ represents a rotation matrix that transforms coordinates from world frame to body frame, defined as:

| $$\mathbf{R}(\psi_{i})=\begin{bmatrix}\cos(\psi_{i})&\sin(\psi_{i})\\ -\sin(\psi_{i})&\cos(\psi_{i})\end{bmatrix}.$$ | (10) |
| --- | --- |

It is important to note that this rotation matrix may vary depending on the specific coordinate system definitions adopted in the implementation. The form presented here corresponds to our system configuration, but alternative representations may be required for different coordinate conventions.

Testing demonstrates that this straightforward application of coordinate transformations provides satisfactory position tracking for intended applications, offering a valuable reference for developers working with commercially-constrained UAV platforms where direct position control is unavailable through the provided SDK.

## IV Experiments and Results

In this section, we present a comprehensive evaluation of our proposed AirSwarm platform through two key experiments: (1) End-to-End Communication Latency Analysis, (2) Navigation Performance Evaluation. The latency analysis quantifies system responsiveness across control and video pathways, establishing the viability of our architecture for real-time applications. The performance evaluation encompasses the system’s navigation capabilities, initialization robustness, localization success rate, and other key metrics.

### IV-A Experimental Platform

Our experimental platform operates independently using onboard sensors without requiring expensive external positioning equipment such as VICON motion capture systems. The system comprises:

•

Three DJI Tello EDU drones,

•

Three Raspberry Pi 4B units (4GB RAM, Ubuntu 20.04) serving as network bridges,

•

One NVIDIA Jetson AGX Orin (64GB RAM, Ubuntu 22.04) as the central computing unit,

•

Intel RealSense D455 camera for mapping.

Note that the RealSense D455 camera (848×480 resolution, 30fps) is used solely for mapping. During navigation, we only use the onboard monocular camera (960×720 resolution, 30fps) on the drone for localization.

### IV-B Communication Latency Analysis

TABLE I: Control Latency Analysis in (ms).

| Component | Protocol | Min | Max | Mean |
| --- | --- | --- | --- | --- |
| PC $\leftrightarrow$ RPi Link | UDP/Ethernet | 0.15 | 1.75 | 0.89 |
| RPi Forwarding | IPTABLES Forward | 0.03 | 0.08 | 0.03 |
| RPi $\leftrightarrow$ Tello Link | UDP/Wi-Fi | 4.14 | 66.3 | 25.9 |

We conduct real-time flight tests with DJI Tello drone hovering at a distance of 10 meters from Raspberry Pi and PC for 5 minutes without obstruction. Table I presents the latency analysis of control commands transmission between PC, Raspberry Pi (functioning as a forwarding node with iptables), and Tello drone. The results show that latency introduced by wired Ethernet connection (PC $\leftrightarrow$ RPi, 0.889ms) and iptables forwarding (0.034ms) is negligible, while the wireless communication between RPi and Tello contributes the majority of command latency (25.886ms). Table II demonstrates the performance metrics of video streaming. The relatively high end-to-end video latency (174.505ms) is primarily attributed to H.264 encoding/decoding process and the bandwidth limitations of the Wi-Fi link, as indicated by the fluctuating bitrate (0.630-4.029 Mbps). Nevertheless, both command and video latencies remain within acceptable bounds for real-time drone control and monitoring applications.

TABLE II: End-to-End Video Stream Analysis

| Metric | Min | Max | Std Dev | Mean |
| --- | --- | --- | --- | --- |
| Latency (ms) | 99.277 | 218.526 | 37.011 | 174.505 |
| Bitrate (Mbps) | 0.630 | 4.029 | 0.643 | 2.876 |
| Resolution | 720p (960×720) | | | |
| Frame Rate (fps) | 30 | | | |
| Codec | H.264 | | | |
| Transport Protocol | UDP | | | |

TABLE III: Performance Comparison of Multi-Agent SLAM Methods. Our system demonstrates greater robustness, higher success rates, and improved accuracy compared to CCM-SLAM. As CP-SLAM requires RGBD input, which UAVs lack, Depth Anything Model V2 (tiny) was used to estimate depth, leading to higher errors due to model inaccuracies. In contrast, our method operates near real-time, handles rotation and intermittent transmission, and eliminates the need for multi-agent calibration and initialization.

| Method | APE (cm) | | | FPS | Success Rate | Communication | Support | | Real-Time | Initialization Free |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | UAV1 | UAV2 | UAV3 | | | | Rotation | Intermittent | | |
| CCM-SLAM[47] | Fail | 3.02 | 6.29 | 14.22 $\times$ 3 | 3% | 0.99 Mbps | ✗ | ✗ | ✓ | ✗ |
| CP-SLAM[48] | 61.30 | 63.90 | 67.30 | 1.67 | 31% | 368.64 Mbps | ✓ | ✓ | ✗ | ✗ |
| Proposed | 2.34 | 2.55 | 3.87 | 10.80 $\times$ 3 | 99% | 1.86 Mbps | ✓ | ✓ | ✓ | ✓ |

### IV-C Navigation Performance Evaluation

Task Design: To demonstrate the capabilities of our system in real-world applications, we designed a coordinated multi-UAV formation task where three Tello drones were commanded to trace the letters “NTU” in 3D space. Our experimental protocol involved simultaneous deployment of all three UAVs, each executing predefined trajectories within a common environment. For each method under evaluation, we first generated prebuilt maps using their respective mapping algorithms on identical datasets, then assessed navigation performance during trajectory execution.

Baseline Selection: For purely multi-agent visual SLAM systems, the available candidates are limited, as most existing works prioritize Stereo [8, 55, 56, 10] or LiDAR-based [5] solutions for robustness. For visual multi-agent SLAM, we selected CCM-SLAM and CP-SLAM, both of which support shared map usage for collaborative SLAM. While newer variants of CCM-SLAM, such as COVINS [57, 58], are available, they lack map reuse capabilities, making direct comparison challenging. Additionally, we included CP-SLAM [48] in our evaluation, as it represents a collaborative SLAM approach leveraging neural point-based representations. However, CP-SLAM presents two key challenges. First, its open-source implementation was non-functional, requiring us to reimplement the system, which we will release upon paper acceptance. Second, CP-SLAM relies on RGB-D input, which is not standard on commercial off-the-shelf (COTS) drones. To address this, we integrated the Depth Anything Model V2 (tiny) to generate depth maps and conducted offline evaluations for faster tracking performance only. The results are summarized in Tab. III.

Results Evaluations: We present the results in Table III and Fig 3. Note that the absolute pose errors (APE) [59] in Table III shows the localization error with ground truth generated by motion capture systems. The results show that each drone in our system maintained centimeter-level accuracy throughout the flight, with APE of 2.34cm, 2.55cm, and 3.87cm for the drones tracing the letters N, T, and U , respectively. Despite comparable APE metrics in successful trials, alternative approaches exhibited critical operational limitations. CCM-SLAM achieved merely 3% successful completions across all trials, compared to our system’s 99% success rate. The key issues with CCM SLAM is that the intermittent image transfers cause the system to lose the connection for a short period, which makes it lose connections.

Figure 3: Comparison of SLAM-estimated and Reference Trajectories in Multi-UAV Formation Flight

(a) 3D trajectory comparison.

(b) 2D trajectory comparison.

(c) Real-time SLAM visualization in Rviz.

(d) Experimental environment.

Our system is also highly efficient. During the mapping phase, AirSwarm achieved a processing rate of 30.83Hz using the RealSense D455 camera. In the relocalization phase, the system maintained consistent performance above 10Hz across all three Tello drone streams simultaneously (average 10.80Hz per drone), meeting the real-time requirements for responsive control. Meanwhile, CP-SLAM’s excessive computational demands prevented real-time operation on resource-constrained Jetson platforms, rendering it impractical for edge computing applications despite acceptable accuracy in laboratory settings. Additionally, CP-SLAM’s substantial communication overhead (368.64 Mbps) would strain network infrastructure in multi-agent deployments. These comparative results highlight that while competing methods may demonstrate acceptable accuracy in isolated successful cases, they lack the computational efficiency and operational reliability required for consistent real-world deployment.

Figure 4: This visualization represents multi-agent aerial tracking and encirlement coordination using the proposed solution.

Detailed Analysis: The fundamental algorithmic distinction between these approaches is illustrated in Fig 5, which contrasts the Maximum A Posteriori (MAP) approach used by CCM-SLAM with our Maximum Likelihood Estimation (MLE) approach. The MAP framework incorporates motion model constraints that create interdependencies between sequential pose estimates, requiring precise initialization and continuous tracking to maintain global consistency. CCM-SLAM consequently failed to properly associate the local map with the global reference frame for UAV1 across multiple experimental iterations, confining navigation to local coordinates and resulting in catastrophic trajectory deviation. UAV2 and UAV3 using CCM-SLAM achieved successful localization only after numerous initialization attempts, highlighting the fragility of this tightly-coupled approach. In contrast, our MLE-based AirSwarm framework establishes direct probabilistic relationships between current camera poses and observations relative to the shared prior map, without enforcing temporal consistency constraints. This architectural decision enables each pose estimate to be derived independently from current observations, conferring inherent resilience against initialization errors and coordinate transformation challenges. As evidenced in our trials, even experience communication failures, the system maintains reliable tracking with respect to the global map.

These characteristics establish our approach as particularly suitable for both educational and research platforms. In educational contexts, the system’s moderate processing requirements ensure that algorithmic behaviors remain transparent and interpretable, allowing students to observe fundamental localization concepts in action. For research applications, the framework’s resilience to communication interruptions and initialization variability provides a reliable foundation for investigating novel multi-agent coordination strategies, collaborative perception algorithms, and autonomous navigation techniques. The consistent centimeter-level accuracy across varying conditions supports repeatable experimentation, while the computational efficiency enables deployment on resource-constrained platforms typical in both preliminary research investigations and instructional laboratories.

Figure 5: In the presence of communication noise, MAP-based SLAM like CCM-SLAM is more prone to errors due to its dependence on prior states, whereas AirSwarm is based on MLE and demonstrates greater resilience with better noise-handling capabilities. It is the key reason why the proposed solution is better for low-cost COTS swarm research.

## V Case Study: Swarm-Based UAV Tracking and Encirclement

To verify the applicability of the proposed AirSwarm framework in real-world control problems, we evaluate its effectiveness in a multi-UAV autonomous encirclement and re-encirclement task [60], as shown in Fig. 4. This application involves a swarm of UAVs dynamically coordinating to track and encircle an adversarial drone using minimal sensing capabilities. The method integrates range-only localization and adaptive anti-synchronization controllers, enabling robust operation in GPS-denied environments. By leveraging AirSwarm’s logically distributed decision-making and multi-agent trajectory planning, we demonstrate that multi-UAV collaboration enhances encirclement efficiency, reducing reaction time in high-speed engagements.

Traditionally, conducting research in UAV swarm coordination and interception would require custom-built drones equipped with Ultra-Wideband (UWB) modules for precise localization and navigation. These setups are not only expensive but also prone to significant hardware damage when intentional collisions or adversarial interactions occur. The cost of repairing or replacing drones, combined with the complexity of integrating specialized localization hardware, has made such research financially inaccessible for many academic institutions and smaller research labs.

With the proposed AirSwarm framework, we enable a more affordable and cost-effective approach to multi-UAV experimentation. By leveraging commercial off-the-shelf (COTS) drones, lightweight sensing strategies, and logically distributed decision-making, AirSwarm eliminates the need for expensive localization infrastructure while maintaining high experimental fidelity. This affordability makes it an ideal platform for educational and research applications, allowing students and researchers to explore multi-agent aerial coordination, interception strategies, and swarm intelligence without incurring prohibitive costs. Furthermore, the modular nature of AirSwarm ensures scalability, making it adaptable for a wide range of budget-friendly experimental setups, ultimately democratizing access to UAV swarm research.

## VI Limitation and Future Works

Despite the promising results demonstrated by AirSwarm, several limitations warrant discussion and point toward future research directions. The primary constraint of the current implementation lies in its computational scalability, as the Nvidia Jetson AGX Orin platform limits simultaneous coordination to three Tello drones. While this limitation could be addressed through more powerful computing hardware, it represents a fundamental trade-off between system cost and swarm size. Additionally, although our localization module demonstrates robust performance across various indoor and outdoor environments under different illumination conditions, its effectiveness diminishes in scenarios with limited point and line features, particularly in textureless environments or areas with repetitive patterns where feature extraction becomes challenging.

Looking forward, these limitations present several promising avenues for future research. The development of more computationally efficient [61] visual SLAM algorithms could enable larger swarm formations on existing embedded hardware. Additionally, an intriguing direction involves implementing a multi-center computational architecture where several embedded computing units work cooperatively through task partitioning and load balancing. These targeted advancements would strategically extend AirSwarm’s capabilities while preserving its fundamental goal of providing accessible, infrastructure-independent swarm robotics technology that bridges the gap between research prototypes and practical applications.

## VII Conclusion

This paper presents AirSwarm, a novel approach to democratizing drone swarm technology by integrating commercial off-the-shelf (COTS) drones with sophisticated visual SLAM techniques and hierarchical control principles. Our system achieves professional-grade performance with cm-level position tracking accuracy and control latencies under 27ms during complex formation flights, all without relying on expensive external positioning infrastructure.

The significance of this work extends beyond its technical implementation, establishing a new paradigm for accessible multi-robot research and education. By implementing logically distributed processes within a centralized computational framework, the system achieves a 99% experimental success rate—substantially outperforming comparable approaches that struggled with initialization and communication resilience.

A fundamental contribution of our work is the versatile control framework that operates with virtually any COTS drone equipped with video feedback capabilities. This design enables drift-free visual localization using only onboard cameras, allowing operation across diverse environments without specialized infrastructure.

The architectural contributions provide methodological insights into designing hierarchical perception-action loops for resource-constrained autonomous systems. By balancing performance, accessibility, and usability, AirSwarm establishes a foundation for democratizing access to sophisticated robotics research, potentially accelerating the transition of swarm technologies from laboratory demonstrations to practical field applications across multiple disciplines.

## References

- [1] Y. Lyu, T.-M. Nguyen, L. Liu, M. Cao, S. Yuan, T. H. Nguyen, and L. Xie, “Spins: A structure priors aided inertial navigation system,” Journal of Field Robotics, vol. 40, no. 4, pp. 879–900, 2023.
- [2] M. Cao, T.-M. Nguyen, S. Yuan, A. Anastasiou, A. Zacharia, S. Papaioannou, P. Kolios, C. G. Panayiotou, M. M. Polycarpou, X. Xu, et al., “Cooperative aerial robot inspection challenge: A benchmark for heterogeneous multi-uav planning and lessons learned,” arXiv preprint arXiv:2501.06566, 2025.
- [3] Y. Lyu, S. Yuan, and L. Xie, “Structure priors aided visual-inertial navigation in building inspection tasks with auxiliary line features,” IEEE Transactions on Aerospace and Electronic Systems, vol. 58, no. 4, pp. 3037–3048, 2022.
- [4] X. Xu, M. Cao, S. Yuan, T. H. Nguyen, T.-M. Nguyen, and L. Xie, “A cost-effective cooperative exploration and inspection strategy for heterogeneous aerial system,” in Proceedings of the 2024 IEEE International Conference on Control and Automation (ICCA). IEEE, 2024, pp. 673–678.
- [5] F. Zhu, Y. Ren, L. Yin, F. Kong, Q. Liu, R. Xue, W. Liu, Y. Cai, G. Lu, H. Li, et al., “Swarm-lio2: Decentralized, efficient lidar-inertial odometry for uav swarms,” IEEE Transactions on Robotics, 2024.
- [6] H. Li, H. Wang, C. Feng, F. Gao, B. Zhou, and S. Shen, “Autotrans: A complete planning and control framework for autonomous uav payload transportation,” IEEE Robotics and Automation Letters, vol. 8, no. 10, pp. 6859–6866, 2023.
- [7] T. Ji, S. Yuan, and L. Xie, “Robust rgb-d slam in dynamic environments for autonomous vehicles,” in 2022 17th International Conference on Control, Automation, Robotics and Vision (ICARCV). IEEE, 2022, pp. 665–671.
- [8] H. Xu, P. Liu, X. Chen, and S. Shen, “D2slam: Decentralized and distributed collaborative visual-inertial slam system for aerial swarm,” IEEE Transactions on Robotics, 2024.
- [9] S. Yuan and H. Wang, “Autonomous object level segmentation,” in Proceedings of International Conference on Control, Automation, Robotics and Vision (ICARCV 2014), 2014, pp. 33–37.
- [10] X. Zhou, X. Wen, Z. Wang, Y. Gao, H. Li, Q. Wang, T. Yang, H. Lu, Y. Cao, C. Xu, et al., “Swarm of micro flying robots in the wild,” Science Robotics, vol. 7, no. 66, p. eabm5954, 2022.
- [11] L. Yin, F. Zhu, Y. Ren, F. Kong, and F. Zhang, “Decentralized swarm trajectory generation for lidar-based aerial tracking in cluttered environments,” in 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2023, pp. 9285–9292.
- [12] Y. Gao, Y. Wang, X. Zhong, T. Yang, M. Wang, Z. Xu, Y. Wang, Y. Lin, C. Xu, and F. Gao, “Meeting-merging-mission: A multi-robot coordinate framework for large-scale communication-limited exploration,” in 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2022, pp. 13 700–13 707.
- [13] Y. Zhang, X. Chen, P. Liu, J. Wang, H. Zou, N. Pan, F. Gao, and S. Shen, “Uniquad: A unified and versatile quadrotor platform series for uav research and application,” in 40th Anniversary of the IEEE Conference on Robotics and Automation (ICRA@40), IEEE. Rotterdam, Netherlands: IEEE, September 2024.
- [14] I. Sa, M. Kamel, M. Burri, M. Bloesch, R. Khanna, M. Popović, J. Nieto, and R. Siegwart, “Build your own visual-inertial drone: A cost-effective and open-source autonomous drone,” IEEE Robotics & Automation Magazine, vol. 25, no. 1, pp. 89–103, 2017.
- [15] T. Baca, M. Petrlik, M. Vrba, V. Spurny, R. Penicka, D. Hert, and M. Saska, “The mrs uav system: Pushing the frontiers of reproducible research, real-world deployment, and education with autonomous unmanned aerial vehicles,” Journal of Intelligent & Robotic Systems, vol. 102, no. 1, p. 26, 2021.
- [16] P. Foehn, E. Kaufmann, A. Romero, R. Penicka, S. Sun, L. Bauersfeld, T. Laengle, G. Cioffi, Y. Song, A. Loquercio, et al., “Agilicious: Open-source and open-hardware agile quadrotor for vision-based flight,” Science robotics, vol. 7, no. 67, p. eabl6259, 2022.
- [17] N. Pan, R. Jin, C. Xu, and F. Gao, “Canfly: A can-sized autonomous mini coaxial helicopter,” in 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2023, pp. 4989–4996.
- [18] N. Chen, Z. Li, L. Quan, X. Chen, C. Xu, F. Gao, and Y. Cao, “Cost-effective swarm navigation system via close cooperation,” IEEE Robotics and Automation Letters, 2024.
- [19] M. A. Esfahani, K. Wu, S. Yuan, and H. Wang, “A new approach to train convolutional neural networks for real-time 6-dof camera relocalization,” in 2018 IEEE 14th international conference on control and automation (ICCA). IEEE, 2018, pp. 81–85.
- [20] H. Wang, S. Yuan, and K. Wu, “Heterogeneous stereo: A human vision inspired method for general robotics sensing,” in TENCON 2017-2017 IEEE Region 10 Conference. IEEE, 2017, pp. 793–798.
- [21] M. A. Esfahani, H. Wang, K. Wu, and S. Yuan, “Unsupervised scene categorization, path segmentation and landmark extraction while traveling path,” in 2020 16th International Conference on Control, Automation, Robotics and Vision (ICARCV). IEEE, 2020, pp. 190–195.
- [22] A. Kushleyev, D. Mellinger, C. Powers, and V. Kumar, “Towards a swarm of agile micro quadrotors,” Autonomous Robots, vol. 35, no. 4, pp. 287–300, 2013.
- [23] K. Mohta, M. Watterson, Y. Mulgaonkar, S. Liu, C. Qu, A. Makineni, K. Saulnier, K. Sun, A. Zhu, J. Delmerico, et al., “Fast, autonomous flight in gps-denied and cluttered environments,” in 2018 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2018, pp. 1–8.
- [24] S. Hauert, S. Leven, M. Varga, F. Ruini, A. Cangelosi, J.-C. Zufferey, and D. Floreano, “Reynolds flocking in reality with fixed-wing robots: communication range vs. maximum turning rate,” 2011 IEEE/RSJ International Conference on Intelligent Robots and Systems, pp. 5015–5020, 2011.
- [25] S. Lupashin, M. Hehn, M. W. Mueller, A. P. Schoellig, M. Sherback, and R. D’Andrea, “A platform for aerial robotics research and demonstration: The Flying Machine Arena,” Mechatronics, vol. 24, no. 1, pp. 41–54, 2014.
- [26] J. A. Preiss and et al., “Crazyswarm: A large nano-quadcopter swarm,” in IEEE International Conference on Robotics and Automation (ICRA), 2017, pp. 3299–3304.
- [27] M. Cao, Y. Lyu, S. Yuan, and L. Xie, “Online trajectory correction and tracking for facade inspection using autonomous uav,” in 2020 IEEE 16th International Conference on Control & Automation (ICCA). IEEE, 2020, pp. 1149–1154.
- [28] Z. Xiao, Y. Yang, G. Xu, X. Zeng, and S. Yuan, “Av-dtec: Self-supervised audio-visual fusion for drone trajectory estimation and classification,” in arXiv preprint arXiv:2412.16928, 2024.
- [29] A. Lei, T. Deng, H. Wang, J. Yang, and S. Yuan, “Audio array-based 3d uav trajectory estimation with lidar pseudo-labeling,” in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP). IEEE, April 2025.
- [30] H. Liang, Y. Yang, J. Hu, J. Yang, F. Liu, and S. Yuan, “Unsupervised uav 3d trajectories estimation with sparse point clouds,” in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP). IEEE, April 2025.
- [31] Y. Yang, S. Yuan, J. Yang, T. H. Nguyen, M. Cao, T.-M. Nguyen, H. Wang, and L. Xie, “Av-fdti: Audio-visual fusion for drone threat identification,” Journal of Automation and Intelligence, vol. 3, no. 3, pp. 144–151, 2024.
- [32] S. Yuan, Y. Yang, T. H. Nguyen, T.-M. Nguyen, J. Yang, F. Liu, J. Li, H. Wang, and L. Xie, “Mmaud: A comprehensive multi-modal anti-uav dataset for modern miniature drone threats,” in 2024 IEEE International Conference on Robotics and Automation (ICRA), 2024, pp. 2745–2751.
- [33] M. Lieser, H. Tjaden, R. Brylka, L. Löffler, and U. Schwanecke, “A low-cost mobile infrastructure for compact aerial robots under supervision,” in IEEE International Conference on Advanced Robotics (ICAR), 2016, pp. 1–7.
- [34] K. Cao, M. Cao, S. Yuan, and L. Xie, “Direct: A differential dynamic programming based framework for trajectory generation,” IEEE Robotics and Automation Letters, vol. 7, no. 2, pp. 2439–2446, 2022.
- [35] Z. Chen, Y. Xu, S. Yuan, and L. Xie, “ig-lio: An incremental gicp-based tightly-coupled lidar-inertial odometry,” IEEE Robotics and Automation Letters, vol. 9, no. 2, pp. 1883–1890, 2024.
- [36] M. A. Esfahani, K. Wu, S. Yuan, and H. Wang, “From local understanding to global regression in monocular visual odometry,” International Journal of Pattern Recognition and Artificial Intelligence, vol. 34, no. 01, p. 2055002, 2020.
- [37] M. A. Esfahani, H. Wang, B. Bashari, K. Wu, and S. Yuan, “Learning to extract robust handcrafted features with a single observation via evolutionary neurogenesis,” Applied Soft Computing, vol. 106, p. 107424, 2021.
- [38] C. Campos, R. Elvira, J. J. G. Rodríguez, J. M. M. Montiel, and J. D. Tardós, “ORB-SLAM3: An accurate open-source library for visual, visual–inertial, and multimap SLAM,” IEEE Transactions on Robotics, vol. 37, no. 6, pp. 1874–1890, 2021.
- [39] R. Gomez-Ojeda, F.-A. Moreno, D. Zuñiga-Noël, D. Scaramuzza, and J. Gonzalez-Jimenez, “PL-SLAM: A stereo SLAM system through the combination of points and line segments,” IEEE Transactions on Robotics, vol. 35, no. 3, pp. 734–746, 2019.
- [40] Z. Teed and J. Deng, “DROID-SLAM: Deep visual SLAM for monocular, stereo, and RGB-D cameras,” in Advances in Neural Information Processing Systems, vol. 34, 2021, pp. 16 558–16 569.
- [41] S. Chen, K. Liu, C. Wang, S. Yuan, J. Yang, and L. Xie, “Salient sparse visual odometry with pose-only supervision,” IEEE Robotics and Automation Letters, vol. 9, no. 5, pp. 4774–4781, 2024.
- [42] Y. Yang, S. Yuan, and L. Xie, “Overcoming catastrophic forgetting for semantic segmentation via incremental learning,” in 2022 17th International Conference on Control, Automation, Robotics and Vision (ICARCV). IEEE, 2022, pp. 299–304.
- [43] X. Ji, S. Yuan, P. Yin, and L. Xie, “Lio-gvm: an accurate, tightly-coupled lidar-inertial odometry with gaussian voxel map,” IEEE Robotics and Automation Letters, vol. 9, no. 3, pp. 2200–2207, 2024.
- [44] T. Deng, N. Wang, C. Wang, S. Yuan, J. Wang, D. Wang, and W. Chen, “Incremental joint learning of depth, pose and implicit scene representation on monocular camera in large-scale scenes,” in arXiv preprint arXiv:2404.06050, 2024.
- [45] P. Yin, H. Cao, T.-M. Nguyen, S. Yuan, S. Zhang, K. Liu, and L. Xie, “Outram: One-shot global localization via triangulated scene graph and global outlier pruning,” in 2024 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2024, pp. 13 717–13 723.
- [46] H. Cao, Y. Xu, J. Yang, P. Yin, S. Yuan, and L. Xie, “Mopa: Multi-modal prior aided domain adaptation for 3d semantic segmentation,” in 2024 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2024, pp. 9463–9470.
- [47] P. Schmuck and M. Chli, “CCM-SLAM: Robust and efficient centralized collaborative monocular simultaneous localization and mapping for robotic teams,” Journal of Field Robotics (JFR), vol. 36, no. 4, pp. 763–781, 2019.
- [48] J. Hu, M. Mao, H. Bao, G. Zhang, and Z. Cui, “CP-SLAM: Collaborative neural point-based slam system,” in Advances in Neural Information Processing Systems, A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, Eds., vol. 36. Curran Associates, Inc., 2023, pp. 39 429–39 442.
- [49] K. Xu, Y. Hao, S. Yuan, C. Wang, and L. Xie, “Airvo: An illumination-robust point-line visual odometry,” in 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2023, pp. 3429–3436.
- [50] H. Cai, S. Yuan, X. Li, J. Guo, and J. Liu, “Bev-lio (lc): Bev image assisted lidar-inertial odometry with loop closure,” arXiv preprint arXiv:2502.19242, 2025.
- [51] S. Yuan, B. Lou, T.-M. Nguyen, P. Yin, M. Cao, X. Xu, J. Li, J. Xu, S. Chen, and L. Xie, “Large-scale uwb anchor calibration and one-shot localization using gaussian process,” in 2025 IEEE International Conference on Robotics and Automation (ICRA), 2025.
- [52] T.-M. Nguyen, Y. Yang, T.-D. Nguyen, S. Yuan, and L. Xie, “Uloc: Learning to localize in complex large-scale environments with ultra-wideband ranges,” in IEEE International Conference on Robotics and Automation (ICRA), 2025.
- [53] K. Xu, Y. Hao, S. Yuan, C. Wang, and L. Xie, “AirSLAM: An efficient and illumination-robust point-line visual slam system,” IEEE Transactions on Robotics (TRO), 2025. [Online]. Available: https://arxiv.org/abs/2408.03520
- [54] M. A. Esfahani, K. Wu, S. Yuan, and H. Wang, “Towards utilizing deep uncertainty in traditional slam,” in 2019 IEEE 15th International Conference on Control and Automation (ICCA), 2019, pp. 344–349.
- [55] P. Liu, C. Feng, Y. Xu, Y. Ning, H. Xu, and S. Shen, “Omninxt: A fully open-source and compact aerial robot with omnidirectional visual perception,” in 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2024, pp. 10 605–10 612.
- [56] P.-Y. Lajoie and G. Beltrame, “Swarm-slam: Sparse decentralized collaborative simultaneous localization and mapping framework for multi-robot systems,” IEEE Robotics and Automation Letters, vol. 9, no. 1, pp. 475–482, 2024.
- [57] P. Schmuck, T. Ziegler, M. Karrer, J. Perraudin, and M. Chli, “COVINS: Visual-inertial SLAM for centralized collaboration,” in 2021 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct). IEEE, 2021, pp. 171–176.
- [58] M. Patel, M. Karrer, P. Bänninger, and M. Chli, “COVINS-G: A generic back-end for collaborative visual-inertial slam,” in 2023 IEEE International Conference on Robotics and Automation (ICRA), 2023, pp. 2076–2082.
- [59] M. Grupp, “evo: Python package for the evaluation of odometry and slam.” https://github.com/MichaelGrupp/evo, 2017.
- [60] F. Liu, S. Yuan, W. Meng, R. Su, and L. Xie, “Non-cooperative stochastic target encirclement by anti-synchronization control via range-only measurement,” in 2023 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2023, pp. 5480–5485.
- [61] T.-M. Nguyen, X. Xu, T. Jin, Y. Yang, J. Li, S. Yuan, and L. Xie, “Eigen is all you need: Efficient lidar-inertial continuous-time odometry with internal association,” IEEE Robotics and Automation Letters, vol. 9, no. 6, pp. 5330–5337, 2024.


> Note: Extracted Text captured from arXiv HTML (https://arxiv.org/html/2503.06890) because Zotero reported no local attachment. Zotero parent metadata remains authoritative for identity.
