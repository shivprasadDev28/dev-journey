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

num = [13,46,24,52,20,9]
n = len(num)

for i in range(1,n):
    j = i
    while j>0 and num[j-1]>num[j]:
        num[j-1],num[j] = num[j],num[j-1]
        j-=1

print(num)