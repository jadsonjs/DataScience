#
# This program is distributed without any warranty and it
# can be freely redistributed for research, classes or private studies,
# since the copyright notices are not removed.
#
# Calculate the convolution between 2 arrays in python
#
# Jadson Santos - jadsonjs@gmail.com
#
#
# to run this exemple install pyhton modules:
#
# python3 -m pip install SciPy
#

# calculate the convolution of a array
def myconv( array, mask ):

	arrayReversed = list(reversed(array))

	initmask = len(arrayReversed)-1          # last position of array
	endmask  = initmask+len(mask)-1          # last position of array + mask size


	while (endmask >= 0):  # while the mask dont pass by all array

		'''
		apply each mask element
		'''
		conv = 0
		for counter in range( len(mask) ):

			'''
		 	Test if the element of the mask is inside of array positions
		 	initmask + counter is the current position of array the will be calculated
			'''
			if( ( initmask + counter < len(arrayReversed) )  and ( initmask + counter >= 0 ) ):
				conv = conv + (arrayReversed[initmask+counter] * mask[counter])

		print(conv)

    	# walk with the mask
		initmask -= 1
		endmask -= 1

array=[1,2,3,4,5]
mask=[1,2,3]

myconv(array, mask)
myconv(mask, array)
