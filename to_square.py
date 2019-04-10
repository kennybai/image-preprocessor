from glob import glob
import cv2

file_list = glob('./cat_dog_256/*.jpg') + glob('./cat_dog_256/*.gif')
# print(file_list)
for filename in file_list:
    # print(filename)

    img = cv2.imread(filename)

    if img is None:
        print('error!!')
        print(filename)
        continue

    size = min(img.shape[0], img.shape[1])
    bias = abs(img.shape[0] - img.shape[1]) // 2

    if img.shape[0] > img.shape[1]:
        img = img[0 + bias: size + bias][0:size][:]
    else:
        img = cv2.transpose(img)
        img = img[0 + bias: size + bias][0:size][:]
        img = cv2.transpose(img)

    img = cv2.resize(img, (256, 256))

    cv2.imwrite(filename[0:-3] + 'jpg', img)
    # cv2.imwrite(filename[0:-4] + "_re" + ".jpg", img)
