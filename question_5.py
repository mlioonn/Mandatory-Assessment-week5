"""Basic Programming Structure
All code for this question must be written in the file question_5.py.
The aim of this exercise is to transform a string representing a molecule into a list of tuples,
where the first element of a tuple is the string corresponding to an atom, and the second element
is the number of occurrences of that atom at the given position in the structure of the molecule.
For example, the molecule CO2 given by the string ’CO2’ is represented by the list of tuples
[(’C’,1),(’O’,2)].
Glucose C6 H12O6 is represented by ’C6H12O6’ and [(’C’,6),(’H’,12),(’O’.6)].
The Acetic acid molecule CH3COOH is given by the string ’CH3COOH’ and the list of tuples
[(’C’,1), (’H’,3), (’C’,1), (’O’,1), (’O’,1), (’H’,1)].
Some atoms are described by more than one character, like calcium Ca. The first character is
uppercase and the second character is lowercase. For example, the calcium carbonate molecule
CaCO3 is represented by the string ’CaCO3’. Its list representation is
[(’Ca’,1), (’C’,1), (’O’,3)].
Implement a function molecule_to_list(molecule) that takes a string representation
of a molecule as described above and returns its list of tuples representation.
The function returns None if:
• molecule does not start with a uppercase letter from the English alphabet,
• molecule contains characters that are not alphanumeric.
• molecule has an invalid format, for example the symbol of an atom is lowercase like ca
instead of Ca or h instead of H.
"""




def molecule_to_list(molecule):
    if not isinstance(molecule, str) or molecule == "":
        return None
    if not molecule[0].isupper():
        return None
    if not molecule.isalnum():
        return None
    result = []      
    i = 0            
    while i < len(molecule):
        if not molecule[i].isupper():
            return None
        atom = molecule[i]  
        i += 1
        if i < len(molecule) and molecule[i].islower():
            atom += molecule[i]
            i += 1
        number_str = ""
        while i < len(molecule) and molecule[i].isdigit():
            number_str += molecule[i]
            i += 1
        number = int(number_str) if number_str != "" else 1
        result.append((atom, number))
    return result
