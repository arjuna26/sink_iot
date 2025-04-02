import os
import time
from google.cloud import storage
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set up Google Cloud Storage client
storage_client = storage.Client.from_service_account_json('/home/arjun/.google/cpsc341-455603-42d7eb9255f6.json')

# Your bucket name
bucket_name = 'cpsc341-images'  # Replace with your actual bucket name
bucket = storage_client.get_bucket(bucket_name)

# Function to upload image
def upload_image(image_path):
    blob = bucket.blob(os.path.basename(image_path))  # Set blob name to the image filename
    blob.upload_from_filename(image_path)
    print(f"Image {image_path} uploaded successfully!")

# Event handler class
class WatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  # Add other image extensions as needed
            print(f"New image detected: {event.src_path}")
            upload_image(event.src_path)

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

