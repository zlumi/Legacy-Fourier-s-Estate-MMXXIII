import matplotlib.pyplot as plt
import numpy as np
import cv2
from luminance import luminance

import dft

image = cv2.imread('resources/test_2.png')
imageData = np.array([
    [luminance(pixel) for pixel in row] for row in image
])

output = np.round(np.abs(np.fft.irfft2(np.fft.fft2(imageData))), 0)
output = np.array([[row[i] for i in range(len(row)) if i % 2 == 0] for row in output])
# output = np.array([[row[i] for i in range(len(row)) if i % 2 != 0] for row in output])

# for x in ["in", "out"]:
#     with open("./debug/" + x + ".csv", "w") as f:
#         for row in [imageData, output][["in", "out"].index(x)]:
#             f.write(",".join([str(x) for x in row]) + "\n")

cv2.imwrite("./debug/out.png", output)

plt.show()