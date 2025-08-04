"""
   A
  ABA
 ABCBA
ABCDCBA
"""


for i in range(4):
    for j in range(4-i-1):
        print(" ",end="")

    ch = 65
    bp = (2*i+1)//2

    for k in range(0,2*i+1):
        print(chr(ch),end="")

        if k < bp: ch+=1
        else: ch-=1
    
    for l in range(4-i-1):
        print(" ",end="")
    print()