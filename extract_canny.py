import cv2
import numpy as np
import glob

img = cv2.imread('001.jpg')

img = cv2.Canny(img, 100, 200)

img = 255 - img

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('', img)
# cv2.waitKey()

cv2.imwrite('001_canny.jpg', img)
