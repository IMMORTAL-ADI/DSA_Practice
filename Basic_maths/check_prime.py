class prime:
    def check(self,x:int)->bool:
        flag=True
        if x==1:
            print
        for i in range(2,(x//2)+1):
            if x%i==0:
                return False
        