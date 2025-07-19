class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        flag=False          # flag for minus sign
        if x<0:             #to check if number is negative and remove the minus sign
            flag=True
        while x>0:
            lastdigit=x%10
            rev=rev*10+lastdigit
            x=x//10
        if flag:              # to asssign the minus sign if number is negative again after reversing
            rev=(-rev)
        return rev
    
sol=Solution()
n=int(input())
print(sol.reverse(n))