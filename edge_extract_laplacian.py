import cv2
import numpy as np
import glob
import os

img_list = glob.glob('./Lpip_nobk/*.jpg')

for img in img_list:

    img_in = cv2.imread(img)

    img_out = cv2.Laplacian(img_in, -1)
    img_out = 255 - img_out

    img_out = cv2.cvtColor(img_out, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('./Lpip_laplacian/' + os.path.split(img)[-1], img_out)

