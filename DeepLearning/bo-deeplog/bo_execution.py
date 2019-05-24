
from numpy import array
from keras.models import load_model

from array_module import reshape_input

from csv_module import load_execution_files


#linux
#base_directory          = '/home/jadson/git/deeplearning/data'
#macos
base_directory           = '/Users/jadson/git/deeplearning/data'

lstm_model              = base_directory+'/lstm_model.h5'



# size of the data set
sample_number = 1
timesteps = 100
features = 1

# load model from single file
model = load_model(lstm_model)


print(' ------- loading traning data ------ ')
x = load_execution_files(base_directory, sample_number)

x = reshape_input(x, 1, timesteps, features)  # 256 samples x 100 timesteps x 1 features

print(x)

# make predictions
yhat = model.predict(x, verbose=0)
#yhat = model.predict_classes(x, verbose=1)
print(yhat)