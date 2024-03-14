#!/bin/bash
#Remove special characters "*" which generates compatibility errors 

for mol in alanine aspartic glutamate histidine lysine phenylalanine serine tryptophan arginine glutamine isoleucine methionine tyrosine aspargine cystine glycine leucine proline threonine valine 
do
for fun in b3lyp m062X pbe0 pbepbe b2plyp 
do

mv $mol'_'$fun'_6-31G*.sum' $mol'_'$fun'_6-31G.sum'

done
done
