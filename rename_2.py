import os
from glob import glob

path = './Mika_pikazo_diff_512'

filename_list = glob(path + '/*.jpg')

for filename in filename_list:
    os.rename(filename, '.' + filename.split('.')[1] + '_diff.jpg')
