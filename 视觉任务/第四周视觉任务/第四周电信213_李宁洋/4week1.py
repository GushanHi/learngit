import cv2
import numpy as np

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
img = cv2.imread('d:/python/works/pictures/label.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转化为灰度图
# ret,binary = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 20)#二值化

cv2.imshow('image',binary)
cv2.waitKey(0)
