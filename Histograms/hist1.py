import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('lena.jpg', 1)
cv.imwrite('normm_l.jpg', img)
plt.hist(img.ravel(),256,[0,256]); plt.show()

img1=cv.pyrDown(img)
img1=cv.resize(img,(512,512))
cv.imwrite('loww_l.jpg', img1)
plt.hist(img1.ravel(),256,[0,256]); plt.show()

img2=cv.pyrUp(img)
img2=cv.resize(img2,(512,512))
cv.imwrite('upp_l.jpg', img2)
plt.hist(img2.ravel(),256,[0,256]); plt.show()
