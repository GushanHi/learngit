import cv2
import numpy as np

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
img = cv2.imread('d:/python/works/pictures/gun.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([0, 100, 0])
upper = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(img, img, mask=mask)  # 对原图与掩膜进行位运算
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)  # 二值化
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 找出所有轮廓

# 找出最大轮廓
area = []  # 定义一个空列表
for k in range(len(contours)):
    area.append(cv2.contourArea(contours[k]))  # 向列表里添加每一个轮廓的面积
max = np.argmax(np.array(area))  # 找到列表中面积最大的元素
cnt = contours[max]
# cv2.drawContours(img, contours, max, (0, 255, 0), 5)

# # 用矩形识别
# x, y, w, h = cv2.boundingRect(cnt)
# center=(int(x+w/2),int(y+h/2))#计算中心点
# print('长', w, '宽', h,'中心点',center)
# img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)

# 用圆识别
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
print('中心点', center, '半径', radius)
img = cv2.circle(img, center, radius, (0, 255, 0), 5)

leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
print('左极点', leftmost, '右极点', rightmost, '上极点', topmost, '下极点', bottommost)

cv2.imshow('image', img)
k = cv2.waitKey(0)
