import numpy as np
import cv2
from matplotlib import pyplot as plt

name = 'crowd'
img = cv2.imread(f'figures/{name}/{name}_1000.jpeg', cv2.IMREAD_GRAYSCALE)

N = img.shape[0]
percentage_remaining = 0.05

dft_cols = np.apply_along_axis(np.fft.fft, 0, img)
dft_cols_b = dft_cols.copy()
dft_cols_b[int(N*percentage_remaining):, :] = 0
idft_cols_b = np.apply_along_axis(np.fft.ifft, 0, dft_cols_b)

dft_rows = np.apply_along_axis(np.fft.fft, 1, img)
dft_rows_b = dft_rows.copy()
dft_rows_b[:, int(N*percentage_remaining):] = 0
idft_rows_b = np.apply_along_axis(np.fft.ifft, 1, dft_rows_b)

plt.subplot(321),plt.imshow(img, cmap = 'gray')
plt.title('Input Image (Nielsen)'), plt.xticks([]), plt.yticks([])

plt.subplot(323),plt.imshow(np.log(1 + np.abs(dft_rows)), cmap = 'gray')
plt.title('Figure 4. Transformed Image (DFT, absolute value)'), plt.xticks([]), plt.yticks([])

plt.subplot(324),plt.imshow(np.log(1 + np.abs(dft_cols)), cmap = 'gray')
plt.title('Figure 5. Transformed Image (DFT, absolute value)'), plt.xticks([]), plt.yticks([])

plt.subplot(325),plt.imshow(np.abs(idft_rows_b), cmap = 'gray')
plt.title(f'Figure 6. Inverse Transformed Image\n(1D-DFT by row, lowest {percentage_remaining*100}% frequencies remaining)')
plt.xticks([]), plt.yticks([])

plt.subplot(326),plt.imshow(np.abs(idft_cols_b), cmap = 'gray')
plt.title(f'Figure 7. Inverse Transformed Image\n(1D-DFT by column, lowest {percentage_remaining*100}% frequencies remaining)')
plt.xticks([]), plt.yticks([])

fig = plt.gcf()
fig.subplots_adjust(left=0.02, top=0.96, right=0.98, bottom=0.02)
fig.subplots_adjust(wspace=0.05)

figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()

plt.show()