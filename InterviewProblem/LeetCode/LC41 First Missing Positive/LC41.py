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

### 这题难在会有负数和0

### TC: O(n) and SC: O(1)
class Solution:
    def firstMissingPositive(self, nums):
        i = 0
        while i < len(nums):
            cur = nums[i]
            if 0 < cur <= len(nums) and nums[cur-1] != cur:
                nums[i], nums[cur-1] = nums[cur-1], nums[i] ### we can not move forward after swapping, because we don't know what number is swapped to here e.g. [0,4,2,1]
                ### trick: i remains the same
            else:
                i += 1
        
        curMAX = len(nums)+1 ### trick: default answer is len(nums)+1 因为最极端的情况每个index对应的数都有，那这时候最小的缺失正数就是n+1
        for i in range(len(nums)): 
            if nums[i] != i+1: ### 如果有index对应的正数没被标记，说明这个正数缺失的，但这题不能用negative mark因为数组中可能存在负数
                curMAX = i+1
                break
        return curMAX

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        nums = set(nums)
        for i in range(1, n+1):
            if i not in nums:
                return i
        return n+1


