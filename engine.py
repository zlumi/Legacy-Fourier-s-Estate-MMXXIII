import matplotlib.pyplot as plt
import cv2
import numpy as np
from luminance import to_grayscale
from time import time
import dft

def transform_byRow(image, percentage_freqLim):
    frequency_limit = int(len(image[0]) * (percentage_freqLim/100))
    transformed_image = []
    for i, row in enumerate(image):
        transformed_image.append(dft.fourier_transform(row)[:frequency_limit] + [0]*(len(row)-frequency_limit))
        print(f"[{i}/{len(image)}]", end='\r')
    return transformed_image

def invTransform_byRow(image):
    inverse_transformed_image = []
    for i, row in enumerate(image):
        inverse_transformed_image.append(dft.inverse_fourier_transform(row))
        print(f"[{i}/{len(image)}]", end='\r')
    return inverse_transformed_image

image = to_grayscale(cv2.imread('resources/test_5.png'))

print("Test began with image of shape", image.shape)

plt.subplot(2, 5, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')

tests = [100, 75, 50, 25, 10, 8, 6, 4, 2]

for p in tests:
    t = time();     rTrnsfrmed = transform_byRow(image, p);          print(f"[R] Transformed in {time()-t} seconds")
    t = time();     i_rTrnsfrmed = np.abs(invTransform_byRow(rTrnsfrmed));  print(f"[R] Inverse transformed in {time()-t} seconds")

    plt.subplot(2, 5, tests.index(p)+2)
    plt.imshow(i_rTrnsfrmed, cmap='gray')
    plt.title(f'{p}%')

plt.show()