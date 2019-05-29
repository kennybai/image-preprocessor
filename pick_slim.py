import numpy as np
import random
import os
import matplotlib.pyplot as plt
import glob
import shutil

root = "/dataset/kana"

for dirpath, dirnames, filenames in os.walk(root):
    counter = 0
    test_path = dirpath.replace('kana', 'kana_slim')
    os.makedirs(test_path, exist_ok=False)
    print(dirpath)
    for filename in filenames:

        if counter == 1000:
            break

        shutil.copy(os.path.join(dirpath, filename), os.path.join(test_path, filename))

        if counter % 100 == 0:
            print(counter)

        counter += 1

