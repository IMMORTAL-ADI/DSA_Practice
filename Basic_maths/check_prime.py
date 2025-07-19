class prime:
    def check(self,x:int)->bool:
        if x==1:
            print("Its coprime")
        for i in range(2,(x//2)+1):
            if x%i==0:
                return False
        return True

n=int(input())
print(prime().check(n))