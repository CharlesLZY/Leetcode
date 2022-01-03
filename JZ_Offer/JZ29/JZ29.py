'''
JZ29 顺时针打印矩阵

描述：
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
'''

# @param matrix List[List[int]]
# @return List[int]

class Solution:
    def printMatrix(self, matrix):
        ans = []
        
        h, w = len(matrix), len(matrix[0])
        up = 0
        bottom = h-1
        left = 0
        right = w-1

        while len(ans) < h*w: ### Trick 1: loop end condition
            '''
            Trick 2:
            ——————————
            |        |
            |        |
            |        |
            ——————————
            '''
            for i in range(left, right+1): ### print whole up line (to avoid dead lock)
                ans.append(matrix[up][i])
            for i in range(up+1, bottom):
                ans.append(matrix[i][right])
            if bottom > up: ### Trick 3: avoid replicated print
                for i in range(right, left-1, -1):
                    ans.append(matrix[bottom][i])
            if left < right:
                for i in range(bottom-1, up, -1):
                    ans.append(matrix[i][left])
            up += 1
            bottom -= 1
            left += 1
            right -= 1
        return ans