from matplotlib import pyplot as plt
import numpy as np

side = 600;

img = np.zeros([side, side, 3], dtype = np.uint8)

img[1:200, :, 0] = 255
img[201:400, :, 1] = 255
img[401:600, :, 2] = 255

plt.imshow(img)
plt.show()
