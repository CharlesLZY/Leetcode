'''
JZ40 最小的K个数

描述：
给定一个长度为 n 的可能有重复值的数组，找出其中不去重的最小的 k 个数。
例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4(任意顺序皆可)。
'''

# @param nums List[int]
# @param k int
# @return List[int]

### Intuitive solution: sort O(nlogn)

from heapq import *
### Heap Solution: maintain a k-sized max heap
### TC: O(nlogk) (heap insert & pop operation is O(logk)) and SC: O(k)
class MAX_Heap:
    heap = [] ### min heap
    def push(self, x):
        heappush(self.heap, -x)
    def pop(self):
        if len(self.heap) == 0:
            return None
        else:
            return -heappop(self.heap)
    def top(self):
        if len(self.heap) == 0:
            return None
        else:
            return -self.heap[0]
    def __len__(self):
        return len(self.heap)

class Solution:
    def GetLeastNumbers_Solution(self, nums, k):
        if k == 0: ### corner case
            return []
        heap = MAX_Heap()
        for n in nums:
            if len(heap) < k:
                heap.push(n)
            else:
                if n < heap.top():
                    heap.pop()
                    heap.push(n)
        return [-x for x in heap.heap]


### Quick Partition Solution
### TC: Expected O(n) Worst case: O(n^2) and SC: O(1)
### Each partition: n + n/2 + n/4 + ... = 2n
class Solution:
    def GetLeastNumbers_Solution(self, nums, k):
        def partition(low, high):
            pivot = nums[high]
            j = low
            for i in range(low, high):
                if nums[i] < pivot:
                    nums[j], nums[i] = nums[i], nums[j] ### easy to make a mistake here
                    j += 1
            nums[j], nums[high] = nums[high], nums[j] 
            return j

        if k == 0: ### corner case
            return []

        def select(low, high):
            pivot_index = partition(low, high)
            if k-1 == pivot_index:
                return nums[:pivot_index+1]
            elif k-1 < pivot_index:
                return select(low, pivot_index - 1)
            else:
                return select(pivot_index + 1, high)

        return select(0, len(nums)-1)

### Non-recursive version
class Solution:
    def GetLeastNumbers_Solution(self, nums, k):
        def partition(low, high):
            pivot = nums[high]
            j = low
            for i in range(low, high):
                if nums[i] < pivot:
                    nums[j], nums[i] = nums[i], nums[j] ### easy to make a mistake here
                    j += 1
            nums[j], nums[high] = nums[high], nums[j] 
            return j

        if k == 0: ### corner case
            return []

        lp = 0
        rp = len(nums)-1
        while lp < rp:
            pivot_index = partition(lp, rp)
            if pivot_index == k-1:
                return nums[:k]
            elif pivot_index < k-1:
                lp = pivot_index + 1
            else:
                rp = pivot_index - 1

        return nums[:k]