import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("d:/python/works/pictures/girl.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(gray)#直方图均衡化
cv2.imshow('image1',equ)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])#计算直方图
plt.imshow(hist)#绘制直方图
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()