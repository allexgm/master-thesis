# 1-VALIDATION_STEP
In the validation step, the NNAIMGUI code with the default FFNN inplemented to predict the partial charges of each atom from a xyz given file is appied to a selected group of molecules in order to comprobe the aplicability of this method. To do this, the predicted results was compared with the obtained with the QTAIM-based AIMQB program.

To validate the NNAIMGUI code the purposed methodology is:

## Chose a set of molecules ("pdb" directory)
In my case I took 18 esential amino-acids availables from PDB in 'xml' format, transformin it in 'xyz' format using openbabel.

## Optimize its geometries 
In my case I did it with Gaussian at M06-2X/def-TZVP level of theory.

## Predict its charge with NNAIMGUI ("NNAIMGUI-results directory")
For the optimized geometries I predict the QTAIM property using NNAIMGUI (with the default parameters).
[With "nnaimgui_properties_extractor" the QTAIM properties in the 'nnaim' files can be extracted in a proper format with 'csv' format]

## Calculate its charges at QTAIM level of theory ("aimqb-results" directory)
From the optimized geometries I run a SP (single-point) calculation with Gaussian generating a 'wfn' file for different combinations of functional and basis. After, using this 'wfn' files as input, a QTAIM calculation were performed with AIMQB package, obtaining the QTAIM properties for each atom in each system at the different levels of theory. (the results obtained with M06-2X/def-TZVP are considered the "reference method" in our case).
[With "aimqb_properties_extractor" the QTAIM properties in the 'sum' files can be extracted in a proper format with 'csv' format]

## Calculate the errors ("RESULTS" directory)
Using the NNAIMGUI results and the reference method, the error in the prediction can be calculated. To show it, two types of plots were dcided to be used:
- Dispersion graphs: Split by atoms, they show how much diverge the predictions with respect to the reference.
- S-curve: Graph that shows the accumulated error depending on the percentage of atoms considered.
[With "error_calculator.sh" script the results files can be created from the NNAIMGUI-results and reference_method folders]
[With "plot_creator", from the results files (created with "error_calculator.sh") the explained plots can be created]

