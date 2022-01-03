'''
Leetcode 200. Number of Islands

Description:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
'''

# @param grid List[List[int]] 
# @return int

### DFS Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def numIslands(self, grid):
        ans = 0
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue

                visited[i][j] = 1
                if grid[i][j] == '1':
                    ans += 1
                    stack = [(i,j)]
                    while stack:
                        x, y = stack.pop()
                        visited[x][y] = 1
                        directions = [(0,1), (1,0), (0,-1), (-1,0)]
                        for dx, dy in directions:
                            xx = x+dx
                            yy = y+dy
                            if 0 <= xx < m and 0 <= yy < n:
                                if visited[xx][yy] == 0 and grid[xx][yy] == '1':
                                    stack.append((xx, yy))
                                visited[x+dx][y+dy] = 1

        return ans


### BFS Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def numIslands(self, grid):
        ans = 0
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue

                visited[i][j] = 1
                if grid[i][j] == '1':
                    ans += 1
                    queue = [(i,j)]
                    while queue:
                        x, y = queue.pop(0)
                        visited[x][y] = 1
                        directions = [(0,1), (1,0), (0,-1), (-1,0)]
                        for dx, dy in directions:
                            xx = x+dx
                            yy = y+dy
                            if 0 <= xx < m and 0 <= yy < n:
                                if visited[xx][yy] == 0 and grid[xx][yy] == '1':
                                    queue.append((xx, yy))
                                visited[x+dx][y+dy] = 1

        return ans




