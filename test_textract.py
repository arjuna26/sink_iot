from google.cloud import vision
import io

def detect_text(path):
    """Detects text in the image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    for text in texts:
        print(f'{text.description}')

    return texts


image_path = "IMG_4208.jpg"
detect_text(image_path)

