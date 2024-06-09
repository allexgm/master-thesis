#!/bin/bash
#script to run the ASE MD, transform the output traj file in xyz format and split it ind one xyz file per geometry
#==> Needs: "run_md.py", "xyz_splitter_jumping.py" and (in my case) "alanine.xyz"

rm traj_alanine.xyz alanine.traj 
python3 run_md.py
ase convert alanine.traj traj_alanine.xyz
python3 xyz_splitter_jumping.py
awk '{print $1,$2,$3,$4}' selected_traj_alanine.xyz > tmp && mv tmp selected_traj_alanine.xyz
