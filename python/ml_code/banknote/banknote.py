import numpy as np
import urllib
from sklearn.lda import LDA
from sklearn import metrics

#URL
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt'
#download the file
raw_data = urllib.urlopen(url)
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
		print "OOps!!" 


no_of_training_example = 0.8 * counter
featureMat = np.array(vectors)
targets = np.array(labels, dtype=float)
clf = LDA()#MultinomialNB(alpha=.01)
#print featureMat[:2,:]
clf.fit(featureMat[:no_of_training_example,:], targets[:no_of_training_example])

print clf.predict(featureMat[no_of_training_example:,:])
print 'No of rows excluded !! ' 
print  count_excluded
