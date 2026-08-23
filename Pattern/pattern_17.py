"""
A
BB
CCC
DDDD
EEEEE
"""

def pattern(n):
    x=65
    for i in range(1,n+1):
        print(chr(x)*i)
        x+=1
if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)