'''
Leetcode 1730. Shortest Path to Get Food

Description:
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.
'''

# @param grid List[List[str]]
# @return int

### TC: O(mn) and SC: O(mn)
class Solution:
    def getFood(self, grid):
        w, h = len(grid), len(grid[0])
    
        def isValid(x, y):
            if (x < 0) or (x >= w) or (y < 0) or (y >= h):
                return False
            if grid[x][y] == 'X': ### obstacle
                return False
            return True
        
        def getFoodPosition():
            for x in range(w):
                for y in range(h):
                    if grid[x][y] == '*':
                        return (x, y)
        
        target_x, target_y = getFoodPosition()

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = {(target_x, target_y)}
        queue = deque() ### （x, y, min_steps)
        queue.append((target_x, target_y, 0)) ### start from the food
        while queue:
            x, y, steps = queue.popleft()
            if grid[x][y] == '#': ### reach your location
                return steps
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if ((new_x, new_y) not in visited) and isValid(new_x, new_y):
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, steps+1))
        return -1


### Follow Up: You can move at most k steps at a time.
from collections import deque
def solution(grid, k):
    w, h = len(grid), len(grid[0])
    
    def isValid(x, y):
        if (x < 0) or (x >= w) or (y < 0) or (y >= h):
            return False
        if grid[x][y] == 1: ### obstacle
            return False
        return True

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = {(0, 0)}
    queue = deque() ### （x, y, min_steps)
    queue.append((0, 0, 0))
    while queue:
        x, y, steps = queue.popleft()
        if (x == w-1) and (y == h-1): ### reach the right-down corner
            return steps
        for dx, dy in directions:
            for i in range(1, k+1):
                new_x, new_y = x + i*dx, y + i*dy
                if (new_x, new_y) in visited:
                    continue
                if isValid(new_x, new_y):
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, steps+1))
                else:
                    break
    return -1