import cv2
import numpy as np
import glob
import os

img_list = glob.glob('./Lpip_nobk/*.jpg')

neiborhood8 = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]],
                       np.uint8)

for img in img_list:

    img_in = cv2.imread(img)

    img_dilate = cv2.dilate(img_in, neiborhood8, iterations=1)
    img_diff = cv2.absdiff(img_in, img_dilate)
    # img_diff = cv2.absdiff(img_dilate, img_in)
    img_diff_not = cv2.bitwise_not(img_diff)

    img_out = cv2.cvtColor(img_diff_not, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('./Lpip_diff/' + os.path.split(img)[-1], img_out)

