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

def pattern(n):
    for i in range(1,n+1,):
                print("*"*i + (n-i)*2*' ' + '*'*i)
    for i in range(n-1,0,-1):
        print("*"*i + (n-i)*2*' ' + '*'*i)
        
if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)