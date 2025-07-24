class hcf:
    def find(self,a:int,b:int)->int:
        while (a>0 and b>0 ):
            if (a>b):
                a=a%b
            else:
                b=b%a
        
        return b if a==0 else a
    
a,b=map(int,input().split())

print("The HCF is",hcf().find(a,b))