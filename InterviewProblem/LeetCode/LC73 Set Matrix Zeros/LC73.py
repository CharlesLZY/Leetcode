'''
Leetcode 73. Set Matrix Zeroes

Description:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''

# @param matrix List[List[int]]
# @return None

'''
To be efficient, we only record which column and row should be set to 0s
'''
### TC: O(mn) and SC: O(max(m,n))
class Solution:
    def setZeroes(self, matrix):
        n_row, n_col = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        for i in range(n_row):
            for j in range(n_col):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in rows:
            for j in range(n_col):
                matrix[i][j] = 0

        for j in cols:
            for i in range(n_row):
                matrix[i][j] = 0

### Inplace Mark Solution
### TC: O(mn) and SC: O(1))
class Solution:
    def setZeroes(self, matrix):
        n_row, n_col = len(matrix), len(matrix[0])

        ### trick: the first row and column need to be handled seperatly
        firstRow = False ### whether to set the first row to 0s
        firstCol = False ### whether to set the first column to 0s

        for i in range(n_row):
            for j in range(n_col):
                if matrix[i][j] == 0:
                    matrix[i][0] = -1
                    matrix[0][j] = -1
                    if i == 0:
                        firstRow = True
                    if j == 0:
                        firstCol = True
        
        for j in range(1, n_col):
            if matrix[0][j] == -1:
                for i in range(n_row):
                    matrix[i][j] = 0
        
        for i in range(1, n_row):
            if matrix[i][0] == -1:
                for j in range(n_col):
                    matrix[i][j] = 0
        
        if firstRow:
            for j in range(n_col):
                matrix[0][j] = 0
        
        if firstCol:
            for i in range(n_row):
                matrix[i][0] = 0