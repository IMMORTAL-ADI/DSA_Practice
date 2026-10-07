class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        swap =1
        last_unique = nums[0]

        for i in range(1,len(nums)):
            if nums[i] != last_unique:
                nums[swap]= nums[i]
                swap+=1
                last_unique = nums[i]
        
        return swap

if __name__ == "__main__":
    arr=list(map(int,input().strip().split(" ")))

    sol= Solution()
    print(sol.removeDuplicates(arr))