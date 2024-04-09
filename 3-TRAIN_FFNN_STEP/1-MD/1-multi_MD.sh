#!/bin/bash
#script to run the "md_simulation.sh" script over all the amino acids in different directories.
#Moreover it creates "all_trajectories" a directory with all the selected geometries of each system
#==> Needs: "md_simulation.sh" and its requered files 

for mol in glycine  histidine  isoleucine  leucine  lysine  phenylalanine  proline  serine  threonine  tryptophan  tyrosine  valine
do
mkdir $mol
cp $mol'.xyz' md_simulation.sh run_md.py traj2xyz.py xyz_splitter_jumping.py $mol
cd $mol
./md_simulation.sh
cd ..
done
rm -rf all_trajectories
mkdir all_trajectories
cp */selected_traj* all_trajectories 
