import numpy as np
import cv2
from matplotlib import pyplot as plt

name = 'crowd'
img = cv2.imread(f'figures/{name}/{name}_1000.jpeg', cv2.IMREAD_GRAYSCALE)

percentage_remaining = 0.02

dft_cols = np.apply_along_axis(np.fft.fft, 0, img)
dft_cols_2 = dft_cols.copy()
dft_cols[int(img.shape[0]*percentage_remaining/2)+2:-int(img.shape[0]*percentage_remaining/2), :] = 0
idft_cols = np.apply_along_axis(np.fft.ifft, 0, dft_cols)

dft_rows = np.apply_along_axis(np.fft.fft, 1, img)
dft_rows_2 = dft_rows.copy()
dft_rows[:, int(img.shape[1]*percentage_remaining/2)+2:-int(img.shape[1]*percentage_remaining/2)] = 0
idft_rows = np.apply_along_axis(np.fft.ifft, 1, dft_rows)

plt.subplot(321),plt.imshow(img, cmap = 'gray')
plt.title('Original Image to Compress with DFT (Nielsen)'), plt.xticks([]), plt.yticks([])

plt.subplot(322),plt.title(f'(Figure 6-9 are own work)'), plt.xticks([]), plt.yticks([])

plt.subplot(323),plt.imshow(np.log(1 + np.abs(dft_rows_2)), cmap = 'gray')
plt.title('Figure 6: Transformed Image\n(DFT, absolute value & in logarithmic scale)', fontsize=13), plt.xticks([]), plt.yticks([])
plt.axvline(x=int(img.shape[1]*percentage_remaining/2)+2, color='r')
plt.axvline(x=img.shape[1]-int(img.shape[1]*percentage_remaining/2)-1, color='r')

plt.subplot(324),plt.imshow(np.log(1 + np.abs(dft_cols_2)), cmap = 'gray')
plt.title('Figure 7: Transformed Image\n(DFT, absolute value & in logarithmic scale)', fontsize=13), plt.xticks([]), plt.yticks([])
plt.axhline(y=int(img.shape[0]*percentage_remaining/2)+3, color='r')
plt.axhline(y=img.shape[0]-int(img.shape[0]*percentage_remaining/2)-1, color='r')

plt.subplot(325),plt.imshow(np.abs(idft_rows), cmap = 'gray')
plt.title(f'Figure 8: Inverse Transformed Image\n(1D-DFT by row, actual lowest {percentage_remaining*100}% frequencies remaining)', fontsize=13)
plt.xticks([]), plt.yticks([])

plt.subplot(326),plt.imshow(np.abs(idft_cols), cmap = 'gray')
plt.title(f'Figure 9: Inverse Transformed Image\n(1D-DFT by column, actual lowest {percentage_remaining*100}% frequencies remaining)', fontsize=13)
plt.xticks([]), plt.yticks([])

fig = plt.gcf()
fig.subplots_adjust(left=0.02, top=0.96, right=0.98, bottom=0.02)
fig.subplots_adjust(wspace=0.05)

figManager = plt.get_current_fig_manager()
figManager.resize(2400, 2200)
for ax in fig.get_axes(): ax.set_frame_on(False)
plt.tight_layout(pad=0.75)
plt.subplots_adjust(left=0, right=1)
plt.savefig(f'compressor1d.png')

plt.show()