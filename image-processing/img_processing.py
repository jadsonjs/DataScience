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
# python3 -m pip install Pillow
# python3 -m pip install SciPy
# python3 -m pip install numpy
# python3 -m pip install matplotlib
#

# USING PIL

#
#LA mode has luminosity (brightness) and alpha.
#If you use LA mode, then greyscale.png will be an RGBA
#image with the alpha channel of image.png preserved.
#If you use L mode, then greyscale.png will be an RGB image (with no alpha
#
#https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
#
from PIL import Image
im = Image.open("/Users/jadson/Desktop/DL04_Img1.jpg")
imgGray = im.convert('LA')
imgGray.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from scipy import ndimage

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

# gaussian filters 
blurred_image1 = ndimage.gaussian_filter(img1Gray, sigma=3)
blurred_image2 = ndimage.gaussian_filter(img1Gray, sigma=7)
blurred_image3 = ndimage.gaussian_filter(img1Gray, sigma=11)
blurred_image4 = ndimage.gaussian_filter(img1, sigma=11)

mask3 = np.array([[1/9, 1/9, 1/9],
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



mask113D = np.array([ [ [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
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
              ],
           [
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
            [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
            [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121]
            ],
             [
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
          [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121],
          [1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121, 1/121]
          ]
          ])

average3 = ndimage.convolve(img1Gray, mask3);
average7 = ndimage.convolve(img1Gray, mask7);
average11 = ndimage.convolve(img1Gray, mask11);
originalAverage11 = ndimage.convolve(img1, mask113D);

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

print('--- Image Reconstruction ---')

img2 = misc.imread('/Users/jadson/Desktop/DL04_Img2.2.jpg')
img3 = misc.imread('/Users/jadson/Desktop/DL04_Img2.1.jpg')

img2Gray = rgb2gray(img2)
img3Gray = rgb2gray(img3)

medianImg = ndimage.median_filter(img2Gray, 3)

averageImg = ndimage.convolve(img2Gray, mask3);

plt.imshow(medianImg, cmap = plt.get_cmap('gray'))
plt.suptitle('Reconstruction with Median Filter 3x3')
plt.show()

plt.imshow(averageImg, cmap = plt.get_cmap('gray'))
plt.suptitle('Reconstruction with Average Filter 3x3')
plt.show()

plt.imshow(img3Gray, cmap = plt.get_cmap('gray'))
plt.suptitle('Original Image')
plt.show()





#plt.imshow(blurred_image1, cmap = plt.get_cmap('gray'))
#plt.show()

#plt.imshow(blurred_image2, cmap = plt.get_cmap('gray'))
#plt.show()

#plt.imshow(blurred_image3, cmap = plt.get_cmap('gray'))
#plt.show()

#plt.imshow(blurred_image4)
#plt.show()

# show the imagem
#plt.imshow(img1Gray)


#plt.imshow(img1, cmap = plt.get_cmap('gray'))
#plt.show()

#from scipy import misc
#face = misc.face(gray=True)
#misc.imsave('/Users/jadson/Desktop/DL04_Img1.jpg', face)



#face = misc.imread('face.png')

#plt.imshow(imgGray)
#plt.show()
#imgGray[0, 40]
print('--- END ---')
