from sklearn import tree
import re
from sklearn import datasets, linear_model
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
data = open('yacht_hydrodynamics.data', 'r')

row_list = []#list(line.split(' ') for line in data)
pattern = re.compile(r"\s+")

#string_without_whitespace = pattern.sub("", string_with_whitespace)
for line in data:
	line = line.strip()
	line_list = line.split(' ')
	index = -1
	for l in line_list:
		index += 1
		
		if l == ' ':
			del line_list[index]
		if l == '':
			del line_list[index]
	line_list[index] = line_list[index].rstrip() 
#	print len(line_list)
	if len(line_list) != 7:
		print line_list
	row_list.append(line_list)
	#print row_list
#print row_list[5]
#row_list=list(row.rstrip() for row in row_list)
output_list = list(row[6] for row in row_list)
#monthDict = {"jan": "01","feb":"02" ,"mar": "03", "apr":"04", "may":"05", "jun":"06", "jul":"07", "aug":"08", "sep":"09", "oct":"10", "nov":"11", "dec":"12"}

#daysDict = {"mon":"01", "tue":"02", "wed":"03", "thu":"04", "fri":"05", "sat":"06","sun":"07"}
#for row in row_list:
	#print row
	#print row[6]
#	del row[6]
#	row[2] = monthDict[row[2]]
#	row[3] = daysDict[row[3]]

x_train = row_list[:-20]
#poly = PolynomialFeatures(degree=2)
#x_train = poly.fit_transform(np.array(x_train).astype(float))
x_target = output_list[:-20]
x_test = row_list[-20:]
#x_test = np.array(x_test).astype(float)
#x_test = poly.fit_transform(x_test)
print len(x_train)
print len(x_target)
x_test_target = output_list[-20:]
regr = tree.DecisionTreeRegressor()
#print x_train
regr.fit(np.array(x_train).astype(float), np.array(x_target).astype(float))
y_pred = regr.predict(np.array(x_test).astype(float))
print y_pred
print output_list[-20:]
