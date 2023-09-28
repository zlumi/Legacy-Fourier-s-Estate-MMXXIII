from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

img = Image.open('figures/candle.jpg').convert('L')
data = np.array(img)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(data, cmap='gray')
axs[0].axis('off')
axs[0].set_title('Figure 1a: Candle (Smabs)\nblack/white binarized, down sampled')

ax = fig.add_subplot(122, projection='3d')
axs[1].axis('off')
axs[1].set_title('Figure 1b: 3D histogram by intensity (own work)')
x, y = data.shape

cmap = plt.get_cmap('gray')

for i in range(x):
    for j in range(y):
        ax.bar3d(i, j, 0, 1, 1, data[i][j], color=cmap(data[i][j]))

plt.show()