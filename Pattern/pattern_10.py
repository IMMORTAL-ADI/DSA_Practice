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

def pattern(n):
    for i in range(n):
            seq=' '*(n-i-1)+"*"*(2*i+1)
            print(seq)
            
    for i in range(n):
            seq=" "*i+"*"*(2*(n-i)-1)
            print(seq)
            
if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)