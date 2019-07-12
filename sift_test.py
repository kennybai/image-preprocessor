import cv2
import numpy as np

img1 = cv2.imread('ABC3.png')
img2 = cv2.imread('ABC2.png')

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGRA2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGRA2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

img1 = cv2.drawKeypoints(img1, kp1, img1, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img2 = cv2.drawKeypoints(img2, kp2, img2, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)



# cv2.imshow('sift_keypoints.jpg', img2)
# cv2.waitKey()



FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# goodMatch = []
# for m, n in matches:
# 	# goodMatch是经过筛选的优质配对，如果2个配对中第一匹配的距离小于第二匹配的距离的1/2，基本可以说明这个第一配对是两幅图像中独特的，不重复的特征点,可以保留。
#     if m.distance < 0.50*n.distance:
#         goodMatch.append(m)
# # 增加一个维度
# goodMatch = np.expand_dims(goodMatch, 1)
# print(goodMatch[:20])

img_out = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches[:10], None, flags=2)

cv2.imwrite('SIFT2.jpg', img_out)
# cv2.waitKey()