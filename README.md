# Master-thesis

## 1-VALIDATION_STEP
In the validation step, the NNAIMGUI code with the default FFNN inplemented to predict the partial charges of each atom from a xyz given file is appied to a selected group of molecules in order to comprobe the aplicability of this method. To do this, the predicted results was compared with the obtained with the QTAIM-based AIMQB program 

- Initial geometries: geometries of the main candidates amino acids to be used for the project with a "list" with the finally selected in xlm and xyz formats.
- NNAIMGUI-results: Obtained outputs with NNAIMGUI (.nnaim files), python script to extract the results and print in a proper format (nnaimgui_properties_extractor.ipynb / .py) and the three results files (.csv) for each molecule: for the charge, for the localization index and for the delocalization index of every atom.
- wfn: Intermediate files generated for the QTAIM properties calculation with Gaussian given to AIMQB as input.
- aimqb-results: output files (sum_files) of AIMQB, python script to extract the results and print in a proper format (aimqb_properties_extractor.ipynb / .py) and the three result files (.csv) for each molecule in three different directories: for charge, localization index and delocalization index of every atom.
- RESULTS: Dispersion plots for each atom and s-curve (.png) and the python script used to create it (plot_creator.ipynb / .py).

