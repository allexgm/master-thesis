import os
from ase import Atoms, units
from ase.md import Langevin  #, VelocityVerlet, Andersen
from ase.io import read, write
from xtb.ase.calculator import XTB

#----------------------------------------------------------------------------------------+
# Code to run the MD with ASE using as starting geometry the xyz file in this directory  |
#----------------------------------------------------------------------------------------+

# Read xyz file
mol = os.path.basename(os.getcwd()) 
atoms = read(str(mol)+'.xyz')
atoms.calc = XTB(method='GFN1-xTB',electronic_temperature=900)

# Configurate the MD
#-->Clasical Verlet
#dyn = VelocityVerlet(atoms, timestep=0.02 * units.fs, trajectory='str(mol)+.traj', logfile='str(mol)+.log')
#-->Andersen (NVT ensemble)
#dyn = Andersen(atoms, 0.05 * units.fs, 600, 0.10, trajectory='str(mol)+.traj') 
#                                           ^^^^ with this probability atoms get
#                                                assigned random v components
#-->Langevin (NVT ensemble)
dyn = Langevin(atoms, 1 * units.fs, temperature_K=900, friction=0.1 / units.fs, trajectory=str(mol)+'.traj') 

n_steps = 50000
dyn.run(n_steps)


