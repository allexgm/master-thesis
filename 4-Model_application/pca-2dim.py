import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

#dbdata=['training_db_extended.xyz_C.dtbse', 'training_db_extended.xyz_H.dtbse', 'training_db_extended.xyz_N.dtbse', 'training_db_extended.xyz_O.dtbse']
atom='O'
plt.rcParams['font.size'] = 14
dbdata=['training_db_extended.xyz_'+atom+'.dtbse']

with open('dopa-'+atom+'.dtbse', 'r') as file:
  data_dopa=[]
  for line in file:
    line = line.strip()
    str_values = line.split(',')
    float_values = [float(value) for value in str_values]
    data_dopa.append(float_values)
with open('orni-'+atom+'.dtbse', 'r') as file:
  data_orni=[]
  for line in file:
    line = line.strip()
    str_values = line.split(',')
    float_values = [float(value) for value in str_values]
    data_orni.append(float_values)

with open('hpro-'+atom+'.dtbse', 'r') as file:
  data_hpro=[]
  for line in file:
    line = line.strip()
    str_values = line.split(',')
    float_values = [float(value) for value in str_values]
    data_hpro.append(float_values)

with open('folic-'+atom+'.dtbse', 'r') as file:
  data_folic=[]
  for line in file:
    line = line.strip()
    str_values = line.split(',')
    float_values = [float(value) for value in str_values]
    data_folic.append(float_values)

for db in dbdata:
  with open(db, 'r') as file:
    data=[]
    for line in file:
      line = line.strip()
      str_values = line.split(',')
      float_values = [float(value) for value in str_values]
      data.append(float_values)
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(data)
    dopa_dots=[[],[]]
    orni_dots=[[],[]]
    hpro_dots=[[],[]]
    folic_dots=[[],[]]
    for pos in range(len(data_dopa)):
      data_dopa[pos-1]=np.array(data_dopa[pos-1])
      tmp=pca.transform(data_dopa[pos-1].reshape(1,-1))
      tmp2=str(tmp)
      dopa_dot = tmp2.replace('[', '').replace(']', '').split()
      dopa_dots[0].append(float(dopa_dot[0]))
      dopa_dots[1].append(float(dopa_dot[1]))
    for pos in range(len(data_orni)):
      data_orni[pos-1]=np.array(data_orni[pos-1])
      tmp=pca.transform(data_orni[pos-1].reshape(1,-1))
      tmp2=str(tmp)
      orni_dot = tmp2.replace('[', '').replace(']', '').split()
      orni_dots[0].append(float(orni_dot[0]))
      orni_dots[1].append(float(orni_dot[1]))
    for pos in range(len(data_hpro)):
      data_hpro[pos-1]=np.array(data_hpro[pos-1])
      tmp=pca.transform(data_hpro[pos-1].reshape(1,-1))
      tmp2=str(tmp)
      hpro_dot = tmp2.replace('[', '').replace(']', '').split()
      hpro_dots[0].append(float(hpro_dot[0]))
      hpro_dots[1].append(float(hpro_dot[1]))
    for pos in range(len(data_folic)):
      data_folic[pos-1]=np.array(data_folic[pos-1])
      tmp=pca.transform(data_folic[pos-1].reshape(1,-1))
      tmp2=str(tmp)
      folic_dot = tmp2.replace('[', '').replace(']', '').split()
      folic_dots[0].append(float(folic_dot[0]))
      folic_dots[1].append(float(folic_dot[1]))
    print(folic_dots)
    plt.grid(True)
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c='blue', s=40, alpha=0.5, label='Database')
    plt.scatter(dopa_dots[0], dopa_dots[1], c='purple', edgecolor='k', s=80, marker='s', label='L-DOPA')    
    plt.scatter(orni_dots[0], orni_dots[1], c='green', edgecolor='k',  s=80, marker='^', label='L-ornithine')    
    plt.scatter(hpro_dots[0], hpro_dots[1], c='orange', edgecolor='k', s=100, marker='P', label='L-hydroxyproline')    
    plt.scatter(folic_dots[0], folic_dots[1], c='red', edgecolor='k',  s=130, marker='*', label='Folic acid')    
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    #plt.title(atom+' atom')
    #for O
    plt.legend()
    #for C, H and N
    #plt.legend(loc='upper right')
    plt.savefig(atom+'-pca.png', dpi=300, bbox_inches='tight')
