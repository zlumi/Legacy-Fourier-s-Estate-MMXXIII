from numpy import fft
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

signals = [
    [np.sin(2*np.pi*2*x/12) for x in range(12)],
    [np.cos(2*np.pi*2*x/12) for x in range(12)],
    [np.sin(2*np.pi*2*x/12)+np.cos(2*np.pi*2*x/12) for x in range(12)]
]

fig, axs = plt.subplots(3, 1, figsize=(8, 10))
fig.suptitle('Figure 5: DFTs - Real, Imaginary parts; conjugate symmetry (own work)')

for i, signal in enumerate(signals):
    fft_array = fft.fft(signal)

    axs[i].plot(signal)
    axs[i].plot(fft_array.real)
    axs[i].plot(fft_array.imag)

    axs[i].legend([
        f'Input Signal {["(sin)", "(cos)", "(sin+cos)"][i]} (2 Cycles/12 Units)',
        'DFT of Input Signal (real)',
        'DFT of Input Signal (imaginary)'
    ])

fig.subplots_adjust(top=0.95, bottom=0.05, left=0.05, right=0.95, hspace=0.2,)
plt.savefig('figure5.png')
plt.show()