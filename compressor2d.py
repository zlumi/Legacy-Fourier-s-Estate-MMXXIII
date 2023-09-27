import numpy as np
import cv2
from matplotlib import pyplot as plt

name = "crowd"
wide = 1000

img = cv2.imread(f'figures/{name}/{name}_{str(wide)}.jpeg', cv2.IMREAD_GRAYSCALE)
M, N = img.shape

dft1 = np.apply_along_axis(np.fft.fft, 0, np.apply_along_axis(np.fft.fft, 1, img))
dft2 = dft1.copy()
dft1[30:, :] = dft1[:, 30:] = 0
dft2[:, :-30] = dft2[:-30, :] = 0

idft1 = np.apply_along_axis(np.fft.ifft, 0, np.apply_along_axis(np.fft.ifft, 1, dft1))
idft2 = np.apply_along_axis(np.fft.ifft, 0, np.apply_along_axis(np.fft.ifft, 1, dft2))

fig, axs = plt.subplots(2, 3)
fig.subplots_adjust(left=0, top=1, right=1, bottom=0)
fig.subplots_adjust(wspace=0.05)

axs[0][0].imshow(img, cmap = 'gray')
axs[0][0].set_title('Input Image'), axs[0][0].set_xticks([]), axs[0][0].set_yticks([])
axs[0][1].imshow(np.log(1 + np.abs(dft1)), cmap = 'gray')
axs[0][1].set_title('DFT'), axs[0][1].set_xticks([]), axs[0][1].set_yticks([])
axs[0][2].imshow(idft1.real, cmap = 'gray')
axs[0][2].set_title('IDFT'), axs[0][2].set_xticks([]), axs[0][2].set_yticks([])

axs[1][0].imshow(img, cmap = 'gray')
axs[1][0].set_title('Input Image'), axs[1][0].set_xticks([]), axs[1][0].set_yticks([])
axs[1][1].imshow(np.log(1 + np.abs(dft2)), cmap = 'gray')
axs[1][1].set_title('DFT'), axs[1][1].set_xticks([]), axs[1][1].set_yticks([])
axs[1][2].imshow(idft2.real, cmap = 'gray')
axs[1][2].set_title('IDFT'), axs[1][2].set_xticks([]), axs[1][2].set_yticks([])

plt.show()