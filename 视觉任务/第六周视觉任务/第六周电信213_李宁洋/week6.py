import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('d:/python/works/pictures/checkerboard .png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
m, m1 = 0, 0

# 白子操作
template = cv2.imread('white.png', 0)
w, h = template.shape[:]  # 读取模板像素
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)  # 模板匹配
threshold = 0.6
loc = np.where(res >= threshold)

# 黑子操作
template1 = cv2.imread('black.png', 0)
w1, h1 = template1.shape[:]
res1 = cv2.matchTemplate(img_gray, template1, cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc1 = np.where(res1 >= threshold)

# 寻找最远距离的同色棋子
for pt1 in zip(*loc[::-1]):
    for pt2 in zip(*loc[::-1]):
        float(m)
        a = ((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) ** 1 / 2  # 计算各与模板匹配的对象之间的距离
        if a > m:  # 寻找最大值
            m = a
            pt1m = (pt1[0] + int(w / 2), pt1[1] + int(h / 2))
            pt2m = (pt2[0] + int(w / 2), pt2[1] + int(h / 2))

for pt3 in zip(*loc1[::-1]):
    for pt4 in zip(*loc1[::-1]):
        float(m1)
        a = ((pt3[0] - pt4[0]) ** 2 + (pt3[1] - pt4[1]) ** 2) ** 1 / 2
        if a > m1:
            m1 = a
            pt3m = (pt3[0] + int(w / 2), pt3[1] + int(h / 2))
            pt4m = (pt4[0] + int(w / 2), pt4[1] + int(h / 2))

cv2.line(img_rgb, pt1m, pt2m, (0, 0, 255), 2)  # 连线
cv2.line(img_rgb, pt3m, pt4m, (255, 0, 0), 2)

edges = cv2.Canny(img_gray, 50, 150, 3)  # 对图像进行边缘检测
# cv2.imshow("edges", edges)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)  # 霍夫变换检测直线
for line in lines:  # 找出直线位置并画线
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv2.line(img_rgb, (x1, y1), (x2, y2), (0, 255, 255), 2)

cv2.imshow('image', img_rgb)
cv2.waitKey(0)
