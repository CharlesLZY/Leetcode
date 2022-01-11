'''
Leetcode 

Description:
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1
Input: nums = [3,4,-1,1]
Output: 2

Example 2
Input: nums = [1,2,0]
Output: 3
'''

# @param nums List[int]
# @return int

### TC: O(n) and SC: O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            cur = nums[i]
            if 0 < cur <= len(nums) and nums[cur-1] != cur:
                nums[i], nums[cur-1] = nums[cur-1], nums[i] ### we can not move forward after swapping, because we don't know what number is swapped to here e.g. [0,4,2,1]
            else:
                i += 1
        
        curMAX = len(nums)+1 ### trick: default answer is len(nums)+1
        for i in range(len(nums)):
            if nums[i] != i+1:
                curMAX = i+1
                break
        return curMAX
