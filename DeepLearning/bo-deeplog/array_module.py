

from numpy import array

'''
  This method receive the array of one dimension of all feature 
  and return the 1 sample n features.

  receive an array [1, 10, ‘http://exempla1’, 2, 20, ‘http://exempla2’]
  returns 
'''
def reshape_input(cvs_raw_data, samples, timesteps, features): 
	data = array(cvs_raw_data).reshape(samples, timesteps, features)
	return data;

