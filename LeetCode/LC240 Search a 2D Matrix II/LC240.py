'''
Leetcode 240. Search a 2D Matrix II

Description:
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.
'''

# @param matrix List[List[int]] 
# @param target int 
# @return bool

'''
Searching all kinds of sorted arrays should be implemented with binary search.
The key to this problem is to find the pivot (which we can help us know which side to go.
Arr 0  1  2  3  4
0   <  <  <  < pivot
1               >
2               >
3     tar       >
4               >

We can eliminate one row or column at a time.
'''

### TC: O(m+n) and SC: O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        x = 0
        y = n-1
        while x < m and y >= 0:
            pivot = matrix[x][y]
            if pivot == target:
                return True
            elif pivot < target:
                x += 1
            else:
                y -= 1
        return False

