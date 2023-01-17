'''
Leetcode 209. Minimum Size Subarray Sum

Description:
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [nums_l, nums_l+1, ..., nums_r-1, nums_r] 
of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''

# @param target int 
# @param nums List[int] 
# @return int

'''
In this problem, all numbers are postive and we need to find the contiguous subarray
'''
### TC: O(n) and SC: O(n)
class Solution:
    def minSubArrayLen(self, target, nums):
        ans = float("inf")
        curLength = 0
        cur = 0
        lp = 0
        for n in nums:
            cur += n
            curLength += 1
            if cur >= target:
                while cur - nums[lp] >= target:
                    cur -= nums[lp]
                    lp += 1
                    curLength -= 1
                ans = min(ans, curLength)

        return 0 if ans == float("inf") else ans
