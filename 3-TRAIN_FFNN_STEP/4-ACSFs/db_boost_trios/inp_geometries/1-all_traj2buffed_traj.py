import os
import random
import shutil

#-----------------------------------------------------------------------------------------------------------+
# Code to create a database of geometries for the ACSFs with more molecules including the trios NNN and OOO |
#==> Needs: "all_trajectories" directory created in "MD" step                                               | 
#-----------------------------------------------------------------------------------------------------------+

if os.path.exists("buff_trajectories"):
    shutil.rmtree("buff_trajectories")
    os.makedirs("buff_trajectories")
else:
    os.makedirs("buff_trajectories")
# Obtener la lista de archivos en la carpeta de entrada
files = os.listdir("all_trajectories")
# Iterar sobre cada archivo
for file in files:
    atom_name = file.replace('.xyz','').replace('selected_traj_','')
    os.makedirs("buff_trajectories/"+atom_name)
    # Hacer algo con cada archivo
    # Por ejemplo, imprimir el nombre del archivo
    print("Processing:", file)
    text = open("all_trajectories/"+file)
    lines = text.readlines()
    natom = int(lines[0])
    #I want 10*natom xyz frames from the 10000 generated:
    #Nevetheless, I want to buff the NNN and OOO trios in the database !!!
    if atom_name in ['histidine','aspartic','glutamate']:
        index_list =random.sample(range(9999),60*(natom))
    elif atom_name in ['arginine','aspargine','serine','glutamine','threonine','tyrosine']:
        index_list =random.sample(range(9999),40*(natom))
    else:
        index_list = random.sample(range(9999),20*(natom))
    for ntraj in index_list:
        subtraj = lines[(natom+2)*ntraj:(natom+2)*(ntraj+1)]
        with open('buff_trajectories/'+atom_name+'/traj'+str(ntraj).zfill(4)+file.replace('selected_traj',''),'w') as inp:
            inp.writelines(subtraj)
