import numpy as np
import cv2
from matplotlib import pyplot as plt

name = "crowd"
wide = 1000
removed = 0.05

img = cv2.imread(f'figures/{name}/{name}_{str(wide)}.jpeg', cv2.IMREAD_GRAYSCALE)
M, N = img.shape

dft = np.apply_along_axis(np.fft.fft, 0, np.apply_along_axis(np.fft.fft, 1, img))

# dft[:int(M*removed), :int(N*removed)] = dft[int(M*(1-removed)):, :int(N*removed)] = dft[:int(M*removed), int(N*(1-removed)):] = dft[int(M*(1-removed)):, int(N*(1-removed)):] = 0
# dft[int(M*removed):int(M*(1-removed)), :] = dft[:, int(N*removed):int(N*(1-removed))] = 0

# v = 5
# dft[v:, :] = dft[:, v:] = 0
# dft[:M-v, :] = dft[:, :N-v] = 0
# dft[v:, :] = dft[:, :N-v] = 0
# dft[:M-v, :] = dft[:, v:] = 0

# v = 5
# dftc = dft.copy()
# dft[v:M-v, :] = dft[:, v:] = 0
# dftc[v:M-v, :] = dftc[:, :-v] = 0

idft = np.apply_along_axis(np.fft.ifft, 0, np.apply_along_axis(np.fft.ifft, 1, dft))
# idftc = np.apply_along_axis(np.fft.ifft, 0, np.apply_along_axis(np.fft.ifft, 1, dftc))

# Display the original image, DFT, and IDFT side-by-side
fig, axs = plt.subplots(1, 3)
fig.subplots_adjust(left=0, top=1, right=1, bottom=0)
fig.subplots_adjust(wspace=0.05)

axs[0].imshow(img, cmap = 'gray')
axs[0].set_title('Input Image')
axs[0].set_xticks([])
axs[0].set_yticks([])

axs[1].imshow(np.log(1 + np.abs(dft)), cmap = 'gray')
axs[1].set_title('DFT')
axs[1].set_xticks([])
axs[1].set_yticks([])

# axs[1].imshow(idftc.real, cmap = 'gray')
# axs[1].set_title('IDFT')
# axs[1].set_xticks([])
# axs[1].set_yticks([])

axs[2].imshow(idft.real, cmap = 'gray')
axs[2].set_title('IDFT')
axs[2].set_xticks([])
axs[2].set_yticks([])

plt.show()