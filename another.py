
import pytesseract
from PIL import Image
from difflib import SequenceMatcher

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = Image.open('img2.png')
text = pytesseract.image_to_string(img , lang='eng', config="--user-words words.txt")
print(text)

##Accuracy printer



ground_value = "A Cup of tea \n Cat \n laptop"

ocr_value = text

sm = SequenceMatcher(None, ocr_value, ground_value)
true_positive_char_num = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
  if tag== 'equal':
    true_positive_char_num += (j2 - j1)
  else:
    pass

print(f'accuracy = {true_positive_char_num/len(ground_value)}')

# text_file = open("sample.txt", "w")
# text_file.write(text)
# text_file.close()