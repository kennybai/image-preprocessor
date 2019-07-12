import cv2
import math
import PIL.ImageOps
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plot


def processing(img):
    for c in range(3):
        img[:, :, c] = img[:, :, c] * img[:, :, 3] + (1 - img[:, :, 3])

    h, w, _ = img.shape
    if h > w:
        exp_len = (h - w) / 2
        el = math.ceil(exp_len)
        er = math.floor(exp_len)
        img = cv2.copyMakeBorder(img, 0, 0, el, er, cv2.BORDER_CONSTANT, value=[1., 1., 1., 0.])
    elif h > w:
        exp_len = (w - h) / 2
        et = math.ceil(exp_len)
        eb = math.floor(exp_len)
        img = cv2.copyMakeBorder(img, et, eb, 0, 0, cv2.BORDER_CONSTANT, value=[1., 1., 1., 0.])

    img *= 255
    img = img.astype(np.uint8)
    return img


root = '/toho'

counter = 0
for dirpath, dirnames, filenames in os.walk(root):
    new_dirpath = dirpath[:1] + '_' + dirpath[1:]
    os.makedirs(new_dirpath, exist_ok=False)
    for filename in filenames:

        if os.path.splitext(filename)[-1] != '.png':
            continue

        if counter % 100 == 0:
            print(counter)

        img = plot.imread(os.path.join(dirpath, filename))
        img = processing(img)
        plot.imsave(os.path.join(new_dirpath, filename), img)
        counter += 1
