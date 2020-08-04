import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('.jpg', 0)
cv.imwrite('norm_.jpg', img)
plt.hist(img.ravel(),256,[0,256]); plt.show()

img1=cv.pyrDown(img)
cv.imwrite('low_.jpg', img1)
plt.hist(img1.ravel(),256,[0,256]); plt.show()

img2=cv.pyrUp(img)
cv.imwrite('up_.jpg', img2)
plt.hist(img2.ravel(),256,[0,256]); plt.show()
