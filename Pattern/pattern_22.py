"""
****
    
*  *
    
*  *
    
****
"""

def pattern(n):
    print("*" * n)
    for i in range(1,(2*n-1)-1):
        if i%2 == 0:
            print("*"+" "*(n-2)+"*")
        else:
            print(" "*n)
    print("*" * n) 

if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)