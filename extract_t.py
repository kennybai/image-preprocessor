import cv2
import numpy as np
import glob

neiborhood8 = np.ones([3,3], np.uint8)

img_in = cv2.imread('001.jpg')
#
img_out = cv2.Laplacian(img_in, -1)
img_out = 255-img_out
#
# kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]],np.float32)
#
# img_out = cv2.filter2D(img_in, -1,kernel)


# img_dilate = cv2.dilate(img_in, neiborhood8, iterations=1)
img_diff = cv2.absdiff(img_in, img_dilate)
img_diff = cv2.absdiff(img_dilate, img_in)
# img_diff_not = cv2.bitwise_not(img_diff)
# img_out = img_diff_not
#
img_out = cv2.cvtColor(img_out, cv2.COLOR_BGR2GRAY)



cv2.imshow('', img_out)
cv2.waitKey()
