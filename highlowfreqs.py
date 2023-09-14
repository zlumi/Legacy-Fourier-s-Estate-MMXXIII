import numpy as np
import matplotlib.pyplot as plt
import random

x = [random.choice([0,50,60,100,255]) for i in range(100)]
X = np.fft.fft(x)

X1 = X.copy()
X1[:-25] = 0
x_reconstructed1 = np.fft.ifft(X1)

X2 = X.copy()
X2[25:] = 0
x_reconstructed2 = np.fft.ifft(X2)

fig, axs = plt.subplots(3, 1)

axs[0].imshow(np.tile(x, (10, 1)), cmap='gray', aspect='auto', vmin=0, vmax=255)
axs[0].set_title('Original Signal')

axs[1].imshow(np.tile(x_reconstructed1.real, (10, 1)), cmap='gray', aspect='auto', vmin=0, vmax=255)
axs[1].set_title('Reconstructed Signal with High Frequencies Removed')

axs[2].imshow(np.tile(x_reconstructed2.real, (10, 1)), cmap='gray', aspect='auto', vmin=0, vmax=255)
axs[2].set_title('Reconstructed Signal with Low Frequencies Removed')

plt.tight_layout()

fig2, ax2 = plt.subplots()
bars = ax2.bar(range(len(x)), x, width=1.0)
bars2 = ax2.bar(range(len(X)), abs(X), alpha=0.25, width=1.0)

ax2.set_title('Original Signal and its Fourier Transform')
ax2.legend(
    (bars[0], bars2[0]),
    ('Original Signal', 'Fourier Transform (absolute value)')
)

plt.show()