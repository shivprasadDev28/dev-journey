"""
1      1
12    21
123  321
12344321
"""


for i in range(4):
    
    for j in range(i+1):
        print(j+1,end="")
    
    for k in range(6-i*2):
        print(" ",end="")

    for l in range(i,-1,-1):
        print(l+1,end="")
    
    print()