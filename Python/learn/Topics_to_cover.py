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

#print sum of n using recursion
def rev(l,r):
    if l >= r:
        return
    num[l] , num[r] = num[r],num[l]
    return rev(l+1,r-1)
num = [5,4,3,2,1]
rev(0,4)
print(num)