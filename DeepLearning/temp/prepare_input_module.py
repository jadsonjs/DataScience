

''' 
    prepare the log data fo the input of LSTM deep network
    
    We have this information:
    157610555	16	2017-10-27T09:12:30.0179Z	https://sigeventos.ufrn.br/eventos/menu.xhtml 6	 FALSE

    And we wants to format like this

    0,000122 0,0333	0,02030234234234 0,00032423404234234234324323 0,3

    for the input network
    
    @author jadsonjs@gmail.com
'''


from csv_module import load_csv_data
from csv_module import save_csv_data
from hash_module import textual_hash
from hash_module import date_milliseconds
from normalization_module import normalize_feature
from array_module import reshape_input




def prepareLSTMdata(raw_data_file_name, deep_network_file_name, features_indexes):

	qtd_features = len(features_indexes)

	# load just the feature located in this possition on cvs file
	cvs_raw_data = load_csv_data(raw_data_file_name, features_indexes)

	print('### 1 ###')
	print(cvs_raw_data)

	# converte the url to numeric value
	cvs_numeric_data = textual_hash(cvs_raw_data, 3, qtd_features)
	
	# converte the date to numeric value
	cvs_numeric_data = date_milliseconds(cvs_numeric_data, 2, qtd_features)
    
	print('### 2 ###')
	print(cvs_numeric_data)

	cvs_normalized_data = []
    
	for feature in range( len(cvs_numeric_data) ):
		cvs_normalized_data = normalize_feature(cvs_numeric_data, feature, qtd_features)

	print('### 3 ###')
	print(cvs_normalized_data)
	

	save_csv_data(deep_network_file_name, cvs_normalized_data, qtd_features)






