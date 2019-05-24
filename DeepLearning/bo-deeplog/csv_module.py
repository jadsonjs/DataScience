
'''
Federal University of Rio Grande do Norte

Prepare the log data for input in the deep learning



csv_module.py
create at 28/05/2018

'''
import csv 
import sys

import numpy as np

'''
This if the function that read the csv file with the log to train the neural network

csv_file_name: the name of the csv file
columns: the columns of the csv file that will be returning
'''
def load_csv_data(csv_file_name, included_cols):
	
	data = []

	with open(csv_file_name) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=';')
		for row in readCSV:
			for col in included_cols:
				data.append(row[col])		

	#print(data)    	
	return data


def load_csv_data2(csv_file_name):
	
	data = []

	with open(csv_file_name) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=';')
		for row in readCSV:
			data.append(row)
	#print(data)    	
	return data	


'''
   write the data pre processed to the temp file 
'''
def save_csv_data(csv_file_name, cvs_data, qtd_feature):

    with open(csv_file_name,'w') as resultFile:
    	wr = csv.writer(resultFile, delimiter=';', dialect='excel')

    	qtd_rows =  int( len(cvs_data) / qtd_feature)
    	for row_number in range( qtd_rows ):
    		row = []
    		for column_number in range( qtd_feature ):
    			row.append( cvs_data[   (row_number * qtd_feature ) + column_number] )

    		wr.writerow(row)



'''
  LOAD ALL traning files data and return in one big array
'''
def load_traning_files(training_directory, samples):
	
	data = []

	for sample in range( 1, samples+1 ):

		with open( training_directory+'/'+'training_norm_'+str(sample)+'.csv' ) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=';')
			for row in readCSV:
				data.append(row)
		#print(data)    	
	
	return data


'''
  LOAD ALL traning output files data and return in one big array
'''
def load_traning_output_files(training_directory, samples):
	
	data = []

	for sample in range( 1, samples+1 ):

		with open( training_directory+'/'+'y_training_'+str(sample)+'.csv' ) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=';')
			for row in readCSV:
				data.append(row)
	
	return data



'''
  LOAD ALL traning files data and return in one big array
'''
def load_test_files(test_directory, samples):
	
	data = []

	for sample in range( 1, samples+1 ):

		with open( test_directory+'/'+'test_norm_'+str(sample)+'.csv' ) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=';')
			for row in readCSV:
				data.append(row)
		#print(data)    	
	
	return data


'''
  LOAD ALL traning output files data and return in one big array
'''
def load_test_output_files(test_directory, samples):
	
	data = []

	for sample in range( 1, samples+1 ):

		with open( test_directory+'/'+'y_test_'+str(sample)+'.csv' ) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=';')
			for row in readCSV:
				data.append(row)
	
	return data




'''
  LOAD ALL traning files data and return in one big array
'''
def load_validation_files(validation_directory, samples):
	
	data = []

	for sample in range( 1, samples+1 ):

		with open( validation_directory+'/'+'test_norm_'+str(sample+200)+'.csv' ) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=';')
			for row in readCSV:
				data.append(row)
		#print(data)    	
	
	return data


'''
  LOAD ALL traning output files data and return in one big array
'''
def load_validation_output_files(validation_directory, samples):
	
	data = []

	for sample in range( 1, samples+1 ):

		with open( validation_directory+'/'+'y_test_'+str(sample+200)+'.csv' ) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=';')
			for row in readCSV:
				data.append(row)
	
	return data



'''
  LOAD ALL test files data and return in one big array 
'''
def load_execution_files(execution_directory, sample_number):
	
	data = []

	#for sample in range( sample_number, samples+1 ):

	with open( execution_directory+'/'+'xtest_norm_1_'+str(sample_number)+'.csv' ) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=';')
		for row in readCSV:
			data.append(row)
		#print(data)    	
	
	return data




'''
  LOAD ALL test values files data (or labels)  and return in one big array

def load_test_output_files(training_directory):
	
	data = []

	with open( training_directory+'/'+'ytest_1'+'.csv' ) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			data.append(row)
	#print(data)    	
	
	return data
'''
