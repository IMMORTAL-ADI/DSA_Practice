"""
Print this Pattern :

****
****
****
****

"""


def pattern(n):
    for i in range(1,n+1):
        print("*"*n)
        
if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)