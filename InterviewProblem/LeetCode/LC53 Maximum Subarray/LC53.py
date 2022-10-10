'''
Leetcode 53. Maximum Subarray

Description:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
'''

# @param nums List[int]
# @return int

### TC: O(n) and SC: O(1)
class Solution:
    def maxSubArray(self, nums):
        MAX = nums[0]
        cur = nums[0]
        for n in nums[1:]:
            curMAX = max(n, curMAX+n)
            MAX = max(curMAX, MAX)
        return MAX

'''
Intuitive DP Solution
DP[i] Maximum sum of sub-array ending at i ### the key point: sub-array ending at i
State transition equation: DP[i] = max(DP[i-1]+array[i], array[i])  array[i] must be included
'''
### TC: O(n) and SC: O(n)
class Solution:
    def maxSubArray(self, nums):
        DP_table = [0]*len(nums)
        DP_table[0] = nums[0]
        for i in range(1, len(nums)):
            DP_table[i] = max(nums[i], DP_table[i-1] + nums[i])
        return max(DP_table)
