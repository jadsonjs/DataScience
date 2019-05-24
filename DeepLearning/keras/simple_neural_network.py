

#
#For a single-input model with 10 classes (categorical classification):
#
#
from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100)) # the first layer in a Sequential model needs to receive information about its input shape
model.add(Dense(10, activation='softmax'))




# Before training a model, you need to configure the learning process, which is done via the compile method. 

# ----
# *** rmsprop ***  optimizer. It is recommended to leave the parameters of this optimizer at their default values (except the learning rate, which can be freely tuned).
# This optimizer is usually a good choice for recurrent neural networks.
# ----

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])



#  --------------------------- Training  -------------------------------------

# Generate dummy data
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)

