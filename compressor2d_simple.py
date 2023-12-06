import cv2
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
from math import pi, sqrt

for name in ['crowd']:
    for res in [1000, 500, 100]:
        img = cv2.imread(f'figures/{name}/{name}_{res}.jpeg', cv2.IMREAD_GRAYSCALE)

        M, N = img.shape

        DFT_matrix = fftpack.fft2(img)
        F_shifted = fftpack.fftshift(DFT_matrix)

        new_size = 0.05
        r = sqrt(M*N*new_size/pi)
        c = 0
        mask = np.zeros((M, N))
        for i in range(M):
            for j in range(N):
                if (i-M/2)**2 + (j-N/2)**2 < r**2:
                    mask[i, j] = 1
                    c += 1

        F_restored = fftpack.ifftshift(F_shifted*mask)
        img_restored = fftpack.ifft2(F_restored).real

        plt.imshow(img_restored, cmap='gray')
        plt.title(f'{c/(M*N)*100:.2f}%')
        plt.axis('off')

        plt.tight_layout()
        plt.subplots_adjust(left=0, right=1, top=0.95, bottom=0, wspace=0.01)
        plt.suptitle(f'image of {name}, sized at {img.shape[1]}px x {img.shape[0]}px')

        plt.show()