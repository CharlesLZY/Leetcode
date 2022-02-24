'''
Leetcode 347. Top K Frequent Elements

Description:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

# @param nums List[int]
# @param k int
# @return List[int]

### Heap Solution
### TC: O(nlogk) and SC: O(n)
from collections import Counter
from heapq import *
class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        # return heapq.nlargest(k, count.keys(), key=count.get)

        minHeap = [] ### maintain a k min heap
        heapify(minHeap)
        for num in count:
            if len(minHeap) < k:
                heappush(minHeap, (count[num], num))
            else:
                if count[minHeap[0][1]] < count[num]:
                    heappop(minHeap) ### O(logk)
                    heappush(minHeap, (count[num], num)) ### O(logk)
        return [x[1] for x in minHeap]


### Quick Select Solution
### TC: O(n) and SC: O(n)
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        arr = list(count.keys())
        def QuickSelect(arr, k): ### select the kth largest number
            def partition(low, high):
                if low < high:
                    pivot = arr[high]
                    j = low
                    for i in range(low, high):
                        if count[arr[i]] < count[pivot]:
                            arr[i], arr[j] = arr[j], arr[i]
                            j += 1
                    arr[j], arr[high] = arr[high], arr[j]
                    return j
                else:
                    return low

            def select(low, high):
                pivot_index = partition(low, high)
                if pivot_index == len(arr) - k:
                    return
                elif pivot_index > len(arr) - k:
                    select(low, pivot_index-1)
                else:
                    select(pivot_index+1, high)

            select(0, len(arr)-1)

        QuickSelect(arr, k)
        return arr[len(arr)-k:]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        arr = list(count.keys())
        
        if len(arr) < k:
            return arr
        
        def partition(arr, low, high):
            if low < high:
                pivot = arr[high]
                j = low
                for i in range(low, high):
                    if count[arr[i]] < count[pivot]:
                        arr[i], arr[j] = arr[j], arr[i]
                        j += 1
                
                arr[high], arr[j] = arr[j], arr[high]
                return j
            return low
        
        lp = 0
        rp = len(arr) - 1
        while lp <= rp:
            pivotIdx = partition(arr, lp, rp)    
            if pivotIdx == len(arr) - k:
                return arr[pivotIdx:]
            elif pivotIdx < len(arr) - k:
                lp = pivotIdx + 1
            else:
                rp = pivotIdx - 1


'''
### Recitation of Quick Sort and Quick Select
import random
def QuickSort(arr, low, high):
    if low < high:
        r = random.randint(low, high)
        arr[r], arr[high] = arr[high], arr[r]

        pivot = arr[high]
        j = low
        for i in range(low, high):
            if arr[i] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        arr[high], arr[j] = arr[j], arr[high]
        QuickSort(arr, low, j-1)
        QuickSort(arr, j+1, high)

def QuickSelect(arr, k): ### find the k-th largest number
    def partition(low, high):
        if low < high:
            r = random.randint(low,high)
            arr[r], arr[high] = arr[high], arr[r]

            pivot = arr[high]
            j = low
            for i in range(low,high):
                if arr[i] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    j += 1
            arr[j], arr[high] = arr[high], arr[j]
            return j
        else:
            return low

    def select(low, high):
        pivot_index = partition(low, high)
        if pivot_index == len(arr) - k:
            return arr[pivot_index]
        elif pivot_index > len(arr) - k:
            return select(low, pivot_index-1)
        else:
            return select(pivot_index+1, high)

    return select(0, len(arr)-1)
'''