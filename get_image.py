import picamera
import time

# Define the file name for the image
image_file = 'image.jpg'

# Create a PiCamera object
with picamera.PiCamera() as camera:
    # Optionally, you can adjust the camera's resolution
    camera.resolution = (1920, 1080)
    
    # Give the camera some time to adjust settings before capturing
    time.sleep(2)

    # Capture the image and save it to the specified file
    camera.capture(image_file)

print(f"Image saved as {image_file}")
