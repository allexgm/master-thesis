import os
import pandas as pd

#------------------------------------------------------------------------------------
# For each nnaim file (NNAIMGUI output) extract the charge of each atom in a csv file
#------------------------------------------------------------------------------------

all_files = os.listdir()
nnaim_files = [file for file in all_files if file.endswith(".nnaim")]
charge=[['Atom','Charge']] # atom_name + atom_charge
for output in nnaim_files:
    file = open(output)
    text = file.readlines()
    line = 0
    while True:
        line+=1
        if text[line+1].startswith(' #'):
            break
        data_line = text[line].split()
        charge.append([str(data_line[1])+str(data_line[0]),float(data_line[2])]) 
    df_charge = pd.DataFrame(charge)
    df_charge.to_csv(output[:-6]+'_charge_nnaim.csv', sep=' ', index=False, header=False)
    charge = [charge[0]]
    print('Properties extracted from "'+output+'" file')
print('All done!')
