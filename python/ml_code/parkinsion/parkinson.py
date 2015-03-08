from sklearn import datasets, linear_model
import numpy as np
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
park_file = open('parkinsons_updrs.data', 'r');

b = []
x = list((line.split(',') for line in park_file))
motor_UPDRS_list = []
total_UPDRS_list = [] 
for attribute in x:
	 total_UPDRS_list.append(attribute[5])
	 motor_UPDRS_list.append(attribute[4])

for val in x:
	del val[4]
	del val[5]

##Split into training and test
input_train = x[:-20]
input_test = x[-20:]
motor_train = motor_UPDRS_list[:-20] #target
motor_test = motor_UPDRS_list[-20:]
total_train = total_UPDRS_list[:-20] #target
total_test = total_UPDRS_list[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()


# Train the model using the training sets
print 'MOTOR'
regr.fit(np.array(input_train).astype(float), np.array(motor_train).astype(float))
y_pred = regr.predict(np.array(input_test).astype(float))
print type(y_pred)
cm = confusion_matrix(np.array(motor_test).astype(int), y_pred.astype(int))

print(cm)

# Show confusion matrix in a separate window
plt.matshow(cm)
plt.title('Confusion matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()
print 'TOTAL'
regr.fit(np.array(input_train).astype(float), np.array(total_train).astype(float))
print regr.predict(np.array(input_test).astype(float))
