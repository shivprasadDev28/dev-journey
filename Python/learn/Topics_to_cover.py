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

#* current TOPIC HAShing

# Input: arr[] = {10,5,10,15,10,5};
# o/p
#10 3
#5 2
#15 1

num = [1,1,0,1,1,1]

c = 0
a = 0
for n in num:
    if n == 1:
        a += 1
    else:
        if c < a:
            c = a
        a = 0

print(c)