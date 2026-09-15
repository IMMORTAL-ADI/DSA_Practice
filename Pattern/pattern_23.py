"""
4444444
4333334
4322234
4321234
4322234
4333334
4444444
"""

def pattern(n):
    x= 2*n-1
    for i in range ( x ):
        for j in range(x):
            print(4-min(i,j,x-i-1,x-j-1), end="")
        print()

if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)