'''
Leetcode 329. Longest Increasing Path in a Matrix

Description:
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
'''

# @param matrix List[List[int]] 
# @return int

'''
这题因为是找递增，所以其实是个有向图
'''
### Recursion with memoization
### TC: O(mn) and SC: O(mn)
class Solution:
    def longestIncreasingPath(self, matrix):
        visited = {}
        ans = 1
        m, n = len(matrix), len(matrix[0])
        def DFS(x,y):
            nonlocal m, n, visited
            if (x,y) in visited:
                return visited[(x,y)]

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            curMAX = 1
            for dx, dy in directions:
                X, Y = x+dx, y+dy
                if 0 <= X < m and 0 <= Y < n and matrix[X][Y] > matrix[x][y]:
                    curMAX = max(curMAX, DFS(X, Y)+1)

            visited[(x,y)] = curMAX ### memorization

            return curMAX


        for i in range(m):
            for j in range(n):
                ans = max(ans, DFS(i,j))

        return ans
        