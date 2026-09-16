
def reverseArray(arr,l,r):
    if l> r:
        return arr
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1

    return reverseArray(arr,l,r)

if __name__ == "__main__":
    n= int(input())
    arr = list(map(int,input().split(" ")))
    l=0
    r=n-1
    print(reverseArray(arr,l,r))
