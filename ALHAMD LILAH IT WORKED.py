import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

dft_seq1 = np.zeros((10, 10), dtype=np.complex64)
dft_seq1[1][0] = 1
idft_seq1 = fft.ifft2(dft_seq1)

dft_seq2 = np.zeros((10, 10), dtype=np.complex64)
dft_seq2[-2][-1] = 1
idft_seq2 = fft.ifft2(dft_seq2)

fig = plt.figure()

fig.add_subplot(221).imshow(dft_seq1.real, cmap='gray')
fig.add_subplot(222).imshow(idft_seq1.real, cmap='gray')
fig.add_subplot(223).imshow(dft_seq2.real, cmap='gray')
fig.add_subplot(224).imshow(idft_seq2.real, cmap='gray')

plt.show()