"""
E
DE
CDE
BCDE
ABCDE
"""

def pattern(n):
    for i in range(n):
        char=65+n-1
        for j in range(i,-1,-1):
            print(chr(char-j),end="")
        print()
if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)