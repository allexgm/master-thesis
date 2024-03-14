for mol in alanine aspartic glycine leucine proline tryptophan arginine glutamate histidine lysine serine tyrosine aspargine glutamine isoleucine phenylalanine threonine valine
do
  cp xyz_splitter.py $mol
  cd $mol
    python3 xyz_splitter.py
  cd ..
done

