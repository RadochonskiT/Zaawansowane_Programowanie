import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\tombo\AppData\Local\Tesseract-OCR\tesseract'

def GetPossibleCaptchas(filename :str):
    captchas = []

    #load image to preprocess
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    #PreprocessingImagesList creating
    converted_img = []
    converted_img.append(cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
    converted_img.append(cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
    converted_img.append(cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
    converted_img.append(cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2))
    converted_img.append(cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2))
    converted_img.append(cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2))

    for im in converted_img:
        text = pytesseract.image_to_string(im)
        captchas.append(text)
    
    return captchas

captchas_list = GetPossibleCaptchas('captcha.png')
print(captchas_list)