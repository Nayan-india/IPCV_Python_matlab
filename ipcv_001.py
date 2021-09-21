import numpy as np
import cv2 as cv
img = np.ones([500, 700, 3], dtype = np.uint8)
img[:] = 255
img[200:300] = 0
img[:,300:400] = 0
cv.imshow("Black Plus", img)
