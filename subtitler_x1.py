import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
img = mpimg.imread('1.png')

plt.figure()
plt.imshow(img)
plt.axis('off')
plt.suptitle('')

plt.show()