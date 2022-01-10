'''
Leetcode 

Description:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
'''

# @param board List[List[str]]
# @return bool

### TC: O(n^2) and SC: O(n^2)
class Solution:
    def isValidSudoku(self, board):
        N = 9 ### classical sudoku

        rows = [[0]*N for _ in range(N)]
        cols = [[0]*N for _ in range(N)]
        blocks = [[0]*N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] != '.':
                    if rows[r][int(board[r][c])-1] != 0:
                        return False
                    else:
                        rows[r][int(board[r][c])-1] = 1

        for c in range(N):
            for r in range(N):
                if board[r][c] != '.':
                    if cols[c][int(board[r][c])-1] != 0:
                        return False
                    else:
                        cols[c][int(board[r][c])-1] = 1

        for i in range(3):
            for r in range(3):
                for j in range(3):
                    for c in range(3):
                        idx = 3*i + j
                        cur = board[3*i+r][3*j+c]
                        if cur != '.':
                            if blocks[idx][int(cur)-1] != 0:
                                return False
                            else:
                                blocks[idx][int(cur)-1] = 1

        return True
