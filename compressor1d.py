import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load the image as a grayscale 2D matrix
# img = cv2.imread('figures/tree/tree_1000.jpeg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('figures/sun/sun_1000.jpeg', cv2.IMREAD_GRAYSCALE)

# Save the width of the image
N = img.shape[1]

# Compute the 1D discrete Fourier transform of each row of the image
dft_rows = np.apply_along_axis(np.fft.fft, 1, img)

percentage_remaining = 0.1
dft_rows[:, int(N*percentage_remaining):int(N*(1-percentage_remaining))] = 0

# Compute the inverse Fourier transform of the DFT rows
idft_rows = np.apply_along_axis(np.fft.ifft, 1, dft_rows)

# Display the original image, DFT rows, and IDFT rows side-by-side
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(np.log(1 + np.abs(dft_rows)), cmap = 'gray')
plt.title('DFT Rows'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(np.abs(idft_rows), cmap = 'gray')
plt.title('IDFT Rows'), plt.xticks([]), plt.yticks([])

fig = plt.gcf()
fig.subplots_adjust(left=0, top=1, right=1, bottom=0)
fig.subplots_adjust(wspace=0.05)
plt.show()