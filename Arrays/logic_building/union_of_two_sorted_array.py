class Solution:
    def unionArray(self, nums1, nums2):
        n1= len(nums1)
        n2= len(nums2)
        i=0
        j=0
        union_arr=[]

        while i<n1 and j<n2:
            if nums1[i] <= nums2[j]:
                if len(union_arr) == 0  or union_arr[-1] != nums1[i]:
                    union_arr.append(nums1[i])
                i+=1
            else:
                if len(union_arr) == 0 or union_arr[-1] != nums2[j]:
                    union_arr.append(nums2[j])
                j+=1


        while i < n1:
            if len(union_arr) == 0 or union_arr[-1] != nums1[i]:
                union_arr.append(nums1[i])
            i+=1

        while j < n2:
            if len(union_arr) == 0 or union_arr[-1] != nums2[j]:
                union_arr.append(nums2[j])
            j+=1

        return union_arr


if __name__ == "__main__":
    arr1=list(map(int,input().strip().split(" ")))
    arr2=list(map(int,input().strip().split(" ")))

    sol= Solution()
    print(sol.moveZeroes(arr1,arr2))