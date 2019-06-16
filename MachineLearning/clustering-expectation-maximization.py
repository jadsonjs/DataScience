
#
# This program is distributed without any warranty and it
# can be freely redistributed for research, classes or private studies,
# since the copyright notices are not removed.
#
# This code Calculates the unsupervised model ***Expecation Maximization***
#
# Jadson Santos - jadsonjs@gmail.com
# base on: alexlimatds - https://github.com/alexlimatds/doctorate_machine_learning
# 
# to run this exemple install pyhton modules:
#
# pip3 install scikit-learn
# pip3 install pandas
# pip3 install numpy
#


import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_samples, davies_bouldin_score, adjusted_rand_score

#
# DEFINE YOUR DATASET HERE, ALREADY PRE PROCESSED ! 
#
# read the CSV file with your data base and put into a Pandas DataFrame 
# https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/
#
df = pd.read_csv('/Users/jadson/tmp/WDBC_preprocessed.csv')


#Getting ground truth
gtruth = df['diagnosis']



#########################   Davies-Bouldin   #########################

# keep the final indexes the will be save to a file
dbsIndexes = {}

# calc DB index using
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html
def calcDBsIndexes(preds, k):
  db = davies_bouldin_score(df, preds)
  dbsIndexes[k].append(db)

# salve in a file the DB indexes
def printDBsIndexesToFile():
  log_file = open('em-DBs.txt', 'w+')
  log_file.write('k,DB_1,DB_2,DB_3,DB_4,DB_5\n')
  for k in dbsIndexes.keys():
    v = ','.join(map(str, dbsIndexes[k]))
    log_file.write('{},{}\n'.format(k, v))
  log_file.close()




#########################   silhouettesIndexes   #########################

# keep the final indexes the will be save to a file
silhouettesIndexes = {}

# calc silhouette index using
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html
def calcSilhouettesIndexes(preds, k):
  # Compute the silhouette scores for each instance
  sample_silhouette_values = silhouette_samples(df, preds)
  #iterate over clusters numbers
  clusters = np.unique(preds)
  avg = 0
  for c_i in clusters:
    #getting silhouette of ith cluster
    avg += sample_silhouette_values[preds == c_i].mean()
  avg = avg / clusters.size
  silhouettesIndexes[k].append(avg)

# salve in a file the silhouttes indexes
def printSilhouettesIndexesToFile():
  log_file = open('em-silhouettesIndexes.txt', 'w+')
  log_file.write('k,silhouette_1,silhouette_2,silhouette_3,silhouette_4,silhouette_5\n')
  for k in silhouettesIndexes.keys():
    v = ','.join(map(str, silhouettesIndexes[k]))
    log_file.write('{},{}\n'.format(k, v))
  log_file.close()





#########################   Adjusted Rand   #########################

# keep the final indexes the will be save to a file
crsIndexes = {}

# calc CR index using
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html
def calcCRsIndexes(preds, k):
  cr = adjusted_rand_score(gtruth, preds)
  crsIndexes[k].append(cr)

# salve in a file the CR indexes
def printCRsIndexesToFile():
  log_file = open('em-CRs.txt', 'w+')
  log_file.write('k,CR_1,CR_2,CR_3,CR_4,CR_5\n')
  for k in crsIndexes.keys():
    v = ','.join(map(str, crsIndexes[k]))
    log_file.write('{},{}\n'.format(k, v))
  log_file.close()
  


#########################   Experiment of Check Point 2  #########################
# we will make experiments with k varying from 2 to 20. 
# Because it is a method with initialization, for each value of k, 5 executions will be made 
# (varying the value of the seed). After the experiments, the three indices will 
# be calculated for all generated partitions (built-up clusters).

for k in range(2, 21):
  silhouettesIndexes[k] = []
  dbsIndexes[k] = []
  crsIndexes[k] = []
  for i in range(1, 6):
    algorithm = GaussianMixture(n_components=k, init_params='random')
    predictions = algorithm.fit_predict(df)
    calcSilhouettesIndexes(predictions, k)
    calcDBsIndexes(predictions, k)
    calcCRsIndexes(predictions, k)

printSilhouettesIndexesToFile()
printDBsIndexesToFile()
printCRsIndexesToFile()