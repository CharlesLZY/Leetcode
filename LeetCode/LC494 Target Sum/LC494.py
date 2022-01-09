'''
Leetcode 494. Target Sum

Description:
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
'''

# @param nums List[int] 
# @param target int 
# @return int

'''
Refer to LC416
'''

### Brute Recursion Solution 
### TC: O(2^n) and SC: O(2^n)
class Solution:
    ans = 0
    def findTargetSumWays(self, nums, target):
        self.ans = 0
        def DFS(idx, res):
            if idx == len(nums):
                if res == target:
                    self.ans += 1
                return

            DFS(idx+1, res+nums[idx])
            DFS(idx+1, res-nums[idx])

        DFS(0, 0)
        return self.ans


### Recursion Solution with Memoization
### TC: O(t*n) and SC: O(t*n) where t = sum([abs(n) for n in nums)
class Solution:
    def findTargetSumWays(self, nums, target):
        DP_table = {} ### { (curIdx, curSum) : number of ways to achieve the target sum }
        def DFS(idx, res):
            if idx == len(nums):
                return 1 if res == target else 0 ### this line can acelerate 30%
            if (idx, res) in DP_table:
                return DP_table[(idx, res)]

            DP_table[(idx, res)] = DFS(idx+1, res+nums[idx]) + DFS(idx+1, res-nums[idx])
            return DP_table[(idx, res)]

        return DFS(0, 0)