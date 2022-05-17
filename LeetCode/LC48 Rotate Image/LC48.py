'''
Leetcode 48. Rotate Image

Description:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

# @param matrix List[List[int]] 
# @return None

'''
      rotate
1 2 3        7 4 1
4 5 6   ->   8 5 2
7 8 9        9 6 3
 
      transpose       mirrot
1 2 3           1 4 7         7 4 1
4 5 6     ->    2 5 8    ->   8 5 2
7 8 9           3 6 9         9 6 3

'''

class Solution:
    def rotate(self, matrix):
        def transpose(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i, n):
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        def transpose(matrix):
            m, n = len(matrix), len(matrix)
            matrixT = [[None]*m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    matrixT[i][j] = matrix[j][i]
            return matrixT


        def mirror(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

        matrix = transpose(matrix)
        mirror(matrix) # transpose then mirrot


'''
Transpose:

1 2 3 
4 5 6

1 4
2 5 
3 6


''' 
