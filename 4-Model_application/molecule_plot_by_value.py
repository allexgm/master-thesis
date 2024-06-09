import numpy as np
from PIL import Image
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import sys
import subprocess
import os
import argparse
from argparse import RawTextHelpFormatter

# Definimos unos cuantos diccionarios de interes
CHON = ['C','H','O','N','c','h','o','n','B','b','Y','y','Rh','rh']
atomic_number= dict({'C': 6 ,'H': 1  ,'O': 8 ,'N': 7, 'B': 5, 'Y': 39, 'c': 6 ,'h': 1  ,'o': 8 ,'n': 7, 'b': 5, 'y': 39, 'Rh': 45})
radii= dict({'C': 1.7 ,'H': 1.2  ,'O': 1.52 ,'N': 1.55, 'B': 2 , 'Y': 4 , 'c': 1.7 ,'h': 1.2  ,'o': 1.52 ,'n': 1.55, 'Rh': 4})
celem= dict({'C': 'black' ,'H': 'white'  ,'O': 'red' ,'N': 'blue','B': 'pink', 'Y': 'blue','c': 'black' ,'h': 'white'  ,'o': 'red' ,'n': 'blue', 'Rh': 'blue'})
bond_cut = 0.5 # Cutoff for plotting a bond between two atoms (in AA).

# Definimos unas cuantas variables por defecto

def set_axes_equal(ax):
    """
    A function to force the axis to exhibit an equal aspect ratio in the 
    3D visualization.
    """
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()
    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)
    plot_radius = 0.5*max([x_range, y_range, z_range])
    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])
    return None

def visualize():
   # Function for the 3D visualization of the molecules and the atomic charges
   # The plot_frame is set to global so that it can be modified inside and outside the function.

   name = args.filename.split('.')[0]
   img_name = name + ".png"
   scale_factor=args.scale
   print(scale_factor)
   #print(args.size)
   # Creating some arrays to define the labels, sizes and color of the atoms
   atom_size=[]
   atom_size.clear()
   color = []
   color.clear()
   p_labels = []
   p_labels.clear()
   for i in np.arange(natoms):
       # The atom size is the VdW radii with a scaling factor
       atom_size.append(radii[elements[i]])
       color.append(local_values[i])
       #if (vis_label == 'Element'): p_labels.append(elements[i])
       if (vis_label == 'Element'): p_labels.append(elements[i]+str(i+1))
       if (vis_label == 'Value'): p_labels.append("{: .3f}".format(local_values[i]))
   atom_size=np.asarray(atom_size,dtype=float)
   atom_size=atom_size*25*scale_factor
   # Setting the main figure
   figure = plt.figure(figsize=args.size,dpi=args.dpi) 
   ax = figure.add_subplot(projection='3d')
   print(coords)
   print(coords[:,0])
   print(coords[:,1])
   print(coords[:,2])
   # Plotting the atoms as points and the bonds as lines between nearby points
   for i in np.arange(len(coords[:,0])-1):              # i from 1 to N-1
       for j in np.arange(i+1,len(coords[:,0])):        # j from i+1 to N
           atomi = np.array((coords[i,0],coords[i,1],coords[i,2])) # set atom i
           atomj = np.array((coords[j,0],coords[j,1],coords[j,2])) # set atom j
           dist = np.linalg.norm(atomi-atomj)           # compute the distance
           # Plotting the lines between i and j
           #if (dist <= bond_cut):
           if (dist <= bond_cut*(radii[elements[i]]+radii[elements[j]])):
              ax.plot3D([atomi[0], atomj[0]], [atomi[1], atomj[1]], [atomi[2], atomj[2]], color = "black")
   # Plotting the atoms as points
   ax.scatter(xs=coords[:,0],ys=coords[:,1],zs=coords[:,2],s=atom_size,c=color,edgecolor='black',cmap=args.tcbar,alpha=1)
   #ax.scatter(xs=coords[:,0],ys=coords[:,1],zs=coords[:,2],s=atom_size,c=color,edgecolor='black',alpha=1)
   if (args.title != None): plt.title(args.title)
   # Coloring the points according to the atomic charge (if desired)
   if (args.cbar == 'yes'):  
      clb = figure.colorbar(ax.scatter(xs=coords[:,0],ys=coords[:,1],zs=coords[:,2],s=atom_size,c=color,edgecolor='black',cmap=args.tcbar), ax=ax, shrink=0.4, pad = 0.1)
      if (args.setcbar != None):
         clb.mappable.set_clim(vmin=args.setcbar[0], vmax=args.setcbar[1])
         clb._draw_all()
   # Turn off the grid and the axis of our 3D plot
   ax.grid(False)
   ax.set_axis_off()
   set_axes_equal(ax)
   #ax.view_init(-140, 60) # Esto es para ajustar la orientacion del plot
   # Set the atomic labels (if desired)
   #if (vis_label != 'None'):
   if (args.label == 'yes'):
      for i, txt in enumerate(p_labels):
          # The clip_on function is used to make sure that the labels stay in place
          # A 0.05 AA offset is added to the labels
          ax.text(coords[i,0]+0.05, coords[i,1]+0.05,coords[i,2]+0.05,txt).set_clip_on(True)

   if (args.setor != None):
      #print(args.setor)
      ax.view_init(args.setor[0],args.setor[1]) # Esto es para ajustar la orientacion del plot
      
   
   if (args.checkor == 'yes'):
      plt.show()
      print('ax.elev {}'.format(ax.elev))
      print('ax.azim {}'.format(ax.azim))
   else:
      plt.savefig(img_name,dpi=args.dpi,transparent=True,bbox_inches='tight')
      #image=Image.open(img_name)
      #image.load()
      #
      #image_data = np.asarray(image)
      #image_data_bw = image_data.max(axis=2)
      #non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
      #non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
      #cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))
      #
      #image_data_new = image_data[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]
      #
      #new_image = Image.fromarray(image_data_new)
      #new_image.save(name+"_cropped.png")
# El archivo de entrada se lo pasaremos como un argumento durante la ejecucion del codigo

parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
parser.add_argument("-f", "--filename", help="\n"
                                             "Specify the name of the file containing the Cartesian coordinates (XYZ) in angstroms.\n"
                                             "\n",type=str)
parser.add_argument("-label", "--label", choices=['yes', 'no'], default='no',help="\n"
                                             "Specify if you want to label the data.\n"
                                             "\n",type=str)
parser.add_argument("-tlabel", "--tlabel", choices=['Element','Value'], default='Element',help="\n"
                                             "Specify the label type.\n"
                                             "\n",type=str)
parser.add_argument("-dpi", "--dpi", default=350,help="\n"
                                             "Choose the resolution in dpi.\n"
                                             "\n",type=int)
parser.add_argument("-size", "--size", nargs = '*',  default = [6,8] ,help="\n"
                                             "Choose the image size (height,width).\n"
                                             "\n",type=int)
parser.add_argument("-title", "--title",help="\n"
                                             "Set the title of the plot.\n"
                                             "\n",type=str)
parser.add_argument("-cbar", "--cbar", default='yes',help="\n"
                                             "Do you want a color bar?.\n"
                                             "\n",type=str)
parser.add_argument("-checkor", "--checkor", default='no',help="\n"
                                             "Do you want to check the orientation of the plot?.\n"
                                             "\n",type=str)
parser.add_argument("-setor", "--setor", nargs = '*',help="\n"
                                             "Set the orientation of the plot.\n"
                                             "\n",type=float)
parser.add_argument("-setcbar", "--setcbar", nargs = '*',help="\n"
                                             "Set the color bar limits of the plot.\n"
                                             "\n",type=float)
parser.add_argument("-tcbar", "--tcbar", choices= plt.colormaps(), default='gist_ncar',help="\n"
                                             "Set the color bar type.\n"
                                             "\n",type=str)
parser.add_argument("-scale", "--scale", default=1,help="\n"
                                             "Choose the scaling factor.\n"
                                             "\n",type=float)
args = parser.parse_args()
print(args)
vis_label=args.tlabel
# Tomamos los directorios iniciales
initial_dir = os.getcwd()                # Getting execution direcotory
#print(initial_dir)
#pathname = os.path.dirname(sys.argv[0])  # Getting main location of the nnaimq code
#print(pathname)
#if getattr(sys, 'frozen', False):
#    # If the application is run as a bundle, the PyInstaller bootloader
#    # extends the sys module by a flag frozen=True and sets the app 
#    # path into variable _MEIPASS'.
#    os.chdir(sys._MEIPASS)    # Changing to the temporary directory
#else:                         # Canging to the main location of the nnaimq code
#    os.chdir(pathname)

if (args.filename is None):
   # If no input file is given, the run will be aborted
   print("\n")
   print(" # Error : no input file was given, aborting the run !")
   print("\n")
   parser.print_help()
   exit(0)
else:
   # Opening the file and reading relevant information
   infile = open(os.path.join(initial_dir,args.filename), "r")
   natoms = int(infile.readline())       # Obtain the number of atoms.    
   natoms_check=0
   stuff= infile.readline()              # Skipping blank line
   elements = []
   elements.clear()
   local_values= []
   local_values.clear()
   coords = np.zeros((natoms,3),float)
   natoms_check =0
   for line in infile:
       label,x,y,z,val = line.split()    # C 1.1 2.2 0.0 +34.5 (label, r1, r2, r3, valor)
       elements.append(label)            # Obtain the element label
       coords[natoms_check,:] = x,y,z    # Obtain the atomic coordinates
       local_values.append(val)
       natoms_check+=1
   # Closing the file
   local_values = np.asarray(local_values,float)
   infile.close()
   visualize()
