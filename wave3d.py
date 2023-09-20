import numpy as np
import matplotlib.pyplot as plt
from math import pi
import numpy.fft as fft

periods = 1
samples = 30
x = np.linspace(0, 2*periods*pi, samples)
y = np.linspace(0, 2*periods*pi, samples)
x, y = np.meshgrid(x, y)

z = np.sin(x*2+y*5)
z_transformed = fft.fft2(z)

# plot z_transformed as a 3d surface, ignoring the complex part
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, np.abs(z_transformed), cmap='gray')

plt.show()