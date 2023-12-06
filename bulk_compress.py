import cv2
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
from math import pi, sqrt

for name in ['crowd']:
    for res in [1000, 500, 100]:
        img = cv2.imread(f'figures/{name}/{name}_{res}.jpeg', cv2.IMREAD_GRAYSCALE)

        M, N = img.shape

        ny, nx = 3, 4
        fig, axs = plt.subplots(ny,nx)

        for I, new_size in enumerate([
            1.00,0.75,0.50,0.40,
            0.30,0.20,0.10,0.05,
            0.04,0.03,0.02,0.01
        ]):
            DFT_matrix = fftpack.fft2(img)
            F_shifted = fftpack.fftshift(DFT_matrix)

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

            axscoord = (I//nx, I%nx)
            print(I, nx, axscoord)
            axs[axscoord].imshow(img_restored, cmap='gray')
            axs[axscoord].set_title(f'{c/(M*N)*100:.2f}%')
            axs[axscoord].axis('off')

        plt.tight_layout()
        plt.subplots_adjust(left=0, right=1, top=0.95, bottom=0, wspace=0.01)
        # plt.get_current_fig_manager().full_screen_toggle()
        plt.suptitle(f'image of {name}, sized at {img.shape[1]}px x {img.shape[0]}px')
        # plt.savefig(f'out/{name}_{res}.png'

        plt.show()

# import subprocess
# import os

# for file in os.listdir('out'):
#     FileName = os.path.join('out', file)
#     subprocess.call(['open', FileName])