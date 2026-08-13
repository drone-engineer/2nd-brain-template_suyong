---
source_url: "https://api.github.com/repos/PX4/PX4-Autopilot/releases"
ingested: 2026-08-13
sha256: "86e60e2fc9934883127628305c58371b1697f0be7a1337293b823d980d090f52"
title: "PX4 릴리즈 노트 (2026-08-13)"
captured_via: 2nd-brain-cron
---
# PX4-Autopilot 릴리즈 노트 (2026-08-13)

수집 일시: 2026-08-13T08:30:00Z
출처: https://api.github.com/repos/PX4/PX4-Autopilot/releases

## v1.18.0-beta2

- 이름: v1.18.0-beta2
- 날짜: 2026-08-09
- 프리릴리즈: True
- 드래프트: False

```
## What's Changed
This is a pre-release for flight testing, [full release notes can be found here](https://docs.px4.io/main/en/releases/1.18).

Fixes since beta1:
- Fixed-wing: NaN eas2tas from zero-airspeed division in lat/lon control (#28107), tailsitter false quadchute from wrong attitude frame (#27834)
- QGC compatibility regressions from stricter command validation: multicopter guided takeoff, camera mission items, and VTOL landing patterns are accepted again (#27853, #28079)
- SD card read corruption on STM32H7 boards fixed via NuttX SDMMC cache coherency (#28071)
- Parameter storage: FMUv6X-RT FRAM multi-page writes (#28127), flashparams compaction moved to boot (#28093)
- FMUv6X-RT: boot-time FlexSPI DLL calibration, fixing load-dependent hardfaults (#28141)
- Estimator: external position estimate hard reset while aiding is active (#27856), DroneCAN rangefinder out-of-range readings no longer fused as terrain (#27963)
- Navigation: DO_JUMP set as current mission item is resolved to its target (#28063)
- Battery: unknown time-remaining no longer trips RTL (#27929), coulomb counting uses unclamped dt (#27866)
- Commander: COM_PARACHUTE warning-only mode (#27903), multicopter autotune can re-trigger without reboot (#27851)
- VOXL2 / Qurt platform: implement px4_task_join (#27886), Hexagon NaN comparison fixes (#27931), startup stdout TLS race (#28013), keepalive file directory (#28053)
- GPS: RTCM corrections and moving-baseline data split into separate uORB topics (#27097)
- MAVLink: receive thread stack right-sized (#28124); FMUv4 (Pixracer) configs right-sized for flash margin, dropping UAVCAN, uXRCE-DDS, mag bias estimator, and SIH from the default build (#28124)
- Boards: CUAV X25-mega uses the renamed heater sensor ID parameter (#27846)

**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.18.0-beta1...v1.18.0-beta2

```

## v1.18.0-beta1

- 이름: v1.18.0-beta1
- 날짜: 2026-07-08
- 프리릴리즈: True
- 드래프트: False

```
## What's Changed
This is a pre-release for flight testing, [full release notes can be found here](https://docs.px4.io/main/en/releases/1.18).

**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.17.0-alpha1...v1.18.0-beta1
```

## v1.18.0-alpha1

- 이름: v1.18.0-alpha1
- 날짜: 2026-05-13
- 프리릴리즈: True
- 드래프트: False

```
## What's Changed
This is a pre-release for flight testing, full release notes will be available soon.

**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.17.0-alpha1...v1.18.0-alpha1
```

## v1.17.0

- 이름: v1.17.0 - Stable Release
- 날짜: 2026-05-13
- 프리릴리즈: False
- 드래프트: False

```
## What's Changed
PX4 v1.17 builds on [PX4 v1.16](https://docs.px4.io/main/en/releases/1.16), with the changes below landing since v1.16.2. This release adds [Altitude Cruise](https://docs.px4.io/main/en/flight_modes_mc/altitude_cruise) mode, improves Fixed Wing Takeoff behaviour on navigation loss, and exposes cleaner high-level fixed-wing and rover control interfaces for ROS 2 workflows. The in-tree Zenoh middleware matures to rmw_zenoh compatibility, simulation gains Gazebo Jetty support and Ackermann SIH, and three new INS drivers (MicroStrain, sbgECom, EULER-NAV) join the ecosystem alongside Septentrio GNSS resilience reporting and barometer auto-calibration against GNSS height. PX4 v1.17 also includes user-visible MAVLink, RC, logging, failsafe, and rover refinements across the stack.

## Major Changes
* New multicopter flight mode: [Altitude Cruise](https://docs.px4.io/main/en/flight_modes_mc/altitude_cruise). Holds tilt and heading on stick release so the vehicle keeps cruising at a steady velocity instead of stopping like Altitude mode does.
* [Fixed Wing Takeoff mode](https://docs.px4.io/main/en/flight_modes_fw/takeoff) now keeps climbing with level wings on navigation loss and can use the takeoff waypoint latitude and longitude to define the loiter position. ([PX4-Autopilot#25226](https://github.com/PX4/PX4-Autopilot/pull/25226))
* Fixed-wing vehicles (and VTOLs in fixed-wing mode) can now be controlled from ROS 2 via the new [FwLateralLongitudinalSetpointType](https://docs.px4.io/main/en/ros2/px4_ros2_control_interface#fw-lateral-longitudinal-setpoint) in the PX4 ROS 2 Control Interface, exposing direct lateral and longitudinal setpoints.
* Rovers can now be controlled from ROS 2 via the new [RoverSetpointTypes](https://docs.px4.io/main/en/ros2/px4_ros2_control_interface#rover-setpoints) in the PX4 ROS 2 Control Interface, with valid combinations of position, speed, throttle, attitude, rate, and steering setpoints exposed as guaranteed-valid setpoint types. See [Rovers Apps & API](https://docs.px4.io/main/en/flight_modes_rover/api).
* The in-tree [Zenoh middleware](https://docs.px4.io/main/en/middleware/zenoh) matures to rmw_zenoh compatibility (CDRv1 serialization, ROS 2 graph liveliness, auto-generated config from dds_topics.yaml, Domain ID parameter, Zenoh CLI). Zenoh is built into the default firmware on FMU-v6xRT (make px4_fmu-v6xrt_default); on FMU-v6x and SITL it ships as a zenoh build variant (make px4_fmu-v6x_zenoh, make px4_sitl_zenoh).
* Initial [MC Neural Network Control](https://docs.px4.io/main/en/neural_networks/mc_neural_network_control) test path: PX4 v1.17 integrates [TensorFlow Lite Micro](https://docs.px4.io/main/en/neural_networks/tflm) on-device so an externally trained network (for example trained with reinforcement learning in [Aerial Gym](https://ntnu-arl.github.io/aerial_gym_simulator/)) can be loaded as a tflite model and substituted for the multicopter controller for research and bench testing. It is not a replacement for the production controller stack.([PX4-Autopilot#24366](https://github.com/PX4/PX4-Autopilot/pull/24366))

## Release Notes
* [Click here to view the full Release Notes](https://docs.px4.io/main/en/releases/1.17)
* Full Changelog [v1.16.2...v1.17.0](https://github.com/PX4/PX4-Autopilot/compare/v1.16.2...v1.17.0)

## New Contributors
* @ischollETH - first contribution: #25215
* @vololand - first contribution: #25362
* @czx-fly - first contribution: #25364
* @Sayshara - first contribution: #24991
* @accton-iot - first contribution: #25102
* @ljarvela - first contribution: #25454
* @fbaklanov - first contribution: #24534
* @renjieDLUT - first contribution: #25527
* @rmahoney-skai - first contribution: #25539
* @HTRamsey - first contribution: #25486
* @jyhminwang - first contribution: #25411
* @tolesam - first contribution: #24137
* @SolderSyntax - first contribution: #25441
* @alexespinoza28 - first contribution: #25525
* @Hs293Go - first contribution: #25444
* @tobias-auterion - first contribution: #25602
* @Luka-Filipovic - first contribution: #25618
* @Louis-max-H - first contribution: #25012
* @msberk - first contribution: #25587
* @Parkhb1106 - first contribution: #25619
* @radiolinkW - first contribution: #25562
* @Siri2K - first contribution: #25637
* @airpixel-cz - first contribution: #25651
* @JacopoPan - first contribution: #24040
* @annoybot - first contribution: #25649
* @asherikov - first contribution: #25742
* @ttechnick - first contribution: #25897
* @MDEAGEWT - first contribution: #25776
* @AkaiEurus - first contribution: #26199

```

## v1.16.2

- 이름: v1.16.2 - Stable Release
- 날짜: 2026-04-22
- 프리릴리즈: False
- 드래프트: False

```
## What's Changed
* [Backport 1.16] fix(ekf2): allow optical flow to start when range finder is height reference by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/26961
* fix(ekf2): break unbounded recursion [BACKPORT v1.16] by @julianoes in https://github.com/PX4/PX4-Autopilot/pull/27166

## Release Notes
* [Click here to view the full Release Notes](https://docs.px4.io/main/en/releases/1.16.html).
**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.16.1...v1.16.2
```

## v1.17.0-rc2

- 이름: v1.17.0-rc2
- 날짜: 2026-03-13
- 프리릴리즈: True
- 드래프트: False

```
## Security Fixes

  - CVE-2026-32705 - BST device name buffer overflow ([GHSA-79mp](https://github.com/PX4/PX4-Autopilot/security/advisories/GHSA-79mp-34pp-2f3f))
  - CVE-2026-32706 - CRSF variable-length packet buffer overflow ([GHSA-mqgj](https://github.com/PX4/PX4-Autopilot/security/advisories/GHSA-mqgj-hh4g-fg5p))
  - CVE-2026-32707 - TattuCan CAN frame buffer overflow ([GHSA-wxwm](https://github.com/PX4/PX4-Autopilot/security/advisories/GHSA-wxwm-xmx9-hr32))
  - CVE-2026-32708 - Zenoh uORB subscriber stack overflow ([GHSA-69g4](https://github.com/PX4/PX4-Autopilot/security/advisories/GHSA-69g4-hcqf-j45p))
  - CVE-2026-32709 - MAVLink FTP path traversal ([GHSA-fh32](https://github.com/PX4/PX4-Autopilot/security/advisories/GHSA-fh32-qxj9-x32f))
  - CVE-2026-32713 - MAVLink FTP session validation bypass ([GHSA-pp2c](https://github.com/PX4/PX4-Autopilot/security/advisories/GHSA-pp2c-jr5g-6f2m))

## What's Changed
* fix(security): backport security fixes to release/1.17 by @mrpollo in https://github.com/PX4/PX4-Autopilot/pull/26741


**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.17.0-rc1...v1.17.0-rc2

```

