import pytesseract
from PIL import Image

def recognize_handwriting(image_path):
    """Extracts handwritten text from an image using OCR."""
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    result = recognize_handwriting("handwriting_sample.jpg")
    print("Recognized Text:\n", result)
