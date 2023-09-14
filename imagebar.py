from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

img = Image.open('figures/candle.jpg').convert('L')
data = np.array(img)

# Create a 1x2 subplot grid. Adjust the size and spacing as needed.
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Display the image in black and white on the left subplot.
axs[0].imshow(data, cmap='gray')
axs[0].axis('off')  # Hide axes for the left subplot.

# Create a 3D plot on the right subplot.
ax = fig.add_subplot(122, projection='3d')
axs[1].axis('off')
x, y = data.shape

cmap = plt.get_cmap('gray')

for i in range(x):
    for j in range(y):
        ax.bar3d(i, j, 0, 1, 1, data[i][j], color=cmap(data[i][j]))

plt.show()