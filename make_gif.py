import sys
import imageio
import glob

path = "./Omni_dcgan_0"

image_list = glob.glob(path + "/*.jpg")

frames = []

for image_name in image_list:

    frames.append(imageio.imread(image_name))


# imageio.mimsave("created_gif.gif", frames, 'GIF', loop=1, duration=0.1, )

imageio.mimwrite(path.split("\\")[-1] + ".gif", frames, 'GIF', loop=1, duration=[1, 0.1])
