'''
JZ47 礼物的最大价值

描述
在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
'''

# @param grid List[List[int]]
# @return int

class Solution:
    def maxValue(self, grid):
    	n_row = len(grid)
        n_col = len(grid[0])
        DP_table = [[None for _ in range(n_col)] for _ in range(n_row)]
        
        DP_table[0][0] = grid[0][0] ### initialize the DP_table
        ### the agent can only move right or down
        for i in range(1, n_row):
            DP_table[i][0] = DP_table[i-1][0] + grid[i][0]  ### we can assert that the agent can only move down
         
        for i in range(1, n_col):
            DP_table[0][i] = DP_table[0][i-1] + grid[0][i] ### we can assert that the agent can only move right
            
        for i in range(1, n_row):
            for j in range(1, n_col):
                DP_table[i][j] = max(DP_table[i-1][j], DP_table[i][j-1]) + grid[i][j]
            
        return DP_table[n_row-1][n_col-1]