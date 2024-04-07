import pytesseract
import re

def time_from_photo(img_obj):
    # Open the image file
    image = Image.open(img_obj)
    # Extract text from the image
    text = pytesseract.image_to_string(image)
    # Look for time pattern (hh:mm)
    time_pattern = re.compile(r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b')
    matches = time_pattern.findall(text)
    return matches

def save_to_sheets():
  pass

def telegram_chat():
  pass

def calculate_hours():
  pass
