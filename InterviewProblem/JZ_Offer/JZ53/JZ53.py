'''
JZ53 数字在升序数组中出现的次数

描述：
给定一个长度为 n 的非降序数组和一个非负数整数 k，要求统计 k 在数组中出现的次数。
'''

# @param data List[int]
# @param k int
# @return int

### TC: O(logn) and SC: O(1)
class Solution:
    def GetNumberOfK(self, data, k):
        def binarySearch(arr, k): ### find the smallest number larger than k
            lp = 0
            rp = len(arr)-1
            while lp < rp:
                mid = (lp + rp) // 2
                if arr[mid] >= k: ### we want to find the left upper boundary that any number on the left side of the boundary is smaller than k
                    rp = mid ### while lp < rp and mid = (1p+rp)//2 implies rp > mid, so here we will not cause infite loop
                else: ### arr[mid] < k
                    lp = mid + 1
            return lp
        if data:
            first = binarySearch(data, k)
            last = binarySearch(data, k+1)
            if first == 0 and data[first] != k:
                return 0
            elif data[last] == k: ### if k is the biggest value in the array
                return last - first + 1
            else:
                return last - first
        else: ### corner case: empty array
            return 0


### Elegent Solution
class Solution:
    def GetNumberOfK(self , data, k):
        def search(n): ### we want to find the position before n
            lp = 0
            rp = len(data) - 1
            while lp <= rp:
                mid = (lp + rp) // 2
                if data[mid] > n:
                    rp = mid - 1
                elif data[mid] < n:
                    lp = mid + 1
                elif data[mid] == n:
                    rp = mid - 1 ### trick: rp can be -1
            return min(lp,rp)
        
        
        if len(data) == 0: ### corner case
            return 0
        lp = search(k)
        rp = search(k+1)
        
        return rp - lp