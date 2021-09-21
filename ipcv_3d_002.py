from matplotlib import pyplot as plt
import numpy as np

width = 600
height = 600

img = np.zeros([height, width, 3], dtype = np.uint8)

# Red Shades
shades = np.round(np.linspace(0, 255, height))
#shades = np.round(np.linspace(255, 0, height)) for reverse pattern

for i in range(0, height):
    img[i, : , 0] = shades[i]

plt.imshow(img)
plt.show()
