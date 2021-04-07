import numpy as np
import os
import argparse



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
    if atom_distance > minn and atom_distance <= maxx:
        return True
    else:
        return False



def open_xyz(file):
    '''
    open and xyz file and return a tuple of the atoms and coords
    '''
    xyz_file=np.genfromtxt(fname=file,skip_header=2,dtype='unicode')
    atoms=xyz_file[:,0]
    coords=(xyz_file[:,1:])
    coords=coords.astype(float)
    return atoms, coords

'''
We need to add one more thing to our code. When you write a code that includes function definitions and a main script,
you need to tell python which part is the main script. (This becomes very important later when we are talking about testing.)
After your import statements and function definitions and before use argparse
'''

if __name__=='__main__':

    parser = argparse.ArgumentParser(description="This script analyzes a user given xyz file and outputs the length of the bonds.") # to add arguments to expect
    parser.add_argument("xyz_file", help="The filepath for the xyz file to analyze.")# parser.add_argument("argument_name", help="Your help message for this argument.")

    '''
    We can add optional arguments by putting a dash (-) or two dashes (--) in front of the argument name when we add an argument.
    '''
    parser.add_argument('-minimum_length',help='The minimum distance to consider atoms bonded',type=float,default=0)
    parser.add_argument('-maximum_length',help='The maximum distance to consider atoms bonded',type=float,default=1.5)

    # we have to go back and fix the arguments in bond_check call
    args = parser.parse_args() # here, we have to get the arguments.

    atoms, coords = open_xyz(args.xyz_file) #syntax varbliename.argument

    for num1 in range(0,len(atoms)):
        for num2 in range(0,len(atoms)):
            if num1<num2:
                bond_length=calculate_distance(coords[num1],coords[num2])
                if bond_check(bond_length,minn=args.minimum_length,maxx=args.maximum_length) is True:
                    print(f'{atoms[num1]} to {atoms[num2]} : {bond_length:0.3f} ')


