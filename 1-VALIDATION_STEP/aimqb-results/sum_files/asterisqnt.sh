#!/bin/bash

for mol in alanine aspartic glutamate histidine lysine phenylalanine serine tryptophan arginine glutamine isoleucine methionine tyrosine aspargine cystine glycine leucine proline threonine valine 
do
for fun in b3lyp m062X pbe0 pbepbe b2plyp 
do

#for bas in def2SVP def2TZVP def2QZVP '6-31G*' '6-311G(d,p)'
#do
mv $mol'_'$fun'_6-31G*.sum' $mol'_'$fun'_6-31G.sum'
#/opt/aimall/17.01.25/bin/aimqb.exe -nogui -nproc=16 $mol'_'$fun'_6-311Gdp.wfn'
#done

done
done
