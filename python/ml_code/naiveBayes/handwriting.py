import numpy as np
import urllib
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

#URL
handwriting_file = open('/home/mebin/ml_code/naiveBayes/optdigits-orig.windep', 'r+')
vectors=[]
labels=[]
end = 11
counter = 0
count_excluded = 0
number_count = 0
feature_count = 0
rowvector=[]
for row in handwriting_file:
	counter += 1

	if counter > 21:
			
		row = row.rstrip()

		number_count += 1
		if number_count % 32 == 0:
			feature_count +=1
			label = row
			rowvector = np.array(rowvector)			
			rowvector = rowvector.astype(np.float)
			vectors.append(rowvector)
			rowvector = []
			labels.append(label)
		else:
		
		#label = row_data[end - 1]
		#rowvector = np.array(rowvector);
			try:
				counter = counter + 1
				#rowvector = rowvector.astype(np.float)
				#vectors.append(rowvector)
				#labels += label
			except ValueError:
				count_excluded += 1
				print "OOps!!"
			

			rowvector.append(row.split('\n')[0])


			



#print 'The input vector is ' 
#for vector in vectors:
	#print 'The input vector is'
	#print vector
#print 'The labels are'
no_of_training_example = 0.8 * feature_count

featureMat = np.array(vectors)
print featureMat[:no_of_training_example,:]
targets = np.array(labels, dtype=float)
clf = MultinomialNB(alpha=.01)
#no_of_training_example = 2
clf.fit(featureMat[:no_of_training_example,:], targets[:no_of_training_example])

print clf.predict(featureMat[no_of_training_example:,:])
print 'No of rows excluded !! ' 
print  count_excluded
