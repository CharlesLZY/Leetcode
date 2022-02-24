'''
Leetcode 1314. Matrix Block Sum

Description:
Given a m x n matrix mat and an integer k, return a matrix answer 
where each answer[i][j] is the sum of all elements mat[r][c] for:
- i - k <= r <= i + k,
- j - k <= c <= j + k, and
- (r, c) is a valid position in the matrix.

Example
Input: mat =  [[1,2,3],
               [4,5,6],
               [7,8,9]], 
       k = 1

Output: [[12,21,16],
         [27,45,33],
         [24,39,28]]
'''

# @param mat List[List[int]] 
# @param k int
# @return List[List[int]]

'''
Prefix Sum
DP[i][j] means the sum of the rectangle
DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + mat[i][j]

ans[i][j] = DP[i+k][j+k] - DP[i][j-k-1] - DP[i-k-1][j] + DP[i-k-1][j-k-1]
          = rightBottom - leftBottom - rightTop + leftTop
1 2 3                 1 2 3   1 _ _   1 2 3   1 _ _
4 5 6  -->  5 6  -->  4 5 6 - 4 _ _ - _ _ _ + _ _ _  
7 8 9       8 9       7 8 9   7 _ _   _ _ _   _ _ _
'''
### DP Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def matrixBlockSum(self, mat, k):
        m, n = len(mat), len(mat[0])
        DP_table = [[0]*n for _ in range(m)]
        DP_table[0][0] = mat[0][0]
        for i in range(1, m):
            DP_table[i][0] = DP_table[i-1][0] + mat[i][0]
        for i in range(1, n):
            DP_table[0][i] = DP_table[0][i-1] + mat[0][i]

        for i in range(1,m):
            for j in range(1,n):
                DP_table[i][j] = DP_table[i-1][j] + DP_table[i][j-1] - DP_table[i-1][j-1] + mat[i][j]

        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                top = i - k - 1
                bottom = min(i + k, m-1)
                left = j - k -1 
                right = min(j + k, n-1)
                leftTop = DP_table[top][left] if top >= 0 and left >= 0 else 0
                rightTop = DP_table[top][right] if top >= 0 else 0
                leftBottom = DP_table[bottom][left] if left >= 0 else 0
                rightBottom = DP_table[bottom][right]

                ans[i][j] = rightBottom - leftBottom - rightTop + leftTop
                
        return ans