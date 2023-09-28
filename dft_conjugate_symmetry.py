from numpy import fft
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

dft_signal = [0]*12
dft_signal[2] = 6
idft_signal_real = fft.ifft(dft_signal).real
idft_signal_imag = fft.ifft(dft_signal).imag
dft_idft_real = fft.fft(idft_signal_real)

plt.figure(figsize=(10, 7))
plt.plot(dft_signal, label='DFT Signal')
plt.plot(idft_signal_real, label='IDFT Signal (Real)')
plt.plot(dft_idft_real.real, label='DFT of IDFT Signal')

plt.title('Figure 14: Conjugate Symmetry of DFT')
plt.legend()
plt.show()