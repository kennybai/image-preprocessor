import cv2
import numpy as np
import glob

img_in = cv2.imread('001.jpg')
#
img_out = cv2.Laplacian(img_in, -1)
img_out = 255-img_out

# kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]],np.float32)
# img_out = cv2.filter2D(img_in, -1,kernel)

img_out = cv2.cvtColor(img_out, cv2.COLOR_BGR2GRAY)

# cv2.imshow('', img_out)
# cv2.waitKey()

cv2.imwrite('001_laplacian.jpg', img_out)
