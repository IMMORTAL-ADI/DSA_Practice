class Solution:
    def intersectionArray(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0

        intersection_arr = []

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if not intersection_arr or intersection_arr[-1] != nums1[i]:
                    intersection_arr.append(nums1[i])
                i += 1
                j += 1
                
        return intersection_arr

if __name__ == "__main__":
    arr1=list(map(int,input().strip().split(" ")))
    arr2=list(map(int,input().strip().split(" ")))

    sol= Solution()
    print(sol.moveZeroes(arr1,arr2))