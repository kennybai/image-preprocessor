import cv2
import numpy as np
import glob
import os

img_original_list = glob.glob('./Lpip_nobk/*.jpg')
img_mono_list = glob.glob('./Lpip_diff/*.jpg')

if len(img_mono_list) != len(img_original_list):
    raise Exception


for i in range(len(img_mono_list)):

    img_original = cv2.imread(img_original_list[i])
    img_mono = cv2.imread(img_mono_list[i])

    img_out = np.concatenate((img_mono, img_original), axis=1)

    cv2.imwrite('./Lpip_diff_512/' + os.path.split(img_mono_list[i])[-1], img_out)