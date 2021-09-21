from matplotlib import pyplot as plt
import numpy as np

side = 400
mid = side/2

img = np.ones([side, side, 3], dtype = np.uint8)
img[:] = 255

for y in range(0, side):
    for x in range(0, side): 
        if x == y and x <= mid:
            img[y, x:side-x] = 0
            
plt.imshow(img)
plt.show()
