# 2-NNAIMQ_re-validation
[All the scripts available are self-explanatory, explaining what it does in the header and some comments through the code]

Once the partial charges have been calculated, the next step is to predict them using the code of NNAIMGUI where the model selected in this case was NNAIMQ. This generates a prediction of the partial charge, which can be compared with the one taken as reference, i.e. the one calculated with AIMQB, in different ways. 

Then, to validate the NNAIMQ model purposed methodology is:


## Extract its charges at QTAIM level of theory ("1-aimqb-results" directory)
From the 'sum' files obtained in the creation of the database, the different charges cab be extrated in a poper format. These values will form the reference results
[With "aimqb_properties_extractor" the QTAIM properties obtained in the 'sum' files can be extracted in a proper format with 'csv' format]

## Predict charges with NNAIMGUI ("2-NNAIMGUI-results directory")
For the generated geometries I predict the QTAIM property using NNAIMGUI (with the default parameters).
[With "nnaimgui_properties_extractor" the QTAIM properties in the obtained 'nnaim' files can be extracted in a proper format with 'csv' format]

## Calculate the errors ("3-RESULTS" directory)
Using the NNAIMGUI results and the reference values (AIMQB results), the error in the prediction can be calculated. To show it, two types of plots were decided to be used: <br>
- Dispersion graphs: Split by atoms, they show how much diverge the predictions with respect to the reference. <br>
- S-curve: Graph that shows the accumulated error depending on the percentage of atoms considered (ordered from lower to higher error). <br>
[With "error_calculator.sh" script the results files can be created from the NNAIMGUI-results and reference_method folders with both types of 'cvs' files for NNAIMGUI and AIMQB respectively] <br>
[With "pro_plot_creator", from the results files (created with "error_calculator.sh") the explained plots can be created for all atoms and split by atom type]

