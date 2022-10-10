'''
Leetcode 62. Unique Paths

Description:
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
'''

# @param m int
# @param n int 
# @return int

### DP Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def uniquePaths(self, m, n):
        DP_table = [[1] * n for _ in range(m)] ### DP[i][j] how many ways can robot come to here
        ### The robot can only move down or right, so DP[0][:] and DP[0][:] are 1
        for col in range(1, m):
            for row in range(1, n):
                DP_table[col][row] = DP_table[col - 1][row] + DP_table[col][row - 1]
        return DP_table[m - 1][n - 1]

### Math Solution
### TC: O(m) and SC: O(1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(n):
            res = 1
            for i in range(1,n+1):
                res *= i
            return int(res)
        return int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))