"""
Built-in Data Structures.
All code for this question must be written in the file question_4.py.
The Caesar cipher is a very simple encryption method and it is easily breakable. In this question
we use an improved encryption method. Given a plain text message T of n characters using an
alphabet A of m letters, and a list S of n positive integers from the set {0, 2, .., k − 1}, T is
encrypted by shifting the kth character T[k] by an amount S[k]. An example is given in Figure 1
where T = [B, A, B, Y] and S = [2, 1, 1, 3]. The first character ’B’ is shifted by 2 giving the
character ’D’, then the second character ’A’ is shifted by 1 giving ’B’ and so on. The encrypted
message is "DBCB".

Implement the function encrypt(message, shifts, alphabet) that takes a plain
text message as a string, the shifts sequence as a list of integers, and the alphabet as
a string. The alphabet can be any sequence of symbols, not necessarily the English alphabet.
The function returns a string containing the encrypted message.
The function returns None if:
• the message contains characters that are not in the alphabet,
• the size of the shifts is not the same as the size of message,
• shifts contains negatives values or values greater or equal to the size of the alphabet
"""


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
