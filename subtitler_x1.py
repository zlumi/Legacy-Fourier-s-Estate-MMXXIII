import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
img = mpimg.imread('/Users/h.zhong@aics.espritscholen.nl/Downloads/aaa.png')

plt.imshow(img)
plt.axis('off')
plt.suptitle('(Figure 14-15 are own work)')

plt.subplots_adjust(wspace=0.1, hspace=0.1, top=0.9, bottom=0.1, left=0.1, right=0.9)

plt.show()