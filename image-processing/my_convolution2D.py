#
# This program is distributed without any warranty and it
# can be freely redistributed for research, classes or private studies,
# since the copyright notices are not removed.
#
# This file contains a function to calculate matriz convolution
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
from scipy import signal

#7x7
A = np.array(  [
               [8, 5, 8, 1, 6, 8, 7],
               [9, 9, 2, 8, 2, 7, 8],
               [2, 9, 4, 9, 7, 3, 2],
               [9, 2, 9, 7, 1, 9, 5],
               [6, 9, 8, 7, 3, 1, 5],
               [1, 9, 9, 7, 1, 4, 6],
               [3, 5, 6, 4, 1, 4, 7] ] )
#3x3
B = np.array([ [3, 2, 2],
               [1, 1, 3],
               [3, 1, 2]
               ])



print("--------------- Full --------------------")
con1 = signal.convolve(A, B, mode='full', method='direct')
print(" ")
print(con1)

con2 = signal.convolve(B, A, mode='full', method='direct')
print(" ")
print(con2)

print("---------------Same-----------------")

con3 = signal.convolve(A, B, mode='same', method='direct')
print(" ")
print(con3)

con4 = signal.convolve(B, A, mode='same', method='direct')
print(" ")
print(con4)

print("----------------My--------------------")

# calculate the convolution of a square matriz with hte mode "same"
def myconv2D( matrix, mask ):
    matrixLen = len(matrix)
    maskLen = len(mask)
    border  = int(maskLen / 2);


    # the result matrix will be a bigger in the full model
    tempMatrix = np.zeros( (matrixLen+(border*2), matrixLen+(border*2)), dtype=int  )
    convMatrix = np.zeros( (matrixLen, matrixLen), dtype=int  )

    # copy data of original matrix to convMatrix
    for i in range( matrixLen ):
        for j in range( matrixLen ):
            tempMatrix[i+1][j+1] = matrix[i][j]

    convMatrixLen = len(convMatrix)

    # the shift of the mask over the convMatrix
    # the size of original matriz
    #maxShift = matrixLen
    shiftX = 0
    shiftY = 0

    for shiftI in range( matrixLen ):
        for shiftJ in range( matrixLen ):

            for i in range( maskLen ):
                for j in range( maskLen ):
                    convMatrix[shiftI][shiftJ] = convMatrix[shiftI][shiftJ] + ( tempMatrix[i+shiftI][j+shiftJ] * mask[i][j])

    print(" ")
    print(convMatrix)

myconv2D(A, B)
myconv2D(B, A)
