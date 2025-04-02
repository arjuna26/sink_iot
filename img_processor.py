import os
import cv2
from time import sleep
from datetime import datetime
from sense_hat import SenseHat

# Initialize Sense HAT
sense = SenseHat()

# Ensure ./img directory exists
img_dir = "./img"
os.makedirs(img_dir, exist_ok=True)

# Initialize webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

# set res
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"Resolution set to: {actual_width}x{actual_height}")

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

def capture_photo():
    """Captures a photo from the USB webcam and saves it in ./img."""
    ret, frame = cap.read()  # Capture frame
    if ret:
        filename = os.path.join(img_dir, f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
        cv2.imwrite(filename, frame)  # Save image
        print(f"Photo saved: {filename}")
        
        # Display a success message on the Sense HAT
        sense.show_message("Photo Taken!", text_colour=[0, 255, 0])
    else:
        print("Error: Failed to capture image.")

print("Press the middle button to take a photo...")

# Main loop to listen for joystick events
while True:
    for event in sense.stick.get_events():
        if event.direction == "middle" and event.action == "pressed":
            capture_photo()

# Cleanup (this part never runs unless you stop the script)
cap.release()
cv2.destroyAllWindows()
