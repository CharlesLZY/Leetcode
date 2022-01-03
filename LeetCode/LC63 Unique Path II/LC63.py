'''
Leetcode 63. Unique Paths II

Description:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the 
bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
'''

# @param obstacleGrid List[List[str]] 
# @return int

### DP Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        DP_table = [[-1]*n for _ in range(m)] ### DP[i][j] how many ways can robot come to here
        if obstacleGrid[0][0] == 1: ### corner case
            return 0
        DP_table[0][0] = 1
        ### The robot can only move down or right, so DP[0][:] and DP[0][:] are 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1: ### obstacle
                DP_table[i][0] = 0
            else:
                DP_table[i][0] = DP_table[i-1][0]
        ### The robot can only move down or right, so DP[0][:] and DP[0][:] are 1
        for i in range(1, n):
            if obstacleGrid[0][i] == 1: ### obstacle
                DP_table[0][i] = 0
            else:
                DP_table[0][i] = DP_table[0][i-1]

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    DP_table[i][j] = DP_table[i-1][j] + DP_table[i][j-1]
                else: ### obstacle
                    DP_table[i][j] = 0

        return DP_table[m-1][n-1]


### Optimized DP Solution (use obstacleGrid as DP table)
### TC: O(mn) and SC: O(1)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1: ### corner case
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1: ### obstacle
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]

        for i in range(1, n):
            if obstacleGrid[0][i] == 1: ### obstacle
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else: ### obstacle
                    obstacleGrid[i][j] = 0

        return obstacleGrid[m-1][n-1]
