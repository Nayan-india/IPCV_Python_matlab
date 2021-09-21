from matplotlib import pyplot as plt
import numpy as np

width = 600
height = 600

img = np.zeros([height, width, 3], dtype = np.uint8)

img[  1:400, :, 0] = 255
img[200:600, :, 2] = 255

plt.imshow(img)
plt.show()
