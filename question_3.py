"""
Python’s Dictionaries
All code for this question must be written in the file question_3.py.
The standard atomic weight of an element is the average mass of the atoms of an element. A
sample of atoms and their standard atomic weight is shown in Table 1. The molar masses of
molecules are calculated from the standard atomic weights of each element. One can compute
the molar mass of a compound by adding the standard atomic weights of its constituent atoms.
For example the molar mass of water (H2O) is given by:
mH2O = 2 × mH + mO
= 2 × 1.00797 + 15.9994 = 18.01534
Symbol Name Atomic Weight (g/mol)
H Hydrogen 1.00797
He Helium 4.00260
C Carbon 12.011
O Oxygen 15.9994
Table 1: List of elements and their atomic weights.
For this question, the table of atomic weight is stored in a global variable ATOMS. The variable
ATOMS is a dictionary where the keys are the atoms’ symbol, and the values are another
dictionary. This second dictionary has two keys, the ’name’ mapped to the full name of the
atom and the ’weight’ mapped to the atomic weight of that atom. An extract from the
dictionary is given below.
ATOMS = {’H’:{’name’:’Hydrogen’, ’weight’:1.00797},
’He’:{’name’:’Helium’, ’weight’:4.00260},
...}
A molecule is represented by a list of tuples, where the first element of a tuple is the string
corresponding to an atom symbol, and the second element is the number of occurrences of that
atom at the given position in the structure of the molecule.
For example, the molecule H2O is given by [(’H’,2),(’O’,1)], whereas the Acetic acid
molecule CH3COOH is represented by
[(’C’,1), (’H’,3), (’C’,1), (’O’,1), (’O’,1), (’H’,1)].
Implement a function molar_mass(molecule) that takes a list of tuples representing a
molecule and returns its molar mass.
The function returns None if the molecule contains an unknown atom, that is an atom symbol
that is not in the dictionary ATOMS.
"""







ATOMS = {'H' : {'name' : 'Hydrogen' , 'weight' : 1.00797},
             'He' : {'name' : 'Helium' , 'weight' : 4.00260},
             'C' : {'name' : 'Carbon' , 'weight' : 12.011},
             'O' : {'name' : 'Oxygen' , 'weight' : 15.9994}
             }
def molar_mass(molecule):
    molarMass = 0
    for name, number in molecule:
        if name  not in ATOMS:
            return None
        else:
            molarMass += ATOMS[name]['weight'] * number
    return molarMass
    
