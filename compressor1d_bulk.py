import numpy as np
import cv2
from matplotlib import pyplot as plt

# trees, crowd, map, sun, map
name = 'crowd'
n = 1
imgs = [
    cv2.imread(f'figures/{name}/{name}_100.jpeg', cv2.IMREAD_GRAYSCALE),
    cv2.imread(f'figures/{name}/{name}_500.jpeg', cv2.IMREAD_GRAYSCALE),
    cv2.imread(f'figures/{name}/{name}_1000.jpeg', cv2.IMREAD_GRAYSCALE)
]

sizes = [1.0, 0.25, 0.1, 0.05, 0.025]

for size_remaining in sizes:
    for img in imgs:
        dft_rows = np.apply_along_axis(np.fft.fft, 1, img)
        dft_rows[:, int(img.shape[1]*size_remaining):] = 0
        idft_rows = np.apply_along_axis(np.fft.ifft, 1, dft_rows)

        plt.subplot(len(sizes),len(imgs),n)
        plt.imshow(np.abs(idft_rows), cmap = 'gray')
        # plt.title(f'{size_remaining*100}% size of original')
        plt.xticks([])
        plt.yticks([])

        n+=1

fig = plt.gcf()
fig.subplots_adjust(left=0.02, top=0.96, right=0.98, bottom=0.02)
fig.subplots_adjust(wspace=0.05)

figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()

plt.show()