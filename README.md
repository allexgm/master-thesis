# Master-thesis
The thesis document itself is the pdf file called "Alejandro_Garcia-Master_Thesis.pdf"\\
[Too see in detail each step, check the "README.md" files in each directory]

## 1-Database_creation
For the steps (2) and (3) a database of geometries is needed. For both cases, the same database was created, and its main scripts and methodology are grouped in the directory "1-Database_creation".

## 2-NNAIMQ_re-validation
In this second step, the NNAIMGUI code with the pre-built model implemented to predict the partial charges (NNAIMQ) of each atom from a xyz given file is appied to the created database in order to comprobe its applicability and accuracy. Its main scripts and methodology are grouped in the directory "2-NNAIMQ_re-validation".

## 3-FFNN_model_development
In this third step, the FFNN model for the prediction of the Localization Index (LI) is developed. To achieve this, the aforementioned database an the NNAIMGUI and MM2SF codes were used. Its main scripts and methodology are grouped in the directory "3-FFNN_model_development".

## 4-Model_application
In this fourth step, the model developed for LI prediction is applied to four bio-systems of biochemical interest in order to show its applicability and limitations. Its main scripts and methodology are grouped in the directory "4-Model-application"
