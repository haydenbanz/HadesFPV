# Raspberry Pi Zero Drone Circuit Design

## Components Required

- **Raspberry Pi Zero W**
- **Brushed Motors (4x)**
- **Motor Driver (L298N or similar)**
- **LiPo Battery (2S or 3S)**
- **MCU Sensor (e.g., MPU6050)**
- **Propellers**
- **Power Distribution Board (optional)**
- **Connectors and Wires**
- **Voltage Regulator (5V)**
- **Telemetry Module (optional for communication with Mission Planner)**
- **Breadboard (optional for prototyping)**
- **Miscellaneous (soldering tools, heat shrink, etc.)**

## Circuit Connections

### 1. Power Supply
- **LiPo Battery**: Connect the LiPo battery to the power distribution board (PDB) if using one. If not, connect the battery directly to the motor driver and voltage regulator.
- **Voltage Regulator**: Use a 5V regulator to power the Raspberry Pi Zero W and other 5V components.
  - **Output**: 5V to Raspberry Pi Zero W `5V` pin and `GND` pin.

### 2. Motor Connections
- **Motor Driver (L298N)**:
  - **IN1, IN2, IN3, IN4**: Connect these to GPIO pins on the Raspberry Pi Zero W (e.g., `GPIO17`, `GPIO18`, `GPIO27`, `GPIO22`).
  - **OUT1, OUT2, OUT3, OUT4**: Connect these to the positive terminals of the brushed motors.
  - **GND**: Connect to the common ground.
  - **12V**: Connect to the positive terminal of the LiPo battery (if directly powering from the battery).

- **Motors**:
  - **Positive Terminal**: Connect to the corresponding output pins of the motor driver.
  - **Negative Terminal**: Connect to the motor driver’s ground.

### 3. Sensor Connections
- **MCU Sensor (e.g., MPU6050)**:
  - **VCC**: Connect to the 3.3V pin on the Raspberry Pi Zero W.
  - **GND**: Connect to the common ground.
  - **SCL**: Connect to `GPIO3 (SCL)` on the Raspberry Pi.
  - **SDA**: Connect to `GPIO2 (SDA)` on the Raspberry Pi.

### 4. Telemetry Module (Optional)
- **Telemetry Module**:
  - **TX**: Connect to `GPIO14 (TXD)` on the Raspberry Pi Zero W.
  - **RX**: Connect to `GPIO15 (RXD)` on the Raspberry Pi Zero W.
  - **VCC**: Connect to the 5V pin.
  - **GND**: Connect to the common ground.

### 5. Propellers
- **Propellers**:
  - Attach the propellers to the motors. Ensure that the propeller direction matches the motor rotation direction.

### 6. Additional Connections (Optional)
- **LED Indicators** (optional):
  - Connect an LED to a GPIO pin for status indication, with an appropriate resistor.

### 7. Common Ground
- Ensure all components share a common ground to avoid issues with different voltage levels.

### 8. Raspberry Pi Zero W GPIO Layout
Here’s a quick reference for the Raspberry Pi Zero W GPIO pins used:

| GPIO Pin | Function       | Connected Component              |
|----------|----------------|----------------------------------|
| GPIO17   | Motor IN1       | Motor Driver IN1                |
| GPIO18   | Motor IN2       | Motor Driver IN2                |
| GPIO27   | Motor IN3       | Motor Driver IN3                |
| GPIO22   | Motor IN4       | Motor Driver IN4                |
| GPIO3    | SCL             | MPU6050 (SCL)                   |
| GPIO2    | SDA             | MPU6050 (SDA)                   |
| GPIO14   | TXD             | Telemetry Module TX             |
| GPIO15   | RXD             | Telemetry Module RX             |
| 5V       | Power           | Voltage Regulator, Sensors, etc.|
| GND      | Ground          | Common Ground                   |

---

## Circuit Diagram

While this text describes the connections, it's recommended to create a visual schematic using tools like Fritzing, KiCad, or similar for better clarity.

