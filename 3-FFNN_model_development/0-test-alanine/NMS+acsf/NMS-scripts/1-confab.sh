#!/bin/bash
#script to obtain conformers for the 18 selected amino acids from its xyz files in different directories.

for mol in alanine aspartic glycine leucine proline tryptophan arginine glutamate histidine lysine serine tyrosine aspargine glutamine isoleucine phenylalanine threonine valine
do
  mkdir $mol
  cp xyz/$mol'.xyz' $mol
  cd $mol
  obabel $mol'.xyz' -O confs_$mol'.xyz' --confab
  cd ..
done

