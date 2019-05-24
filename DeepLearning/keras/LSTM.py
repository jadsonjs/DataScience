

'''Trains an LSTM model on the IMDB sentiment classification task.
The dataset is actually too small for LSTM to be of any advantage
compared to simpler, much faster methods such as TF-IDF + LogReg.
# Notes
- RNNs are tricky. Choice of batch size is important,
choice of loss and optimizer is critical, etc.
Some configurations won't converge.
- LSTM loss decrease patterns during training can be quite different
from what you see with CNNs/MLPs/etc.

https://github.com/keras-team/keras/blob/master/examples/imdb_lstm.py

if you run this example of MAC_OS:
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777)

So, to skip this error:

pip3 install requests

In file /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/keras/utils/data_utils.py

just below the import statements, add:

-----
import requests
requests.packages.urllib3.disable_warnings()
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
----

@see https://github.com/keras-team/keras/issues/1425

'''
from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.datasets import imdb

max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

print('Loading data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

print('Build model...')
model = Sequential()

# normaly use Embedding layer on text data.
# The first step in using an embedding layer is to encode this sentence by indices. 
# In this case we assign an index to each unique word.
# “deep learning is very deep” -> 1 2 3 4 1
#
# A word embedding is a class of approaches for representing words and documents using a dense vector representation.
#
# It is an improvement over more the traditional bag-of-word model encoding schemes where large sparse vectors were used to 
# represent each word or to score each word within a vector to represent an entire vocabulary. 
# These representations were sparse because the vocabularies were vast and a given word or document would be represented 
# by a large vector comprised mostly of zero values
#
# Instead, in an embedding, words are represented by dense vectors where a vector represents the projection of the word 
# into a continuous vector space.
# 
# It requires that the input data be integer encoded, so that each word is represented by a unique integer. 
# This data preparation step can be performed using the Tokenizer API also provided with Keras.
#
# The Embedding layer is initialized with random weights and will learn an embedding for all of the words in the training dataset.
#
# For example, below we define an Embedding layer with a vocabulary of 200 (e.g. integer encoded words from 0 to 199, inclusive), 
# a vector space of 32 dimensions in which words will be embedded, and input documents that have 50 words each
#
# e = Embedding(200, 32, input_length=50)
#
# input_dim: This is the size of the vocabulary in the text data. For example, if your data is integer encoded to values 
# between 0-10, then the size of the vocabulary would be 11 words.
#
# output_dim: This is the size of the vector space in which words will be embedded. It defines the size of the output 
# vectors from this layer for each word. For example, it could be 32 or 100 or even larger. Test different values for your problem.
#
# input_length: This is the length of input sequences, as you would define for any input layer of a Keras model. 
# For example, if all of your input documents are comprised of 1000 words, this would be 1000
# 
model.add(Embedding(max_features, 128))

# the LSTM layer
#
#dropout: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs.
# recurrent_dropout: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state.
#
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))

# full conected layer a "normal" neural network
model.add(Dense(1, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=15,
          validation_data=(x_test, y_test))
score, acc = model.evaluate(x_test, y_test,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)


