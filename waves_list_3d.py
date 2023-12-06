import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 12))
fig.suptitle('Figure 10: 2D-DFT Multiplier Matrix Visualized (own work)', fontsize=16)

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
x, y = np.meshgrid(x, y)

for i in range(4):
    for j in range(4):
        ax = fig.add_subplot(4, 4, i * 4 + j + 1, projection='3d')
        z = np.cos(2 * np.pi * i * x / (x.max() - x.min()) + 2 * np.pi * j * y / (y.max() - y.min()))
        ax.plot_surface(x, y, z, cmap='gray')
        ax.set_title(f'u={i}, v={j}', fontsize=15)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])

plt.subplots_adjust(hspace=0.2, wspace=0, left=0.02, right=0.98, top=0.9, bottom=0.02)
figManager = plt.get_current_fig_manager()
figManager.resize(1600, 1800)
plt.savefig('figure_9.png')
plt.show()