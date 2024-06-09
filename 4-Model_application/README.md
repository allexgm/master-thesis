## 4-MODEL_APPLICATION_STEP
[All the scripts available are self-explanatory, explaining what it does in the header and some comments through the code]

In this step, I used the developed model to predict the LI of 4 bio-systems of biochemical interest. This application shows the usefulness of this FFNN model and its limitations.

The methodology followed are the same as in the validation step: Obtain the geometries (this case, optimized with Gaussian), get the 'wfn' file with a SP, calculate the desired property (LI in this case) and compare the obtained results
Additionally to this methodology, a representation of the chemical space cover by the database and the location of the different atoms of the studied bio-systems in this representation were done. The technique used is Principal Component Analysis (PCA).
[With "pca-2dim.py" the PCA is applied to a dataset and specific data from different molecules and represented]
[With "molecule_plot_by_value" the atoms from the different bio-systems are shown colored by it error commited]


