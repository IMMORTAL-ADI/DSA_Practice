def printNumbers(n):
    if n<1:
        return
    print(n)
    printNumbers(n-1)
    return 

if __name__ == "__main__":
    n= int(input())
    count=0
    printNumbers(n)