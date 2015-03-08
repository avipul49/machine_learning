import numpy as np
import urllib
import sys
sys.path.insert(0, '../')
import classifier_functions
#URL
handwriting_file = open('optdigits-orig.windep', 'r+')
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
		if number_count % 33 == 0:
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

featureMat = np.array(vectors)
targets = np.array(labels, dtype=float)

classifier_functions.callAllClassifiers(featureMat,targets,feature_count)

