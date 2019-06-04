import cv2
import math
import PIL.ImageOps
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plot

root = '/_full'

counter = 0
for dirpath, dirnames, filenames in os.walk(root):
    # new_dirpath = dirpath[:1] + '_' + dirpath[1:]
    new_dirpath = dirpath.replace('_full', 'full_512')

    os.makedirs(new_dirpath, exist_ok=False)
    for filename in filenames:

        if os.path.splitext(filename)[-1] != '.png':
            continue

        if counter % 100 == 0:
            print(counter)

        img = Image.open(os.path.join(dirpath, filename))
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize((512, 512), PIL.Image.BICUBIC)
        img.save(os.path.join(new_dirpath, filename), compress_level=9)

        counter += 1

