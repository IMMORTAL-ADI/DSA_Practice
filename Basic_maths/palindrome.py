class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        temp=x
        if x<0:
            return False
        while temp>0:
            lastdigit=temp%10
            rev=rev*10+lastdigit
            temp=temp//10
        if x==rev:
            return True
        else:
            return False
        
sol=Solution()
n=int(input())
print(sol.isPalindrome(n))