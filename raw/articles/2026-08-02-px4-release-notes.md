---
source_url: https://api.github.com/repos/PX4/PX4-Autopilot/releases
sha256: b9b904b84caf72a5c1746fbd2d18951688387a4e241c448927738021e657cf3e
fetched: 2026-08-02T08:30:00Z
---
# PX4-Autopilot 최신 릴리즈
**수집일**: 2026-08-02

## v1.18.0-beta1 (2026-07-08) [prerelease]
## What's Changed
This is a pre-release for flight testing, [full release notes can be found here](https://docs.px4.io/main/en/releases/1.18).

**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.17.0-alpha1...v1.18.0-beta1

## v1.18.0-alpha1 (2026-05-13) [prerelease]
## What's Changed
This is a pre-release for flight testing, full release notes will be available soon.

**Full Changelog**: https://github.com/PX4/PX4-Autopilot/compare/v1.17.0-alpha1...v1.18.0-alpha1

## v1.17.0 (2026-05-13) 
## What's Changed
PX4 v1.17 builds on [PX4 v1.16](https://docs.px4.io/main/en/releases/1.16), with the changes below landing since v1.16.2. This release adds [Altitude Cruise](https://docs.px4.io/main/en/flight_modes_mc/altitude_cruise) mode, improves Fixed Wing Takeoff behaviour on navigation loss, and exposes cleaner high-level fixed-wing and rover control interfaces for ROS 2 workflows. The in-tree Zenoh middleware matures to rmw_zenoh compatibility, simulation gains Gazebo Jetty support and Ackermann SIH, and three new INS drivers (MicroStrain, sbgECom, EULER-NAV) join the ecosystem alongside Septentrio GNSS resilience reporting and barometer auto-calibration against GNSS height. PX4 v1.17 also includes user-visible MAVLink, RC, logging, failsafe, and rover refinements across the stack.

## Major Changes
* New multicopter flight mode: [Altitude Cruise](https://docs.px4.io/main/en/flight_modes_mc/altitude_cruise). Holds tilt and heading on stick release so the vehicle keeps cruising at a steady velocity instead of stopping like Altitude mode does.
* [Fixed Wing Takeoff mode](https://docs.px4.io/main/en/flight_modes_fw/takeoff) now keeps climbing with level wings on navigation loss and can use the takeoff waypoint latitude and longitude to define the loiter position. ([PX4-Autopilot#25226](https://github.com/PX4/PX4-Autopilot/pull/25226))
* Fixed-wing vehicles (and VTOLs in fixed-wing mode) can now be controlled from ROS 2 via the new [FwLateralLongitudinalSetpointType](https://docs.px4.io/main/en/ros2/px4_ros2_control_interface#fw-lateral-longitudinal-setpoint) in the PX4 ROS 2 Control Interface, exposing direct lateral and longitudinal setpoints.
* Rovers can now be controlled from ROS 2 via the new [RoverSetpointTypes](https://docs.px4.io/main/en/ros2/px4_ros2_control_interface#rover-setpoints) in the PX4 ROS 2 Control Interface, with valid combinations of position, speed, throttle, attitude, rate, and steering setpoints exposed as guaranteed-valid setpo

