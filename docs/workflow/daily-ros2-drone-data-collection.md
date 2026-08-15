---
name: daily-ros2-drone-data-collection
type: automation
category: automation
description: Daily collection of ROS2 drone technical data from GitHub API, official docs and release notes
---

# Daily ROS2 Drone Data Collection Workflow

## Overview
This workflow automates the collection of ROS2 drone related technical data from public sources including GitHub API, official documentation, and release notes.

## Steps
1. Collect GitHub repositories using search queries:
   - ros2 drone detection (object detection)
   - ros2 drone autonomous (autonomous flight)  
   - ros2 drone navigation (navigation systems)
   - PX4 ros2 bridge (PX4 integration)
   - YOLO ros2 drone (YOLO object detection)
   - zenoh ros2 middleware (networking)
   - MediaPipe ros2 (computer vision)
   - SLAM ros2 drone (SLAM systems)
   - ArUco ros2 detection (Aruco marker detection)

2. Collect official documentation:
   - PX4 official documentation
   - ROS2 official documentation
   - PX4 release notes
   - ArduPilot release notes

3. Process and format collected data:
   - Save as markdown files with SHA256 checksums
   - Generate daily Korean technical report
   - Commit changes to git repository

## Implementation
- Python script using GitHub API v3 
- Official documentation scrapers
- File integrity validation using SHA256
- Automated reporting in Korean language