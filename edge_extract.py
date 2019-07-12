import cv2
import numpy as np
import glob
import os

filenames = glob.glob('./Mika_pikazo_512/*.jpg')

neiborhood8 = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]],
                       np.uint8)

for filename in filenames:

    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_dilate = cv2.dilate(img, neiborhood8, iterations=1)
    img_diff = cv2.absdiff(img, img_dilate)
    # img_diff = cv2.absdiff(img_dilate, img_in)
    img_diff_not = cv2.bitwise_not(img_diff)

    _, img_out = cv2.threshold(img_diff_not, 0, 255, cv2.THRESH_OTSU)
    # _, img_out = cv2.threshold(img_diff_not, 230, 255, cv2.THRESH_TOZERO)
    # _,img_out = cv2.threshold(img_out, 150, 255, cv2.THRESH_BINARY)



    cv2.imwrite('./Mika_pikazo_512_didi/' + os.path.split(filename)[-1], img_out)

