import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------
# From the "result" files (generated with 'error_calculator.sh') create the plots:
# dispersion graphs and s-curves for all the atoms and split by atom type in all the systems
#-------------------------------------------------------------------------------------------

all_files = os.listdir()
result_files = [file for file in all_files if file.startswith("result_")]
plt.rcParams['font.style'] = 'italic'
plt.rcParams['font.size'] = 12
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
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
plt.scatter(x_axis, y_axis, color='blue', marker='.')
plt.xscale('log')
plt.xlabel("Error (a.u.)")
plt.ylabel("Accumulated percentage of atoms")
plt.savefig('s_curve.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

#dispersion graph
carbon = [[],[],[]]
hydrogen = [[],[],[]]
oxygen = [[],[],[]]
nitrogen = [[],[],[]]
for output in result_files:
    file = open(output)
    next(file)
    text = file.readlines()
    for line in range(len(text)):
        data_line = text[line].split(' ')
        if text[line].startswith(('C')):
            carbon[0].append(float(data_line[1]))
            carbon[1].append(float(data_line[2]))
            carbon[2].append(float(data_line[3]))
        if text[line].startswith(('H')):
            hydrogen[0].append(float(data_line[1]))
            hydrogen[1].append(float(data_line[2]))
            hydrogen[2].append(float(data_line[3]))
        if text[line].startswith(('O')):
            oxygen[0].append(float(data_line[1]))
            oxygen[1].append(float(data_line[2]))
            oxygen[2].append(float(data_line[3]))
        if text[line].startswith(('N')):
            nitrogen[0].append(float(data_line[1]))
            nitrogen[1].append(float(data_line[2]))
            nitrogen[2].append(float(data_line[3]))
            
#C-dispersion
plt.scatter(carbon[0], carbon[1], color='blue', marker='.')
plt.plot(carbon[0], carbon[0], color='red', linestyle='-')
plt.plot(carbon[1], carbon[1], color='red', linestyle='-')
plt.xscale('linear')
plt.xlim(min(carbon[0]+carbon[1]),max(carbon[0]+carbon[1]))  
plt.ylim(min(carbon[0]+carbon[1]),max(carbon[0]+carbon[1]))  
plt.xlabel(r'$q(r)_{ref}$ [au]')
plt.ylabel(r'$q(r)_{pred}$ [au]')
plt.savefig('carbon_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

#H-dispersion
plt.scatter(hydrogen[0], hydrogen[1], color='blue', marker='.')
plt.plot(hydrogen[0], hydrogen[0], color='red', linestyle='-')
plt.plot(hydrogen[1], hydrogen[1], color='red', linestyle='-')
plt.xlim(min(hydrogen[0]+hydrogen[1]),max(hydrogen[0]+hydrogen[1]))  
plt.ylim(min(hydrogen[0]+hydrogen[1]),max(hydrogen[0]+hydrogen[1]))  
plt.xlabel(r'$q(r)_{ref}$ [au]')
plt.ylabel(r'$q(r)_{pred}$ [au]')
plt.savefig('hydrogen_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

#O-dispersion
plt.scatter(oxygen[0], oxygen[1], color='blue', marker='.')
plt.plot(oxygen[0], oxygen[0], color='red', linestyle='-')
plt.plot(oxygen[1], oxygen[1], color='red', linestyle='-')
plt.xlim(min(oxygen[0]+oxygen[1]),max(oxygen[0]+oxygen[1]))  
plt.ylim(min(oxygen[0]+oxygen[1]),max(oxygen[0]+oxygen[1]))  
plt.xlabel(r'$q(r)_{ref}$ [au]')
plt.ylabel(r'$q(r)_{pred}$ [au]')
plt.savefig('oxygen_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

#N-dispersion
plt.scatter(nitrogen[0], nitrogen[1], color='blue', marker='.')
plt.plot(nitrogen[0], nitrogen[0], color='red', linestyle='-')
plt.plot(nitrogen[1], nitrogen[1], color='red', linestyle='-')
plt.xlim(min(nitrogen[0]+nitrogen[1]),max(nitrogen[0]+nitrogen[1]))  
plt.ylim(min(nitrogen[0]+nitrogen[1]),max(nitrogen[0]+nitrogen[1]))   
plt.xlabel(r'$q(r)_{ref}$ [au]')
plt.ylabel(r'$q(r)_{pred}$ [au]')
plt.savefig('nitrogen_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

#C+H+O+N-dispersion
plt.scatter(carbon[0], carbon[1], color='blue', marker='.', label='C atoms')
plt.scatter(hydrogen[0], hydrogen[1], color='grey', marker='+', label='H atoms' )
plt.scatter(nitrogen[0], nitrogen[1], color='brown', marker='x', label='N atoms')
plt.scatter(oxygen[0], oxygen[1], color='orange', marker='*', label='O atoms')
plt.plot([0,10],[0,10], color='red')
plt.xlim(min(carbon[0]+carbon[1]+hydrogen[0]+hydrogen[1]+oxygen[0]+oxygen[1]+nitrogen[0]+nitrogen[1]),max(carbon[0]+carbon[1]+hydrogen[0]+hydrogen[1]+oxygen[0]+oxygen[1]+nitrogen[0]+nitrogen[1]))
plt.ylim(min(carbon[0]+carbon[1]+hydrogen[0]+hydrogen[1]+oxygen[0]+oxygen[1]+nitrogen[0]+nitrogen[1]),max(carbon[0]+carbon[1]+hydrogen[0]+hydrogen[1]+oxygen[0]+oxygen[1]+nitrogen[0]+nitrogen[1]))
plt.xlabel(r'$q(r)_{ref}$ [au]')
plt.ylabel(r'$q(r)_{pred}$ [au]')
plt.legend()
plt.savefig('all_atoms_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

#C-s-curve
df_errors = pd.DataFrame(carbon[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
plt.scatter(x_axis, y_axis, color='blue', marker='.')
plt.xscale('log')
plt.xlabel("Error (a.u.)")
plt.ylabel("Accumulated percentage of carbon atoms")
plt.savefig('s_curve_carbon.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

#H-s-curve
df_errors = pd.DataFrame(hydrogen[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
plt.scatter(x_axis, y_axis, color='blue', marker='.')
plt.xscale('log')
plt.xlabel("Error (a.u.)")
plt.ylabel("Accumulated percentage of hydrogen atoms")
plt.savefig('s_curve_hydrogen.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

#O-s-curve
df_errors = pd.DataFrame(oxygen[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
plt.scatter(x_axis, y_axis, color='blue', marker='.')
plt.xscale('log')
plt.xlabel("Error (a.u.)")
plt.ylabel("Accumulated percentage of oxygen atoms")
plt.savefig('s_curve_oxygen.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

#N-s-curve
df_errors = pd.DataFrame(nitrogen[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
plt.scatter(x_axis, y_axis, color='blue', marker='.')
plt.xscale('log')
plt.xlabel("Error (a.u.)")
plt.ylabel("Accumulated percentage of nitrogen atoms")
plt.savefig('s_curve_nitrogen.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

#C+H+O+N-s-curve
df_errors = pd.DataFrame(carbon[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
plt.plot(x_axis, y_axis, color='blue', lw=3, label='C atoms')

df_errors = pd.DataFrame(hydrogen[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
plt.plot(x_axis, y_axis, color='grey', lw=3, label='H atoms')

df_errors = pd.DataFrame(oxygen[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
plt.plot(x_axis, y_axis, color='orange', lw=3, label='O atoms')

df_errors = pd.DataFrame(nitrogen[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
plt.plot(x_axis, y_axis, color='brown', lw=3, label='N atoms')
plt.xscale('log')
plt.xlabel("Error (a.u.)")
plt.ylabel("Accumulated percentage of each atoms type")
plt.legend()
plt.savefig('s_curve_all_splitted.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()


