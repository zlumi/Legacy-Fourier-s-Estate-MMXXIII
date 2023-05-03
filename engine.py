import matplotlib.pyplot as plt
import numpy as np
import cv2
from luminance import luminance

import dft

image = cv2.imread('resources/test_3.png')
imageData = np.array([
    [luminance(pixel) for pixel in row] for row in image
])

output = np.round(np.fft.irfft2(np.fft.fft2(imageData)), 0)

for x in ["in", "out"]:
    with open("./debug/" + x + ".txt", "w") as f:
        for row in [imageData, output][["in", "out"].index(x)]:
            f.write(str(row) + ",\n")

plt.subplot(1, 2, 1)
plt.imshow(imageData, cmap='gray')

plt.subplot(1, 2, 2)
plt.imshow(output, cmap='gray')

plt.show()