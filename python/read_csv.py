

#
# READ a CSV em python
#
#
import csv 
import sys
 
f = open('/home/jadson/Documentos/temp_files/test.csv', 'rt')
reader = csv.reader(f, delimiter=';')
for row in reader:
	print ('row:')
	print (row)
	print ('--- coluns ---')
	for col in row:
		print (col)

	print ('--- read especific column number ---')	
	colnum = 0	
	for col in row:
		print ('reading colum '+str(colnum)+': '+row[colnum])
		colnum += 1	
 
f.close()