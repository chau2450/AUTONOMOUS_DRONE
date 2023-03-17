import time
from pymavlink import mavutil

# Connect to the APM 2.8
connection_string = "/dev/ttyACM0"  # Replace this with your serial port (e.g., /dev/ttyUSB0)
baudrate = 115200
mav = mavutil.mavlink_connection(connection_string, baud=baudrate)

# Wait for a heartbeat to ensure the connection is established
mav.wait_heartbeat()
print("Heartbeat received from APM 2.8")

# Request GPS data
def request_gps_data():
    mav.mav.request_data_stream_send(
        mav.target_system, mav.target_component,
        mavutil.mavlink.MAV_DATA_STREAM_POSITION, 1, 1)

# Main loop
while True:
    request_gps_data()

    msg = mav.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
    if msg:
        lat = msg.lat / 1e7
        lon = msg.lon / 1e7
        alt = msg.alt / 1e3

        print("Current GPS coordinates:")
        print("Latitude:", lat)
        print("Longitude:", lon)
        print("Altitude (meters):", alt)

    time.sleep(1)
