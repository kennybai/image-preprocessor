from glob import glob
import cv2
import numpy as np
filename = "in2.jpg"


img = cv2.imread(filename)
size = min(img.shape[0], img.shape[1])
bias = abs(img.shape[0] - img.shape[1]) // 2

if img.shape[0] > img.shape[1]:
    img = img[0 + bias: size + bias][0:size][:]
else:
    img = cv2.transpose(img)
    img = img[0 + bias: size + bias][0:size][:]
    img = cv2.transpose(img)

    img = cv2.resize(img,(128,128))


cv2.imwrite("./fdfd/" + filename[0:-4] + "_re" + ".jpg", img)