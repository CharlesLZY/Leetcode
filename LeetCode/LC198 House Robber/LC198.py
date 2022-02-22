'''
Leetcode 198. House Robber

Description:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

# @param nums List[int]
# @return int

'''
Difference between two kinds of sub-structure overlapping method
1. DP[i] = max(DP[i-1], DP[i-2]+nums[i]) where DP[i] ending at robbing i 
2. DP[i] = max(DP[i+1], DP[i+2]+nums[i]) where DP[i] starting from robbing i 
'''

### Recursion DP Solution (recursion with memoization)
class Solution:
    def rob(self, nums):
        DP_table = [None]*(len(nums))
        def robFrom(i):
            if i >= len(nums):
                return 0
            if DP_table[i] is not None:
                return DP_table[i]

            DP_table[i] = max(robFrom(i+1), robFrom(i+2)+nums[i])
            return DP_table[i]
        return robFrom(0)

class Solution:
    def rob(self, nums):
        DP_table = [None]*(len(nums))
        def robEndAt(i):
            if i < 0:
                return 0
            if DP_table[i] is not None:
                return DP_table[i]

            DP_table[i] = max(robEndAt(i-1), robEndAt(i-2)+nums[i])
            return DP_table[i]
        return robEndAt(len(nums)-1)

### 2. DP[i] = max(DP[i+1], DP[i+2]+nums[i]) where DP[i] starting from robbing i 
### DP Solution 
### TC: O(n) and SC: O(n)
class Solution:
    def rob(self, nums):
        DP_table = [0]*(len(nums)+2)
        for i in range(len(nums)-1, -1, -1):
            DP_table[i] = max(DP_table[i+1], DP_table[i+2]+nums[i])
        return DP_table[0]

### 1. DP[i] = max(DP[i-1], DP[i-2]+nums[i]) where DP[i] ending at robbing i 
### Another Version
class Solution:
    def rob(self, nums):
        DP_table = [0]*(len(nums)+1)
        DP_table[1] = nums[0]
        for i in range(2, len(nums)+1):
            DP_table[i] = max(DP_table[i-2]+nums[i-1], DP_table[i-1])
        return DP_table[len(nums)]


### Optimized DP Solution
### TC: O(n) and SC: O(1)
class Solution:
    def rob(self, nums):
        prev1 = 0
        prev2 = 0
        cur = None
        for i in range(len(nums)-1, -1, -1):
            cur = max(prev1, prev2+nums[i])
            prev1, prev2 = cur, prev1
        return cur