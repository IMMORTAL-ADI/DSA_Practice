n=int(input())

for i in range(n):
    print(" "*i+f"{n-i}"*(2*(n-i)-1))

for i in range(2,n+1):
    print(" "*(n-i)+f"{i}"*(2*i-1))