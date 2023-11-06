# 1d dft compress test.png

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)

fig, axs = plt.subplots(2, 2)
fig.suptitle('Figure 9: 1D-DFT Compression (own work)', fontsize=16)

axs[0,0].imshow(image, cmap='gray')
axs[0,0].set_title('Original Image')

dft_img = np.array([np.fft.fft(row) for row in image])
dft_img[:, 12:] = 0
idft_img = np.array([np.fft.ifft(row) for row in dft_img])
axs[1,0].imshow(idft_img.real, cmap='gray')
axs[1,0].set_title('lowest 10%')

dft_img = np.array([np.fft.fft(row) for row in image])
dft_img[:, 12:-10] = 0
idft_img = np.array([np.fft.ifft(row) for row in dft_img])
axs[1,1].imshow(idft_img.real, cmap='gray')
axs[1,1].set_title('lowest 10% and highest 10%')

dft_img = np.array([np.fft.fft(row) for row in image])
dft_img[:, 1:-10] = 0
idft_img = np.array([np.fft.ifft(row) for row in dft_img])
axs[0,1].imshow(idft_img.real, cmap='gray')
axs[0,1].set_title('highest 10%')

plt.tight_layout()
plt.show()