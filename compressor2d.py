import cv2
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
from math import pi, sqrt

name = "crowd"
res = 1000
img = cv2.imread(f'figures/{name}/{name}_{res}.jpeg', cv2.IMREAD_GRAYSCALE)
new_size = 0.05

M, N = img.shape

fig, axs = plt.subplots(2, 2)

DFT_matrix = fftpack.fft2(img)
axs[0, 0].imshow(np.log(np.abs(DFT_matrix)), cmap='gray')
axs[0, 0].set_title('2D DFT (logarithmic scale, absolute value)')

F_shifted = fftpack.fftshift(DFT_matrix)
axs[0, 1].imshow(np.log(np.abs(F_shifted)), cmap='gray')
axs[0, 1].set_title('2D DFT shifted')

r = sqrt(M*N*new_size/pi)
c = 0
mask = np.zeros((M, N))
for i in range(M):
    for j in range(N):
        if (i-M/2)**2 + (j-N/2)**2 < r**2:
            mask[i, j] = 1
            c += 1

axs[1, 0].imshow(mask, cmap='gray')
axs[1, 0].set_title(f'Mask, covers {c/(M*N)*100:.2f}% of the image')

F_compressed = F_shifted * mask
axs[1, 1].imshow(np.log(np.abs(F_compressed)), cmap='gray')
axs[1, 1].set_title('Compressed 2D DFT')

fig2 = plt.figure()
a2 = fig2.add_subplot(111)
a2.imshow(img, cmap='gray')
a2.set_title('Input image')
a2.axis('off')
# fig2.savefig('input.png')

fig3 = plt.figure()
F_restored = fftpack.ifftshift(F_compressed)
img_restored = fftpack.ifft2(F_restored).real
a3 = fig3.add_subplot(111)
a3.imshow(img_restored, cmap='gray')
a3.set_title('Output')
a3.axis('off')
# fig3.savefig('output.png')

plt.subplots_adjust(left=0.05, right=0.99, top=1, bottom=0.05, wspace=0.1, hspace=0)

plt.show()