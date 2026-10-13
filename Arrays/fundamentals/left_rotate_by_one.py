class Solution:
    def rotateArrayByOne(self, nums):
        for i in range(1, len(nums)):
            nums[i-1],nums[i] =nums[i],nums[i-1]


if __name__ == "__main__":
    arr=list(map(int,input().strip().split(" ")))

    sol= Solution()
    print(sol.removeDuplicates(arr))