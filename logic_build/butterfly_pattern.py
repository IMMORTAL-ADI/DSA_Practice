n=int(input())

for i in range(1,n+1):
    print("*"*(i)+"  "*(n-i)+"*"*i)
for i in range(1,n+1):
    print("*"*(n-i)+"  "*i+"*"*(n-i))