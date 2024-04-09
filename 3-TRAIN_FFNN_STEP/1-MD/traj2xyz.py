import os
from ase.io import read, write

#-------------------------------------------------------+
# Code to transform the traj output file in xyz format  |
#-------------------------------------------------------+
# Replace '*traj_file_prefix*' with the prefix of your .traj file (without extension)
#         ( in my case I use "mol" = directory name )
# Replace '*output_xyz_file.xyz*' with the desired name for the output .xyz file

def traj_to_xyz(traj_file_prefix, *output_xyz_file*):

   # Read the trajectory file
    traj = read(traj_file_prefix + '.traj', format='traj', index=":")
    # Write all frames to a single .xyz file
    write(*output_xyz_file*, traj, format='xyz')

mol = os.path.basename(os.getcwd())
traj_to_xyz(str(mol), 'traj_'+str(mol)+'.xyz')

