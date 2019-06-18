#/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from random import randint, seed
from time import time

filter_values = {'kg': 0.5, 'Error Estimate': 2, 'Error Measurement': 4, 'Estimate': 0, 'Previous Estimate': 0, 'Error Estimate': 2, 'Previous Error Estimate': 2}
seed(time())

def kalman_filter(measurement):
    filter_values['kg'] = filter_values['Error Estimate'] / (filter_values['Error Estimate'] + filter_values['Error Measurement'] )
    filter_values['Estimate'] = filter_values['Previous Estimate'] + filter_values['kg']*(measurement - filter_values['Previous Estimate'])
    filter_values['Error Estimate'] = (1 - filter_values['kg']) * filter_values['Previous Error Estimate']
    filter_values['Previous Estimate'], filter_values['Previous Error Estimate'] = filter_values['Estimate'], filter_values['Error Estimate']

    return filter_values['Estimate']


measurement_line = plt.plot([c for c in np.arange(0,100.1, 0.1)], [randint(-1, 1) for c in np.arange(0,100.1, 0.1)], label='Measurement')
desired_line = plt.plot([c for c in np.arange(0,100.1, 0.1)], [kalman_filter(element) for element in measurement_line[0].get_data()[1].tolist()], label='Kalman Filter output')

plt.xlabel("Time")
plt.ylabel("Units")
plt.title("Measurement vs Kalman filter")
 
with open('output.txt', 'w')  as f: 
    ax = plt.gca()
    line = ax.lines[0]
    output = ""
    output_list = [measurement_line[0].get_data()[1].tolist(), desired_line[0].get_data()[1].tolist()]
    for c in range(0,len(output_list[0])):
        output += "Measurement = %f,\tKalman Filter = %f\n" % (output_list[0][c], output_list[1][c])
         
    f.write(output)

plt.legend()
plt.show()
