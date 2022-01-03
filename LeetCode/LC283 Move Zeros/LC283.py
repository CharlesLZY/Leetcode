'''
Leetcode 283. Move Zeroes

Description:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

# @param nums List[int]
# @return None

### TC: O(n) and SC: O(1)
class Solution:
    def moveZeroes(self, nums):
        lp = 0 ### refer to quick sort
        for rp in range(len(nums)):
            if nums[rp] != 0: 
                nums[lp], nums[rp] = nums[rp], nums[lp] 
                lp += 1


