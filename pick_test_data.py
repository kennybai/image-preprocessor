import numpy as np
import random
import os
import matplotlib.pyplot as plt
import glob
import shutil

input_path = "./celeba_4st/train/Not_Male_Smiling"

output_path = './celeba_4st/test/Not_Male_Smiling'

if not os.path.isdir(output_path):
    os.makedirs(output_path)

name_list = glob.glob(input_path + "/*")

random_list = random.sample(name_list, len(name_list)//5)

for name in random_list:
    shutil.move(name, output_path)
