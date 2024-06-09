## 3-TRAIN_FFNN_STEP
[All the scripts available are self-explanatory, explaining what it does in the header and some comments through the code]

In this step, I develop the FFNN with NNAIMGUI and MM2SF for the prediction of the Localization Index (LI) using the aforementioned database.

To develop the FFNN model, the purposed methodology is:


## Build the ACSFs to describe the chemical space ("1-ACSFs")
In my case, first I used the same xyz files as in the database for the creation of the ACSFs ("same_db_as_training" folder) but checking the results, a poor description of the trios NNN and OOO was founded. <br>
By this I decided to boost this trios (and all the geometries in general) adding more geometries with this trios (and geometries per amoni acid) in is atomic structure ("db_boost_trios" folder). <br>
[With "radial.py" and "angular.py" the two and three body components respectively will be calculated with MM2SF code which applies GMM for and optimal unsupervised selection of parameters] <br>
[With "1-all_traj2buffed_traj.py" the dataset boosting the NNN and OOO trios will be created from a directory with all the selected geometries in the MDs] <br>

## Find the best combination of hyperparameters ("2-Benchmarking")
The hyperparameters values that I decided to test are: learning rate (0.01, 0.001 and 0.0001), optimizer algorithm (RMSProp and Adam), number of hidden layers (2, 3, 4), number of neurons per layer (5, 10, 15) and the activation function (ReLU, SELU and tanh).
[With "benchmarking" for each combination of hyperparameters candidates it training a model with a fraction of the database]

## Analyze the preformance of the final model ("3-Model_performance")
With the resulting as the best combination of hyperparameters a training with the whole database is performed. And with dispersion graphs and s-curves its performace can be measured.
[With "pro_plot_final_model" the same outputs as with "pro_plot_creator" are obtined but split by training and test subsets]

