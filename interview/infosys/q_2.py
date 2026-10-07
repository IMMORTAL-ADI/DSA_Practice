def runningSum(arr):
    sum=0
    max_even=-1
    max_odd =-1
    for i in range(len(arr)):
        if i%2 ==0:
            max_even = max(max_even,arr[i])
            sum+=max_even
        else:
            max_odd = max(max_odd,arr[i])
            sum+=max_odd
    return sum

if __name__ =="__main__":
    arr=list(map(int,input().split()))

    print(runningSum(arr))