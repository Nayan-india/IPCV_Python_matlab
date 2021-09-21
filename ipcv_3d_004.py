from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import copy

img = np.array(Image.open('football.jpg'))
[h, w, p] = img.shape

plt.subplot(2,2,1)
plt.title('Original')
plt.axis('off')
plt.imshow(img)

plt.subplot(2,2,2)
img2 = copy.deepcopy(img)
img2[:, :, 1] = 0 #G=0
img2[:, :, 2] = 0 #B=0
plt.title('Red')
plt.axis('off')
plt.imshow(img2)

plt.subplot(2,2,3)
img3 = copy.deepcopy(img)
img3[:, :, 0] = 0 #R=0
img3[:, :, 2] = 0 #B=0
plt.title('Green')
plt.axis('off')
plt.imshow(img3)

plt.subplot(2,2,4)
img4 = copy.deepcopy(img)
img4[:, :, 0] = 0 #R=0
img4[:, :, 1] = 0 #G=0
plt.title('Blue')
plt.axis('off')
plt.imshow(img4)

plt.show()
