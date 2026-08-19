"""
*********
 *******
  *****
   ***
    *
"""

def pattern(n):
    for i in range(n):
        seq=" "*i+"*"*(2*(n-i)-1)
        print(seq)
            
if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)