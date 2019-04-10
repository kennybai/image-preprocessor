import os

path = "./Omni_wgan-gp_0"

image_list = os.listdir(path)

for name in image_list:

    # temp = name[:]
    temp = name[0:-4]
    temp = temp.split("_")
    name_end = temp.pop(-1).split("of")
    name_end[0] = name_end[0].zfill(4)
    name_end[1] = name_end[1].zfill(4)
    temp.append(name_end[0])
    temp.append(name_end[1])
    temp[1] = temp[1].zfill(4)
    temp[3] = temp[3].zfill(5)

    rename =""
    for n in temp[0:-1]:
        rename = rename + n
        rename = rename + "_"

    rename = rename[0:-1]
    rename = rename + "of"
    rename = rename + temp[-1]
    rename = rename + ".jpg"

    os.rename(path + "/" + name,path + "/" + rename)