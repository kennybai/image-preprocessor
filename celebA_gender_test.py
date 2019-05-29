import os
import glob
import shutil

# num = 1000
c = 20 #20 male, 15 eyeglasses, 31 smiling

path = 'C:\dataset\img_align_celeba'

files = glob.glob(path + '/*.jpg')

with open('list_attr_celeba.txt', 'r') as f:
    labels = f.readlines()

classes = labels[1].split()

for i in labels[2:]:
    label = i.split()

    if label[c+1] == '1':
        dst_path = classes[c]
    else:
        dst_path = 'Not_' + classes[c]

    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    shutil.copy(os.path.join(path,label[0]), dst_path)

