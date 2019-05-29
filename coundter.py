import cv2
import math
import PIL.ImageOps
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plot

root = '/full'

c0 = 0
c1 = 0
li = []
for dirpath, dirnames, filenames in os.walk(root):
    # print(dirpath)
    # print(dirnames)
    new_dirpath = '.' + dirpath
    os.makedirs(new_dirpath, exist_ok=False)
    for filename in filenames:

        if os.path.splitext(filename)[-1] != '.png':
            c0 += 1
            li.append(os.path.join(dirpath, filename))
        else:
            c1 += 1
print(c0)
print(c1)
