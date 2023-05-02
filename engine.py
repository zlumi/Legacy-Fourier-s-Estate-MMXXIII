from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import cv2
from time import time

image = cv2.imread('resources/test.png')
imageData = np.array(image)

def luminance(pixel, option=1, intify=True):

    # https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color

    if intify:
        if option == 1:
            return int(0.2126*pixel[0] + 0.7152*pixel[1] + 0.0722*pixel[2])
        elif option == 2:
            return int(0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2])
        elif option == 3:
            return int(sqrt(0.241*pixel[0]**2 + 0.691*pixel[1]**2 + 0.068*pixel[2]**2))
    else:
        if option == 1:
            return 0.2126*pixel[0] + 0.7152*pixel[1] + 0.0722*pixel[2]
        elif option == 2:
            return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]
        elif option == 3:
            return sqrt(0.241*pixel[0]**2 + 0.691*pixel[1]**2 + 0.068*pixel[2]**2)

start = time()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.autoscale(enable=True, axis='both', tight=True)
ax.set_facecolor('lightblue')

for x in range(imageData.shape[0]):
    for y in range(imageData.shape[1]):
        grayness = luminance(imageData[x][y], option=1, intify=True)
        ax.bar3d(x, y, 0, 1, 1, 255-grayness, shade=False, color=str(grayness/255))

print("process completed in: " + str(time() - start) + "seconds")

while True:
    plt.show()