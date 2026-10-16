class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count =0
        count = 0
        for i in nums:
            if i==0:
                max_count = max(max_count,count)
                count =0
            else:
                count +=1
                
        max_count = max(max_count,count)
        
        return max_count

if __name__ == "__main__":
    arr=list(map(int,input().strip().split(" ")))

    sol= Solution()
    print(sol.largestElement(arr))