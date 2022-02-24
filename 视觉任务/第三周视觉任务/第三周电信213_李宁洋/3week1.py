import cv2
import numpy as np

cv2.namedWindow('image')
img1 = cv2.imread('football.png')
img2 = cv2.imread('img.png')
resize = cv2.resize(img2, (750, 467))#将第二张图与第一张图的大小变为一样


def nothing(x):#回调函数
    pass


cv2.createTrackbar('weight', 'image', 0, 100, nothing)#创建滑动条


ball = img1[390:460, 460:535]#选取足球区域
football = ball.copy()#复制足球图像
img1[385:465, 455:540] = [0, 0, 255]#将比足球略大的一块矩形区域变为红色
img1[390:460, 460:535] = football#将该区域用足球图像覆盖,因红色矩形区域大于足球图像,会出现红框效果

def blend(img1, resize):#混合过渡函数
    w2= cv2.getTrackbarPos('weight', 'image') / 100
    w1 = 1 - w2
    return cv2.addWeighted(img1, w1, resize, w2, 0)


while 1:
    cv2.imshow('image', blend(img1, resize))
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
