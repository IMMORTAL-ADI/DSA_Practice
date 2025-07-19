from math import sqrt
class factors:
    def all_factors(self,x:int):
        for i in range(1,(x//2)+1):
            if x%i==0:
                print(i)
        print(x)
        
    def impr_all_factors(self,x:int):
        for i in range(1,int(sqrt(x))+1):
            if x%i==0:
                print(i)
                if (x//i)!=i:
                    print(x//i)
                
            
n=int(input())
factors().impr_all_factors(n)
