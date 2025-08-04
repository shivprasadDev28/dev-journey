"""
    *    
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
"""

for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")

    for k in range(2*i+1):
        print("*",end="")

    for l in range(5-i-1):
        print(" ",end="")
    print()

for i in range(5):
    
    for j in range(i):
        print(" ",end="")
    
    for k in range(9-i*2):
        print("*",end="")

    for l in range(i):
        print(" ",end="")
    print()