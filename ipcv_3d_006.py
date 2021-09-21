import numpy as np
import os
import cv2 as cv

dir = ('C:/users/administrator/documents/matlab_scilab/snaps')
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

img = cv.imread('football.jpg')
[h, w, p] = img.shape

n = 3 # nxn
m = 2

rm = np.round(np.linspace(0, h, n+1))
cm = np.round(np.linspace(0, w, m+1))

for r in range(n):
    for c in range(m):
        SI = img[int(rm[r]):int(rm[r+1]), int(cm[c]):int(cm[c+1]), :]
        file_name = f'C:/users/administrator/documents/matlab_scilab/snaps/img_n_{n}_m_{m}__r__{r}__c_{c}.png'
        cv.imwrite(file_name, SI)
