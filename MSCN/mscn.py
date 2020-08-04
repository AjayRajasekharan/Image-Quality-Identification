import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread("test2.png", 0) # read as gray scale
img = img.astype(np.uint8)
cv2.imshow('win1',img)
cv2.imwrite('pimg1.png',img)

blurred = cv2.GaussianBlur(img, (7, 7), 1.166) # apply gaussian blur to the image
blurred = blurred.astype(np.uint8)
cv2.imshow('win2',blurred)
cv2.imwrite('pimg2.png',blurred)

n = img - blurred
n = n.astype(np.uint8)
cv2.imshow('win3', n)
cv2.imwrite('pimg3.png',n)

blurred_sq = blurred * blurred
blurred_sq = blurred_sq.astype(np.uint8)
# cv2.imshow('win4',blurred_sq)

iss =  img * img
iss = iss.astype(np.uint8)
# cv2.imshow('winnn', iss)

sigma = cv2.GaussianBlur(img * img, (7, 7), 1.166)
sigma = sigma.astype(np.uint8)
# cv2.imshow('win5',sigma)

sigma = (sigma - blurred_sq) ** 0.5
sigma = sigma.astype(np.uint8)
cv2.imshow('win6', sigma)
cv2.imwrite('pimg4.png',sigma)

sigma = sigma + 1.0/255 # to make sure the denominator doesn't give DivideByZero Exception

structdis = (img - blurred)/sigma # final MSCN(i, j) image
structdis = structdis.astype(np.uint8)
cv2.imshow('win7',structdis)

cv2.imwrite('pimg5.png',structdis)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
NOTE:
Due to the different range expectation of the two functions - imwrite and imshow,
imwrite always expects [0,255], whereas imshow expects [0,1] for floating point and [0,255] for unsigned chars.

In order to display the correct output with imshow, 
we need to reduce the range of your floating point image from [0,255] to [0,1]. 
We can do this using convertTo and an appropriate scaling factor (uint8), or simply by dividing your image by 255.
'''
