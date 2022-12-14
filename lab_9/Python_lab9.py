import cv2
#import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\tombo\AppData\Local\Tesseract-OCR\tesseract'

def GetDataFromImage(filename :str):
    foundItems = []

    img = cv2.imread(filename)

    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    keys = list(d.keys())

    date_pattern = input("Wprowadz szukane slowo")

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 60:
            if re.match(date_pattern, d['text'][i]):
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                foundItems.append(d['text'])

    cv2.imshow('imge', img)
    cv2.waitKey(0)
    return foundItems

data = GetDataFromImage('Lab9_4.jpg')

#img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.imshow(img_convert)
#plt.show()