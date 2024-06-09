import os
import pandas as pd

#----------------------------------------------------------------------------------------
# For each sum file (from aimqb calculations) in this directory extract the charge,
# the localization index and the delocalization index in three different csv files. 
#----------------------------------------------------------------------------------------

all_files = os.listdir()
sum_files = [file for file in all_files if file.endswith(".sum")]
charge=[['Atom','Charge']] # atom_name + atom_charge
loc=[['Atom','Loc_index']] # atom_name + delocation_index
deloc=[['Atom(A)','Atom(B)','Deloc_index']] # atom_A + atom_B + delocation_index_AB
for output in sum_files:
    file = open(output)
    text = file.readlines()
    for line in range(len(text)):
         if text[line].startswith(('Atom A          q(A)              L(A)')): # ~charge
                i=1
                while True:
                    i+=1
                    if text[line+i].startswith('---'):
                        break
                    data_line = text[line+i].split()
                    charge.append([data_line[0],float(data_line[1])])
         
         if text[line].startswith(('Atom A          N(A)             LI(A)            %Loc(A)')): # ~loc
                i=1
                while True:
                    i+=1
                    if text[line+i].startswith('---'):
                        break
                    data_line = text[line+i].split()
                    loc.append([data_line[0],float(data_line[2])])
        
         if text[line].startswith(('Atom A    Atom B       2*D2(A,B)          DI(A,B)')): # ~deloc
                i=1
                while True:
                    i+=1
                    if text[line+i].startswith(' '):
                        break
                    data_line = text[line+i].split()
                    deloc.append([data_line[0],data_line[1],float(data_line[3])])
    df_charge = pd.DataFrame(charge)
    df_loc = pd.DataFrame(loc)
    df_deloc = pd.DataFrame(deloc)
    df_charge.to_csv(output[:-4]+'_charge.csv', sep=' ', index=False, header=False)
    df_loc.to_csv(output[:-4]+'_loc.csv', sep=' ', index=False, header=False)
    df_deloc.to_csv(output[:-4]+'_deloc.csv', sep=' ', index=False, header=False)
    charge = [charge[0]]
    loc = [loc[0]]
    deloc = [deloc[0]]
    print('Properties extracted from "'+output+'" file')
print('All done !')
