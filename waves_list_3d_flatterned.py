import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=4, ncols=4, figsize=(12, 12))
fig.suptitle('Figure 12: 2D-DFT Multiplier Matrix Visualized\nTop-Down Flatterned View (own work)', fontsize=16)

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
x, y = np.meshgrid(x, y)

for i in range(4):
    for j in range(4):
        z = np.cos(2 * np.pi * i * x / (x.max() - x.min()) + 2 * np.pi * j * y / (y.max() - y.min()))
        axs[i, j].imshow(z, cmap='gray')
        axs[i, j].set_title(f'u={i}, v={j}', fontsize=10)

plt.subplots_adjust(hspace=0.3, wspace=0)
plt.savefig('figure_12.png')
plt.show()