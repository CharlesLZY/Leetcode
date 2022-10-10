'''
Leetcode 130. Surrounded Regions

Description:
Given an m x n matrix board containing 'X' and 'O', 
capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

# @param board List[List[str]] 
# @return None

### TC: O(n) and SC: O(n)
class Solution:
    def solve(self, board):
        m, n = len(board), len(board[0])
        visited = set()
        actions = [(1,0), (-1,0), (0,1), (0,-1)]
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0 and i != m-1 and j != n-1: ### only keep the blocks on the border
                    continue
                ### if we meet a block on the border
                if (i,j) not in visited:
                    visited.add((i,j))
                    if board[i][j] == 'O': ### if this block on the border is 'O
                        queue = [(i,j)]
                        while queue: ### find all its neighbour
                            x, y = queue.pop(0)
                            board[x][y] = 'E' ### mark them as 'E' and keep them
                            for dx, dy in actions:
                                if 0 <= x+dx < m and 0 <= y+dy < n:
                                    if (x+dx, y+dy) not in visited:
                                        visited.add((x+dx, y+dy))
                                        if board[x+dx][y+dy] == 'O':
                                            queue.append((x+dx, y+dy))
        
        ### erase the surrounded 'O' which are not the neighbour of the 'O' blocks on the border
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'E':
                    board[i][j] = 'O'      










