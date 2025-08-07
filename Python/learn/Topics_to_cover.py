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

s = "leetcode"

h = {}

for ss in s:
    h[ss] = h.get(ss,0)+1

for i, c in enumerate(s):
    if h[c] == 1:
        print(i)
        break
