def encrypt(message, shifts, alphabet):
    string = ""
    wordList = list(message)
    alphabetList = list(alphabet)
    if len(shifts) != len(wordList):
        return None
    for numbers in shifts:
        if numbers < 0 or numbers >= len(alphabetList):
            return None
    for letters in wordList:
        if letters not in alphabetList:
            return None
        else: 
            indexOfLetter = alphabetList.index(letters)
            indexOfLetter += shifts[0]
            shifts.pop(0)
            if indexOfLetter > len(alphabetList):
                string += str(alphabetList[indexOfLetter % len(alphabetList)])
            else:
                string += str(alphabetList[indexOfLetter])
    return string
            
    
print(encrypt("АБВ", [2, 1, 1, 3], "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"))