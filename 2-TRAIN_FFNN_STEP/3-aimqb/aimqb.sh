#!/bin/bash
#Run aimqb calculations of all the wfn files in this path
#==> Needs: All the wfn files obtained in the "Gaussian-SP" step grouped in a directory called "wfn"
#The path for run aimqb is from my specific cluster (check how to run aimqb in your case)

cd wfn
#short by name
files=$(ls *wfn)
#To run in a randon order
#files=$(ls *wfn|shuf) 
for file in $files
do
/opt/aimall/17.01.25/bin/aimqb.exe -nogui -nproc=16 -scp=false -altaprhocps=true -nnat=8 $file
done
cd ..
