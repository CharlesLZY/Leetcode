'''
JZ51 数组中的逆序对

描述：
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P mod 1000000007
'''

# @param data List[int]
# @return int

'''
把数逆序对和merge分开来，一方面为了可读性，一方面和LC493超级逆序对统一
'''
### TC: O(nlogn) and SC: O(n)
class Solution:
    count = 0
    def InversePairs(self, data):
        temp = [None]*len(data) ### auxiliary array for merge sort
        self.count = 0
        def mergeSort(arr, temp, low, high): ### temp should be an array has the same length with arr

            if low < high:
                mid = (low + high) // 2

                mergeSort(arr, temp, low, mid)
                mergeSort(arr, temp, mid+1, high)
                
                ### since the left half and right half are sorted, we can count the inverse pairs
                p = low
                q = mid + 1
                while p <= mid and q <= high:
                    if arr[p] > arr[q]:
                        self.count += mid - p + 1 ### trick: number after arr[p:] in the left half must be larger than arr[p] because the half-array is sorted 
                        q += 1
                    else:
                        p += 1

                ### merge part
                for i in range(low, high+1):
                    temp[i] = arr[i] ### temporarily store the array for convenience to merge
                p1 = low
                p2 = mid + 1
                for i in range(low, high+1):
                    if p1 <= mid and p2 <= high:
                        if temp[p1] <= temp[p2]:
                            arr[i] = temp[p1]
                            p1 += 1
                        else: ### inverse pairs occur
                            arr[i] = temp[p2]
                            p2 += 1
                    elif p1 <= mid:
                        arr[i] = temp[p1]
                        p1 += 1
                    else:
                        arr[i] = temp[p2]
                        p2 += 1

        mergeSort(data, temp, 0, len(data)-1)
        return self.count % 1000000007 ### 牛客网的傻逼要求


class Solution:
    def InversePairs(self, data):
        temp = [None]*len(data)
        
        def mergeSort(arr, temp, low, high): ### temp should be an array has the same length with arr
            count = 0
            if low < high:
                mid = (low + high) // 2

                count += mergeSort(arr, temp, low, mid)
                count += mergeSort(arr, temp, mid+1, high)

                ### check reverse pair
                p = low
                q = mid + 1
                while p <= mid and q <= high:
                    if arr[p] > arr[q]:
                        count += mid - p + 1 ### trick: number after arr[p:] in the left half must be larger than arr[p] because the half-array is sorted
                        q += 1
                    else:
                        p += 1
                
                for i in range(low, high+1):
                    temp[i] = arr[i] ### temporarily store the array for convenience to merge
                p1 = low
                p2 = mid + 1
                for i in range(low, high+1):
                    if p1 <= mid and p2 <= high:
                        if temp[p1] <= temp[p2]: ### key point: only when temp[p1] > temp[p2], we consider it as inverse pair 
                            arr[i] = temp[p1]
                            p1 += 1
                        else: ### temp[p1] > temp[p2] inverse pairs occur
                            arr[i] = temp[p2]
                            p2 += 1
                    elif p1 <= mid:
                        arr[i] = temp[p1]
                        p1 += 1
                    else:
                        arr[i] = temp[p2]
                        p2 += 1
                return count
                
            else:
                return 0

        return mergeSort(data, temp, 0, len(data)-1) % 1000000007




### Merge Sort (Easy to understand version)
def mergeSort(arr):
    def merge(arr1, arr2):
        merged = [None] * (len(arr1) + len(arr2))
        p1 = 0
        p2 = 0
        for i in range(len(arr1)+len(arr2)):
            if p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] < arr2[p2]:
                    merged[i] = arr1[p1]
                    p1 += 1
                else:
                    merged[i] = arr2[p2]
                    p2 += 1

            elif p1 < len(arr1):
                merged[i] = arr1[p1]
                p1 += 1
            else:
                merged[i] = arr2[p2]
                p2 += 1
        return merged

    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))

### Merge Sort Standard Verison
def mergeSort(arr, temp, low, high): ### temp should be an array has the same length with arr
    def merge(arr, temp, low, high):
        for i in range(low, high+1):
            temp[i] = arr[i] ### temporarily store the array for convenience to merge

        mid = (low + high) // 2
        p1 = low
        p2 = mid + 1
        for i in range(low, high+1):
            if p1 <= mid and p2 <= high:
                if temp[p1] < temp[p2]:
                    arr[i] = temp[p1]
                    p1 += 1
                else:
                    arr[i] = temp[p2]
                    p2 += 1
            elif p1 <= mid:
                arr[i] = temp[p1]
                p1 += 1
            else:
                arr[i] = temp[p2]
                p2 += 1

    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, temp, low, mid)
        mergeSort(arr, temp, mid+1, high)
        merge(arr, temp, low, mid, high)