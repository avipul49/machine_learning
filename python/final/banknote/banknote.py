import numpy as np
import urllib
import sys
sys.path.insert(0, '../')
import classifier_functions
#URL
#download the file
raw_data = open('data.txt', 'r+')
vectors=[]
labels=[]
end = 5
counter = 0
count_excluded = 0
for row in raw_data:
	row = row.rstrip()
	row_data = row.split(',')
	rowvector = row_data[0: end -1]
	label = row_data[end - 1]
	rowvector = np.array(rowvector);
	try:
		counter = counter + 1
		rowvector = rowvector.astype(np.float)
		vectors.append(rowvector)
		labels += label
	except ValueError:
		count_excluded += 1


featureMat = np.array(vectors)
targets = np.array(labels, dtype=float)

classifier_functions.callAllClassifiers(featureMat,targets,counter)

