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

num = [10,22,12,3,0,6]
l = []
l.append(num[-1])
maxi = num[-1]

for i in range(len(num)-1,-1,-1):
    if num[i] > maxi:
        maxi = num[i]
        l.append(num[i])

print(l)