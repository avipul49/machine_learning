import numpy as np
import sys
sys.path.insert(0, '../')
import Regressor
data = open('yacht_hydrodynamics.data', 'r')

row_list = []

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
	if len(line_list) != 7:
		print line_list
	row_list.append(line_list)

output_list = list(row[6] for row in row_list)

Regressor.callAllRegressor(np.array(row_list).astype(float), np.array(output_list).astype(float), len(row_list))