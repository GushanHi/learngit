import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('d:/python/works/pictures/house.jpg', 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)  # 进行频率变换，得到图像中心频率
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))  # 将实部和虚部都转换为实部，乘以20是扩大值，投射到空间域
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)  # 取图片中心点

mask = np.zeros((rows, cols, 2), np.uint8)  # 创建掩膜
mask[crow - 14:crow + 14, ccol - 14:ccol + 14] = 1  # 图中该位置用掩膜覆盖

fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)  # 傅里叶逆变换
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
plt.subplot(121), plt.imshow(img, "gray"), plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, 'gray'), plt.title('Result')
plt.show()
