"""
A
AB
ABC
ABCD
ABCDE
"""

def pattern(n):
    for i in range(n):
        for j in range(65, i+65+1):
            print(chr(j),end="")
        print()
if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)