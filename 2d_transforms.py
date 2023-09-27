import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(f'232.png', cv2.IMREAD_GRAYSCALE)
n = image.shape[0] // 2

dft = np.fft.fft2(image)
idft = np.fft.ifft2(dft).real

magnitude_spectrum_real = np.log1p(np.abs(dft.real))
magnitude_spectrum_imag = np.log1p(np.abs(dft.imag))

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 1].imshow(idft, cmap='gray')
axs[0, 1].set_title('IDFT Image')
axs[1, 0].imshow(magnitude_spectrum_real, cmap='gray')
axs[1, 0].set_title('Magnitude Spectrum (Real)')
axs[1, 1].imshow(magnitude_spectrum_imag, cmap='gray')
axs[1, 1].set_title('Magnitude Spectrum (Imaginary)')

for i in range(2):
    for j in range(2):
        axs[i, j].set_xticks([])
        axs[i, j].set_yticks([])

plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
plt.show()