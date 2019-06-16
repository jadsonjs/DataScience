
#
# This program is distributed without any warranty and it
# can be freely redistributed for research, classes or private studies,
# since the copyright notices are not removed.
#
# This code Calculates the unsupervised model *** Hierarchical Agglemerative ***
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
from sklearn.cluster import AgglomerativeClustering
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

# remove the class because is unsupervisor
df = df.drop(columns="diagnosis")



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
  log_file = open('agglomerative-DBs.txt', 'w+')
  log_file.write('k,DB_1\n')
  for k in dbsIndexes.keys():
    log_file.write('{},{}\n'.format(k, dbsIndexes[k][0]))
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
  log_file = open('agglomerative-silhouettesIndexes.txt', 'w+')
  log_file.write('k,silhouette_1\n')
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
  log_file = open('agglomerative-CRs.txt', 'w+')
  log_file.write('k,CR_1\n')
  for k in crsIndexes.keys():
    log_file.write('{},{}\n'.format(k, crsIndexes[k][0]))
  log_file.close()



#########################   Experiment of Check Point 2  #########################
# As in k-means, experiments will be performed with the number of groups ranging from 2 to 20. 
# Since this is a deterministic algorithm, it is necessary to perform only one execution of 
# the algorithm by k, calculating in the sequence the same indexes discussed previously. 
# Also, create the same graphs shown in section 2.1.1, 
# and finally define the best number of groups for the three indexes.

for k in range(2, 21):
  silhouettesIndexes[k] = []
  dbsIndexes[k] = []
  crsIndexes[k] = []
  for i in range(0, k):
    silhouettesIndexes[k].insert(i, [])
  algorithm = AgglomerativeClustering(n_clusters=k, linkage='average')
  predictions = algorithm.fit_predict(df)
  calcSilhouettesIndexes(predictions, k)
  calcDBsIndexes(predictions, k)
  calcCRsIndexes(predictions, k)

printSilhouettesIndexesToFile()
printDBsIndexesToFile()
printCRsIndexesToFile()