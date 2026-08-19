"""
1
22
333
4444
55555
"""
def pattern(n):
    for i in range(1,n+1):
        print(f"{i}"*i)
        
if __name__=="__main__":
    n=int(input("Enter the number: "))
    pattern(n)