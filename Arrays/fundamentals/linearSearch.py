class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1

if __name__ == "__main__":
    arr=list(map(int,input().strip().split(" ")))

    sol= Solution()
    print(sol.largestElement(arr))