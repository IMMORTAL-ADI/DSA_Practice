def printSum(n,sum):
    if n<1:
        print(sum)
        return
    sum +=n
    printSum(n-1,sum)
    return 

def returnSum(n,sum):
    if n<1:
        return sum
    sum +=n
    return returnSum(n-1,sum)


if __name__ == "__main__":
    n= int(input())
    sum=0
    printSum(n,sum)

    print("Return :", returnSum(n,sum=0))