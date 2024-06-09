import MM2SF as mm2sf
from MM2SF.angular import *
mm2sf_angular.angular_selector(trjname="./conformer_anti.xyz", rcut=4, nbins=500, trj_step=10, nmax=20, max_iter=100000000,
             cv_type='full', gmm_crit="bicconv", afrac=1, percbic=30, percdiff=40,new_format=False)
