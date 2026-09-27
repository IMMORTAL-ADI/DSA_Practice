class Solution:
    def merge(self,arr,low,mid,high):
        temp =[]
        left =low
        right= mid+1

        while (left<= mid and right <=high ):
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1

        temp += arr[left:mid + 1]
        temp += arr[right:high + 1]

        arr[low : high+1] = temp
        return arr

    def merge_sort(self,arr,low,high):
        if low >= high:
            return
        mid = (low+high)//2
        self.merge_sort(arr,low,mid)
        self.merge_sort(arr,mid+1,high)

        return self.merge(arr,low,mid,high)

if __name__ == "__main__":
    n= int(input())
    arr= list(map(int,input().strip().split(" ")))

    sort= Solution()
    print(sort.merge_sort(arr,0,len(arr)-1))