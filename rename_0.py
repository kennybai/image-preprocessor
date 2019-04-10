import os
from glob import glob

path = './LpipX'

filename_list = glob(path + '/*.jpg')+glob(path + '/*.png')

renum=0

for filename in filename_list:
    renum+=1
    os.rename(filename, path + '/Lpip_' + str(renum).zfill(3) + filename[filename.rfind('.'):])
