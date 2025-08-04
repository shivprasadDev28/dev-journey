"""
4444444
4333334
4322234
4321234
4322234
4333334
4444444
"""

n = 7
center = n // 2

for i in range(n):
    for j in range(n):
        val = max(abs(center - i), abs(center - j)) + 1
        print(val, end="")
    print()
