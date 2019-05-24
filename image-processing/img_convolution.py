#
# This program is distributed without any warranty and it
# can be freely redistributed for research, classes or private studies,
# since the copyright notices are not removed.
#
# This file performs image processing in pyhton
#
# Jadson Santos - jadsonjs@gmail.com
#
# http://www.scipy-lectures.org/advanced/image_processing/
#
# to run this exemple install pyhton modules:
#
# python3 -m pip install SciPy
# python3 -m pip install numpy
# python3 -m pip install matplotlib
#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from scipy import ndimage
from scipy.signal import convolve2d

#
# Function the convert a RGB array to grayscale array
# Using Y' = 0.299 R + 0.587 G + 0.114 B
#
# https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale
#
def rgb2gray(rgbImg):
    return np.dot(rgbImg[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)


# Read the image as array
img1 = misc.imread('/Users/jadson/Desktop/DL04_Img1.jpg')
print(type(img1))    # print the img1 type
print(img1[0, 40])   # the value of possition 0,40
print(img1.shape)    # print the dimesions of image
print(img1.dtype)    # dtype  uint8 = 0 to 255 values

img1Gray = rgb2gray(img1)
print(type(img1Gray))    # print the img1 type
print(img1Gray[0, 40])   # the value of possition 0,40
print(img1Gray.shape)    # print the dimesions of image
print(img1Gray.dtype)    # dtype  uint8 = 0 to 255 values


mask3 = np.array([
               [1/9, 1/9, 1/9],
               [1/9, 1/9, 1/9],
               [1/9, 1/9, 1/9]])

mask7 = np.array([ [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
               [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
               [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
               [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
               [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
               [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
               [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49]])

mask11 = np.array([ [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
              [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
              [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
              [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
              [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
              [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
              [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
              [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
              [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
              [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
              [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
              [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121]
              ])


#
# apply convolution fuction with a average filter
#
average3  = ndimage.convolve(img1Gray, mask3);
average7  = ndimage.convolve(img1Gray, mask7);
average11 = ndimage.convolve(img1Gray, mask11);


#Convolves im with window, over all three colour channels
#
# http://songhuiming.github.io/pages/2017/04/16/convolve-correlate-and-image-process-in-numpy/
#
ims = []
for d in range(3):
    im_conv_d = ndimage.convolve(img1[:,:,d], mask11)
    ims.append(im_conv_d)

originalAverage11 = np.stack(ims, axis=2).astype("uint8")


print(type(originalAverage11))    # print the img1 type
print(originalAverage11.shape)    # print the dimesions of image
print(originalAverage11.dtype)    # dtype  uint8 = 0 to 255 values

# prit the result of convolution
plt.imshow(average3, cmap = plt.get_cmap('gray'))
plt.suptitle('Convolution Average 3x3')
plt.show()

plt.imshow(average7, cmap = plt.get_cmap('gray'))
plt.suptitle('Convolution Average 7x7')
plt.show()

plt.imshow(average11, cmap = plt.get_cmap('gray'))
plt.suptitle('Convolution Average 11x11')
plt.show()

plt.imshow(originalAverage11)
plt.suptitle('Convolution Average 11x11 In Original Image')
plt.show()

plt.imshow(img1Gray, cmap = plt.get_cmap('gray'))
plt.suptitle('Original Image')
plt.show()
