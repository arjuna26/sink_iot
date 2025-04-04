from PIL import Image
from pillow_heif import register_heif_opener
import os

def convert_heic_to_jpg(heic_filepath, jpg_filepath):
    """Converts a HEIC image to JPG format."""
    register_heif_opener()
    try:
        image = Image.open(heic_filepath)
        image.convert('RGB').save(jpg_filepath, 'jpeg')
        return True
    except Exception as e:
        print(f"Error converting {heic_filepath}: {e}")
        return False

def batch_convert_heic_to_jpg(directory):
    """Converts all HEIC images in a directory to JPG format."""
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.heic', '.heif')):
            heic_filepath = os.path.join(directory, filename)
            jpg_filepath = os.path.join(directory, os.path.splitext(filename)[0] + '.jpg')
            if convert_heic_to_jpg(heic_filepath, jpg_filepath):
                print(f"Converted {filename} to {os.path.basename(jpg_filepath)}")

if __name__ == "__main__":
    directory = input("Enter the directory containing HEIC files: ")
    if os.path.exists(directory):
        batch_convert_heic_to_jpg(directory)
    else:
        print("Invalid directory path.")
