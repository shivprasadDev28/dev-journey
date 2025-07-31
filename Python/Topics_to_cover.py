#PYTHON

#* topic completed

"""
output
variabls
input
If/else
loops (for, while)
nested conditions
"""

#* current TOPIC
#TODO LIST

# todo Find common elements between two lists.
l = [1,2,4]
ll = [3,4,5]

for i in range(len(l)):
    for j in range(len(l)-1):
        if l[i] == ll[j]:
            print(ll[j])
            break