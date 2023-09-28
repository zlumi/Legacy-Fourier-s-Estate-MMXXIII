from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('figures/candle.jpg').convert('L')
data = np.array(img)

# Create a 1x2 subplot grid. Adjust the size and spacing as needed.
fig, axs = plt.subplots(1, 2, figsize=(10, 5), gridspec_kw={'width_ratios': [1, 4]})

# big title for the figure with padding 10
fig.suptitle('Figure 2: Demonstration of how repetitions of an image leads to periodicity (own work)', fontsize=16, y=0.95, x=0.5)

# Create a 2D bar plot on the left subplot.
x = data.shape[1]
y = data[10]
cmap = plt.get_cmap('gray')
axs[0].bar(range(x), y, color=cmap(y), width=1.0)

# Create a new 2D bar plot on the right subplot.
x2 = x * 5
y2 = np.tile(y, 5)
axs[1].bar(range(x2), y2, color=cmap(y2), width=1.0, alpha=0.75)

axs[1].set_xlim(-5, x2+5)

axs[1].get_yaxis().set_visible(False)
axs[1].get_xaxis().set_visible(False)

axs[1].spines['top'].set_color('white')
axs[1].spines['right'].set_color('white')
axs[1].spines['left'].set_color('white')
axs[1].spines['bottom'].set_color('white')

axs[1].annotate(text='', xy=(-5, 0), xytext=(x2+5, 0), arrowprops=dict(arrowstyle='<->'))

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####

from scipy.interpolate import make_interp_spline
import numpy as np

x_ = np.array(range(x2))

num_points = 1000
spline = make_interp_spline(x_, y2, k=3)
x_smooth = np.linspace(x_.min(), x_.max(), num_points)
y_smooth = spline(x_smooth)
axs[1].plot(x_smooth, y_smooth, color='red')

plt.show()