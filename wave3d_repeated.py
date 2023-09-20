import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Open the image file
img = Image.open('figures/candle.jpg').convert('L')
img = img.point(lambda x: x/4)

# Convert the image data to a numpy array
img_data = np.asarray(img)

# Repeat the image data 3 times along each axis
new_img_data = np.tile(img_data, (3, 3))

# Create a grid of x, y coordinates that correspond to the new image dimensions
y = np.arange(new_img_data.shape[0])
x = np.arange(new_img_data.shape[1])
x, y = np.meshgrid(x, y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, new_img_data, cmap='gray')

ax.view_init(elev=90, azim=-90)
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
plt.axis('off')

ax.set_zlim(0, 500)

# Show the plot
plt.show()