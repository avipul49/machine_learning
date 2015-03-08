import numpy as np
import urllib
import sys
sys.path.insert(0, '../')
import classifier_functions

#URL
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00252/pop_failures.dat'
file_dataset = open('dataset.txt', 'r')
#download the file
raw_data = urllib.urlopen(url)
vectors=[]
labels=[]
end = 20
counter = 0
count_excluded = 0
for row in file_dataset:
	row = row.rstrip()
	row_data = row.split(' ')
	# print len(row_data)
	if len(row_data) == 20:
		rowvector = row_data[0: end -1]
		label = row_data[end - 1]
		rowvector = np.array(rowvector);
		try:
			rowvector = np.array(rowvector)
			rowvector = rowvector.astype(np.complex128)
			#rowvector = rowvector.astype(np.float64)
			vectors.append(rowvector)
			labels +=  label
			counter = counter + 1
		except ValueError:
			count_excluded += 1
			# print "OOps!!" 


featureMat = np.array(vectors)
targets = np.array(labels).astype(np.float)

classifier_functions.callAllClassifiers(featureMat,targets,counter)


