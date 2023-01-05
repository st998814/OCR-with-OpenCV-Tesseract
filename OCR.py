import PIL
from PIL import Image
import pytesseract 
import cv2
import numpy  as np 
import re
from pytesseract import Output
from matplotlib import pyplot as plt

IMG_DIR = 'images/'

#Pre-processing

#Turn gray scale
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#remove noise
def remove_noise(image):
    return cv2.medianBlur(image,5)
#hresholding 
def thresholding(image): 
    return cv2.threshold(image, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# if necessary

#dilate
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
#erode
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)
#####################################################

def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
def canny(image):
    return cv2.Canny(image, 100, 200)
#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 


#Boxing
image = cv2.imread(IMG_DIR + 'PIDPDF.jpeg')
h, w, c = image.shape
boxes = pytesseract.image_to_boxes(image) 
for b in boxes.splitlines():
    b = b.split(' ')
    image = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)


d = pytesseract.image_to_data(image, output_type=Output.DICT) 
date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
n_boxes = len(d['text'])
for i in range(n_boxes):
 if int(d['conf'][i]) > 100:
        if re.match(date_pattern, d['text'][i]):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            
b,g,r = cv2.split(image)
rgb_img = cv2.merge([r,g,b])
plt.figure(figsize=(14,12))
plt.imshow(image)
plt.title('Test')
#plt.show()



gray = get_grayscale(image)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)
images = {'gray': gray, 
          'thresh': thresh, 
          'opening': opening, 
          'canny': canny}
plt.imshow(images['gray'])
plt.show()
fig = plt.figure(figsize=(11,11))


  


#output
custom_config = r' -l chi_tra --oem 3 --psm 6'
print(pytesseract.image_to_string(image, config=custom_config))
