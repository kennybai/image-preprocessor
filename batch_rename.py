import cv2
import math
import PIL.ImageOps
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plot

root = '/comocr'

counter = 0
for dirpath, dirnames, filenames in os.walk(root):
    # new_dirpath = dirpath[:1] + '_' + dirpath[1:]
    # new_dirpath = dirpath.replace('full_512', 'full_512_rename')
    # os.makedirs(new_dirpath, exist_ok=False)
    for filename in filenames:

        if os.path.splitext(filename)[-1] != '.jpg':
            continue

        if counter % 100 == 0:
            print(counter)

        os.rename(os.path.join(dirpath, filename), os.path.join('/comocr_re', (str(counter).zfill(4) + '.jpg')))

        counter += 1
