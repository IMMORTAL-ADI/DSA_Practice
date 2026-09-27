class Solution:
    def bubble_sort(self,arr):
        n= len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr

if __name__ == "__main__":
    arr= list(map(int,input().strip().split(" ")))

    sort =Solution()

    print(sort.bubble_sort(arr))