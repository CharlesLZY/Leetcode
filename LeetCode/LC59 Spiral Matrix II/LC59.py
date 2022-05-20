'''
Leetcode 59. Spiral Matrix II

Description:
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''

# @param n int
# @return List[List[int]]

### TC: O(n) and SC: O(n)
class Solution:
    def generateMatrix(self, n):
        matrix = [[0]*n for _ in range(n)]

        up = 0
        down = n-1
        left = 0
        right = n-1
        n = 1
        while up <= down and left <= right:
            for i in range(left, right+1):
                matrix[up][i] = n
                n += 1
            for i in range(up+1, down):
                matrix[i][right] = n
                n += 1
            if up < down:
                for i in range(right, left-1, -1):
                    matrix[down][i] = n 
                    n += 1
            if left < right:
                for i in range(down-1, up, -1):
                    matrix[i][left] = n
                    n += 1

            up += 1
            down -= 1
            left += 1
            right -= 1

        return matrix