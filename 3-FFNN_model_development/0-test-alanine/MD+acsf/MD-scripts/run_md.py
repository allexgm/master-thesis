from ase import Atoms, units
from ase.io import read, write
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet, Andersen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Lee el archivo XYZ
atoms = read('test.xyz')
MaxwellBoltzmannDistribution(atoms, temperature_K=600)
atoms.calc = EMT()

# Configura la dinámica molecular
#-->Clasical Verlet
#dyn = VelocityVerlet(atoms, timestep=0.02 * units.fs, trajectory='alanine.traj', logfile='alanine.log')
#-->NVT ensemble
dyn = Andersen(atoms, 0.05 * units.fs, 600, 0.1, trajectory='alanine.traj') 

n_steps = 50000
dyn.run(n_steps)


