class Solution:
    def partition_finder(self,arr,low,high):
        pivot =arr[low]
        i=low
        j=high

        while i < j:
            while arr[i] <= pivot and i < high:
                i+=1
            while arr[j] > pivot and j > low:
                j-=1

            if i < j:
                arr[i],arr[j]=arr[j],arr[i]

        arr[low],arr[j] = arr[j],arr[low]

        return j

    def quick_sort(self,arr,low,high):
        if low >= high:
            return arr
        partition = self.partition_finder(arr,low,high)
        self.quick_sort(arr,low,partition-1)
        self.quick_sort(arr,partition+1 ,high)

        return arr


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().strip().split(" ")))
    sort = Solution()

    print(sort.quick_sort(arr,0,n-1))
