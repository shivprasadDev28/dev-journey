"""
1
01
101
0101
10101
"""

start = 1

for i in range(5):
    if i % 2 == 0: start = 1
    else: start = 0

    for j in range(i+1):
        print(start,end="")
        start = 1-start
    print()