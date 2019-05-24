

''' 
    https://github.com/keras-team/keras/issues/2045
    input data should be 3D tensor with shape (nb_samples, timesteps, input_dim).

    If I have 1000 sentences,each sentence has 10 words, and each word is presented in a 3-dim vector, so:
    1000 is nb_samples, 
    10 is the timesteps and 
    3 is the input_dim

    https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/

    to run:  

	execute the tensorflow emvoriment 

    cd tensorflow 
    source bin/activate

    python3 bussiness_op_lstm.py

'''

from __future__ import print_function

import numpy as np
from numpy import array

from csv_module import load_csv_data
from csv_module import load_csv_data2
from array_module import reshape_input

from prepare_input_module import prepareLSTMdata

from process_learning_module import buildLSTMModel
from process_learning_module import processLSTMLearning


# ==================== input values ====================

#macos
raw_data_file_name     = '/Users/jadson/Desktop/tinytrainingmock.csv'
deep_network_file_name = '/Users/jadson/Desktop/trainingdata.csv'
businnes_op_lstm_model = '/Users/jadson/Desktop/final_model.h5'

#ubuntu
#raw_data_file_name      = '/home/jadson/Documentos/deeplog/csvs/tinytrainingmock2.csv'
#deep_network_file_name  = '/home/jadson/Documentos/deeplog/csvs/trainingdata.csv'
#businnes_op_lstm_model  = '/home/jadson/Documentos/deeplog/csvs/final_model.h5'

samples = 156 
timesteps = 100
features = 1
#features_indexes = [0,1,2,3,5]

lstm_layer_size = 32
dence_layer_size = 10
batch_size= 64
epochs=10
# ======================================================



# ==================== prepare LSTM data ===============


#prepareLSTMdata(raw_data_file_name, deep_network_file_name, features_indexes)

cvs_raw_data = load_csv_data2(deep_network_file_name)
#print(cvs_raw_data)

x_train = reshape_input(cvs_raw_data, samples, timesteps, features)  # 1 x 10 x 5
#print('### 4 ###')
#print(lstm_input_data)

y_train = np.array( [ [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] ] ) # 1 x 10

# 5 features, 10 timesteps
x_test = array([
  [0.1, 1.0, 0.1, 1.0, 0.0],
  [0.2, 0.9, 0.1, 1.0, 0.0],
  [0.3, 0.8, 0.1, 1.0, 0.0],
  [0.4, 0.7, 0.1, 1.0, 0.0],
  [0.5, 0.6, 0.1, 1.0, 0.0],
  [0.6, 0.5, 0.1, 1.0, 0.0],
  [0.7, 0.4, 0.1, 1.0, 0.0],
  [0.8, 0.3, 0.1, 1.0, 0.0],
  [0.9, 0.2, 0.1, 1.0, 0.0],
  [1.0, 0.1, 0.1, 1.0, 0.0]])

x_test = reshape_input(x_test, samples, timesteps, features) # 1 x 10 x 5

y_test =  np.array( [ [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] ] ) # 1 x 10


# 5 features, 10 timesteps
x_val = array([
  [0.1, 1.0, 0.1, 1.0, 0.0],
  [0.2, 0.9, 0.1, 1.0, 0.0],
  [0.3, 0.8, 0.1, 1.0, 0.0],
  [0.4, 0.7, 0.1, 1.0, 0.0],
  [0.5, 0.6, 0.1, 1.0, 0.0],
  [0.6, 0.5, 0.1, 1.0, 0.0],
  [0.7, 0.4, 0.1, 1.0, 0.0],
  [0.8, 0.3, 0.1, 1.0, 0.0],
  [0.9, 0.2, 0.1, 1.0, 0.0],
  [1.0, 0.1, 0.1, 1.0, 0.0]])

x_val = reshape_input(x_val, samples, timesteps, features) # 1 x 10 x 5

y_val =  np.array( [ [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] ] )  # 1 x 10


# ==================== Process LSTM Model ===============


#print('--- X_train ---')
#print(x_train)
#print(len(x_train))
#print('--- y_train ---')
#print(y_train)
#print(len(y_train))


model = buildLSTMModel(lstm_layer_size, dence_layer_size, timesteps, features)

traningLSTM(model, batch_size, epochs, x_train, y_train, x_val, y_val, x_test, y_test)

# ==================== Save the Model ===============

# save model to single file
# sudo pip install h5py
model.save(businnes_op_lstm_model)



