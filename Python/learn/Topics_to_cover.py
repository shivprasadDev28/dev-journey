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

for i in range(len(num)-1):
    min = i
    for j in range(i,len(num)):
        if num[j] < num[min]:
            min = j
    num[i] , num[min] = num[min],num[i]

print(num)