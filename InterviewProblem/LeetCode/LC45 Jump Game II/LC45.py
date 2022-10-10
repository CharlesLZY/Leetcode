'''
Leetcode 45. Jump Game II

Description:
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
'''

# @param nums List[int] 
# @return int

### Greedy Solution
### TC: O(n) and SC: O(1)
class Solution:
    def jump(self, nums):
        jumps = 0
        currentJumpEnd = 0
        canReach = 0
        for i in range(len(nums)-1): ### trick: we will end at the last index, we will not consider it
            canReach = max(canReach, i + nums[i])
            if i == currentJumpEnd: ### [2 5 1 0 0]
                jumps += 1 ### jumps update when i = 0 and i = 2 (have to move)
                currentJumpEnd = canReach
        return jumps


### DP Solution
class Solution:
    def jump(self, nums):
        DP_table = [float("inf")] * len(nums) ### inf means unreachable
        DP_table[0] = 0

        for i in range(len(nums)):
            for j in range(i):
                if DP_table[j] != float("inf") and j + nums[j] >= i: ### can access i from j
                    DP_table[i] = min(DP_table[i], DP_table[j] + 1)
        return DP_table[-1] 