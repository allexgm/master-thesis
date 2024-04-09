import os

#---------------------------------------------------------------------------------------+
# Code to split a xyz file with multiple geometries in xyz files, one for each geometry |
#---------------------------------------------------------------------------------------+

# Obtain the name of the molecule from the current directory
mol = os.path.basename(os.getcwd())

file = open("traj_"+str(mol)+".xyz")
text = file.readlines()
natom = int(text[0])
trajs = len(text) // (natom+2) 
nstep = 5 #select 1 geometry each 'natom' geometries

# Iterate through trajs and write each to a separate file
output = f'selected_traj_{mol}.xyz'
with open(output, 'w'):
    pass
for i in range(trajs):
    if i % nstep == 0:
        subgeom = text[i * (natom+2): (i + 1) * (natom+2)]
        with open(output, 'a') as file:
            file.writelines(subgeom)
print('All done !')
