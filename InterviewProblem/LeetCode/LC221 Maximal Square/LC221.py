'''
Leetcode 221. Maximal Square

Description:
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
'''

# @param matrix List[List[str]] 
# @return int

'''
Different from LC85
'''

### Brute Solution
### TC: O((mn)^2) and SC: O(1)
class Solution:
    def maximalSquare(self, matrix):
        ans = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0': ### matrix[i][j] will be use as the right-bottom corner
                    continue
                for k in range(min(i,j)+1):
                    dx, dy = i-k, j-k ### left-up corner
                    square = True
                    for x in range(dx, i+1):
                        if matrix[x][dy] == '0':
                            square = False
                            break

                    if square:
                        for y in range(dy, j+1):
                            if matrix[dx][y] == '0':
                                square = False
                                break

                    if square:
                        ans = max(ans, (k+1)**2)
                    else:
                        break

        return ans

'''
1 0 1 1 1
1 1 0 1 0
1 1 1 1 1
1 1 1 1 1
if matrix[i][j] == 1: DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1 ### where DP[i][j] the biggest square size ends at (i,j)
'''
### DP Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def maximalSquare(self, matrix):
        ans = 0
        m, n = len(matrix), len(matrix[0])
        DP_table = [[0]*(n+1) for _ in range(m+1)] ### square side length not area
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    DP_table[i][j] = min(DP_table[i-1][j], DP_table[i][j-1], DP_table[i-1][j-1]) + 1
                    ans = max(ans, DP_table[i][j]) ### remember to square
        return ans**2