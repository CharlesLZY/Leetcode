'''
Leetcode 70. Climbing Stairs

描述：
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

# @param n int
# @return int

### DP Table Solution
### TC: O(n) and SC: O(n)
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        DP_table = [0]*n ### DP[i] denotes the number of ways to reach on ith step
        DP_table[0] = 1 
        DP_table[1] = 2
        for i in range(2, n):
            DP_table[i] = DP_table[i-1] + DP_table[i-2]
        return DP_table[-1]

### DP Space Complexity Optimized Solution
### TC: O(n) and SC: O(1)
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        prev = 1
        cur = 2
        for i in range(2, n):
            cur, prev = cur+prev, cur
        return cur