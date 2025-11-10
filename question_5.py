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
