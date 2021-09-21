from matplotlib import pyplot as plt
import numpy as np

height = 600
width = 600

img = np.ones([height, width, 3], dtype = np.uint8)
img[:] = 255

n = 12 #n = number of bands
shade = np.linspace(0, 255, n)
markers = np.round(np.linspace(0, height-1, n+1))
for i in range(0, len(markers)-1):
    img[int(markers[i]):int(markers[i+1]), :] = shade[i]
    
plt.title(f'Bands = {n}')
plt.imshow(img)
plt.show()
