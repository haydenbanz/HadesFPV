from pymavlink import mavutil

# Connect to the vehicle
connection = mavutil.mavlink_connection('/dev/serial0', baud=57600)

# Wait for a heartbeat from the vehicle
connection.wait_heartbeat()

# Arm the vehicle
connection.mav.command_long_send(
    connection.target_system,    # target_system
    connection.target_component, # target_component
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, # command
    0, # confirmation
    1, # param1 (1 to arm, 0 to disarm)
    0, 0, 0, 0, 0, 0)  # param2-7 (unused)

# Wait for the vehicle to arm
print("Waiting for the vehicle to arm")
connection.motors_armed_wait()

# Control the motors
def set_motor_pwm(pwm_value):
    connection.mav.rc_channels_override_send(
        connection.target_system,  # target_system
        connection.target_component,  # target_component
        pwm_value, pwm_value, pwm_value, pwm_value,  # RC channel 1-4
        0, 0, 0, 0)  # RC channel 5-8 (unused)

# Example: Run the motors at half throttle
set_motor_pwm(1500)

# Add your main loop or other functionality here...

# Disarm the vehicle
connection.mav.command_long_send(
    connection.target_system,
    connection.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0,  # Disarm
    0, 0, 0, 0, 0, 0)
