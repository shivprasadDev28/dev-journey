"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

"""


# solving the top 1st then bottom 
# symetric

#top
for i in range(5):
    for j in range(i,5):
        print("*",end="")

    for j in range(2*i):
        print(" ",end="")
    
    for j in range(i,5):
        print("*",end="")
    print()

#bottom 

for i in range(5):
    for j in range(i+1):
        print("*",end="")
    
    for j in range(8-i*2):
        print(" ",end="")
    
    for j in range(i+1):
        print("*",end="")
    print()