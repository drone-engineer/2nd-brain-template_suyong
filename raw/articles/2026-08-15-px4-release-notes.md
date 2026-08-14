---
source_url: "https://api.github.com/repos/PX4/PX4-Autopilot/releases"
ingested: 2026-08-15
title: PX4 릴리즈 노트 (2026-08-15)
captured_via: 2nd-brain-cron
sha256: eacd366d36b9ceadaf197b7520201d27716c153e5f119475b482f85adfd4c2a9
---
# PX4-Autopilot 릴리즈 노트 (2026-08-15)

수집 일시: 2026-08-15T08:30:00Z
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

## v1.17.0-rc1

- 이름: v1.17.0-rc1
- 날짜: 2026-03-11
- 프리릴리즈: True
- 드래프트: False

```
## What's Changed
* [BACKPORT 1.17] Include PWM Center PR by @ttechnick in https://github.com/PX4/PX4-Autopilot/pull/26317
* [Backport 1.17] Fix VTOL stuck after back-transition in Mission Fast RTL by @AkaiEurus in https://github.com/PX4/PX4-Autopilot/pull/26319
* [BACKPORT] failsafe: Prevent Offboard to Position without RC by @ttechnick in https://github.com/PX4/PX4-Autopilot/pull/26391
* [1.17] CI: replace all usage of addnab/docker-run-action by @mrpollo in https://github.com/PX4/PX4-Autopilot/pull/26480
* [1.17] ci: fix S3 upload so tags don't overwrite stable firmware by @mrpollo in https://github.com/PX4/PX4-Autopilot/pull/26479


**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.17.0-beta1...v1.17.0-rc1
```

## v1.17.0-beta1

- 이름: v1.17.0-beta1
- 날짜: 2026-01-21
- 프리릴리즈: True
- 드래프트: False

```
## What's Changed
* [BACKPORT 1.17] Zenoh docs and zenoh oom fixes by @PetervdPerk-NXP in https://github.com/PX4/PX4-Autopilot/pull/26053
* [BACKPORT 1.17] imxrt related fixes and mr-tropic support by @PetervdPerk-NXP in https://github.com/PX4/PX4-Autopilot/pull/26052
* [1.17] Bugfix: Let user take over from a degraded failsafe by @MaEtUgR in https://github.com/PX4/PX4-Autopilot/pull/26269
* FW Takeoff: fix loiter altitude not set in some cases by @sfuhrer in https://github.com/PX4/PX4-Autopilot/pull/26293


**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.17.0-alpha1...v1.17.0-beta1
```

## v1.16.1

- 이름: v1.16.1 - Stable Release
- 날짜: 2026-01-21
- 프리릴리즈: False
- 드래프트: False

```
## What's Changed
* [Backport 1.16] of fix: let UXRCE DDS agent IP to be set via parameter in SITL (#25231) by @sansha in https://github.com/PX4/PX4-Autopilot/pull/25299
* VOXL2 patch back port for release 1.16 by @katzfey in https://github.com/PX4/PX4-Autopilot/pull/25377
* [v1.16] Add relnote etc by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25384
* [BACKPORT] commander: accel cal rotate offsets and scales from body frame back into sensor frame before saving (#25626) by @dagar in https://github.com/PX4/PX4-Autopilot/pull/25639
* [Docs] PX4 v1.16 Add warning for RTL mode issues in return.md by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25623
* Docs deploy AWS to v1.16 branch by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25641
* Fix formatting to trigger v1.16 release build for testing by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25643
* [BACKPORT 1.16] boards: ark_fpv add vtol att control by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25655
* [backport] macos ci fixes for v1.16 by @mrpollo in https://github.com/PX4/PX4-Autopilot/pull/25672
* AWS docs deploy workflow - modify release branch to same form by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25678
* Fix up v1.16 docs version by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25679
* Trigger v1.16 docs build by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25681
* Trigger v1.16 docs build 3 by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25682
* ci: docs deploy branchname for build step by @mrpollo in https://github.com/PX4/PX4-Autopilot/pull/25684
* docs: fix deploy variables by @mrpollo in https://github.com/PX4/PX4-Autopilot/pull/25685
* Change runner to ubuntu-latest for deployment by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25686
* Update GitHub Actions output setting syntax to use envfile by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25687
* AWS docs deployment - revert runs-on from ubuntu for test by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25689
* AWS docs deployment - add back paths revert runner by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25690
* [BACKPORT 1.16] uavcan: esc: init msg to avoid publishing random values by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25656
* [BACKPORT 1.16] mavlink: add message spacing for AVAILABLE_MODES, for low bandwidth by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25662
* [BACKPORT 1.16] cuav_7-nano：use new sensors (#25098) by @cuav-liu1 in https://github.com/PX4/PX4-Autopilot/pull/25546
* [v1.16 backport] Enable clean URLs in VitePress config by @hamishwillee in https://github.com/PX4/PX4-Autopilot/pull/25759
* [BACKPORT 1.16] V6X-RT Add sensor set V6XRT001 and V6XRT002 by @PetervdPerk-NXP in https://github.com/PX4/PX4-Autopilot/pull/25732
* [BACKPORT 1.16] ci: fix failsafe sim by @MaEtUgR in https://github.com/PX4/PX4-Autopilot/pull/25768
* [BACKPORT 1.16] flight task auto: fix offtrack mission landing bug by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25726
* [BACKPORT 1.16] Loiter at the last mission waypoint on mission end by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25727
* [BACKPORT 1.16] Correction of routing issue of mavlink parameter messages to CAN nodes by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25658
* [BACKPORT 1.16] serial: nuttx: revert tcdrain back to fsync by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25657
* [BACKPORT 1.16] mission: delay until: mark next setpoint invalid by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25729
* [Backport 1.16] modules/navigator: Fix position setpoint update logic in Mission RTL by @msberk in https://github.com/PX4/PX4-Autopilot/pull/25861
* [Docs] [Backport 1.16] flight_modes_fw/return.md: remove warning about now-fixed RTL bug by @msberk in https://github.com/PX4/PX4-Autopilot/pull/25869
* [BACKPORT 1.16] drivers/gps: RTCM injection fixes by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25862


## Release Notes
* [Click here to view the full Release Notes](https://docs.px4.io/main/en/releases/1.16.html).
* **Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.16.0...v1.16.1
```

## v1.16.1-rc2

- 이름: v1.16.1-rc2
- 날짜: 2025-11-17
- 프리릴리즈: True
- 드래프트: False

```
## What's Changed
* [BACKPORT 1.16] Correction of routing issue of mavlink parameter messages to CAN nodes by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25658
* [BACKPORT 1.16] serial: nuttx: revert tcdrain back to fsync by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25657
* [BACKPORT 1.16] mission: delay until: mark next setpoint invalid by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25729
* [Backport 1.16] modules/navigator: Fix position setpoint update logic in Mission RTL by @msberk in https://github.com/PX4/PX4-Autopilot/pull/25861
* [Docs] [Backport 1.16] flight_modes_fw/return.md: remove warning about now-fixed RTL bug by @msberk in https://github.com/PX4/PX4-Autopilot/pull/25869
* [BACKPORT 1.16] drivers/gps: RTCM injection fixes by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/25862


**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.16.1-rc1...v1.16.1-rc2
```
