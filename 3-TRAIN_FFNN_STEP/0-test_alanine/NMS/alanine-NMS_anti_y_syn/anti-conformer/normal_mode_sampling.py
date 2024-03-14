#!/usr/bin/env python3

from __future__ import print_function

import sys
import numpy as np
from copy import deepcopy

import cclib

from cclib.parser import ccopen

NAME = {
    1:  'H'  , 
    2:  'He' , 
    3:  'Li' , 
    4:  'Be' , 
    5:  'B'  , 
    6:  'C'  , 
    7:  'N'  , 
    8:  'O'  , 
    9:  'F'  , 
   10:  'Ne' , 
   11:  'Na' , 
   12:  'Mg' , 
   13:  'Al' , 
   14:  'Si' , 
   15:  'P'  , 
   16:  'S'  , 
   17:  'Cl' , 
   18:  'Ar' , 
   19:  'K'  , 
   20:  'Ca' , 
   21:  'Sc' , 
   22:  'Ti' , 
   23:  'V'  , 
   24:  'Cr' , 
   25:  'Mn' , 
   26:  'Fe' , 
   27:  'Co' , 
   28:  'Ni' , 
   29:  'Cu' , 
   30:  'Zn' , 
   31:  'Ga' , 
   32:  'Ge' , 
   33:  'As' , 
   34:  'Se' , 
   35:  'Br' , 
   36:  'Kr' , 
   37:  'Rb' , 
   38:  'Sr' , 
   39:  'Y'  , 
   40:  'Zr' , 
   41:  'Nb' , 
   42:  'Mo' , 
   43:  'Tc' , 
   44:  'Ru' , 
   45:  'Rh' , 
   46:  'Pd' , 
   47:  'Ag' , 
   48:  'Cd' , 
   49:  'In' , 
   50:  'Sn' , 
   51:  'Sb' , 
   52:  'Te' , 
   53:  'I'  , 
   54:  'Xe' , 
   55:  'Cs' , 
   56:  'Ba' , 
   57:  'La' , 
   58:  'Ce' , 
   59:  'Pr' , 
   60:  'Nd' , 
   61:  'Pm' , 
   62:  'Sm' , 
   63:  'Eu' , 
   64:  'Gd' , 
   65:  'Tb' , 
   66:  'Dy' , 
   67:  'Ho' , 
   68:  'Er' , 
   69:  'Tm' , 
   70:  'Yb' , 
   71:  'Lu' , 
   72:  'Hf' , 
   73:  'Ta' , 
   74:  'W'  , 
   75:  'Re' , 
   76:  'Os' , 
   77:  'Ir' , 
   78:  'Pt' , 
   79:  'Au' , 
   80:  'Hg' , 
   81:  'Tl' , 
   82:  'Pb' , 
   83:  'Bi' , 
   84:  'Po' , 
   85:  'At' , 
   86:  'Rn' , 
   87:  'Fr' , 
   88:  'Ra' , 
   89:  'Ac' , 
   90:  'Th' , 
   91:  'Pa' , 
   92:  'U'  , 
   93:  'Np' , 
   94:  'Pu' , 
   95:  'Am' , 
   96:  'Cm' , 
   97:  'Bk' , 
   98:  'Cf' , 
   99:  'Es' , 
  100:  'Fm' , 
  101:  'Md' , 
  102:  'No' , 
  103:  'Lr' , 
  104:  'Rf' , 
  105:  'Db' , 
  106:  'Sg' , 
  107:  'Bh' , 
  108:  'Hs' , 
  109:  'Mt' , 
  110:  'Ds' , 
  111:  'Rg' , 
  112:  'Cn' , 
  114:  'Uuq', 
  116:  'Uuh'}

def get_force_constants(filename):

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    force_constants = []

    for line in lines:

        if "Frc consts  --" in line:

            tokens = line.split()

            if len(tokens) == 6:
                force_constants.append(float(tokens[3]))
                force_constants.append(float(tokens[4]))
                force_constants.append(float(tokens[5]))
            if len(tokens) == 5:
                force_constants.append(float(tokens[3]))
                force_constants.append(float(tokens[4]))
            if len(tokens) == 4:
                force_constants.append(float(tokens[3]))

    return np.array(force_constants)


if __name__ == "__main__":
    # Reads in a Gaussian09 log file from a normalmode/force 
    # constants calculation (freq)
    #
    # Usage:
    # ======
    #
    # ./normal_mode_sampling.py <myfile.log> <T> <n_samples> > output.xyz
    #
    #
    # where <myfile.log> is a gaussian 09 logfile and
    # T is the temperature in Kelvin
    # <n_samples> is the number of distorted samples requested.
    #


    filename = sys.argv[1]
    T = float(sys.argv[2])
    n_structures = int(sys.argv[3])

    mylogfile = ccopen(filename)
    data = mylogfile.parse()

    coords = data.atomcoords[-1]
    atoms = [NAME[i] for i in data.atomnos]
    modes = data.vibdisps

    force = get_force_constants(filename)

    # Temperature in Kelvin
    #T = 900

    force_min = 0.02

    for n in range(n_structures):

        dcoords = deepcopy(coords)
        
        c = np.random.uniform(0, 1, size=len(force))
        c /= np.sum(c)
        r_scale = np.random.uniform(0, 1)

        c *= r_scale

        for i, mode in enumerate(modes):

            s = np.random.choice([-1.0, 1.0])

            frc = max(force_min, force[i])
            r = s * np.sqrt(3 * c[i] * len(atoms) * 1.380e-23 * T/ (frc*100) ) * 1e10

            # Wrong: dcoords = dcoords + mode * r
            dcoords = dcoords + mode/np.linalg.norm(mode) * r

        print(len(atoms))
        print()
        for j, atom in enumerate(atoms):
            print("%2s %20.12f %20.12f %20.12f" % \
                    (atom, dcoords[j,0], dcoords[j,1], dcoords[j,2]))
