import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('messi.jpg',1)

img1=cv.pyrUp(img)
img2=cv.pyrUp(img1)

plt.hist(img1.ravel(),256,[0,256]); plt.show()
plt.hist(img2.ravel(),256,[0,256]); plt.show()

cv.imwrite('higher_m.jpg',img2)
