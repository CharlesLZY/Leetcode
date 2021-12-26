'''
Leetcode 215. Kth Largest Element in an Array

Description:
Given an integer array nums and an integer k, return the kth largest element in the array.
'''

# @param nums List[int]
# @param k int
# @return int

### Recursive Solution
### TC: O(n)
class Solution:
    def findKthLargest(self, nums, k):
        def partition(low, high):
            pivot = nums[high]
            j = low
            for i in range(low, high):
                if nums[i] < pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
            nums[j], nums[high] = nums[high], nums[j]
            return j

        def select(low, high):
            p = partition(low, high)

            if p == len(nums) - k:
                return nums[p]
            elif p < len(nums) - k:
                return select(p+1, high)
            else:
                return select(low, p-1)

        return select(0, len(nums) - 1)


### Iterative Solution
### TC: O(n) and SC: O(1)
import random 
class Solution:
    def findKthLargest(self, nums, k):
        def partition(low, high):
            ran = random.randint(low, high)
            nums[high], nums[ran] = nums[ran], nums[high]

            pivot = nums[high]
            j = low
            for i in range(low, high):
                if nums[i] < pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
            nums[j], nums[high] = nums[high], nums[j]
            return j

        def select(low, high):
            while low <= high:
                p = partition(low, high)
                if p == len(nums) - k:
                    return nums[p]
                elif p < len(nums) - k:
                    low = p + 1
                else:
                    high = p - 1

        return select(0, len(nums) - 1)