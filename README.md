# Master-thesis

## 1-VALIDATION_STEP
In the validation step, the NNAIMGUI code with the default FFNN inplemented to predict the partial charges of each atom from a xyz given file is appied to a selected group of molecules in order to comprobe the aplicability of this method. To do this, the predicted results was compared with the obtained with the QTAIM-based AIMQB program.

## 2-HF_PORTION_STEP
In this step, I modify the HF contribution in the B3LYP functional to study the relation between the percentage used and the error committed in the prediction of QTAIM properties.

- aimqb-results: same structure as in the validation step, but only at B3LYP/def-TZVP level of theory and with different percentage of HF included.
- hf-RESULTS: not jet!

## 3-TRAIN_FFNN_STEP
In this step, I obtain the selected geometries, the ACSFs with MM2SF code and the QTAIM propertie LI (Localization index) first for a test population and after for thw whole selected population of training.
- test_alanine: training steps applied for the alanine molecule. NMS and MD methodologies where compared, looking for the best method to obtain geometries for the training. After, the ASCFs are obtained and the FFNN built with different parameters, optimizing it to get the best results (lowest errors).
- final-geometries: not jet!
