

from numpy import array

'''
  This method normalize the values of the features betwenn 0 and 1 values
'''
def normalize_feature(input_numeric_array, start_position, next_position):

    # normaliza the values of one feature
    bigger = 0
    smaller = 0 

    # for each numeric feature define the bigger and smaller value
    for index in range(start_position, len(input_numeric_array), next_position ):
        
        data = float(input_numeric_array[index])

        if bigger < data:
            bigger = data
        if smaller == 0 or  smaller > data:
            smaller = data

    # now normalize 
    for index in range(start_position, len(input_numeric_array), next_position ):
        input_numeric_array[index] = normalize ( float(input_numeric_array[index]), smaller, bigger )
              
    return input_numeric_array


def normalize(data, smaller, bigger): 
    if smaller == bigger:
        data = 0
    else:    
        data = float(data - smaller) /  float( bigger - smaller )

    return data
