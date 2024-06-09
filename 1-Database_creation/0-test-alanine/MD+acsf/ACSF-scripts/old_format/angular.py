import MM2SF as mm2sf
import os
import psutil

def set_cpu_num(num_processors):
    """
    Limit the number of CPUs
    """
    pid = os.getpid()
    p = psutil.Process(pid)
    available_cpus = psutil.cpu_count(logical=False)

    if num_processors > available_cpus:
        print(f"Error: Requested {num_processors} processors, but only {available_cpus} available.")
        return

    cpu_affinity = list(range(num_processors))
    p.cpu_affinity(cpu_affinity)
    print(f"Script restricted to {num_processors} processor(s): {cpu_affinity}")
    return None

set_cpu_num(20)

from MM2SF.angular import *
mm2sf_angular.angular_selector(trjname="./selected_traj_alanine.xyz", rcut=4, nbins=500, trj_step=10, nmax=20, max_iter=100000000,
             cv_type='full', gmm_crit="bicconv", afrac=1, percbic=30, percdiff=40,new_format=False)
