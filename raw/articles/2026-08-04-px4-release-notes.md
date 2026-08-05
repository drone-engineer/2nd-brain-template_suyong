---
source_url: https://api.github.com/repos/PX4/PX4-Autopilot/releases
sha256: 0998144893e0862fce835634b74ab02054c31684b3431c2a37a3cf074ffe37df
fetched: 2026-08-04T08:30:00Z
---
# PX4-Autopilot 최신 릴리즈
**수집일**: 2026-08-04
**출처 URL**: https://api.github.com/repos/PX4/PX4-Autopilot/releases

## v1.18.0-beta1 (2026-07-08) [prerelease]
- 태그: v1.18.0-beta1
- URL: https://github.com/PX4/PX4-Autopilot/releases/tag/v1.18.0-beta1
## What's Changed
This is a pre-release for flight testing, [full release notes can be found here](https://docs.px4.io/main/en/releases/1.18).

**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.17.0-alpha1...v1.18.0-beta1

## v1.18.0-alpha1 (2026-05-13) [prerelease]
- 태그: v1.18.0-alpha1
- URL: https://github.com/PX4/PX4-Autopilot/releases/tag/v1.18.0-alpha1
## What's Changed
This is a pre-release for flight testing, full release notes will be available soon.

**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.17.0-alpha1...v1.18.0-alpha1

## v1.17.0 (2026-05-13) [stable]
- 태그: v1.17.0
- URL: https://github.com/PX4/PX4-Autopilot/releases/tag/v1.17.0
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

## v1.16.2 (2026-04-22) [stable]
- 태그: v1.16.2
- URL: https://github.com/PX4/PX4-Autopilot/releases/tag/v1.16.2
## What's Changed
* [Backport 1.16] fix(ekf2): allow optical flow to start when range finder is height reference by @dakejahl in https://github.com/PX4/PX4-Autopilot/pull/26961
* fix(ekf2): break unbounded recursion [BACKPORT v1.16] by @julianoes in https://github.com/PX4/PX4-Autopilot/pull/27166

## Release Notes
* [Click here to view the full Release Notes](https://docs.px4.io/main/en/releases/1.16.html).
**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.16.1...v1.16.2

## v1.17.0-rc2 (2026-03-13) [prerelease]
- 태그: v1.17.0-rc2
- URL: https://github.com/PX4/PX4-Autopilot/releases/tag/v1.17.0-rc2
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

## v1.17.0-rc1 (2026-03-11) [prerelease]
- 태그: v1.17.0-rc1
- URL: https://github.com/PX4/PX4-Autopilot/releases/tag/v1.17.0-rc1
## What's Changed
* [BACKPORT 1.17] Include PWM Center PR by @ttechnick in https://github.com/PX4/PX4-Autopilot/pull/26317
* [Backport 1.17] Fix VTOL stuck after back-transition in Mission Fast RTL by @AkaiEurus in https://github.com/PX4/PX4-Autopilot/pull/26319
* [BACKPORT] failsafe: Prevent Offboard to Position without RC by @ttechnick in https://github.com/PX4/PX4-Autopilot/pull/26391
* [1.17] CI: replace all usage of addnab/docker-run-action by @mrpollo in https://github.com/PX4/PX4-Autopilot/pull/26480
* [1.17] ci: fix S3 upload so tags don't overwrite stable firmware by @mrpollo in https://github.com/PX4/PX4-Autopilot/pull/26479


**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.17.0-beta1...v1.17.0-rc1
