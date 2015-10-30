from sklearn import linear_model
from sklearn import tree
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.lda import LDA
from sklearn import metrics
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


def runClassifier( clf,featureMat,targets,no_of_training_example,imageName):
	try:
		clf.fit(featureMat[:no_of_training_example,:], targets[:no_of_training_example])
		pred = clf.predict(featureMat[no_of_training_example:,:])
		# Compute confusion matrix
		cm = confusion_matrix(targets[no_of_training_example:], pred)
		print cm
		#Show confusion matrix in a separate window
		plt.matshow(cm)
		plt.title('Confusion matrix')
		plt.colorbar()
		plt.ylabel('True label')
		plt.xlabel('Predicted label')
		plt.savefig(imageName+'.jpg')
	except Exception, e:	
		print e
	return;


def callAllClassifiers(featureMat,targets,counter):
	size = 70;
	for x in range(0, 3):
		size += 5;
		no_of_training_example = size*counter/100;
		print 'The confusion matrix is MultinomialNB:- '
		clf = MultinomialNB(alpha=.01)
		runClassifier(clf,featureMat,targets,no_of_training_example,str(size)+'mnb');


		print 'The confusion matrix for k-nn:- '
		n_neighbors = 10
		clf = neighbors.KNeighborsClassifier(n_neighbors, 'distance')
		runClassifier(clf,featureMat,targets,no_of_training_example,str(size)+'knn');


		print 'The confusion matrix for SVM:- '
		clf = svm.SVC()
		runClassifier(clf,featureMat,targets,no_of_training_example,str(size)+'svm');

		print 'The confusion matrix for LDA:- '
		clf = LDA()
		runClassifier(clf,featureMat,targets,no_of_training_example,str(size)+'lda');

		print 'The confusion matrix for Decision Tree:- '
		clf = tree.DecisionTreeClassifier()
		runClassifier(clf,featureMat,targets,no_of_training_example,str(size)+'dt');


		print 'The confusion matrix for Logistic Regression:- '
		clf = linear_model.LogisticRegression()
		runClassifier(clf,featureMat,targets,no_of_training_example,str(size)+'lr');


