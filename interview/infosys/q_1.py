def ascending_array(n,arr):
    prev = -1
    count = 0
    l=0
    r = n-1
    while l< r:
        if prev > arr[l] and prev > arr[r]:
            break
        elif arr[l] < arr[r] and prev < arr[l]:
            prev = arr[l]
            l+=1
            count+=1
        elif arr[r] < arr[l] and prev < arr[r]:
            prev = arr[r]
            r-=1
            count+=1
        else:
            if prev > arr[l]:
                prev = arr[r]
                r-=1
                count+=1
            elif prev > arr[r]:
                prev = arr[l]
                l+=1
                count+=1
    return count

if __name__ == "__main__":
    n=int(input())
    arr= list(map(int,input().strip().split(" ")))

    print(ascending_array(n,arr))