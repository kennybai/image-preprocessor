import cv2
import numpy as np
import glob
import os

filenames = glob.glob('./Mika_pikazo_512/*.jpg')

for filename in filenames:
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.Laplacian(img, -1)
    img = 255 - img
    # _, img = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO)
    # _,img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    _,img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

    cv2.imwrite('./Mika_pikazo_512_laplacian/' + os.path.split(filename)[-1], img)
