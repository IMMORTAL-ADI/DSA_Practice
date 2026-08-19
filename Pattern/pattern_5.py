"""
*****
****
***
**
*
"""
def pattern(n):
    for i in range(n,0,-1):
        print('*'*i)
        
        
if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)