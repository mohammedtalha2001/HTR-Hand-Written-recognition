
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = Image.open('writing.png')
text = pytesseract.image_to_string(img)
print(text)

# text_file = open("sample.txt", "w")
# text_file.write(text)
# text_file.close()