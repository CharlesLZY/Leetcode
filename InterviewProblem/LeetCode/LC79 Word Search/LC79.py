'''
Leetcode 79. Word Search

Description:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
'''

# @param board List[List[str]]
# @param word str
# @return bool

class Solution:
    def exist(self, board, word):
        n_row, n_col = len(board), len(board[0])
        def forward(x, y, remain):
            if board[x][y] != remain[0]: ### this contains the check of whether the position was visited, since we use board as visited list
                return False
            else:
                if len(remain) == 1: ### without this branch, if the board only has one grid, it will fail because we will check whether the succeeded position is valid before recursion
                    return True
                board[x][y] = '#' ### marked as visited
                for action in [(0,1), (1,0), (0,-1), (-1,0)]:
                    if 0 <= x + action[0] < n_row and 0 <= y + action[1] < n_col:
                        if forward(x + action[0], y + action[1], remain[1:]):
                            return True
                board[x][y] = remain[0] ### backtrack
                return False

        for i in range(n_row):
            for j in range(n_col):
                if forward(i, j, word):
                    return True
        return False


class Solution:
    def exist(self, board, word):
        n_row = len(board)
        n_col = len(board[0])
        
        def backtrack(row, col, suffix):
            if len(suffix) == 0:
                return True

            if row < 0 or row == n_row or col < 0 or col == n_col or board[row][col] != suffix[0]:
                ### board[row][col] != suffix[0] contains the check of whether the position was visited
                return False
            else:
                board[row][col] = "#" ### explored
                for action in [(0,1), (1,0), (0,-1), (-1,0)]:
                    if backtrack(row + action[0], col + action[1], suffix[1:]):
                        return True
                board[row][col] = suffix[0]
                return False

        for i in range(n_row):
            for j in range(n_col):
                if backtrack(i,j,word) == True:
                    return True
        return False


### Need to optimize, we can have in-place solution
class Solution:
    def exist(self, board, word):
        n_row, n_col = len(board), len(board[0])

        def forward(cur, path):
            curLength = len(path)
            if curLength == len(word)-1:
                return True
            for action in [(0,1), (1,0), (0,-1), (-1,0)]:
                if 0 <= cur[0] + action[0] and cur[0] + action[0] < n_row and 0 <= cur[1] + action[1] < n_col:
                    candidate = (cur[0] + action[0], cur[1] + action[1])
                    if candidate not in path and word[curLength+1] == board[candidate[0]][candidate[1]]: ### cur must be word[curLength-1]
                        if forward(candidate, path+[cur]):
                            return True
            return False

        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == word[0]:
                    if forward((i,j), []):
                        return True

        return False

