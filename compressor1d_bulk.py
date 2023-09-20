import numpy as np
import cv2
from matplotlib import pyplot as plt

# trees, crowd, map, map
name = 'map'
n = 1
imgs = [
    cv2.imread(f'figures/{name}/{name}_100.jpeg', cv2.IMREAD_GRAYSCALE),
    cv2.imread(f'figures/{name}/{name}_500.jpeg', cv2.IMREAD_GRAYSCALE),
    cv2.imread(f'figures/{name}/{name}_1000.jpeg', cv2.IMREAD_GRAYSCALE)
]

sizes = [
    1.0,
    0.25,
    0.10,
    0.05,
    0.025
]

for size_remaining in sizes:
    for img in imgs:
        dft_rows = np.apply_along_axis(np.fft.fft, 1, img)
        dft_rows[:, int(img.shape[1]*size_remaining):] = 0
        idft_rows = np.apply_along_axis(np.fft.ifft, 1, dft_rows)

        plt.subplot(len(sizes),len(imgs),n)
        plt.imshow(np.abs(idft_rows), cmap = 'gray')
        
        if not (n+1)%3:
            plt.title(f'{size_remaining*100}')
        plt.xticks([])
        plt.yticks([])

        n+=1

# Add an arrow axis on the left pointing upwards with the label "% size of original"
plt.annotate('', xy=(0.06, 1), xycoords='figure fraction', xytext=(0.06, 0),  arrowprops=dict(arrowstyle="->", color='black'))
plt.annotate('% frequencies retained', xy=(0.05, 1), xycoords='figure fraction', xytext=(0.01, 0.5), rotation=90, va='center')

fig = plt.gcf()
fig.set_size_inches(6, 6.5)
fig.subplots_adjust(left=0.07, top=0.96, right=0.98, bottom=0.02)
fig.subplots_adjust(wspace=0.05)

figManager = plt.get_current_fig_manager()

plt.show()