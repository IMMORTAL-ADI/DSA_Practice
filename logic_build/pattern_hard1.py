n=int(input())

for i in range(1,n+1):
    # if i ==1:
    #     print(i)
    #     continue
    for j in range(n-i+1,n):
        print(i+sum(range(j,n)),end=" ")
    print(i)
