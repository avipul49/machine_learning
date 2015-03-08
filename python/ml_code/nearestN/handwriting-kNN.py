import numpy as np
import urllib
from sklearn import linear_model
from sklearn import tree
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.lda import LDA
from sklearn import metrics
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
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
no_of_training_example = 0.8 * feature_count

featureMat = np.array(vectors)
targets = np.array(labels, dtype=float)

def runClassifier( clf,featureMat,targets,no_of_training_example ):
	clf.fit(featureMat[:no_of_training_example,:], targets[:no_of_training_example])

	pred = clf.predict(featureMat[no_of_training_example:,:])

	# Compute confusion matrix
	cm = confusion_matrix(targets[no_of_training_example:], pred)
	print cm

	# Show confusion matrix in a separate window
	plt.matshow(cm)
	plt.title('Confusion matrix')
	plt.colorbar()
	plt.ylabel('True label')
	plt.xlabel('Predicted label')
	plt.show()
	return;

print 'The confusion matrix is MultinomialNB:- '
clf = MultinomialNB(alpha=.01)
#runClassifier(clf,featureMat,targets,no_of_training_example);


print 'The confusion matrix for k-nn:- '
n_neighbors = 15
clf = neighbors.KNeighborsClassifier(n_neighbors, 'distance')
#runClassifier(clf,featureMat,targets,no_of_training_example);


print 'The confusion matrix for SVM:- '
clf = svm.SVC()
#runClassifier(clf,featureMat,targets,no_of_training_example);

print 'The confusion matrix for LDA:- '
clf = LDA()
#runClassifier(clf,featureMat,targets,no_of_training_example);

print 'The confusion matrix for Decision Tree:- '
clf = tree.DecisionTreeClassifier()
runClassifier(clf,featureMat,targets,no_of_training_example);


print 'The confusion matrix for Logistic Regression:- '
clf = linear_model.LogisticRegression()
runClassifier(clf,featureMat,targets,no_of_training_example);

