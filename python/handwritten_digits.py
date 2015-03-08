print(__doc__)

from sklearn import linear_model
from sklearn import tree
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.lda import LDA
import numpy as np
from sklearn import tree
from sklearn import svm


fileData = open("forestFire.data","r")

days = {"mon": 1, "tue" : 2, "wed" : 3, "thu" : 4, "fri" : 5, "sat" : 6, "sun": 7} 
months = {"jan": 1, "feb" : 2, "mar" : 3,"apr" : 4 ,"may" : 5, "jun" : 6, "jul" : 7, "aug" : 8, "sep" : 9, "oct" : 10, "nov" : 11, "dec" : 12} 

x = list(row.split(",") for row in fileData)

actual_output = [];

for row in x:
	actual_output.append(float(row[12]))
	row[2] = months[row[2]]
	row[3] = days[row[3]]
	del row[12]

x_train = x[100:]
x_test = x[:100]


output_train = actual_output[100:]
output_test = actual_output[:100]



reg = svm.SVR()
print output_train
reg.fit(np.array(x_train).astype(float),np.array(output_train).astype(float))
output = reg.predict(np.array(x_test).astype(float))

print output
print output_test
