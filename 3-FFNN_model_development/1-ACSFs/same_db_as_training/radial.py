import MM2SF as mm2sf
from MM2SF.radial import *
mm2sf_radial.radial_selector_tailormade(trjname="./all_final_geometries.xyz",nbins=1000, 
			nmax=15,max_iter=10000,bw=None,smooth='no',rcut=7.0,trj_step=5, 
                        cut_type='hard',ndecomp=1,over_thres=0.005,aux="no",new_format=False)
