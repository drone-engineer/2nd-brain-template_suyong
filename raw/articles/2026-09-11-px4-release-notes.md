# PX4-Autopilot Main Release Notes

Alpha
This contains changes to the PX4 main branch that are not included in the next release (PX4 v1.18).

WARNING
PX4 v1.18 is in beta testing. Update these notes with features that are going to be in main (PX4 v2.0 or later) but not the PX4 v1.18 release.

## Read Before Upgrading
Please continue reading for upgrade instructions.

## Major Changes
- Motor failure recovery for hexarotors
  - CA_FAILURE_MODE
  - CA_REV_THR_FRAC
  - [PX4-Autopilot#28078](https://github.com/PX4/PX4-Autopilot/issues/28078)

## Upgrade Guide
- CA_FAILURE_MODE
- Motor Failure Recovery
  - [PX4-Autopilot#28078](https://github.com/PX4/PX4-Autopilot/issues/28078)

## Other changes
- RTL_TYPE
  - [PX4-Autopilot#26993: fix(navigator): goToNextPositionItem skip loops when required](https://github.com/PX4/PX4-Autopilot/issues/26993)

## Hardware Support
- DroneCAN ESCs
  - [PX4-Autopilot#28364](https://github.com/PX4/PX4-Autopilot/issues/28364)

## Safety
- Geofence Aware Return mode
  - [PX4-Autopilot#27145: feat(navigator): Geofence Aware RTL](https://github.com/PX4/PX4-Autopilot/issues/27145)
  - [PX4-Autopilot#28001: docs(navigator): [geofence] added some more warnings about limitations](https://github.com/PX4/PX4-Autopilot/issues/28001)
- Flight termination
- Battery level failsafe
- COM_LOW_BAT_ACT
- Position Loss Failsafe Action
- COM_POS_FS_ACT
  - [PX4-Autopilot#28064: feat(commander): add terminate options for critical battery and lost position failsafes](https://github.com/PX4/PX4-Autopilot/issues/28064)
- Failure injection
  - SYS_FAILURE_EN
- Motor failure recovery
  - for hexarotors: on a single motor failure the control allocator removes the failed motor and additionally stops
  - CA_FAILURE_MODE
  - CA_REV_THR_FRAC
  - [PX4-Autopilot#28078](https://github.com/PX4/PX4-Autopilot/issues/28078)
- [PX4-Autopilot#26968](https://github.com/PX4/PX4-Autopilot/issues/26968)

## Sensors
- u-blox Diagnostics with u-center
  - [PX4-Autopilot#28280](https://github.com/PX4/PX4-Autopilot/issues/28280)