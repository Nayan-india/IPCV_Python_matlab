import numpy as np
import cv2 as cv

height = 50
width = 1000

img = np.ones([height, width, 3], dtype = np.uint8)
img[:] = 255

markers = np.round(np.linspace(0, 1000, 21))
for i in range(0, len(markers)-1, 2):
    img[:,int(markers[i]):int(markers[i+1])] = 0
    
cv.imshow("Black & White strip", img)
