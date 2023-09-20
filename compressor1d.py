import numpy as np
import cv2
from matplotlib import pyplot as plt

# trees, crowd, map, sun, map
name = 'crowd'
img = cv2.imread(f'figures/{name}/{name}_1000.jpeg', cv2.IMREAD_GRAYSCALE)

N = img.shape[1]

percentage_remaining = 0.1
dft_rows = np.apply_along_axis(np.fft.fft, 1, img)
dft_rows_b = dft_rows.copy()
dft_rows_copy_bnt = dft_rows.copy()

dft_rows_b[:, int(N*percentage_remaining):] = 0
dft_rows_copy_bnt[:, int(N*(percentage_remaining)/2):int(N*(1-(percentage_remaining)/2))] = 0

idft_rows_b = np.apply_along_axis(np.fft.ifft, 1, dft_rows_b)
idft_rows_copy_bnt = np.apply_along_axis(np.fft.ifft, 1, dft_rows_copy_bnt)

plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(np.log(1 + np.abs(dft_rows)), cmap = 'gray')
plt.title('Figure 4. Transformed Image'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(np.abs(idft_rows_b), cmap = 'gray')
plt.title(f'Figure 5. Inverse Transformed Image (lowest {percentage_remaining*100}% frequencies remaining)'), plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.imshow(np.abs(idft_rows_copy_bnt), cmap = 'gray')
plt.title(f'Figure 6. Inverse Transformed Image (low {percentage_remaining*50}% & top {percentage_remaining*50}% frequencies remaining)'), plt.xticks([]), plt.yticks([])

fig = plt.gcf()
fig.subplots_adjust(left=0.02, top=0.96, right=0.98, bottom=0.02)
fig.subplots_adjust(wspace=0.05)

figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()

plt.show()