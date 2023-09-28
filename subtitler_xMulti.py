import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img1 = mpimg.imread('1.png')
img2 = mpimg.imread('2.png')

fig, axs = plt.subplots(2, 1)
fig.suptitle('Figure 11: Equivilence of Trignometric Functions for Integer values of x', fontsize=16, y=0.95, x=0.5)

axs[0].imshow(img1)
axs[0].axis('off')
axs[1].imshow(img2)
axs[1].axis('off')

plt.subplots_adjust(left=0, right=1, top=0.9, bottom=0, wspace=0, hspace=0)

plt.show()