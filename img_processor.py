import os
import cv2
from time import sleep
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()

img_dir = "./img"
os.makedirs(img_dir, exist_ok=True)

cap = cv2.VideoCapture(0, cv2.CAP_V4L2) 

# set resolution
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
    for _ in range(5):
        cap.read()
    ret, frame = cap.read()  
    if ret:
        print(f"Captured frame shape: {frame.shape}") 
        filename = os.path.join(img_dir, f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
        cv2.imwrite(filename, frame)  # Save image
        print(f"Photo saved: {filename}")
        sense.show_message("Nice", text_colour=[0, 255, 0])
    else:
        sense.show_message("Bad", text_colour=[255, 0, 0])
        print("Error: Failed to capture image.")

print("Press the middle button to take a photo...")

while True:
    for event in sense.stick.get_events():
        if event.direction == "middle" and event.action == "pressed":
            capture_photo()
            
cap.release()
cv2.destroyAllWindows()
