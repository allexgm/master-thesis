#!/bin/bash
# Calculate the error, for each amino acid, in the NNAIMGUI predictions
# with respect to the reference method (AIMQB) and save it in a file


for mol in alanine glycine proline arginine histidine serine aspargine isoleucine threonine aspartic leucine tryptophan lysine tyrosine glutamate valine glutamine phenylalanine
do
paste reference_method/$mol'_m062X_def2TZVP_charge.csv' NNAIMGUI-results/$mol'_charge_nnaim.csv' | tr -d "\r" | awk '{print $1,$2,$4,$2-$4}' | sed 's/ -/ /g' | sed 's/Atom Charge Charge 0/#Atom q(r)_ref q(r)_pred Error(|ref-pred|)/g' > result_$mol
done
