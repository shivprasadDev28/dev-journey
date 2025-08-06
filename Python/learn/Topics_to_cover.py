#PYTHON

#* topic completed

"""
output
variabls
input
If/else
loops (for, while)
nested conditions
List
Tuple
Set
Dictionary
Functions
CLASS
"""

#* current TOPIC OOP

def pal(i):
    if i >= n//2:
        return True
    
    if word[i] != word[n-i-1]:
        return False
    
    return pal(i+1)


word = " "
word = word.lower().translate(str.maketrans('', '', ' ,:'))
n = len(word)
print(pal(0))