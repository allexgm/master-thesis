#!/bin/bash
# Calculate the error, for each geometry, in the NNAIMGUI predictions
# with respect to the reference method (AIMQB) and save it in a file


geoms=$(basename -s _charge.csv -a ../aimqb-results/charge/*csv)
for geom in $geoms
do
	paste ../aimqb-results/charge/$geom'_charge.csv' ../NNAIMGUI-results/$geom'_charge_nnaim.csv' | tr -d "\r" | awk '{ err=$2-$4; if (err<0) {err=-err} print $1,$2,$4,err}' | sed 's/Atom Charge Charge 0/#Atom q(r)_ref q(r)_pred Error(|ref-pred|)/g' > result_$geom
done

