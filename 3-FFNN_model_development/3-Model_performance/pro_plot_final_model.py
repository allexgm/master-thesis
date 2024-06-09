import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------------
# From the "result" files (generated with 'error_calculator.sh') create the plots:
# dispersion graphs and scurve for all the atoms and split byb atom, in both cases 
# separating between training and test subsets.
#---------------------------------------------------------------------------------

all_files = os.listdir()
pred_files = [file for file in all_files if file.endswith("_pred")]
#plt.rcParams['font.style'] = 'italic'
plt.rcParams['font.size'] = 16
#s-curve graph
#errors = []
#for output in result_files:
#    file = open(output)
#    next(file)
#    text = file.readlines()
#    for line in range(len(text)):
#        data_line = text[line].split(' ')
#        errors.append(float(data_line[3]))
#df_errors = pd.DataFrame(errors)
#df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
#x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
#y_axis = []
#for x_num in x_axis:
#    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
#plt.scatter(x_axis, y_axis, color='blue', marker='.')
#plt.xscale('log')
#plt.xlabel("Error [au]")
#plt.ylabel("Accumulated percentage of atoms")
#plt.savefig('s_curve.png', dpi=1000, bbox_inches='tight')
#plt.show()
#plt.clf()
#

##dispersion graph
train_c = [[],[],[]]
train_h = [[],[],[]]
train_o = [[],[],[]]
train_n = [[],[],[]]
test_c = [[],[],[]]
test_h = [[],[],[]]
test_o = [[],[],[]]
test_n = [[],[],[]]
for output in pred_files:
    file = open(output)
    next(file)
    next(file)
    next(file)
    next(file)
    text = file.readlines()
    for line in range(len(text)):
        data_line = text[line].split(',')
        if output.startswith("model_C.train"):
            train_c[0].append(float(data_line[0]))
            train_c[1].append(float(data_line[1]))
            train_c[2].append(abs(float(data_line[0])-float(data_line[1])))
        if output.startswith("model_C.test"):
            test_c[0].append(float(data_line[0]))
            test_c[1].append(float(data_line[1]))
            test_c[2].append(abs(float(data_line[0])-float(data_line[1])))
        if output.startswith("model_H.train"):
            train_h[0].append(float(data_line[0]))
            train_h[1].append(float(data_line[1]))
            train_h[2].append(abs(float(data_line[0])-float(data_line[1])))
        if output.startswith("model_H.test"):
            test_h[0].append(float(data_line[0]))
            test_h[1].append(float(data_line[1]))
            test_h[2].append(abs(float(data_line[0])-float(data_line[1])))
        if output.startswith("model_O.train"):
            train_o[0].append(float(data_line[0]))
            train_o[1].append(float(data_line[1]))
            train_o[2].append(abs(float(data_line[0])-float(data_line[1])))
        if output.startswith("model_O.test"):
            test_o[0].append(float(data_line[0]))
            test_o[1].append(float(data_line[1]))
            test_o[2].append(abs(float(data_line[0])-float(data_line[1])))
        if output.startswith("model_N.train"):
            train_n[0].append(float(data_line[0]))
            train_n[1].append(float(data_line[1]))
            train_n[2].append(abs(float(data_line[0])-float(data_line[1])))
        if output.startswith("model_N.test"):
            test_n[0].append(float(data_line[0]))
            test_n[1].append(float(data_line[1]))
            test_n[2].append(abs(float(data_line[0])-float(data_line[1])))

plt.scatter(train_c[1], train_c[0], color='black', marker='.',label='train C atoms')
plt.scatter(test_c[1], test_c[0], color='red', marker='.', alpha=0.4, label='Test C atoms')
plt.plot(train_c[0], train_c[0], color='red', linestyle='-')
plt.plot(train_c[1], train_c[1], color='red', linestyle='-')
plt.plot(test_c[0], test_c[0], color='red', linestyle='-')
plt.plot(test_c[1], test_c[1], color='red', linestyle='-')
plt.xscale('linear')
plt.xlim(min(train_c[0]+train_c[1]+test_c[0]+test_c[1]),max(train_c[0]+train_c[1]+test_c[0]+test_c[1]))  
plt.ylim(min(train_c[0]+train_c[1]+test_c[0]+test_c[1]),max(train_c[0]+train_c[1]+test_c[0]+test_c[1]))  
plt.xlabel(r'$LI(r)_{ref}$ [au]')
plt.ylabel(r'$LI(r)_{pred}$ [au]')
plt.legend()
plt.savefig('carbon_li_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

plt.scatter(train_h[1], train_h[0], color='#AAAAAA', marker='.',label='Train H atoms')
plt.scatter(test_h[1], test_h[0], color='red', marker='.', alpha=0.4, label='Test H atoms')
plt.plot(train_h[0], train_h[0], color='red', linestyle='-')
plt.plot(train_h[1], train_h[1], color='red', linestyle='-')
plt.plot(test_h[0], test_h[0], color='red', linestyle='-')
plt.plot(test_h[1], test_h[1], color='red', linestyle='-')
plt.xscale('linear')
plt.xlim(min(train_h[0]+train_h[1]+test_h[0]+test_h[1]),max(train_h[0]+train_h[1]+test_h[0]+test_h[1]))  
plt.ylim(min(train_h[0]+train_h[1]+test_h[0]+test_h[1]),max(train_h[0]+train_h[1]+test_h[0]+test_h[1]))  
plt.xlabel(r'$LI(r)_{ref}$ [au]')
plt.ylabel(r'$LI(r)_{pred}$ [au]')
plt.legend()
plt.savefig('hydrogen_li_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

plt.scatter(train_o[1], train_o[0], color='brown', marker='.',label='Train O atoms')
plt.scatter(test_o[1], test_o[0], color='red', marker='.', alpha=0.4, label='Test O atoms')
plt.plot(train_o[0], train_o[0], color='red', linestyle='-')
plt.plot(train_o[1], train_o[1], color='red', linestyle='-')
plt.plot(test_o[0], test_o[0], color='red', linestyle='-')
plt.plot(test_o[1], test_o[1], color='red', linestyle='-')
plt.xscale('linear')
plt.xlim(min(train_o[0]+train_o[1]+test_o[0]+test_o[1]),max(train_o[0]+train_o[1]+test_o[0]+test_o[1]))  
plt.ylim(min(train_o[0]+train_o[1]+test_o[0]+test_o[1]),max(train_o[0]+train_o[1]+test_o[0]+test_o[1]))  
plt.xlabel(r'$LI(r)_{ref}$ [au]')
plt.ylabel(r'$LI(r)_{pred}$ [au]')
plt.legend()
plt.savefig('oxygen_li_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

plt.scatter(train_n[1], train_n[0], color='blue', marker='.',label='Train N atoms')
plt.scatter(test_n[1], test_n[0], color='red', marker='.', alpha=0.4, label='Test N atoms')
plt.plot(train_n[0], train_n[0], color='red', linestyle='-')
plt.plot(train_n[1], train_n[1], color='red', linestyle='-')
plt.plot(test_n[0], test_n[0], color='red', linestyle='-')
plt.plot(test_n[1], test_n[1], color='red', linestyle='-')
plt.xscale('linear')
plt.xlim(min(train_n[0]+train_n[1]+test_n[0]+test_n[1]),max(train_n[0]+train_n[1]+test_n[0]+test_n[1]))  
plt.ylim(min(train_n[0]+train_n[1]+test_n[0]+test_n[1]),max(train_n[0]+train_n[1]+test_n[0]+test_n[1]))  
plt.xlabel(r'$LI(r)_{ref}$ [au]')
plt.ylabel(r'$LI(r)_{pred}$ [au]')
plt.legend()
plt.savefig('nitrogen_li_dispersion.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

df_errors = pd.DataFrame(train_c[2])
df_errors_test = pd.DataFrame(test_c[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
df_order_errors_test = pd.DataFrame(df_errors_test.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
y_axis_test = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
    y_axis_test.append((df_errors_test.iloc[:,0] < x_num).mean() * 100)
    print('Atom C')
    print(x_num,y_axis_test[-1])
plt.plot(x_axis, y_axis, color='black', lw=5, label='Train C atoms')
plt.plot(x_axis, y_axis_test, color='red', lw=5, ls='--', alpha=0.8, label='Test C atoms')
plt.xscale('log')
plt.xlabel("Error [au]")
plt.ylabel("Accumulated % of C atoms")
plt.legend()
plt.savefig('s_curve_li_carbon.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

df_errors = pd.DataFrame(train_h[2])
df_errors_test = pd.DataFrame(test_h[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
df_order_errors_test = pd.DataFrame(df_errors_test.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
y_axis_test = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
    y_axis_test.append((df_errors_test.iloc[:,0] < x_num).mean() * 100)
    print('Atom H')
    print(x_num,y_axis_test[-1])
plt.plot(x_axis, y_axis, color='#AAAAAA', lw=5, label='Train H atoms')
plt.plot(x_axis, y_axis_test, color='red', lw=5, ls='--', alpha=0.8, label='Test H atoms')
plt.xscale('log')
plt.xlabel("Error [au]")
plt.ylabel("Accumulated % of H atoms")
plt.legend()
plt.savefig('s_curve_li_hydrogen.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

df_errors = pd.DataFrame(train_o[2])
df_errors_test = pd.DataFrame(test_o[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
df_order_errors_test = pd.DataFrame(df_errors_test.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
y_axis_test = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
    y_axis_test.append((df_errors_test.iloc[:,0] < x_num).mean() * 100)
    print('Atom O')
    print(x_num,y_axis_test[-1])
plt.plot(x_axis, y_axis, color='brown', lw=5, label='Train O atoms')
plt.plot(x_axis, y_axis_test, color='red', lw=5, ls='--', alpha=0.8, label='Test O atoms')
plt.xscale('log')
plt.xlabel("Error [au]")
plt.ylabel("Accumulated % of O atoms")
plt.legend()
plt.savefig('s_curve_li_oxygen.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

df_errors = pd.DataFrame(train_n[2])
df_errors_test = pd.DataFrame(test_n[2])
df_order_errors = pd.DataFrame(df_errors.iloc[:, 0].sort_values())
df_order_errors_test = pd.DataFrame(df_errors_test.iloc[:, 0].sort_values())
x_axis = np.logspace(np.log10(0.00005), np.log10(0.5), num=1000)
y_axis = []
y_axis_test = []
for x_num in x_axis:
    y_axis.append((df_errors.iloc[:,0] < x_num).mean() * 100)
    y_axis_test.append((df_errors_test.iloc[:,0] < x_num).mean() * 100)
    print('Atom N')
    print(x_num,y_axis_test[-1])
plt.plot(x_axis, y_axis, color='blue', lw=5, label='Train N atoms')
plt.plot(x_axis, y_axis_test, color='red', lw=5, ls='--', alpha=0.8, label='Test N atoms')
plt.xscale('log')
plt.xlabel("Error [au]")
plt.ylabel("Accumulated % of N atoms")
plt.legend()
plt.savefig('s_curve_li_nitrogen.png', dpi=1000, bbox_inches='tight')
plt.show()
plt.clf()

