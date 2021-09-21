from matplotlib import pyplot as plt
import numpy as np

height = 1000
width = 600

img = np.ones([height, width, 3], dtype = np.uint8)
img[:] = 255

shade = np.linspace(0, 255, height)
for i in range(0, height-1):
    img[i:i+1, :] = shade[i]
    
plt.title('Bands or vertical gradient')
plt.imshow(img)
plt.show()
