'''
Leetcode 37. Sudoku Solver

Description:
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
'''

# @param board List[List[str]]
# @return None

class Solution:
    def solveSudoku(self, board):
        def checkBlock(x, y):
            n_row = x // 3
            n_col = y // 3
            choice = set([str(n) for n in range(1, 10)])
            for i in range(3):
                for j in range(3):
                    cur = board[3*n_row+i][3*n_col+j]
                    if cur != '.':
                        choice.remove(cur)
            return choice
                    
        def checkRow(x, y):
            n_row = x
            choice = set([str(n) for n in range(1, 10)])
            for i in range(9):
                cur = board[n_row][i]
                
                if cur != '.':
                    choice.remove(cur)
            return choice
        
        def checkCol(x, y):
            n_col = y
            choice = set([str(n) for n in range(1, 10)])
            for i in range(9):
                cur = board[i][n_col]
                
                if cur != '.':
                    choice.remove(cur)
            return choice
        
        def nextPos(x, y):
            if y == 8:
                return (x+1, 0)
            else:
                return (x, y+1)
        
        def DFS(x, y):
            if board[x][y] == '.':
                choice = checkBlock(x,y) & checkRow(x,y) & checkCol(x,y)
                for n in choice:
                    board[x][y] = n
                    if x == 8 and y == 8:
                        return True
                    else:
                        next_x, next_y = nextPos(x, y)
                        if DFS(next_x, next_y):
                            return True
                        else:
                            board[x][y] = '.'
            else:
                if x == 8 and y == 8:
                    return True
                else:
                    next_x, next_y = nextPos(x, y)
                    if DFS(next_x, next_y):
                        return True
            
            return False
            
        return DFS(0,0)
        
        
        
        
        
        
