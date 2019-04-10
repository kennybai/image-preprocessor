import cv2
import numpy as np
import glob

img_original = cv2.imread('001.jpg')
img_mono = cv2.imread('001_mono.jpg')

img_out = np.concatenate((img_mono, img_original), axis=1)

cv2.imshow('', img_out)
cv2.waitKey()