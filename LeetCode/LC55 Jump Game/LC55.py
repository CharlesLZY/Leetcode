'''
Leetcode 55. Jump Game

Description:
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''

# @param nums List[int] 
# @return bool

### Greedy Solution
### TC: O(n) and SC: O(1)
class Solution:
    def canJump(self, nums):
        canReach = 0
        cur = 0
        while cur <= canReach and cur < len(nums):
            if canReach >= len(nums)-1:
                return True
            canReach = max(canReach, cur+nums[cur])
            cur += 1
        return False

### TC: O(n) and SC: O(1)
class Solution:
    def canJump(self, nums):
        canReach = 0
        for i in range(len(nums)):
            if i > canReach: ### cannot reach here
                return False
            canReach = max(nums[i]+i, canReach)
            if canReach >= len(nums)-1:
                return True