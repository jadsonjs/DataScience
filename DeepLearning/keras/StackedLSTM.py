
#
# https://keras.io/getting-started/sequential-model-guide/
#

from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

data_dim = 16
timesteps = 8
num_classes = 10

# expected input data shape: (batch_size, timesteps, data_dim)
model = Sequential()

# https://machinelearningmastery.com/return-sequences-and-return-states-for-lstms-in-keras/
# 
# input sample with 3 time steps and one feature observed at each time step
#  
#  t1 = 0.1
#  t2 = 0.2
#  t3 = 0.3
#
#  LSTM(1, return_sequences=True)
#
#  Running the example returns a sequence of 3 values, one hidden state output 
#  for each input time step for the single LSTM cell in the layer
#  
# You must set return_sequences=True when stacking LSTM layers so that the second LSTM 
# layer has a three-dimensional sequence input

model.add(LSTM(32, return_sequences=True, input_shape=(timesteps, data_dim))) # returns a sequence of vectors of dimension 32
model.add(LSTM(32, return_sequences=True))   # returns a sequence of vectors of dimension 32
#model.add(LSTM(32, return_sequences=True))  # returns a sequence of vectors of dimension 32
model.add(LSTM(32))                          # return a single vector of dimension 32
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# Generate dummy training data
#
# 1000 examples, with timesteps, for data_dim features
#
# num_classes = number of classe to learning
#
x_train = np.random.random((1000, timesteps, data_dim))  # 10 x 8 x 16
y_train = np.random.random((1000, num_classes))          # 10 x 10

print("----Train ----")
print(x_train)
print(y_train)

# Generate dummy validation data
x_val = np.random.random((100, timesteps, data_dim))
y_val = np.random.random((100, num_classes))

print("--- Val -----")
print(x_val)
print(y_val)

# Generate dummy test data
x_test = np.random.random((100, timesteps, data_dim))   # 1 x 8 x 16
y_test = np.random.random((100, num_classes))           # 1 x 10


print("---- Test ----")
print(x_test)
print(y_test)

model.fit(x_train, y_train,
          batch_size=64, epochs=5,
          validation_data=(x_val, y_val))

scores = model.evaluate(x_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))

