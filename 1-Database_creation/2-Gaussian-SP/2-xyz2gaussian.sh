#!/bin/bash
#script to create from each xyz file of each molecule a gaussian input to perform:
#SP at M06-2X/def2TZVP generating a wfn file (wavefunction datafile)

cd inp_trajectories
mols=$(ls)
for mol in $mols
do 
cd $mol
files=$(ls *xyz)
for file in $files; do
  name=$(ls $file|sed 's/.xyz//g')
  echo '#'p m062X def2TZVP output=wfn > $name'.com' 
  echo ' ' >> $name'.com'
  echo "$name".wfn >> $name'.com'
  echo ' ' >> $name'.com'
  echo 0 1 >> $name'.com'
  cat $file >> $name'.com'
  echo ' ' >> $name'.com'
  echo "$name".wfn >> $name'.com'
done
cd '/home/alejandro/wd/train_FFNN_step/2-Gaussian-SP/inp_trajectories'
done
cd ..

