import geom_analysis as ga
'''
def calculate_distance(atom1_coord, atom2_coord):
    """Calculate the distance between two three-dimensional points."""

    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    bond_length = np.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return bond_length


def bond_check(atom_distance,minn=0,maxx=1.5):

    a function that takes 3 arguments, bond distance, min and max and checks if it works as a bond or nah

    if atom_distance > minn and atom_distance <= maxx:
        return True
    else:
        return False
'''
import pytest
def test_calculated_distance():
    coord1=[0,0,0]
    coords2=[1,0,0]
    expected=1.0
    observed=ga.calculate_distance(coord1,coords2)
    assert observed == expected

def test_bond_check():
    atom_dis= 1.2
    minn=0
    maxx=1.5
    expected1=True
    observed1=ga.bond_check(atom_dis,minn,maxx)
    assert observed1 == expected1

def test1_bond_check():
    atom_dis= 0
    minn=0
    maxx=1.5
    expected1=False
    observed1=ga.bond_check(atom_dis,minn,maxx)
    assert observed1 == expected1

def test2_bond_check():
    atom_dis= 1.5
    minn=0
    maxx=1.5
    expected1=True
    observed1=ga.bond_check(atom_dis,minn,maxx)
    assert observed1 == expected1

def test_bond_check_negtive():
    atom_dis= -1
    expected1=True
    with pytest.raises(ValueError):
        observed1=ga.bond_check(atom_dis)
