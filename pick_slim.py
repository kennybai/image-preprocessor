import numpy as np
import random
import os
import matplotlib.pyplot as plt
import glob
import shutil

root = "F:\\/datasets/iks"

for dirpath, dirnames, filenames in os.walk(root):
    counter = 0
    test_path = dirpath.replace('iks', 'iks_slim')
    os.makedirs(test_path, exist_ok=False)
    print(dirpath)
    for filename in filenames:

        if counter == 500:
            print(counter)
            break

        if not os.path.exists(os.path.join(dirpath, filename)):
            print(counter)
            break

        shutil.copy(os.path.join(dirpath, filename), os.path.join(test_path, filename))

        if counter % 100 == 0:
            print(counter)

        counter += 1

