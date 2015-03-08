from sklearn import tree
from sklearn import linear_model
from sklearn.gaussian_process import GaussianProcess
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import explained_variance_score
from sklearn.metrics import explained_variance_score
from sklearn import datasets, linear_model
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
data = open('forestfires.csv', 'r')

row_list = list(line.split(',') for line in data)

output_list = list(row[12] for row in row_list)
monthDict = {"jan": "01","feb":"02" ,"mar": "03", "apr":"04", "may":"05", "jun":"06", "jul":"07", "aug":"08", "sep":"09", "oct":"10", "nov":"11", "dec":"12"}

daysDict = {"mon":"01", "tue":"02", "wed":"03", "thu":"04", "fri":"05", "sat":"06","sun":"07"}
for row in row_list:
	del row[12]
	row[2] = monthDict[row[2]]
	row[3] = daysDict[row[3]]

x_train = row_list[:-20]
poly = PolynomialFeatures(degree=2)
x_train = poly.fit_transform(np.array(x_train).astype(float))
x_target = output_list[:-20]
x_test = row_list[-20:]
x_test = np.array(x_test).astype(float)
x_test = poly.fit_transform(x_test)
x_test_target = output_list[:]
regr = linear_model.LinearRegression()
regr.fit(x_train, np.array(x_target).astype(float))
y_pred = regr.predict(x_test)
regr1 = tree.DecisionTreeRegressor()
regr1.fit(x_train, np.array(x_target).astype(float))
y_pred1 = regr1.predict(x_test)
gp = linear_model.BayesianRidge()
gp.fit(x_train, np.array(x_target).astype(float))
y_pred2 = gp.predict(x_test)
LinearRegr = linear_model.LinearRegression()
LinearRegr.fit(x_train, np.array(x_target).astype(float))
y_pred3 = LinearRegr.predict(x_test)
print 'Exponential Regression'
print 'Decision Tree Regression'
print 'Bayesian Regression'
print 'Linear Regression'
print y_pred
print y_pred1
print y_pred2
print y_pred3
print 'variance score'
print 'Exponential Regression'
print explained_variance_score(np.array(x_target[-20:]).astype(float), y_pred)
print 'Decision Tree Regression'
print explained_variance_score(np.array(x_target[-20:]).astype(float), y_pred1)
print 'Bayesian Regression'
print explained_variance_score(np.array(x_target[-20:]).astype(float), y_pred2)
print 'Linear Regression'
print explained_variance_score(np.array(x_target[-20:]).astype(float), y_pred3)
print 'mean absolute error'
print 'Exponential Regression'
print mean_absolute_error(np.array(x_target[-20:]).astype(float), y_pred)
print 'Decision Tree Regression'
print mean_absolute_error(np.array(x_target[-20:]).astype(float), y_pred1)
print 'Bayesian Regression'
print mean_absolute_error(np.array(x_target[-20:]).astype(float), y_pred2)
print 'Linear Regression'
print mean_absolute_error(np.array(x_target[-20:]).astype(float), y_pred3)

print 'explained variance score'
print 'Exponential Regression'
print explained_variance_score(np.array(x_target[-20:]).astype(float), y_pred)
print 'Decision Tree Regression'
print explained_variance_score(np.array(x_target[-20:]).astype(float), y_pred1)
print 'Bayesian Regression'
print explained_variance_score(np.array(x_target[-20:]).astype(float), y_pred2)
print 'Linear Regression'
print explained_variance_score(np.array(x_target[-20:]).astype(float), y_pred3) 
