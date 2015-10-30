import numpy as np
import sys
sys.path.insert(0, '../')
import Regressor

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

# Train the model using the training sets
print 'MOTOR'
Regressor.callAllRegressor(np.array(x).astype(float), np.array(motor_UPDRS_list).astype(float), len(x))
print 'TOTAL'
Regressor.callAllRegressor(np.array(x).astype(float), np.array(total_UPDRS_list).astype(float), len(x))
