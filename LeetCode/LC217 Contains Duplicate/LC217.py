'''
Leetcode 217. Contains Duplicate

Description:
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''

# @param nums List[int]
# @return bool

### Hash Table Solution
### TC: O(n) and SC: O(n)
class Solution:
    def containsDuplicate(self, nums):
        hashTable = set()
        for n in nums:
            if n in hashTable:
                return True
            else:
                hashTable.add(n)
        return False

### Sort Solution
### TC: O(nlogn) and SC: O(1)
class Solution:
    def containsDuplicate(self, nums):
        def quickSort(arr, low, high):
            if low < high:
                import random
                r = random.randint(low, high)
                arr[r], arr[high] = arr[high], arr[r]

                pivot = arr[high]
                j = low ### the first number larger than pivot
                for i in range(low, high):
                    if arr[i] < pivot:
                        arr[i], arr[j] = arr[j], arr[i]
                        j += 1 ### arr[j] is used, so we need to move j

                arr[j], arr[high] = arr[high], arr[j]

                quickSort(arr, low, j-1)
                quickSort(arr, j+1, high)

        quickSort(nums, 0, len(nums)-1)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
