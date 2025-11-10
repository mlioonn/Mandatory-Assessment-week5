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
    
