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
"""

#* current TOPIC Functions 

# TODO Write a function power(x, n) that computes x^n recursively. (Assume n is a non-negative integer.)

def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)

print(power(2,4))