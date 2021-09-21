from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import copy

img = np.array(Image.open('football.jpg'))
[h, w, p] = img.shape

R = copy.deepcopy(img)
R[:, :, 1] = 0
R[:, :, 2] = 0

G = copy.deepcopy(img)
G[:, :, 0] = 0
G[:, :, 2] = 0

B = copy.deepcopy(img)
B[:, :, 0] = 0
B[:, :, 1] = 0

for p in range(8):
    plt.subplot(2, 4, p+1)
    if p == 0: # --B
        plt.title('Blue')
        plt.axis('off')
        plt.imshow(B)
    if p == 1: # _G_
        plt.title('Green')
        plt.axis('off')
        plt.imshow(G)
    if p == 2: # _GB
        plt.title('G+B')
        plt.axis('off')
        plt.imshow(G+B)
    if p == 3: # R__
        plt.title('RED')
        plt.axis('off')
        plt.imshow(R)
    if p == 4: # R_B
        plt.title('R+B')
        plt.axis('off')
        plt.imshow(R+B)
    if p == 5: # RG_
        plt.title('R+G')
        plt.axis('off')
        plt.imshow(R+G)
    if p == 6: # RGB
        plt.title('RGB')
        plt.axis('off')
        plt.imshow(R+G+B)
    if p == 7: # Original
        plt.axis('off')
        plt.title('Original')
        plt.imshow(img)

plt.show()
