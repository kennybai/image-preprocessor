import os
import glob
import shutil

# num = 10000
# c = [20, 31]
c = [20, 15]


path = 'C:\dataset\img_align_celeba'

files = glob.glob(path + '*.jpg')

with open('list_attr_celeba.txt', 'r') as f:
    labels = f.readlines()

classes = labels[1].split()

# for i in labels[2:num + 2]:
for i in labels[2:]:
    label = i.split()

    if label[c[0] + 1] == '1':
        dst_path = classes[c[0]]
    else:
        dst_path = 'Not_' + classes[c[0]]

    if label[c[1] + 1] == '1':
        dst_path = dst_path + '_' + classes[c[1]]
    else:
        dst_path = dst_path + '_Not_' + classes[c[1]]

    dst_path = os.path.join('C:\dataset', dst_path)

    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    shutil.copy(os.path.join(path, label[0]), dst_path)
