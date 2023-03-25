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



# import cv2
# import numpy as np

# # Initialize the camera capture object
# cap = cv2.VideoCapture(0)

# # Check if the camera was successfully initialized
# if not cap.isOpened():
#     print("Error: Could not open camera.")
#     exit()

# # Set the camera capture resolution
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# # Capture an image from the camera
# ret, frame = cap.read()

# # Check if the image was successfully captured
# if not ret:
#     print("Error: Could not capture image.")
#     exit()

# # Encode the frame as a JPEG
# ret, buffer = cv2.imencode(".jpg", frame)

# # Check if encoding was successful
# if not ret:
#     print("Error: Could not encode image.")
#     exit()

# # Convert the JPEG buffer to a NumPy array
# img_array = np.array(buffer)

# # Save the captured image to a file
# with open("image.jpg", "wb") as f:
#     f.write(img_array)

# # Release the camera capture object
# cap.release()

# print("Image captured successfully.")
