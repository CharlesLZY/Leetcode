'''
Leetcode 213. House Robber II

Description:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent 
houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can 
rob tonight without alerting the police.
'''

# @param nums List[int]
# @return int

'''
Since House[1] and House[n] are adjacent, they cannot be robbed together. 
Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], 
depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved.
'''

### TC: O(n) and SC: O(1)
class Solution:
    def rob(self, nums):
        if len(nums) == 1:   ### corner case
            return nums[0]

        prev1, prev2 = 0, 0
        cur = None
        for i in range(len(nums)-2, -1, -1): ### rob nums[0]
            cur = max(prev1, prev2+nums[i])
            prev1, prev2 = cur, prev1
        c1 = cur ### choice 1

        prev1, prev2 = 0, 0
        cur = None
        for i in range(len(nums)-1, 0, -1): ### rob nums[1]
            cur = max(prev1, prev2+nums[i])
            prev1, prev2 = cur, prev1
        c2 = cur ### choice 2

        return max(c1,c2)
