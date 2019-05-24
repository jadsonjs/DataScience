


'''
	Define a function the normalize all elements of a array between 0 and 1
	Feature scaling is used to bring all values into the range [0,1]. This is also called unity-based normalization. 

	O(n2) 
'''
def normalization(array[]):    
    bigger, smaller = 0, 0

    # define the bigger and smaller value
	for i in range(len(array)):
		if bigger < array[i]:
			bigger = array[i]
		if smaller == 0 or  smaller > array[i]:
			smaller = array[i]

	# apply normalization calculation for all elements of array
	for i in range(len(hashs)):
    	array[i] = (array[i] - smaller) /  ( bigger - smaller )

    return array