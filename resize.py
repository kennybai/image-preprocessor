import cv2
import sys
import os.path
from glob import glob


file_list = glob('./Mix_256/*.jpg')

for filename in file_list:
    image = cv2.imread(filename)
    imagec = cv2.resize(image, (512, 256))

    cv2.imwrite(filename[0:-3] + "jpg", imagec)