class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]
        slargest= float("-inf")

        for i in range(1,len(nums)):
            if largest < nums[i]:
                slargest = largest
                largest = nums[i]
            elif largest > nums[i] and slargest < nums[i]:
                slargest=nums[i]
        
        if slargest == float("-inf"):
            return -1
        return slargest
    
if __name__ == "__main__":
    arr=list(map(int,input().strip().split(" ")))

    sol= Solution()
    print(sol.secondLargestElement(arr))
