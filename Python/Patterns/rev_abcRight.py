"""
ABCDE
ABCD
ABC
AB
A
"""


for i in range(0,5):
    for j in range(0,5-i):
        ch = 65 + j
        print(chr(ch),end="")
    print()