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

num = [10,5,10,15,10,5]

h = {}


for n in num:
    h[n] = h.get(n,0)+1


high = max(h,key=h.get)
minn = min(h,key=h.get)

print(high,minn)