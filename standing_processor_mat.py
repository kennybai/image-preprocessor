import matplotlib.pyplot as plot
import math
import PIL.ImageOps
from PIL import Image
import numpy as np

img = plot.imread('test1.png', -1) / 255

# 透明通道作为mask把背景变为白色
for c in range(3):
    img[:, :, c] = img[:, :, c] * img[:, :, 3] + (1 - img[:, :, 3])


# h, w, _ = img.shape
# if h > w:
#     exp_len = (h - w) / 2
#     el = math.ceil(exp_len)
#     er = math.floor(exp_len)
#     img = cv2.copyMakeBorder(img, 0, 0, el, er, cv2.BORDER_REPLICATE)
# elif h > w:
#     exp_len = (w - h) / 2
#     et = math.ceil(exp_len)
#     eb = math.floor(exp_len)
#     img = cv2.copyMakeBorder(img, et, eb, 0, 0, cv2.BORDER_REPLICATE)


img *= 255
img = img.astype(np.uint8)
plot.imshow(img)
plot.imsave('out2.png', img)
