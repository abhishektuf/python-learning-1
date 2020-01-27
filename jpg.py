'''
from PIL import Image

img=Image.open('newspaper.jpg')

transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)

transposed_img.save('newspaper2.jpg')
'''
#CLAHE

import cv2

img=cv2.imread('newspaper.jpg')

clahe=cv2.createCLAHE()

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

enha_img=clahe.apply(gray_img)

cv2.imwrite('enhanced.jpg',enha_img)

print("Done")
