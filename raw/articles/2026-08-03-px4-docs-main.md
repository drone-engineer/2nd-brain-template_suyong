---
source_url: https://docs.px4.io/main/en/
sha256: 2d880287b3761adc98aaed73c1461edc5e35f2a4c2b91dfd9b052cbcc03bf52e
fetched: 2026-08-03T08:30:00Z
---
# PX4 공식 문서 (docs.px4.io)
**수집일**: 2026-08-03

## 메인 페이지

PX4 Autopilot User Guide | PX4 Guide (main)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Skip to content

MenuReturn to top

PX4 Autopilot User Guide ​
 
PX4 is an open-source autopilot for drones and autonomous vehicles. It runs on multirotors, fixed-wing, VTOL, helicopters, rovers, and more. This guide covers everything from assembly and configuration to flight operations and development.
WARNING
This guide is for the development version of PX4 (main branch). Use the Version selector to find the current stable version.
Documented changes since the stable release are captured in the evolving release note.

Try PX4 ​
No hardware needed. Run PX4 in simulation with a single command using Docker or a .deb package. Connect QGroundControl, MAVSDK, or ROS 2 and start flying immediately.
For Developers ​
Want to modify PX4 or build from source? Start with the Development Guide: set up your dev environment, build the code, and run SITL simulation.
Getting Started ​
Start with Basic Concepts for an overview of the flight stack, flight modes, safety features, and supported hardware.
Developer Kits ​
The fastest way to get flying hardware for PX4 development. Official PX4 Developer Kits ship with the latest stable PX4 pre-installed on current Pixhawk-standard hardware, need no build skills, and are certified by the PX4 team.
Build a Vehicle ​
Pick your frame type: Multicopter, Fixed-Wing, VTOL, Helicopter, or Rover. Each section covers complete vehicles, kits, and DIY builds. For assembly instructions see Assembling a Multicopter or the equivalent for your frame.
Configure and Tune ​
Once assembled, follow the configuration guide for your vehicle type (e.g. Multicopter Configuration). This covers sensor calibration, flight mode setup, and tuning.
Hardware ​
The Hardware Selection & Setup section covers flight controllers, sensors, telemetry, RC systems, and payloads. See Payloads for camera and delivery integrations.
Fly ​
Read Operations to understand safety features and failsafe behavior before your first flight. Then see Basic Flying (Multicopter) or the equivalent for your frame type.
Support ​
Get help on the discussion forums or Discord. See the Support page for diagnosing problems, reporting bugs, and joining the weekly dev call.
Contributing ​
See the Contributing section for code, documentation, and translation guidelines.
Translations ​
There are several translations of this guide. Use the language selector in the top navigation.
License ​
PX4 code is free to use and modify under the terms of the permissive BSD 3-clause license. This documentation is licensed under CC BY 4.0. For more information see: Licences.
Calendar & Events ​
The Dronecode Calendar shows important community events for platform users and developers. Select the links below to display the calendar in your timezone (and to add it to your own calendar):
Switzerland – Zurich
Pacific Time – Tijuana
Australia – Melbourne/Sydney/Hobart
TIP
The calendar default time

## Releases 페이지

Releases | PX4 Guide (main)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Skip to content

MenuReturn to top

Releases ​
A list of PX4 release notes, they contain a list of the changes that went into each release, explaining the included features, bug fixes, deprecations and updates in detail.
main (changes planned for v1.19 or later)
v1.18 (changes in v1.18, since v1.17)
v1.17
v1.16
v1.15
v1.14
v1.13
v1.12
The full archive of releases for the PX4 autopilot project can be found on GitHub.
INFO
For maintainers, see Release Process for the tagging and publishing workflow.

## ROS2 통합 페이지

ROS 2 | PX4 Guide (main)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Skip to content

MenuReturn to top

ROS 2 ​
ROS 2 is a powerful general purpose robotics library that can be used with the PX4 Autopilot to create powerful drone applications.
Tip
The PX4 development team highly recommend that you use/migrate to this version of ROS!
This is the newest version of ROS (Robot Operating System). It significantly improves on ROS "1", and in particular allows a much deeper and lower-latency integration with PX4.

ROS benefits from an active ecosystem of developers solving common robotics problems, and access to other software libraries written for Linux. It can be used, for example, for computer vision solutions.
ROS 2 enables a very deep integration with PX4, to the extent that you can create flight modes in ROS 2 that are indistinguisable from internal PX4 modes, and directly read from and write to internal uORB topics at high rate. It is recommended (in particular) for control and communication from a companion computer where low latency is important, when leveraging existing libraries from Linux, or when writing new high level flight modes.
Communication between ROS 2 and PX4 can leverage two independent middlewares:
XRCE-DDS protocol — Original middleware. More tested and included by default in most PX4 builds.
Zenoh protocol — Must be manually added and enabled to most PX4 builds.
The middlewares expose PX4 uORB messages as ROS 2 messages and types, effectively allowing direct access to PX4 from ROS 2 workflows and nodes. The middlewares use uORB message definitions to generate code to serialise and deserialise the messages heading in and out of PX4. These same message definitions are used in ROS 2 applications to allow the messages to be interpreted.
INFO
ROS 2 can also connect with PX4 using MAVROS instead of XRCE-DDS / Zenoh. This option is supported by the MAVROS project (it is not documented here).

To use the ROS 2 over XRCE-DDS / Zenoh effectively, you must (at time of writing) have a reasonable understanding of the PX4 internal architecture and conventions, which differ from those used by ROS. In the near term future we plan to provide ROS 2 APIs to abstract PX4 conventions, along with examples demonstrating their use.
Topics ​
The main topics in this section are:
ROS 2 User Guide: A PX4-centric overview of ROS 2, covering installation, setup, and how to build ROS 2 applications that communicate with PX4.
ROS 2 Offboard Control Example: A C++ tutorial examples showing how to do position control in offboard mode from a ROS 2 node.
ROS 2 Multi Vehicle Simulation: Instructions for connecting to multiple PX4 simulations via single ROS 2 agent.
PX4 ROS 2 Interface Library: A C++ library that simplifies interacting with PX4 from ROS 2. Can be used to create and register flight modes written using ROS2 and send position estimates from ROS2 applications such as a VIO system.
ROS 2 Message Translation Node: A ROS 2 message transl

[원본: https://docs.px4.io/main/en/]
