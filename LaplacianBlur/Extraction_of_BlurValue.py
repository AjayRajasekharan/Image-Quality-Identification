# import the necessary packages
from PIL import Image
import os
from imutils import paths
import argparse
import cv2
from pathlib import Path
import numpy as np
import sys


def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

def get_image_dimensions(imagePath):

    # Inline import for PIL because it is not a common library
    with Image.open(imagePath) as img:
        # Calculate the width and hight of an image
        width, height = img.size
    # calculat ethe size in bytes
    size_bytes = os.path.getsize(imagePath)
    a =  str(height) + ", " + str(width) + ", " + str((size_bytes)/1000)
    return a
    # return dict(width=width, height=height, size_bytes=size_bytes)

# construct the argument parse and parse the arguments

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--images", required=True,
#                 help="path to input directory of images")
# # ap.add_argument("-t", "--threshold", type=float, default=100.0,
# #              -  help="focus measures that fall below this value will be considered 'blurry'")
# args = vars(ap.parse_args())

# loop over the input images

# for imagePath in paths.list_images(args["images"]):
#     print(imagePath)

for i in range(0,4290):

    path = r'C:\Users\training.CSSCORP\Desktop\Video\Vid1\1080\frame'+str(i)+'.png'
    print(path)

    image = cv2.imread(path)
    # image = cv2.resize(image, (1600, 1600))
    # image = cv2.GaussianBlur(image, (3, 3), 0)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(image)
    info = get_image_dimensions(path)
    # text = imagePath + " - " + str(fm)
    # print(imagePath + " -  Blurriness:" + str(fm) + " - " + info)



    f = open(r'C:\Users\training.CSSCORP\Desktop\Notes\Week 4\14.06.19\miniproj\blur_1080_v1.csv','a')
    f.write("  \n" + path + ", " + info + ", " + str(format(fm,'.2f')))
    f.close()
