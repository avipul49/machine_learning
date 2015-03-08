import numpy as np
import urllib
import sys
sys.path.insert(0, '../')
import classifier_functions
#URL
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
#download the file
raw_data = urllib.urlopen(url)
vectors=[]
labels=[]
end = 11
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
