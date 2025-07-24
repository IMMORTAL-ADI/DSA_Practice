from math import sqrt
class prime:
    def check(self,x:int)->bool:
        if x==1:
            return "Its coprime" 
        for i in range(2,int(sqrt(x))+1):
            if x%i==0:
                return False
        return True

n=int(input())
print(prime().check(n))