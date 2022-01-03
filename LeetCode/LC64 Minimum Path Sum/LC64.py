'''
Leetcode 64. Minimum Path Sum

Description:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

# @param grid List[List[int]] 
# @return int

### DP Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        DP_table = [[None]*n for _ in range(m)] ### DP[i][j] the min path to (i,j)
        ### We can only move down or right, so DP[0][:] and DP[0][:] are fixed
        DP_table[0][0] = grid[0][0]
        for i in range(1, m):
            DP_table[i][0] = DP_table[i-1][0] + grid[i][0]
        for i in range(1, n):
            DP_table[0][i] = DP_table[0][i-1] + grid[0][i]

        for i in range(1, m):
            for j in range(1, n):
                DP_table[i][j] = min(DP_table[i-1][j], DP_table[i][j-1]) + grid[i][j]

        return DP_table[m-1][n-1]
