import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load the image as a grayscale 2D matrix
# img = cv2.imread('figures/tree/tree_1000.jpeg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('figures/sun/sun_1000.jpeg', cv2.IMREAD_GRAYSCALE)

# Save the dimensions of the image
M, N = img.shape

# Compute the 2D discrete Fourier transform of the image
dft = np.fft.fft2(img)

percentage_remaining = 0.01

# use M and N to calculate how many outer rims to remove, and apply the removal to dft
dft[int(M*percentage_remaining):int(M*(1-percentage_remaining)), int(N*percentage_remaining):int(N*(1-percentage_remaining))] = 0

# Compute the inverse Fourier transform of the DFT
idft = np.fft.ifft2(dft)

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

axs[2].imshow(np.abs(idft), cmap = 'gray')
axs[2].set_title('IDFT')
axs[2].set_xticks([])
axs[2].set_yticks([])

plt.show()