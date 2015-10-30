import numpy as np
import sys
sys.path.insert(0, '../')
import Regressor

data = open('forestfires.csv', 'r')

row_list = list(line.split(',') for line in data)

output_list = list(row[12] for row in row_list)
monthDict = {"jan": "01","feb":"02" ,"mar": "03", "apr":"04", "may":"05", "jun":"06", "jul":"07", "aug":"08", "sep":"09", "oct":"10", "nov":"11", "dec":"12"}

daysDict = {"mon":"01", "tue":"02", "wed":"03", "thu":"04", "fri":"05", "sat":"06","sun":"07"}
for row in row_list:
	del row[12]
	row[2] = monthDict[row[2]]
	row[3] = daysDict[row[3]]



Regressor.callAllRegressor(np.array(row_list).astype(float), np.array(output_list).astype(float), len(row_list))