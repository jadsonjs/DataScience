

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, Activation, Flatten
from keras.optimizers import Adam, Adamax, RMSprop
from keras.layers import LSTM
from keras.datasets import imdb

# pip3 install pydot
# sudo apt-get install graphviz
#from keras.utils import plot_model
import matplotlib.pyplot as plt


def buildLSTMModel1(lstm_layer_size, dence_layer_size, timesteps, data_dim):


	model = Sequential()

	# The LSTM layer with 10 blocks
	#
	# The three dimensions of this input are:
	#
	# *** Samples ***    : One sequence is one sample. A batch is comprised of one or more samples.
	# *** Time Steps *** : One time step is one point of observation in the sample.
	# *** Features ***   : One feature is one observation at a time step.
	#
	# the network assumes you have 1 or more samples 
	# and requires that you specify the number of time steps and the number of features.
	#
	# return_sequences=True    What this does is ensure that the LSTM cell returns all of 
	#                          the outputs from the unrolled LSTM cell through time.
	#
	model.add( LSTM(lstm_layer_size, return_sequences=True, input_shape=(timesteps, data_dim) ) )
	model.add( LSTM(lstm_layer_size, return_sequences=True) )
	model.add( LSTM(lstm_layer_size) )

	# full conected layer a "normal" neural network
	#model.add(Dense(128, activation='relu'))
	model.add(Dense(dence_layer_size, activation='softmax'))
	#plot_model(model, to_file='model_plot_1.jpg', show_shapes=True, show_layer_names=True)
	return model;



def buildLSTMModel2(lstm_layer_size, dence_layer_size, timesteps, data_dim):


	model = Sequential()

	# The LSTM layer with 10 blocks
	#
	# The three dimensions of this input are:
	#
	# *** Samples ***    : One sequence is one sample. A batch is comprised of one or more samples.
	# *** Time Steps *** : One time step is one point of observation in the sample.
	# *** Features ***   : One feature is one observation at a time step.
	#
	# the network assumes you have 1 or more samples 
	# and requires that you specify the number of time steps and the number of features.
	#
	# return_sequences=True    What this does is ensure that the LSTM cell returns all of 
	#                          the outputs from the unrolled LSTM cell through time.
	#
	model.add( LSTM(lstm_layer_size, input_shape=(timesteps, data_dim) ) )
	

	# full conected layer a "normal" neural network
	#model.add(Dense(128, activation='relu'))
	model.add(Dense(dence_layer_size, activation='softmax'))
	#plot_model(model, to_file='model_plot_2.jpg', show_shapes=True, show_layer_names=True)
	return model;




def buildLSTMModel3(lstm_layer_size, dence_layer_size, timesteps, data_dim):


	model = Sequential()

	# The LSTM layer with 10 blocks
	#
	# The three dimensions of this input are:
	#
	# *** Samples ***    : One sequence is one sample. A batch is comprised of one or more samples.
	# *** Time Steps *** : One time step is one point of observation in the sample.
	# *** Features ***   : One feature is one observation at a time step.
	#
	# the network assumes you have 1 or more samples 
	# and requires that you specify the number of time steps and the number of features.
	#
	# return_sequences=True    What this does is ensure that the LSTM cell returns all of 
	#                          the outputs from the unrolled LSTM cell through time.
	#
	model.add( LSTM(lstm_layer_size, return_sequences=True, input_shape=(timesteps, data_dim) ) )
	model.add( LSTM(lstm_layer_size, return_sequences=True) )
	model.add( LSTM(lstm_layer_size, return_sequences=True) )
	model.add( LSTM(lstm_layer_size, return_sequences=True) )
	model.add( LSTM(lstm_layer_size) )
	

	# full conected layer a "normal" neural network
	#model.add(Dense(128, activation='relu'))
	model.add(Dense(dence_layer_size, activation='softmax'))
	#plot_model(model, to_file='model_plot_3.jpg', show_shapes=True, show_layer_names=True)
	return model;




def traningLSTM1(model, batch_size, epochs, x_train, y_train, x_val, y_val, x_test, y_test):


	# try using different optimizers and different optimizer configs
	# loss:
	# https://en.wikipedia.org/wiki/Loss_function
	# http://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html
	# optimizer:
	# http://ruder.io/optimizing-gradient-descent/index.html#rmsprop
	#
	model.compile(loss='categorical_crossentropy',
	              #optimizer=RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0),
	              #optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False),
	              optimizer=Adamax(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0),
	              metrics=['accuracy'])


	# ===================== Train LSTM  ===================

	# with validation data
	#model.fit(lstm_input_data, lstm_input_label,
	#          batch_size=batch_size,
	#          epochs=1,
	#          validation_data=(lstm_test_data, lstm_test_data))
	#
	# You may need to enable the validation split of your trainset. the validation happens in 1/3 of the trainset. 
	
	# with validation data
	history = model.fit(x_train, y_train, validation_split=0.33, batch_size=batch_size, epochs=epochs, validation_data=(x_val, y_val) )

    
	#score, acc = model.evaluate(lstm_test_data, lstm_test_data,
	#                            batch_size=batch_size)
	#print('Test score:', score)
	#print('Test accuracy:', acc)

	scores = model.evaluate(x_test, y_test, verbose=0)
	print("Accuracy: %.2f%%" % (scores[1]*100))
	plotInfomation(history)





def traningLSTM2(model, batch_size, epochs, x_train, y_train, x_test, y_test):


	# try using different optimizers and different optimizer configs
	# loss:
	# https://en.wikipedia.org/wiki/Loss_function
	# http://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html
	# optimizer:
	# http://ruder.io/optimizing-gradient-descent/index.html#rmsprop
	#
	model.compile(loss='categorical_crossentropy',
	              #optimizer=RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0),
	              #optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False),
	              optimizer=Adamax(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0),
	              metrics=['accuracy'])


	# ===================== Train LSTM  ===================

	# with validation data
	#model.fit(lstm_input_data, lstm_input_label,
	#          batch_size=batch_size,
	#          epochs=1,
	#          validation_data=(lstm_test_data, lstm_test_data))
	#
	# You may need to enable the validation split of your trainset. the validation happens in 1/3 of the trainset. 

	# without validation data
	history = model.fit(x_train, y_train, validation_split=0.33, batch_size=batch_size, epochs=epochs)

    
	#score, acc = model.evaluate(lstm_test_data, lstm_test_data,
	#                            batch_size=batch_size)
	#print('Test score:', score)
	#print('Test accuracy:', acc)

	scores = model.evaluate(x_test, y_test, verbose=1)
	print("Accuracy: %.2f%%" % (scores[1]*100))
	plotInfomation(history)



'''
  Plot Information about the LSTM parameters
'''
def plotInfomation(history):
	
	# summarize history for accuracy
	plt.plot(history.history['acc'])
	plt.plot(history.history['val_acc'])
	plt.title('model accuracy')
	plt.ylabel('accuracy')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()
	# summarize history for loss
	plt.plot(history.history['loss'])
	plt.plot(history.history['val_loss'])
	plt.title('model loss')
	plt.ylabel('loss')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()

	

