'''
Leetcode 289. Game of Life

Description:
According to Wikipedia's article: "The Game of Life, also known simply as Life, 
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: 
ive (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
using the following four rules (taken from the above Wikipedia article):

- Any live cell with fewer than two live neighbors dies as if caused by under-population.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by over-population.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, 
where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

1 1      1 1
1 0  ->  1 1

0 1 0      0 0 0
0 0 1      1 0 1
1 1 1  ->  0 1 1
0 0 0      0 1 0
'''

# @param board List[List[int]] 
# @return None


### Intuitive Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def gameOfLife(self, board):
        direction = {(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)}
        n_row, n_col = len(board), len(board[0])

        temp = [[0]*n_col for _ in range(n_row)]
        for i in range(n_row):
            for j in range(n_col):
                cur = board[i][j]
                neighbour = []
                for d in direction:
                    if i+d[0] < 0 or i+d[0] >= n_row or j+d[1] < 0 or j+d[1] >= n_col:
                        neighbour.append(0)
                    else:
                        neighbour.append(board[i+d[0]][j+d[1]])

                if cur == 1:
                    if sum(neighbour) < 2: ### rule 1: under-population
                        temp[i][j] = 0
                    elif sum(neighbour) > 3: ### rule 3: over-population
                        temp[i][j] = 0
                    else:
                        temp[i][j] = 1

                else:
                    if sum(neighbour) == 3:
                        temp[i][j] = 1
                    else:
                        temp[i][j] = 0

        for i in range(n_row):
            for j in range(n_col):
                board[i][j] = temp[i][j]


'''
We can use some other marks to identify the live cell which is going to die and the dead cell which is going to live.
'''
### Optimized Solution
### TC: O(mn) and SC: O(1)
class Solution:
    def gameOfLife(self, board):
        def live(cell):
            if cell == 1 or cell == -1:
                return True
            else: ### cell = 0 or cell = 2
                return False
        def liveNeighbour(neighbour):
            res = 0
            for n in neighbour:
                res += live(n)
            return res

        direction = {(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)}
        n_row, n_col = len(board), len(board[0])

        for i in range(n_row):
            for j in range(n_col):
                cur = board[i][j]
                neighbour = []
                for d in direction:
                    if i+d[0] < 0 or i+d[0] >= n_row or j+d[1] < 0 or j+d[1] >= n_col:
                        neighbour.append(0)
                    else:
                        neighbour.append(board[i+d[0]][j+d[1]])

                if live(cur):
                    if liveNeighbour(neighbour) < 2: ### rule 1: under-population
                        board[i][j] = -1 ### use -1 to mark the live cell which is going to die
                    elif liveNeighbour(neighbour) > 3: ### rule 3: over-population
                        board[i][j] = -1 ### use -1 to mark the live cell which is going to die


                else:
                    if liveNeighbour(neighbour) == 3:
                        board[i][j] = 2 ### use 2 to mark the dead cell which is going to live

        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0











'''
What if the board is infinite?
1. It would be computationally impossible to iterate a matrix that large.
2. It would not be possible to store that big a matrix entirely in memory. 

Trick: We can use sparse matrix to store the board. (only store the positions of live cells.)
'''