from matplotlib import pyplot as plt
import numpy as np

side = 400
mid = int(side/2)

img = np.ones([side, side, 3], dtype = np.uint8)
img[:] = 255

for y in range(0, side):
    for x in range(0, side): 
        if x == y and x <= mid:
            img[y, x:mid] = 0
        if x+y == side and y <= mid:
            img[y, x:side] = 0
        if x == y and x >= mid:
            img[y, mid:x] = 0
        if x+y == side and x <= mid:
            img[mid:y, x] = 0
img[:, mid] = 0
img[mid, :] = 0

plt.imshow(img)
plt.show()
