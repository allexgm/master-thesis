from NNAIMGUI import trainer
import os
import psutil
import shutil
import subprocess
import itertools

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

set_cpu_num(2)


# List of possible values for the parameters
patnc_values = [10,20]
lr_values = [0.01,0.001,0.0001]
optimizers = ['RMSprop','Adam']
##(2 hlayers)
#neurons_configurations = [(5,5),(10,10),(15,15)]
##(3 hlayers)
#neurons_configurations = [(5,5,5),(10,10,10),(15,15,15)]
##(4 hlayers)
neurons_configurations = [(5,5,5,5),(10,10,10,10),(15,15,15)]
activation_functions = ['relu','tanh','selu']

# Generate all the possible combinations of hyperparameters
hyperparameter_combinations = itertools.product(patnc_values,lr_values,optimizers,neurons_configurations,activation_functions)


#xyz2db step        
database=trainer.xyz2dtbase(datafile="bm_geometries.xyz",itype="input.type",rtype="input.rad",atype="input.ang",fsave='yes')

# Iterate over all the possible combinations
for ptnc_v, lr_v, opts, neurons_c, activation_f in hyperparameter_combinations:
    # Create a new folder, move and go there
    new_dir = '/home/alexg/final-models-FFNN/pat'+str(ptnc_v)+'-lr'+str(lr_v)+'-'+str(opts)+'-n'+str(neurons_c)+'-'+str(activation_f)
    os.makedirs(new_dir)
    os.chdir(new_dir)
    # train step
    for elem in set([item[0] for item in database]):
##(3 hlayers)        
        #trainer.train(database=database, elem=elem, ftra=0.8, vsplit=0.2, nepochs=100000, patnc=ptnc_v, lr=lr_v, loss='mse', optimizer=opts, neurons=neurons_c, activations=(activation_f,activation_f,'linear'))
##(2 hlayers)        
        #trainer.train(database=database, elem=elem, ftra=0.8, vsplit=0.2, nepochs=100000, patnc=ptnc_v, lr=lr_v, loss='mse', optimizer=opts, neurons=neurons_c, activations=(activation_f,'linear'))
##(4 hlayers)
        trainer.train(database=database, elem=elem, ftra=0.8, vsplit=0.2, nepochs=100000, patnc=ptnc_v, lr=lr_v, loss='mse', optimizer=opts, neurons=neurons_c, activations=(activation_f,activation_f,activation_f,'linear'))
###--<    for elem in ['C','H','O','N']:
###--<        trainer.train_from_csv(datafile="/home/alexg/final-models-FFNN/bm_geometries.xyz_"+str(elem)+".dtbse", ftra=0.8, vsplit=0.2, nepochs=100000, patnc=ptnc_v, lr=lr_v, loss='mse', optimizer=opts, neurons=neurons_c, activations=(activation_f,activation_f,'linear'))

