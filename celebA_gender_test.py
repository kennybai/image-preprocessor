import os
import glob
import shutil

num = 1000

path = 'D:/dataset/CelebA_128/'

files = glob.glob(path + '*.jpg')

with open('list_attr_celeba.txt', 'r') as f:
    labels = f.readlines()

for i in labels[10002:10002+num]:
    label = i.split()

    if label[21] == '1':
        dst_path = 'testA'
    else:
        dst_path = 'testB'

    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    shutil.copy(path + label[0], dst_path)

