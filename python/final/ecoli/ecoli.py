import numpy as np
import urllib
import sys
sys.path.insert(0, '../')
import classifier_functions
#URL
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/ecoli/ecoli.data'
#download the file
raw_data = urllib.urlopen(url)
vectors=[]
labels=[]
end = 8
counter = 0
count_excluded = 0


#  cp  (cytoplasm)                                    143 --0
#  im  (inner membrane without signal sequence)        77 --1              
#  pp  (perisplasm)                                    52 --2
#  imU (inner membrane, uncleavable signal sequence)   35 --3
#  om  (outer membrane)                                20 --4
#  omL (outer membrane lipoprotein)                     5 --5 
#  imL (inner membrane lipoprotein)                     2 --6
#  imS (inner membrane, cleavable signal sequence)      2 --7
for row in raw_data:
	row = row.rstrip()
	row_data = row.split(' ')

	row_data = [x for x in row_data if x != '']
	
	for index,x in enumerate(row_data):
		if 'ECOLI' in x:
			row_data.remove(x)
		if 'cp' in x:
			row_data[index] = '0';
		elif'im' in x:
			row_data[index] = '1';
		elif'pp' in x:
			row_data[index] = '2';
		elif'imU' in x:
			row_data[index] = '3';
		elif'om' in x:
			row_data[index] = '4';
		elif'omL' in x:
			row_data[index] = '5';
		elif'imL' in x:
			row_data[index] = '6';
		elif'imS' in x:
			row_data[index] = '7';
			
		x = x.strip()
	# print row_data	
	rowvector = row_data[0: end -1]
	label = row_data[end - 1]
	# print label
	rowvector = np.array(rowvector);
	try:
		counter = counter + 1
		rowvector = rowvector.astype(np.float)
		vectors.append(rowvector)
		labels += label
	except ValueError:
		count_excluded += 1
		# print "OOps!!" 


featureMat = np.array(vectors)
targets = np.array(labels, dtype=float)

classifier_functions.callAllClassifiers(featureMat,targets,counter)

