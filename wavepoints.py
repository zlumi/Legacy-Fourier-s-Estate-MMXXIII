import numpy as np
import matplotlib.pyplot as plt

def cos_wave(x, freq, length):
    return np.cos(2 * np.pi / length * freq * x)

array_length = 5

fig, axs = plt.subplots(5)
fig.suptitle('Figure 10: 1D-DFT Multiplier Matrix Visualized (own work)', fontsize=16)


for k in range(5):
    n = np.arange(array_length)
    heights = cos_wave(n, k, array_length)

    n_detailed = np.arange(0, array_length, 0.1)
    heights_detailed = cos_wave(n_detailed, k, array_length)

    axs[k].plot(n_detailed, heights_detailed, color='blue', label='Line')
    axs[k].scatter(n, heights, color='red', label='Dots')

    axs[k].set_title(f'{k} periods/(array length) = {k} periods/N')
    # axs[k-1].legend()

plt.tight_layout()
plt.show()
