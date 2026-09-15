# PX4 v1.17.0 Stable Release Notes

PX4 v1.17 builds on PX4 v1.16, with the changes below landing since v1.16.2. This release adds Altitude Cruise mode, improves Fixed Wing Takeoff behaviour on navigation loss, and exposes cleaner high-level fixed-wing and rover control interfaces for ROS 2 workflows. The in-tree Zenoh middleware matures to rmw_zenoh compatibility, simulation gains Gazebo Jetty support and Ackermann SIH, and three new INS drivers (MicroStrain, sbgECom, EULER-NAV) join the ecosystem alongside Septentrio GNSS resilience reporting and barometer auto-calibration against GNSS height. PX4 v1.17 also includes user-visible MAVLink, RC, logging, failsafe, and rover refinements across the stack.

## Major Changes

- New multicopter flight mode: Altitude Cruise. Holds tilt and heading on stick release so the vehicle keeps cruising at a steady velocity instead of stopping like Altitude mode does.
- Fixed Wing Takeoff mode
- FwLateralLongitudinalSetpointType
- RoverSetpointTypes
- Zenoh middleware
- MC Neural Network Control test path: PX4 v1.17 integrates TensorFlow Lite Micro, Aerial Gym

## Release Notes

For full release notes, see: https://github.com/PX4/PX4-Autopilot/releases/tag/v1.17.0

## New Contributors

@ischollETH - first contribution: #25215
@vololand - first contribution: #25362
@czx-fly - first contribution: #25364
@Sayshara - first contribution: #24991
@accton-iot - first contribution: #25102
@ljarvela - first contribution: #25454
@fbaklanov - first contribution: #24534
@renjieDLUT - first contribution: #25527
@rmahoney-skai - first contribution: #25539
@HTRamsey - first contribution: #25486
@jyhminwang - first contribution: #25411
@tolesam - first contribution: #24137
@SolderSyntax - first contribution: #25441
@alexespinoza28 - first contribution: #25525
@Hs293Go - first contribution: #25444
@tobias-auterion - first contribution: #25602
@Luka-Filipovic - first contribution: #25618
@Louis-max-H - first contribution: #25012
@msberk - first contribution: #25587
@Parkhb1106 - first contribution: #25619
@radiolinkW - first contribution: #25562
@Siri2K - first contribution: #25637
@airpixel-cz - first contribution: #25651
@JacopoPan - first contribution: #24040
@annoybot - first contribution: #25649
@asherikov - first contribution: #25742
@ttechnick - first contribution: #25897
@MDEAGEWT - first contribution: #25776
@AkaiEurus - first contribution: #26199

## Contributors

asherikov, msberk, and 27 other contributors

## SHA256 Hash

069ea366dd807b9ce0470155f3609d12ab4abeff8c6fec8d487d25e2191866e4