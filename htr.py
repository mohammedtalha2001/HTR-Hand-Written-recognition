import cv2
import numpy as np
import easyocr
<<<<<<< HEAD

reader = easyocr.Reader(['en'],gpu = False) # load once only in memory.

image_file_name='writing.png'
=======
from difflib import SequenceMatcher

reader = easyocr.Reader(['en'],gpu = False) # load once only in memory.

image_file_name='img2.png'
>>>>>>> 1702b70 (Initial commit)
image = cv2.imread(image_file_name)

# sharp the edges or image.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
r_easy_ocr=reader.readtext(thresh,detail=0)


# using list comprehension
listToStr = ' '.join([str(elem) for elem in r_easy_ocr])

print(listToStr)
<<<<<<< HEAD
text_file = open("sample.txt", "w")
text_file.write(listToStr)
text_file.close()
=======

ground_value = "A cup of tea Cat laptop"
ocr_value = listToStr

sm = SequenceMatcher(None, ocr_value, ground_value)
true_positive_char_num = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
  if tag== 'equal':
    true_positive_char_num += (j2 - j1)
  else:
    pass

print(f'accuracy = {true_positive_char_num/len(ground_value)}')


# text_file = open("sample.txt", "w")
# text_file.write(listToStr)
# text_file.close()
















>>>>>>> 1702b70 (Initial commit)
