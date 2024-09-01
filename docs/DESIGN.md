# Design and Architecture

## Overview
The Hades FPV Nano Drone is designed with a focus on compactness and functionality. The drone's architecture integrates a Raspberry Pi Zero with brushed motors and telemetry components.

## Hardware Design

- **Raspberry Pi Zero:** Acts as the central controller for the drone.
- **Brushed Motors:** Provide propulsion and maneuverability.
- **Telemetry Components:** Include sensors for real-time data collection.

## Software Design

- **Control Software:** Runs on the Raspberry Pi, handling motor control and telemetry data.
- **Remote Control Application:** Provides an interface for managing the drone from a separate device.

## Schematics
- **Wiring Diagram:** Detailed wiring schematics are available in the `docs` directory.
- **Component Layout:** Overview of component placement within the drone frame.

## Integration
- **Motor Control:** Managed via GPIO pins on the Raspberry Pi.
- **Telemetry Data:** Collected through sensors and transmitted to the remote control application.

For a detailed explanation of the design decisions and component selection, refer to the `docs` directory.

## Future Improvements
- **Enhanced Flight Stability:** Plans for integrating additional stabilization features.
- **Extended Telemetry:** Options for expanding telemetry data collection.



