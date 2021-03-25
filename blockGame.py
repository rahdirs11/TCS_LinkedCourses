'''
Paul is developing an application for a block game. This block game consists of Number blocks,
Uppercase alphabet blocks, lowercase alphabet blocks, and some symbols. WAP to
help Paul identify the precise category of block.

Input Format:
    First line contains only one character as input of the following category:
        - Number
        - Upper Alphabet
        - Lower Alphabet
        - Symbol
    If the usenters more than one character, only the first character will be taken into consideration.

Output format:
    Output should correctly identify the category of the input entered by the user and print accordingly.

Sample 1:
A -> UPPER ALPHABET

Sample 2:
c -> lower alphabet

Sample 3:
9 -> Number

Sample 4:
% -> Symbol

Sample 5:
asfsDFSDS -> lower alphabet
'''

def decideBlock(string: str):
    if string.isalpha():
        return 'upper alphabet'.upper() if string.isupper() else 'lower alphabet'
    elif string.isdigit():
        return 'Number'
    else:
        return 'Symbol'


print(decideBlock(input()[0]))