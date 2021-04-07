"""
This module has functions associated with analyzing the geometry of a molecule.

When run as a script and given an xyz file, this script will print out the bonds. Run

$ python geometry_analysis.py --help

to see input options.
"""

import numpy as np
import os


def calculate_distance(atom1_coord, atom2_coord):
    """Calculate the distance between two three-dimensional points."""

    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    bond_length = np.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return bond_length



def bond_check(atom_distance,minn=0,maxx=1.5):
    '''
    a function that takes 3 arguments, bond distance, min and max and checks if it works as a bond or nah
    '''
    if atom_distance < 0:
        raise ValueError(f'Invalid atom distance {atom_distance}. did you mean {atom_distance * -1}?')
    if atom_distance < 0:
        raise ValueError(f'Invalid atom distance {atom_distance}. did you mean {atom_distance * -1}?')
    if atom_distance > minn and atom_distance <= maxx:
        return True
    else:
        return False



def open_xyz(file):
    '''
    open and xyz file and return a tuple of the atoms and coords
    '''
    path, extension = os.path.splitext(file)
    if extension.lower() != '.xyz':
        raise ValueError('Incorect file type! File must be type xyz')
    else:
        xyz_file=np.genfromtxt(fname=file,skip_header=2,dtype='unicode')
        atoms=xyz_file[:,0]
        coords=(xyz_file[:,1:])
        coords=coords.astype(float)
        return atoms, coords


file_location=os.path.join('data','water.xyz')
atoms, coords=open_xyz(file_location)
num_atoms=len(atoms)

for num1 in range(0,len(atoms)):
    for num2 in range(0,len(atoms)):
        if num1<num2:
            bond_length=calculate_distance(coords[num1],coords[num2])
            if bond_check(bond_length) is True:
                print(f'{atoms[num1]} to {atoms[num2]} : {bond_length:0.3f} ')



