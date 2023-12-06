import numpy as np
import cv2
from matplotlib import pyplot as plt

name = 'crowd'
img = cv2.imread(f'figures/{name}/{name}_1000.jpeg', cv2.IMREAD_GRAYSCALE)

percentage_remaining = 0.05

dft_cols = np.apply_along_axis(np.fft.fft, 0, img)
dft_cols_2 = dft_cols.copy()
dft_cols[int(img.shape[0]*percentage_remaining/2)+2:-int(img.shape[0]*percentage_remaining/2), :] = 0
idft_cols = np.apply_along_axis(np.fft.ifft, 0, dft_cols)

dft_rows = np.apply_along_axis(np.fft.fft, 1, img)
dft_rows_2 = dft_rows.copy()
dft_rows[:, int(img.shape[1]*percentage_remaining/2)+2:-int(img.shape[1]*percentage_remaining/2)] = 0
idft_rows = np.apply_along_axis(np.fft.ifft, 1, dft_rows)

plt.subplot(121),plt.imshow(np.abs(idft_rows), cmap = 'gray')
plt.title(f'Inverse Transformed Image\n(1D-DFT by row, actual lowest {percentage_remaining*100}% frequencies remaining)')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(np.abs(idft_cols), cmap = 'gray')
plt.title(f'Inverse Transformed Image\n(1D-DFT by column, actual lowest {percentage_remaining*100}% frequencies remaining)')
plt.xticks([]), plt.yticks([])

fig = plt.gcf()
fig.subplots_adjust(left=0.02, top=0.96, right=0.98, bottom=0.02)
fig.subplots_adjust(wspace=0.05)

figManager = plt.get_current_fig_manager()
# figManager.resize(2400, 2000)
for ax in fig.get_axes(): ax.set_frame_on(False)
plt.tight_layout(pad=0.75)
plt.subplots_adjust(left=0, right=1)
# plt.savefig(f'compressor1d.png')

plt.show()