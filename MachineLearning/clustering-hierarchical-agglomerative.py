
#
# This program is distributed without any warranty and it
# can be freely redistributed for research, classes or private studies,
# since the copyright notices are not removed.
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

#########################   Silhouettes   #########################

silhouettes = {}
def calcSilhouettes(preds, k):
  # Compute the silhouette scores for each instance
  sample_silhouette_values = silhouette_samples(df, preds)
  #iterate over clusters numbers
  clusters = np.unique(preds)
  avg = 0
  for c_i in clusters:
    #getting silhouette of ith cluster
    avg += sample_silhouette_values[preds == c_i].mean()
  avg = avg / clusters.size
  silhouettes[k].append(avg)

def printSilhouettes():
  log_file = open('agglomerative-silhouettes.txt', 'w+')
  log_file.write('k,silhouette_1\n')
  for k in silhouettes.keys():
    v = ','.join(map(str, silhouettes[k]))
    log_file.write('{},{}\n'.format(k, v))
  log_file.close()


#########################   Davies-Bouldin   #########################

dbs = {}
def calcDBs(preds, k):
  db = davies_bouldin_score(df, preds)
  dbs[k].append(db)

def printDBs():
  log_file = open('agglomerative-DBs.txt', 'w+')
  log_file.write('k,DB_1\n')
  for k in dbs.keys():
    log_file.write('{},{}\n'.format(k, dbs[k][0]))
  log_file.close()

#########################   Adjusted Rand   #########################

crs = {}
def calcCRs(preds, k):
  cr = adjusted_rand_score(gtruth, preds)
  crs[k].append(cr)

def printCRs():
  log_file = open('agglomerative-CRs.txt', 'w+')
  log_file.write('k,CR_1\n')
  for k in crs.keys():
    log_file.write('{},{}\n'.format(k, crs[k][0]))
  log_file.close()



#########################   Experiment of Check Point 2  #########################
# As in k-means, experiments will be performed with the number of groups ranging from 2 to 20. 
# Since this is a deterministic algorithm, it is necessary to perform only one execution of 
# the algorithm by k, calculating in the sequence the same indexes discussed previously. 
# Also, create the same graphs shown in section 2.1.1, 
# and finally define the best number of groups for the three indexes.

for k in range(2, 21):
  silhouettes[k] = []
  dbs[k] = []
  crs[k] = []
  for i in range(0, k):
    silhouettes[k].insert(i, [])
  algorithm = AgglomerativeClustering(n_clusters=k, linkage='average')
  predictions = algorithm.fit_predict(df)
  calcSilhouettes(predictions, k)
  calcDBs(predictions, k)
  calcCRs(predictions, k)

printSilhouettes()
printDBs()
printCRs()