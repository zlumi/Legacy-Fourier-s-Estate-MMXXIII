import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
img = mpimg.imread('asdf-1.png')

plt.imshow(img)
plt.axis('off')
plt.suptitle('Figure 11 - Compression Pipeline')

plt.subplots_adjust(wspace=0.1, hspace=0.1, top=0.9, bottom=0.1, left=0.1, right=0.9)

plt.show()