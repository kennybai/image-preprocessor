import numpy as np
import random
import os
import matplotlib.pyplot as plt
import glob
import shutil

input_path = "./hy6/train/5"

output_path = './hy6/test/5'

if not os.path.isdir(output_path):
    os.makedirs(output_path)

name_list = glob.glob(input_path + "/*")

random_list = random.sample(name_list, 25)

for name in random_list:
    shutil.move(name, output_path)
