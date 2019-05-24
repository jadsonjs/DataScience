


# Consider the case where you have one sequence of multiple time steps and one feature.
from numpy import array
data = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])


# We can then use the reshape() function on the NumPy array to reshape this one-dimensional array 
# into a three-dimensional array with 1 sample, 10 time steps, and 1 feature at each time step.

data = data.reshape((1, 10, 1))
print(data.shape)


# Consider the case where you have multiple parallel series as input for your model.
# For example, this could be two parallel series of 10 values:
#series 1: 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0
#series 2: 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1

from numpy import array
data = array([ [0.1, 1.0],
	           [0.2, 0.9],
	           [0.3, 0.8],
	           [0.4, 0.7],
	           [0.5, 0.6],
	           [0.6, 0.5],
	           [0.7, 0.4],
	           [0.8, 0.3],
	           [0.9, 0.2],
	           [1.0, 0.1]])


#This data can be framed as 1 sample with 10 time steps and 2 features.
#It can be reshaped as a 3D array as follows:

#model = Sequential()
#model.add(LSTM(32, input_shape=(10, 2)))
#model.add(Dense(1))

data = data.reshape(1, 10, 2)
print(data.shape)




#Here, we have 25 samples, 200 time steps per sample, and 1 feature


# split into samples (e.g. 5000/200 = 25)
samples = list()
length = 200
# step over the 5,000 in jumps of 200
for i in range(0,n,length):
	# grab from i to i + 200
	sample = data[i:i+length]
	samples.append(sample)
print(len(samples))

data = array(samples)
print(data.shape)

# reshape into [samples, timesteps, features]
# expect [25, 200, 1]
data = data.reshape((len(samples), length, 1))
print(data.shape)


#https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/
#
#For a feed-forward network, your input has the shape (number of samples, number of features). With an LSTM/RNN, you add a time dimension, 
#and your input shape becomes (number of samples, number of timesteps, number of features). This is in the documentation.
#So if your feature dimension is 5, and you have 2 timesteps, your input could look like

#[ [ 
#    [1,2,3,4,5], 
#    [2,3,4,5,6]
#  ],
#  [ 
#    [2,4,6,8,0], 
#    [9,8,7,6,5]
#  ] 
#]

#Your output shape depends on how you configure the net. If your LSTM/RNN has return_sequences=False, you'll have one label 
#per sequence; 
#if you set return_sequences=True, you'll have one label per timestep.


#So in the example, [ [[1,2,3,4,5], [2,3,4,5,6]], [[2,4,6,8,0], [9,8,7,6,5]] ]
#input_shape is (2, 2, 5).

#And a 'sequence' is '[[1,2,3,4,5], [2,3,4,5,6]]' I assume.
#and has 2 timesteps






