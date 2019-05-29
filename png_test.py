import cv2
import PIL.ImageOps
from PIL import Image
import numpy as np
import matplotlib.pyplot as plot
import os
import time
# img = cv2.imread('test2.png', -1)
# # img = cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)
# cv2.imwrite('./out2.png', img)
#
# cv2.imshow('', img)
#
# cv2.waitKey()
#
# img1 = Image.open('test1.png')
# img2 = Image.open('test2.png')
# canvas = Image.new("RGBA", (max(img1.size), max(img1.size)), color='white')
# # canvas.show()
# # com = Image.alpha_composite(canvas,img)
# canvas.paste(img1)
# # img = img.rotate(45)
# # img = img.convert('F')
# # img.thumbnail((128,128))
# canvas.save('canvas.png', compress_level=9)
# img1.save('out1.png', compress_level=9)
# img1.show()
#
# # img2RGB = img2.convert('RGB')
# # img2.paste('white', mask=PIL.ImageOps.invert(img2.getchannel(3)))
# # img2.save('out2.png', compress_level=9)
# # img2.show()
#
# canvas = img2.getchannel(3)
# # canvas = PIL.ImageOps.invert(canvas)
# canvas = canvas.convert('RGBA')
# # canvas.paste(img2)
# canvas = np.array(canvas)
#
# canvas.show()
#
# # pillow 不支持直接用numpy
#
# img2 = Image.open('test2.png')
#
# r, g, b, a = img2.split()
#
# r = np.array(r)
# g = np.array(g)
# b = np.array(b)
# a = np.array(a) / 255
#
# r = r * a
# g = g * a
# b = b * a
# a = a * 255
# r = Image.fromarray(r)
# g = Image.fromarray(g)
# b = Image.fromarray(b)
# a = Image.fromarray(a)
#
# r = r.convert('L')
# g = g.convert('L')
# b = b.convert('L')
# a = a.convert('L')
#
# img2 = Image.merge('RGBA', (r, g, b, a))
#
# img2.show()
# img2.save('out2.png', compress_level=9)
# ---------------------------------------


img2 = cv2.imread('test2.png', -1) / 255
# img2 = cv2.imread('アリス（驚く）.png', -1) / 255

# os.rename('1.png', './temp/2.png')

b, g, r, a = cv2.split(img2)
# b, g, r = b * a, g * a, r * a

img2 = cv2.merge((b, g, r, a)) * 255
img2 = img2.astype(np.uint8)
# img2 = img2.astype('uint8')

# 不能用
# img2.dtype = np.uint8
cv2.imshow('', img2)
cv2.waitKey()
cv2.imwrite('（驚く）.png', img2, [cv2.IMWRITE_PNG_COMPRESSION, 9])

if None:
    print('hello')

# ------------------------------------------------
st = time.time()



img = cv2.imread('test2.png', -1)
cv2.imwrite('cv.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 8])


ct = time.time() - st
print('%.3fs'%ct)

st = time.time()


img = Image.open('test2.png')
img.save('pillow.png', compress_level=8)

ct = time.time() - st
print('%.3fs'%ct)


st = time.time()


img = plot.imread('test2.png')
plot.imsave('matplotlib.png', img)

ct = time.time() - st
print('%.3fs'%ct)
