import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, axs = plt.subplots(1, 2)
matrix = np.zeros((10, 10))
idft_matrix = np.fft.ifftn(matrix)

axs[0].imshow(matrix, cmap='viridis')
axs[1].imshow(idft_matrix.real, cmap='viridis')

ax_x = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_y = plt.axes([0.25, 0.15, 0.65, 0.03])

slider_x = Slider(ax_x, 'X', 0, 9, valinit=0, valstep=1)
slider_y = Slider(ax_y, 'Y', 0, 9, valinit=0, valstep=1)

def update(val):
    x = int(slider_x.val)
    y = int(slider_y.val)
    matrix.fill(0)
    matrix[y,x] = 1
    idft_matrix = np.fft.ifftn(matrix)
    axs[0].imshow(matrix, cmap='viridis')
    axs[1].imshow(idft_matrix.real, cmap='viridis')
    fig.canvas.draw_idle()

slider_x.on_changed(update)
slider_y.on_changed(update)

plt.show()
