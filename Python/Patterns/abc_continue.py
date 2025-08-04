"""
A
BB
CCC
DDDD
EEEEE
"""

for i in range(5):
    for j in range(i+1):
        ch = 65 + i
        print(chr(ch),end="")
    print()