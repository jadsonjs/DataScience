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

#
# This function the convert a RGB array to grayscale array
# Using Y' = 0.299 R + 0.587 G + 0.114 B
#
# https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale
#
def rgb2gray(rgbImg):
    return np.dot(rgbImg[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)

averageMask3x3 = np.array(
               [
               [1/9, 1/9, 1/9],
               [1/9, 1/9, 1/9],
               [1/9, 1/9, 1/9]
               ])


img2 = misc.imread('/Users/jadson/Desktop/DL04_Img2.2.jpg')
img3 = misc.imread('/Users/jadson/Desktop/DL04_Img2.1.jpg')

img2Gray = rgb2gray(img2)
img3Gray = rgb2gray(img3)

# apply the media filter
medianImg = ndimage.median_filter(img2Gray, 3)

# apply the average 3x3 filter
averageImg = ndimage.convolve(img2Gray, averageMask3x3);

plt.imshow(medianImg, cmap = plt.get_cmap('gray'))
plt.suptitle('Reconstruction with Median Filter 3x3')
plt.show()

plt.imshow(averageImg, cmap = plt.get_cmap('gray'))
plt.suptitle('Reconstruction with Average Filter 3x3')
plt.show()

plt.imshow(img3Gray, cmap = plt.get_cmap('gray'))
plt.suptitle('Original Image')
plt.show()
