# Checkers
from matplotlib import pyplot as plt
import numpy as np

square_side = 800;

img = np.ones([square_side, square_side, 3], dtype = np.uint8)
img[:] = 255

n = 8;
tile_size = square_side / n;
markers = np.round(np.linspace(0, square_side, n+1));

for r in range(0, len(markers)-1):  # r=0:n
    for c in range(0, len(markers)-1):  #c=0:n
        img[int(markers[r]):int(markers[r+1]), int(markers[c]):int(markers[c+1])] = 255 if np.mod(r+c,2) else 0
plt.title(f'Checkers: {n} x {n}')
plt.imshow(img)
plt.savefig('Chess_Board.png')
plt.show()
