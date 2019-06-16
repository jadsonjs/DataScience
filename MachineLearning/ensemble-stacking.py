
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

from random import randint

from sklearn.model_selection import KFold, cross_validate, cross_val_score

from sklearn.neighbors import KNeighborsClassifier                # KNN
from sklearn.naive_bayes import GaussianNB , ComplementNB         # Naive bayes
from sklearn.neural_network import MLPClassifier                  # MLP
from sklearn import tree                                          # Decision Tree
from sklearn.linear_model import LogisticRegression               # 
from mlxtend.classifier import StackingClassifier                 # Ensemble Stakking
from mlxtend.feature_selection import ColumnSelector
from sklearn.pipeline import make_pipeline



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
# Genarete randem features numbers for each classifiers. between 0 and 29 for my database
#
def genareatedRandomFeatures():
    seed = randint(0, 3)  
    if seed == 0:
	    return (0, 2, 4, 6, 8, 10, 12)
    elif seed == 1:
	    return (1, 3, 5, 7, 9, 11, 13)
    elif seed == 2:
	    return (14, 16, 18, 20, 22, 24, 26, 28)
    else:
	    return (15, 17, 19, 21, 23, 25, 27, 29)


# to test of method genareatedRandomFeatures
#for i in range(0,10):
#    print(genareatedRandomFeatures());


# construct the KNN classifier 
def buildKNNClassifier():
	return KNeighborsClassifier(n_neighbors=3)

# construct the Naive Bayes classifier 
def buildNBClassifier():
	return GaussianNB()

# construct the Naive Bayes classifier 
def buildComplementNBClassifier():
	return ComplementNB()

# construct the Decision tree classifier 
def buildADClassifier():
	criterion = random.sample(['entropy', 'gini'], 1)[0]
	max_features = random.sample(['sqrt', 'log2', None], 1)[0]
	splitter = random.sample(['best', 'random'], 1)[0]
	return tree.DecisionTreeClassifier(criterion=criterion, splitter=splitter, min_samples_split=random.random(), max_features=max_features)

# construct the MLP classifier 
def buildMLPClassifier():
	return MLPClassifier(hidden_layer_sizes=(8), learning_rate_init=0.01, max_iter=10000, activation='tanh', solver='sgd', momentum=0.8)



#
# list of classifiers the will be executed
#
list_base_classifiers = []

#
# create the list of 10 MLP and 10 NB  base classifiers
#
def createStackingHeterogeneus_MLP_NB(selectFeatures):
    #
    # 10 MLP classifiers and 10 NB classifiers
    #
    for i in range(0,10):
        if selectFeatures :
            cols = genareatedRandomFeatures()
            pipe = make_pipeline(ColumnSelector(cols=cols), buildMLPClassifier())
            list_base_classifiers.append(pipe)
        else:
            list_base_classifiers.append(buildMLPClassifier())
    for i in range(0,10):
        if selectFeatures :
            cols = genareatedRandomFeatures()
            pipe = make_pipeline(ColumnSelector(cols=cols), buildComplementNBClassifier())
            list_base_classifiers.append(pipe)
        else:
            list_base_classifiers.append(buildComplementNBClassifier())


createStackingHeterogeneus_MLP_NB(selectFeatures=True)

print(' -------------- run stacking heterogeneous -------------- ')
for i in range(len(list_base_classifiers)):
    print( list_base_classifiers[i] )


#
# Define the ensemble classifier with its base classifiers
#
sclf = StackingClassifier(list_base_classifiers, meta_classifier=buildKNNClassifier())
scores = cross_val_score(sclf, df, classes, cv=KFold(n_splits=10), scoring='accuracy')

print("[%s] Accuracy: %0.16f (+/- %0.16f) " % ('StackingClassifier', scores.mean(), scores.std() ) )
