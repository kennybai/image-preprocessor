import os
import glob
import shutil



path = 'D:/dataset/CelebA_128/'

files = glob.glob(path + '*.jpg')

with open('list_attr_celeba.txt', 'r') as f:
    labels = f.readlines()

for i in labels[2:]:
    label = i.split()

    if label[21] == '1':
        dst_path = 'Male'
    else:
        dst_path = 'Female'

    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    shutil.copy(path + label[0], dst_path)

