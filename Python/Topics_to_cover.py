#PYTHON

#* topic 

"""
output
variabls
input
If/else
loops (for, while)
nested conditions
"""

# todo Password Checker

rows = int(input("Enter number of rows: "))

print("Pattern 1:")
for i in range(1, rows + 1):
    print('*' * i)

print("\nPattern 2:")
for i in range(rows, 0, -1):
    print('*' * i)