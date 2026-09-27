class Solution:
    def insertion_sort(self,arr):
        n= len(arr)
        for i in range(1,n):
            key=arr[i]
            pos=i-1

            while pos >=0 and arr[pos] > key:
                arr[pos +1]=arr[pos]
                pos-=1

            arr[pos +1]=key
        return arr

if __name__ == "__main__":
    arr=list(map(int,input().strip().split(" ")))

    sort= Solution()
    print(sort.insertion_sort(arr))