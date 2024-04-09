#!/bin/bash
#script to run the ASE MD, transform the output traj file in xyz format and split it ind one xyz file per geometry
#==> Needs: "run_md.py", "xyz_splitter_jumping.py" and a xyz file 

mol=$(basename "$PWD")

rm traj_$mol'.xyz' $mol'.traj' 
python run_md.py
python traj2xyz.py
python xyz_splitter_jumping.py
