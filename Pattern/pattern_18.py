"""
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
"""

def pattern(n):
    for i in range(n):
        x=65
        print(' '*(n-i-1),end="")
        breakpoint= (2*i+1)//2
        for j in range(2*i+1):
            print(chr(x),end="")
            if j < breakpoint:
                x+=1
            else:
                x-=1

        print()
if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)