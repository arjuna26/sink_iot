import os
import time
from google.cloud import storage, vision
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set up Google Cloud Storage client
storage_client = storage.Client.from_service_account_json('/home/arjun/.google/cpsc341-455603-42d7eb9255f6.json')
bucket_name = 'cpsc341-images' 
bucket = storage_client.get_bucket(bucket_name)

# Set up Google Cloud Vision client
vision_client = vision.ImageAnnotatorClient()

def extract_text(image_path):
    """Extracts text from an image using Google Cloud Vision."""
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = vision_client.text_detection(image=image)
    texts = response.text_annotations
    if texts:
        return texts[0].description  # Full text
    return ""

def upload_text(text, original_image_path):
    """Uploads extracted text as a .txt file to the bucket."""
    txt_filename = os.path.splitext(os.path.basename(original_image_path))[0] + ".txt"
    blob = bucket.blob(txt_filename)
    blob.upload_from_string(text)
    print(f"Extracted text uploaded as {txt_filename}")

class WatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            print(f"New image detected: {event.src_path}")
            text = extract_text(event.src_path)
            upload_text(text, event.src_path)

# Function to monitor the directory
def monitor_directory(path='./img/'):
    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_directory()
