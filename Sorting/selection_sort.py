class Solution:
    def selection_sort(self,arr):
        n= len(arr)
        for i in range(n-1):
            min_element= i
            for j in range(i,n):
                if arr[j]< arr[min_element]:
                    min_element=j
            if min_element !=i:
                arr[i],arr[min_element] = arr[min_element],arr[i]
        return arr

if __name__ == "__main__":
    arr= list(map(int,input().strip().split(" "))) 
    sort = Solution()

    print(sort.selection_sort(arr))

    