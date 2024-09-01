# Installation Guide

## Hardware Requirements
- Raspberry Pi Zero
- Brushed motors
- Telemetry components
- Battery pack
- Frame and other drone components

## Software Requirements
- Raspbian OS installed on Raspberry Pi Zero
- Required Python libraries (see `requirements.txt`)

## Steps to Install

1. **Prepare the Raspberry Pi Zero:**
   - Install Raspbian OS on the Raspberry Pi Zero.
   - Connect the Raspberry Pi to your network.

2. **Install Dependencies:**
   - Clone the repository:
     ```bash
     git clone https://github.com/yourusername/hades-fpv-nano-drone.git
     cd hades-fpv-nano-drone
     ```
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure Hardware:**
   - Connect the brushed motors to the appropriate GPIO pins on the Raspberry Pi.
   - Set up telemetry components according to the schematic in `DESIGN.md`.

4. **Set Up Remote Control:**
   - Install and configure the remote control application as per the instructions in `USAGE.md`.

5. **Test the Setup:**
   - Run the test scripts provided in the `test` directory to ensure everything is working correctly.

For troubleshooting, refer to the FAQ section in the repository.

## Additional Resources
- [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)
- [Brushed Motors Guide](https://example.com/brushed-motors-guide)
