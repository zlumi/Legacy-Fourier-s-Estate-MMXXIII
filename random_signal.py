import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft

arr = np.random.choice([0,25,50,200,255], 50)
to_remove = 0.75

fig, axs = plt.subplots(3,1)
fig.suptitle('Figure 3: results of low/high frequencies\nfiltering after DFT (Own work)', fontsize=16)

axs[0].imshow(arr.reshape(1,-1), cmap='gray', aspect='auto')
axs[0].set_title('Randomly Generated Signal\n(pixel intensities out of [0,25,50,200,255])'), axs[0].axis('off')

axs[1].imshow(
    ifft(np.concatenate((
        np.array([0]*int(to_remove*len(arr))),
        fft(arr)[-int(to_remove*len(arr)):]
    ))).real.reshape(1,-1),
    cmap='gray',
    aspect='auto',
    vmin=0,
    vmax=255
)
axs[1].set_title(f'IDFT with Lowest {str(to_remove*100)}% Frequencies Removed'), axs[1].axis('off')

axs[2].imshow(
    ifft(np.concatenate((
        fft(arr)[:-int(to_remove*len(arr))],
        np.array([0]*int(to_remove*len(arr)))
    ))).real.reshape(1,-1),
    cmap='gray',
    aspect='auto',
    vmin=0,
    vmax=255
)
axs[2].set_title(f'IDFT with Highest {str(to_remove*100)}% Frequencies Removed'), axs[2].axis('off')

plt.subplots_adjust(hspace=0.75, top=0.75)
plt.show()