import numpy as np
import random
import os
import matplotlib.pyplot as plt
import glob
import shutil

root = "/dataset/iks_slim_en_o/train"

counter = 0
for dirpath, dirnames, filenames in os.walk(root):
    test_path = dirpath.replace('train', 'test')
    os.makedirs(test_path, exist_ok=False)
    print(dirpath)
    for filename in filenames:
        if counter % 5 == 0:
            # shutil.copy(os.path.join(dirpath, filename), os.path.join(test_path, filename))
            shutil.move(os.path.join(dirpath, filename), os.path.join(test_path, filename))

        if counter % 100 == 0:
            print(counter)

        counter += 1

