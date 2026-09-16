def printfactorial(n,factorial=1):
    if n<1:
        print(factorial)
        return
    factorial *=n
    printfactorial(n-1,factorial)
    return 

def returnfactorial(n,factorial=1):
    if n<1:
        return factorial
    factorial *=n
    return returnfactorial(n-1,factorial)


if __name__ == "__main__":
    n= int(input())
    printfactorial(n,factorial=1)

    print("Return :", returnfactorial(n,factorial=1))