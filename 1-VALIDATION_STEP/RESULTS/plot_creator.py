import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------------
# From the "result" files (generated with 'error_calculator.sh') create the plots:
# dispersion graphs for each atom and a s-curve graph with all the systems
#---------------------------------------------------------------------------------

all_files = os.listdir()
result_files = [file for file in all_files if file.startswith("result_")]

#s-curve graph
errors = []
for output in result_files:
    file = open(output)
    next(file)
    text = file.readlines()
    for line in range(len(text)):
        data_line = text[line].split(' ')
        errors.append(float(data_line[3]))
df_errors = pd.DataFrame(errors)
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
print(df_order_errors)
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
plt.scatter(x_axis, y_axis, color='blue', marker='.')
plt.xscale('log')
plt.xlabel('Error (a.u.)')
plt.ylabel('Accumulated percentage of atoms')
plt.savefig('s_curve.png', dpi=1000, bbox_inches='tight')
plt.show()

#dispersion graph
carbon = [[],[]]
hydrogen = [[],[]]
oxygen = [[],[]]
nitrogen = [[],[]]
for output in result_files:
    file = open(output)
    next(file)
    text = file.readlines()
    for line in range(len(text)):
        data_line = text[line].split(' ')
        if text[line].startswith(('C')):
            carbon[0].append(float(data_line[1]))
            carbon[1].append(float(data_line[2]))
        if text[line].startswith(('H')):
            hydrogen[0].append(float(data_line[1]))
            hydrogen[1].append(float(data_line[2]))
        if text[line].startswith(('O')):
            oxygen[0].append(float(data_line[1]))
            oxygen[1].append(float(data_line[2]))
        if text[line].startswith(('N')):
            nitrogen[0].append(float(data_line[1]))
            nitrogen[1].append(float(data_line[2]))

plt.scatter(carbon[0], carbon[1], color='blue', marker='.')
plt.plot(carbon[0], carbon[0], color='red', linestyle='-')
plt.plot(carbon[1], carbon[1], color='red', linestyle='-')
plt.xlim(min(carbon[0]+carbon[1]),max(carbon[0]+carbon[1]))  
plt.ylim(min(carbon[0]+carbon[1]),max(carbon[0]+carbon[1]))  
plt.xlabel('q(r)_ref')
plt.ylabel('q(r)_pred')
plt.savefig('carbon_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()

plt.scatter(hydrogen[0], hydrogen[1], color='blue', marker='.')
plt.plot(hydrogen[0], hydrogen[0], color='red', linestyle='-')
plt.plot(hydrogen[1], hydrogen[1], color='red', linestyle='-')
plt.xlim(min(hydrogen[0]+hydrogen[1]),max(hydrogen[0]+hydrogen[1]))  
plt.ylim(min(hydrogen[0]+hydrogen[1]),max(hydrogen[0]+hydrogen[1]))  
plt.xlabel('q(r)_ref')
plt.ylabel('q(r)_pred')
plt.savefig('hydrogen_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()

plt.scatter(oxygen[0], oxygen[1], color='blue', marker='.')
plt.plot(oxygen[0], oxygen[0], color='red', linestyle='-')
plt.plot(oxygen[1], oxygen[1], color='red', linestyle='-')
plt.xlim(min(oxygen[0]+oxygen[1]),max(oxygen[0]+oxygen[1]))  
plt.ylim(min(oxygen[0]+oxygen[1]),max(oxygen[0]+oxygen[1]))  
plt.xlabel('q(r)_ref')
plt.ylabel('q(r)_pred')
plt.savefig('oxygen_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()

plt.scatter(nitrogen[0], nitrogen[1], color='blue', marker='.')
plt.plot(nitrogen[0], nitrogen[0], color='red', linestyle='-')
plt.plot(nitrogen[1], nitrogen[1], color='red', linestyle='-')
plt.xlim(min(nitrogen[0]+nitrogen[1]),max(nitrogen[0]+nitrogen[1]))  
plt.ylim(min(nitrogen[0]+nitrogen[1]),max(nitrogen[0]+nitrogen[1]))   
plt.xlabel('q(r)_ref')
plt.ylabel('q(r)_pred')
plt.savefig('nitrogen_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()