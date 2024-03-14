import os
# Obtener el nombre del aminoacido de la carpeta actual
mol = str(os.path.basename(os.getcwd()))

file = open("confs_"+mol+".xyz")
text = file.readlines()
natom = int(text[0])
clusters = len(text) // (natom+2) 

# Iterate through chunks and write each to a separate file
for i in range(clusters):
    subfile = text[i * (natom+2): (i + 1) * (natom+2)]  # Get a chunk of 5 lines
    output = f'{mol}_conf{i + 1}.com'  # Define output file name
    with open(output, 'w') as file:
        file.writelines('#p m062X def2TZVP opt freq\n')
        file.writelines(' \n')
        file.writelines(subfile[1:2])
        file.writelines(' \n')
        file.writelines('0 1\n')
        file.writelines(subfile[2:])
        file.writelines(" \n")
print('All done !')
