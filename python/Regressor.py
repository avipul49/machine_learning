import pylab as pl
from sklearn import linear_model
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn import tree
from sklearn import linear_model
from sklearn import gaussian_process
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import explained_variance_score
from sklearn.metrics import explained_variance_score
from sklearn import datasets, linear_model
import numpy as np
from sklearn.preprocessing import PolynomialFeatures


def runRegressor( clf,featureMat,targets,no_of_training_example ):
	try:
		clf.fit(featureMat[:no_of_training_example,:], targets[:no_of_training_example])
		y_pred = clf.predict(featureMat[no_of_training_example:,:])
		print 'Variance Score'
		print explained_variance_score(targets[no_of_training_example:], y_pred)
		print 'Mean absolute error'
		print mean_absolute_error(targets[no_of_training_example:], y_pred)
		print 'Explained variance score'
		print explained_variance_score(targets[no_of_training_example:], y_pred)
	except Exception, e:	
		print e
	return;


def callAllRegressor(featureMat,targets,counter):
	no_of_training_example = 0.75*counter
	print 'Result for Linear Regression:- '
	clf = linear_model.LinearRegression()
	runRegressor(clf,featureMat,targets,no_of_training_example);


	print 'Result for Decision Tree Regression:- '
	clf = tree.DecisionTreeRegressor()
	runRegressor(clf,featureMat,targets,no_of_training_example);


	print 'Result for Bayesian Linear Regression:- '
	clf = linear_model.BayesianRidge()
	runRegressor(clf,featureMat,targets,no_of_training_example);

	print 'Result for Exponential Regression:- '
	poly = PolynomialFeatures(degree=2)
	featureMat = poly.fit_transform(featureMat)
	runRegressor(clf,featureMat,targets,no_of_training_example);
	