## 1-Database_creation
[All the scripts available are self-explanatory, explaining what it does in the header and some comments through the code]

In order to re-validate the NNAIMQ model and to develop the new model to predict the location index, a set of geometries whose QTAIM properties are known is needed. It was chosen to use for both cases the same dataset of geometries, using their partial charges for the re-validation and their localization indices for the development of the new neural network. With the aim of having systems with a biochemical nature, but small enough to be able to build a sufficiently large dataset, it was decided to take as a starting point from among the well-known "20 essential amino acids" the 18 that have only C, H, O or N atoms (without S): Alanine (A), Arginine (R), Aspargine (N), Aspartic acid (D), Glutamic acid (E), Glutamine (Q), Glycine (G), Histidine (H), Isoleucine (I), Leucine (L), Lysine (K), Phenylalanine (F), Proline (P), Serine (S), Threonine (T), Tryptophan (W), Tyrosine (Y) and Valine (V). The general structure of each amino acid are avilable in the "initial_geometries" directory.

For these molecules, different geometries must be generated in order to conform to the database.


## Select the method to generate the geometries ("0-test-alanine")
To create geometries as input for the model two options will be considered: Normal Mode Sampling (NMS) and Molecular Dynamics (MD). In this step, in my case, I took the alanine molecule to compare the results obtained with both methods. <br>
All this step was used to justify why I chose MD as the more effective method to generate geometries.

## Run the MD ("1-MD")
For each amino-acid I run a MD at GFN1-xTB theory level with Langevin dynamics.<br>
[With "run_md.py" script the MD with ASE code will be performed for a given xyz file] <br>
[With "traj2xyz.py" script the traj file output will be transformed into a xyz file] <br>
[With "xyz_splitter_jumping.py" a xyz file with multiple geometries will be splitted in xyz files every some frames] <br>
[With "md_simulation.sh" script "run_md.py","traj2xyz.py" and "xyz_splitter_jumping.py" codes are executed in this directory] <br>
[With "1-multi_MD.sh" script the "md_simulation.sh" will be performed for each amino-acid grouping the results in a directory]

## Calculate its LIs at QTAIM level of theory ("2-Gaussian-SP" + "3-aimqb")
From the selected geometries I run a SP (single-point) calculation with Gaussian generating a 'wfn' file for each one.After, using this 'wfn' files as input, a QTAIM calculation were performed with AIMQB package, obtaining the QTAIM properties for each atom in each geometry. <br>
[With "1-all_traj2inp_traj.py" script from all the files in "all_trajectories" '10*natom' geometries are chosen randomly and saved in different xyz files] <br>
[With "2-xyz2gaussian.sh" script for each xyz file generated before it creates a gaussian input to perform the SP calculation] <br>
[With "aimqb.sh" script from the 'wfn' files generated with Gaussian it run the AIMQB calculation for all of them] <br>