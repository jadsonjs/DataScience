
#
# This program is distributed without any warranty and it
# can be freely redistributed for research, classes or private studies,
# since the copyright notices are not removed.
#
# Jadson Santos - jadsonjs@gmail.com
# 
# to run this exemple install pyhton modules:
#
# pip3 install pandas
# pip3 install numpy
# pip3 install scikit-learn
# pip3 install mlxtend 
#


import pandas as pd
import numpy as np

from sklearn.model_selection import KFold, cross_validate, cross_val_score

from sklearn.neighbors import KNeighborsClassifier  # KNN
from sklearn.naive_bayes import GaussianNB          # Naive bayes
from sklearn.neural_network import MLPClassifier    # MLP
from sklearn import tree                            # Decision Tree
from sklearn.linear_model import LogisticRegression # 
from mlxtend.classifier import StackingClassifier   # Ensemble Stakking
from mlxtend.feature_selection import ColumnSelector



#
# DEFINE YOUR DATASET HERE, ALREADY PRE PROCESSED ! 
#
# read the CSV file with your data base and put into a Pandas DataFrame 
# https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/
#
df = pd.read_csv('/Users/jadson/tmp/WDBC_preprocessed.csv')
#print(df)

#
# Get the classes of the problem
#
classes = df['diagnosis']
#print(classes)


#
# Define the classifiers 
#
classifierKNN = KNeighborsClassifier(n_neighbors=1)
classifierNB = GaussianNB()
#classifierDT = tree.DecisionTreeClassifier(criterion=criterion, splitter=splitter, min_samples_split=random.random(), max_features=max_features)
classifierMLP = MLPClassifier(hidden_layer_sizes=(17), learning_rate_init=0.01, max_iter=50, activation='tanh', solver='sgd', momentum=0.8)
lr = LogisticRegression()


#
# Define the ensemble classifier with its base classifiers
#
sclf = StackingClassifier(classifiers=[classifierMLP, classifierMLP, classifierMLP], meta_classifier=classifierKNN)

#
# run the ensemble classification in a 10-fold cross validation:
#
scores = cross_val_score(sclf, df, classes, cv=KFold(n_splits=10), scoring='accuracy')
print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), 'StackingClassifier'))