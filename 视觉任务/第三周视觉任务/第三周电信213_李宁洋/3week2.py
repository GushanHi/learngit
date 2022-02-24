import cv2
import numpy as np

img = cv2.imread('red block.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([156, 43, 46])  # 红色阈值下限
upper_red = np.array([180, 255, 255])  # 红色阈值上限
mask = cv2.inRange(hsv, lower_red, upper_red)  # 根据阈值构建掩模（低于和高于上限的图像值为0,在阈值之间变为255）
res = cv2.bitwise_and(img, img, mask=mask)  # 对原图与掩膜进行位运算
rows, cols = mask.shape  # 将图片的分辨率赋值
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 71, 0.5)  # rows/2,cols/2找到图片中心,逆时针旋转71°,缩放0.5
dst = cv2.warpAffine(res, M, (cols, rows))  # 仿射变换

cv2.imshow('image', dst)
cv2.waitKey(0)
