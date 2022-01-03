'''
Leetcode 74. Search a 2D Matrix

Description:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.
'''

# @param matrix List[List[int]]
# @param target int
# @return bool

### Binary Search
### TC: O(log(mn)) and SC: O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        def idx2coord(idx):
            return idx // n, idx % n

        lp = 0
        rp = m*n - 1

        while lp <= rp:
            mid = (lp + rp) // 2
            x,y = idx2coord(mid)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                lp = mid + 1
            else:
                rp = mid - 1
        return False