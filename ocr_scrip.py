import pytesseract
import os
import sys
from PIL import Image
from docx import Document

if len(sys.argv) != 3:
    print("Usage python ocr.py: <path_to_image/s> <play_name>")
    sys.exit(1)

dir_path = rf'{sys.argv[1]}'
play_name = sys.argv[2]
text = ''

# Set the path to the Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = (
        r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
)

# Specify the image file path
for image in os.listdir(dir_path):
    if image.endswith('jpg') or image.endswith('jpeg'):
        image_path = dir_path + '\\' + image
        text += pytesseract.image_to_string(Image.open(image_path))

doc = Document()
# Add the text to the document
doc.add_paragraph(text)
# Save the document
doc.save(f"{play_name}.docx")
