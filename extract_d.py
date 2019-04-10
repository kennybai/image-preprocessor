import cv2
import numpy as np
import glob

neiborhood8 = np.ones([3,3], np.uint8)

img = cv2.imread('001.jpg')

img_dilate = cv2.dilate(img, neiborhood8, iterations=1)
img_diff = cv2.absdiff(img, img_dilate)

img_inverse = 255 - img_diff

# ret, img_threshold = cv2.threshold(img_diff, 30, 255, cv2.THRESH_BINARY_INV)
img_out = cv2.cvtColor(img_inverse, cv2.COLOR_BGR2GRAY)


# cv2.imshow('', img_dilate)
# cv2.imshow('', img_out)
# cv2.waitKey()


cv2.imwrite('001_mono.jpg', img_out)
