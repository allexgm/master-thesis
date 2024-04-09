import os
import pandas as pd
import random
import shutil

#-------------------------------------------------------------------------------------------
# From the directory all_trajectories (1 xyz file with 10000 frames per amino acid) create  
# the directory inp_trajectories: 1 dir per aa with [10*natom] frames in different xyz files
#-------------------------------------------------------------------------------------------

if os.path.exists("inp_trajectories"):
    shutil.rmtree("inp_trajectories")
    os.makedirs("inp_trajectories")
else:
    os.makedirs("inp_trajectories")
files = os.listdir("all_trajectories")
for file in files:
    os.makedirs("inp_trajectories/"+file.replace('.xyz','').replace('selected_traj_',''))
    print("Processing:", file)
    text = open("all_trajectories/"+file)
    lines = text.readlines()
    natom = int(lines[0])
    #I want 10*natom xyz frames from the 10000 generated:
    index_list = random.sample(range(9999),10*(natom))
    for ntraj in index_list:
        subtraj = lines[(natom+2)*ntraj+2:(natom+2)*(ntraj+1)]
        with open('inp_trajectories/'+file.replace('.xyz','').replace('selected_traj_','')+'/traj'+str(ntraj).zfill(4)+file.replace('selected_traj',''),'w') as inp:
            inp.writelines(subtraj)
