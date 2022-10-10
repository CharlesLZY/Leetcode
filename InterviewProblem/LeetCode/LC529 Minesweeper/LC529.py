'''
Leetcode 529. Minesweeper

Description:
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:
- 'M' represents an unrevealed mine,
- 'E' represents an unrevealed empty square,
- 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals)
- digit ('1' to '8') represents how many mines are adjacent to this revealed square
- 'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] 
represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:
1. If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
2. If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
3. If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
4. Return the board when no more squares will be revealed.

Example:
Input:
board = [["E","E","E","E","E"],
         ["E","E","M","E","E"],
         ["E","E","E","E","E"],
         ["E","E","E","E","E"]]
click = [3,0]

Output:
[["B","1","E","1","B"],
 ["B","1","M","1","B"],
 ["B","1","1","1","B"],
 ["B","B","B","B","B"]]
'''

# @param board List[List[str]]
# @param click List[int]
# @return List[List[str]]

### TC: O(n) and SC: O(n)
class Solution:
    def updateBoard(self, board, click):
        queue = [click]
        w, h = len(board), len(board[0])

        while queue:
            x, y = queue.pop(0)

            if board[x][y] == 'M':  ### mine
                board[x][y] = 'X'
                break
            
            elif board[x][y] == 'E': ### empty
                n_mine = 0 ### trick: we can not use len(toExplore) to decide mine number, because of the edge case
                toExplore = []

                directions = [ (0,1), (1,1),(1,0), (0,-1), (-1,-1),(-1,0),(-1,1),(1,-1)]
                for dx, dy in directions:
                    if x+dx >= w or x+dx < 0 or y+dy >= h or y+dy < 0:
                        continue
                    else:
                        if board[x+dx][y+dy] == "M":
                            n_mine += 1
                        else:
                            toExplore.append((x+dx, y+dy))
                
                if n_mine > 0:
                    board[x][y] = str(n_mine)
                else: ### blank's non-mine neighbours should be explored
                    board[x][y] = 'B'
                    for pos in toExplore:
                        queue.append(pos)

        return board

        
        