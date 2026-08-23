"""
1
01
101
0101
10101
"""


def pattern(n):
    flag=True
    for i in range(n):
        flag=True if (i %2 ==0) else False
        for j in range(i+1):
            print(int(flag),end="")
            flag= not flag
        print()
if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)