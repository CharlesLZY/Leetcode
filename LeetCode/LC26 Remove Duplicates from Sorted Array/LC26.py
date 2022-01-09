'''
Leetcode 26. Remove Duplicates from Sorted Array

Description:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''

# @param nums List[int]
# @return int

### TC: O(n) and SC: O(1)
class Solution:
    def removeDuplicates(self, nums):
        j = 0 ### prev
        i = 1 ### cur
        originLen = len(nums)
        while i < len(nums):
            if nums[i] == nums[j]:
                del nums[i]
                originLen -= 1
            else:
                j += 1
                i += 1
        return originLen