def printNumbers(n):
    if n<1:
        return
    printNumbers(n-1)
    print(n )
    return 

if __name__ == "__main__":
    n= int(input())
    count=0
    printNumbers(n)