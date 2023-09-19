import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create the x, y, and z coordinate arrays
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
x, y = np.meshgrid(x, y)

fig = plt.figure(figsize=(12,6))

# First subplot
z1 = (
    155 + 50 * np.sin(x * 2 * np.pi) * np.sin(y * 2 * np.pi)
    # + 50 * np.sin(5 * x * 2 * np.pi) * np.sin(5 * y * 2 * np.pi)
)
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(x, y, z1, cmap='gray')
fig.colorbar(surf1, ax=ax1, pad=0.15)
ax1.set_zlim(0, 255)
ax1.view_init(elev=90)

# Second subplot
z2 = (
    155 + 50 * np.sin(x * 2 * np.pi) * np.sin(y * 2 * np.pi)
    + 10 * np.sin(5 * x * 2 * np.pi) * np.sin(5 * y * 2 * np.pi)
)
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(x, y, z2, cmap='gray')
fig.colorbar(surf2, ax=ax2, pad=0.15)
ax2.set_zlim(0, 255)
ax2.view_init(elev=90)

plt.show()
