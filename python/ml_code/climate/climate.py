import numpy as np
import urllib
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn import svm
from decimal import *

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
	print len(row_data)
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
			print "OOps!!" 


no_of_training_example = 0.8 * counter
featureMat = np.array(vectors)
print 'length of training example'
print no_of_training_example
print 'feature matrix length'
print len(vectors)
for x in labels:
	print x
targets = np.array(labels).astype(np.float)
clf = svm.SVC(gamma=0.001, C=100.)#MultinomialNB(alpha=.01)
#print featureMat[:2,:]
clf.fit(featureMat[:no_of_training_example,:], targets[:no_of_training_example])

print clf.predict(featureMat[no_of_training_example:,:])
print 'No of rows excluded !! ' 
print  count_excluded
