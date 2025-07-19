class armstrong:
    def isarmstrong(self,x:int)->bool:
        temp=x
        sum=0
        flag=False
        if x<0:
            x=abs(x)
            flag=True
        while temp>0:
            digit=temp%10
            sum=sum+(digit**3)
            temp//=10
        if flag:
            sum=-sum
        return x==sum

n=int(input())
print(armstrong().isarmstrong(n))
        