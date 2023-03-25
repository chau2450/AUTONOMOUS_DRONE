import time
from pymavlink import mavutil

# Connect to the APM 2.8 flight controller
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)

# Set the LED to turn on
master.mav.command_long_send(
    master.target_system,  # target system ID
    master.target_component,  # target component ID
    mavutil.mavlink.MAV_CMD_DO_SET_RELAY,  # MAVLink command ID
    0,  # Relay number (0 = LED)
    1,  # Activate the relay (1 = on)
    0,  # Unused parameter
    0, 0, 0, 0, 0  # Unused parameters
)

# Wait for a few seconds
time.sleep(20)

# Set the LED to turn off
master.mav.command_long_send(
    master.target_system,  # target system ID
    master.target_component,  # target component ID
    mavutil.mavlink.MAV_CMD_DO_SET_RELAY,  # MAVLink command ID
    0,  # Relay number (0 = LED)
    0,  # Deactivate the relay (0 = off)
    0,  # Unused parameter
    0, 0, 0, 0, 0  # Unused parameters
)

# Close the MAVLink connection
master.close()
