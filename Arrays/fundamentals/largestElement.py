class Solution:
    def largestElement(self, nums):
        largest =nums[0]

        for i in range(1,len(nums)):
            if largest < nums[i]:
                largest = nums[i]
        
        return largest

if __name__ == "__main__":
    arr=list(map(int,input().strip().split(" ")))

    sol= Solution()
    print(sol.largestElement(arr))