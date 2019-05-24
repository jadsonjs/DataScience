#
# This example is a deep learning to identify trafic signs using tensorflow base on:
#
# https://www.datacamp.com/community/tutorials/tensorflow-tutorial
# https://github.com/datacamp/datacamp-community-tutorials/tree/master/TensorFlow%20Tutorial%20For%20Beginners
#
# Jadson Santos - jadsonjs@gmail.com
#
# The data set can be found here:
#
# http://btsd.ethz.ch/shareddata/
# http://btsd.ethz.ch/shareddata/BelgiumTSC/BelgiumTSC_Training.zip
# http://btsd.ethz.ch/shareddata/BelgiumTSC/BelgiumTSC_Testing.zip
#
# to run this example install tensorflow and pyhton modules:
#
# pip3 install --upgrade --no-binary :all:  virtualenv
# virtualenv --system-site-packages -p python3 ~/tensorflow
# cd tensorflow
# source ./bin/activate
#
# pip3 install --upgrade tensorflow
# pip3 install --upgrade --no-binary :all:  tensorflow (on macOS)
#
# pip3 install scikit-image
# python3 -m pip install numpy
# python3 -m pip install matplotlib
#
# After install matploylib:
# On Ubuntu sudo apt-get install python3-tk
# On macOS create a file ~/.matplotlib/matplotlibrc there and add the following code: backend: TkAgg
#

import tensorflow as tf
from skimage import transform
from skimage import data
import matplotlib.pyplot as plt 
import os
import numpy as np
from skimage.color import rgb2gray
import random

# ------------------------------------ loading images --------------------------------

#
# function itself starts off by gathering all the subdirectories
# it basically says that, if you find something in the
# you’ll double check whether this is a directory, and if it is one, you’ll add it to your list. 
# Remember that each subdirectory represents a label.
#
# Next, you have to loop through the subdirectories. You first initialize two lists, labels and images. 
# Next, you gather the paths of the subdirectories and the file names of the images that are stored 
# in these subdirectories. After, you can collect the data in the two lists with the help of 
# the append() function.
def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory) 
                   if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f) 
                      for f in os.listdir(label_directory) 
                      if f.endswith(".ppm")]
        for f in file_names:
            images.append(data.imread(f))
            labels.append(int(d))
    return images, labels

# This path is the one where you have made the directory with your training and test data.
ROOT_PATH = "/home/jadson/Documentos/data"
train_data_directory = os.path.join(ROOT_PATH, "Training")
test_data_directory  = os.path.join(ROOT_PATH, "Testing")

images, labels = load_data(train_data_directory)


# ------------------------------------ data analysis --------------------------------
images_array = np.array(images)
labels_array = np.array(labels)


# Print the `images` dimensions
print(images_array.ndim)

# Print the number of `images`'s elements
print(images_array.size)

# Print the first instance of `images`
images_array[0]

# Print the `labels` dimensions
print(labels_array.ndim)

# Print the number of `labels`'s elements
print(labels_array.size)

# Count the number of labels
print(len(set(labels_array)))

# Make a histogram with 62 bins of the `labels` data
plt.hist(labels, 62)

# Show the plot
plt.show()


# ------------------------------------ visualizing imagens --------------------------------

# Then, you’re going to make a list with 4 random numbers. 
#These will be used to select traffic signs from the images array that you have just inspected in the previous section


# Determine the (random) indexes of the images that you want to see 
traffic_signs = [300, 2250, 3650, 4000]

# Fill out the subplots with the random images that you defined 
for i in range(len(traffic_signs)):
    plt.subplot(1, 4, i+1)
    plt.axis('off')
    plt.imshow(images[traffic_signs[i]])
    plt.subplots_adjust(wspace=0.5)
    print("shape: {0}, min: {1}, max: {2}".format(images[traffic_signs[i]].shape, 
                                                  images[traffic_signs[i]].min(), 
                                                  images[traffic_signs[i]].max()))
plt.show()



# ---------------------------------  Feature Extraction   -----------------------------------


# Resize images
images32 = [transform.resize(image, (28, 28)) for image in images]
images32 = np.array(images32)

# Image Conversion to Grayscale
images32 = rgb2gray(np.array(images32))

#for i in range(len(traffic_signs)):
#    plt.subplot(1, 4, i+1)
#    plt.axis('off')
#    plt.imshow(images32[traffic_signs[i]], cmap="gray")
#    plt.subplots_adjust(wspace=0.5)
#    
#plt.show()

#print(images32.shape)


# ----------------------------- Modeling The Neural Network -------------------------------


# Initialize placeholders 
# Remember that placeholders are values that are unassigned and that will be initialized by the session when you run it.
x = tf.placeholder(dtype = tf.float32, shape = [None, 28, 28])
y = tf.placeholder(dtype = tf.int32, shape = [None])

# Flatten the input data
#Then, you build up the network. 
#You first start off by flattening (convert a matrix to an arrray) the input with the help of the flatten() function, 
#which will give you an array of shape [None, 784] instead of the [None, 28, 28], which is the shape of your grayscale images.
images_flat = tf.contrib.layers.flatten(x)

# Fully connected layer
#After you have flattened the input, you construct a fully connected layer that generates logits of size [None, 62]
#Logits is the function operates on the unscaled output of earlier layers and that uses the relative scale to understand the units is linear.
logits = tf.contrib.layers.fully_connected(images_flat, 62, tf.nn.relu)


# Define a loss function
# With the multi-layer perceptron built out, you can define the loss function.
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels = y, logits = logits))

# Define an optimizer 
# You also want to define a training optimizer; 
# Some of the most popular optimization algorithms used are the Stochastic Gradient Descent (SGD), ADAM and RMSprop. 
# Depending on whichever algorithm you choose, you’ll need to tune certain parameters, such as learning rate or momentum. 
# In this case, you pick the ADAM optimizer, for which you define the learning rate at 0.001.
train_op = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

# Convert logits to label indexes
correct_pred = tf.argmax(logits, 1)

# Define an accuracy metric
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

print("images_flat: ", images_flat)
print("logits: ", logits)
print("loss: ", loss)
print("predicted_labels: ", correct_pred)


# ----------------------------  Running The Neural Network  -------------------------


tf.set_random_seed(1234)
sess = tf.Session()

sess.run( tf.global_variables_initializer() )

for i in range(201):
        print('EPOCH', i)
        _, accuracy_val = sess.run([train_op, accuracy], feed_dict={x: images32, y: labels})
        if i % 10 == 0:
            print("Loss: ", loss)
        print('DONE WITH EPOCH')


# ------------------------ Evaluating Your Neural Network  ----------------------------


# Pick 10 random images
sample_indexes = random.sample(range(len(images32)), 10)
sample_images = [images32[i] for i in sample_indexes]
sample_labels = [labels[i] for i in sample_indexes]

# Run the "predicted_labels" op.
predicted = sess.run([correct_pred], feed_dict={x: sample_images})[0]
                        
# Print the real and predicted labels
print(sample_labels)
print(predicted)

# Display the predictions and the ground truth visually.
fig = plt.figure(figsize=(10, 10))
for i in range(len(sample_images)):
    truth = sample_labels[i]
    prediction = predicted[i]
    plt.subplot(5, 2,1+i)
    plt.axis('off')
    color='green' if truth == prediction else 'red'
    plt.text(40, 10, "Truth:        {0}\nPrediction: {1}".format(truth, prediction), 
             fontsize=12, color=color)
    plt.imshow(sample_images[i])

plt.show()

