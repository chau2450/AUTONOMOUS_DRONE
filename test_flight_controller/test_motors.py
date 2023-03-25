import time
from dronekit import connect
from pymavlink import mavutil

# Connect to the APM 2.8
connection_string = "/dev/ttyACM0"  # Replace this with your serial port
baudrate = 115200
vehicle = connect(connection_string, baud=baudrate, wait_ready=True)

# Arm the motors
vehicle.armed = True
vehicle.flush()

# Wait for the APM 2.8 to arm the motors
while not vehicle.armed:
    print("Waiting for APM 2.8 to arm motors...")
    time.sleep(1)

# Set the throttle to 50% (between 1000 and 2000)
throttle = 1500

# Send the motor command to the APM 2.8
msg = vehicle.message_factory.command_long_encode(
    0, 0,  # target system, target component
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO,  # command
    0,  # confirmation
    9,  # servo number
    throttle,  # servo position in microseconds
    0, 0, 0, 0, 0)  # parameters 2-6 (not used)
vehicle.send_mavlink(msg)
vehicle.flush()

# Wait for 5 seconds
time.sleep(5)

# Disarm the motors
vehicle.armed = False
vehicle.flush()

# Wait for the APM 2.8 to disarm the motors
while vehicle.armed:
    print("Waiting for APM 2.8 to disarm motors...")
    time.sleep(1)

# Close the connection to the APM 2.8
vehicle.close()
