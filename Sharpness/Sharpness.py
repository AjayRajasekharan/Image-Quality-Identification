# import the necessary packages
from PIL import Image
import os
from imutils import paths
import argparse
import cv2
from pathlib import Path
import numpy as np
import sys
from sightengine.client import SightengineClient

def get_image_sharpness2(path):
    im = Image.open(path).convert('L')  # to grayscale
    array = np.asarray(im, dtype=np.int32)

    gy, gx = np.gradient(array)
    gnorm = np.sqrt(gx ** 2 + gy ** 2)
    sharpness = np.average(gnorm)
    return sharpness

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

for i in range(0,4290):

    path = r'C:\Users\training.CSSCORP\Desktop\Video\Vid1\1080\frame'+str(i)+'.png'
    print(path)

    # image = cv2.imread(path)
    # image = cv2.resize(image, (1600, 1600))
    # image = cv2.GaussianBlur(image, (3, 3), 0)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = get_image_sharpness2(path)
    info = get_image_dimensions(path)
    # text = imagePath + " - " + str(fm)
    # print(imagePath + " -  Blurriness:" + str(fm) + " - " + info)

    f = open(r'C:\Users\training.CSSCORP\Desktop\Notes\Week 4\14.06.19\miniproj\sharp_1080_v1.csv','a')
    f.write("  \n" + path + ", " + info + ", " + str(fm))
    f.close()
