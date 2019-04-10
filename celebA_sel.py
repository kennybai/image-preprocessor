import os
import glob
import shutil


sel = 20

path = 'D:/dataset/CelebA_128/'

files = glob.glob(path + '*.jpg')

with open('list_attr_celeba.txt', 'r') as f:
    labels = f.readlines()

for i in labels[2:100]:
    label = i.split()

    if label[sel + 1] == '1':
        dst_path = labels[1].split()[sel]
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        shutil.copy(path + label[0], dst_path)

# for i in labels[1].split():
#     print(str(counter) + i)
#     counter = counter + 1