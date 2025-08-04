"""
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""



for i in range(5):
    for j in range(i+1):
        print("*",end="")
    
    for j in range(8-i*2):
        print(" ",end="")
    
    for j in range(i+1):
        print("*",end="")
    print()


for i in range(1,5):
    for j in range(i,5):
        print("*",end="")

    for j in range(2*i):
        print(" ",end="")
    
    for j in range(i,5):
        print("*",end="")
    print()