from pymavlink import mavutil

# Connect to the APM 2.8 via USB
connection_string = "/dev/ttyACM0"  # This is the correct serial device on your Raspberry Pi
baudrate = 115200  # Change this to the correct baud rate for your APM 2.8

# Create a connection to the APM 2.8
mav = mavutil.mavlink_connection(connection_string, baud=baudrate)
# Wait for a heartbeat message from the APM 2.8 to ensure the connection is established
mav.wait_heartbeat()
print("Connected to APM 2.8")
