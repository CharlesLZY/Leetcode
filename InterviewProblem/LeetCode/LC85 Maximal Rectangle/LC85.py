'''
Leetcode 85. Maximal Rectangle

Description:
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
'''

# @param matrix List[List[int]] 
# @return int


'''
matrix      DP_table
1 0 1 0 0   1 0 1 0 0
1 0 1 1 1   1 0 1 2 3
1 1 1 1 1   1 2 3 4 5
1 0 0 1 0   1 0 0 1 0

for the second row and the 5th column of DP-table
1 0 1 2 3
        5
        0
the max area is 3x2
'''

### Brute Solution with DP
### TC: O(mn^2) and SC: O(mn)
class Solution:
    def maximalRectangle(self, matrix):
        m, n = len(matrix), len(matrix[0])
        DP_table = [[0]*n for _ in range(m)] ### DP[i][j] means in the ith row, if ends at (i,j), the max width the rectangle can have
        for i in range(m): ### initialize the first column
            if matrix[i][0] == '1':
                DP_table[i][0] = 1 

        for i in range(m):
            for j in range(1, n): ### DP for each row
                if matrix[i][j] != '0':
                    DP_table[i][j] = DP_table[i][j-1] + 1
        MAX = 0
        for i in range(m): ### for each row, solve a largest rectangle in histogram problem(LC84)
            for j in range(n):
                minWidth = float("inf")
                for k in range(i,m):
                    minWidth = min(minWidth, DP_table[k][j])
                    MAX = max(MAX, minWidth * (k-i+1))
        return MAX


### Stack Solution with DP
### TC: O(mn) and SC: O(mn) ### the SC can be optimized to O(m)
class Solution:
    def maximalRectangle(self, matrix):
        m, n = len(matrix), len(matrix[0])
        DP_table = [[0]*n for _ in range(m)] ### DP[i][j] means in the ith row, if ends at (i,j), the max width the rectangle can have
        for i in range(m): ### initialize the first column
            if matrix[i][0] == '1':
                DP_table[i][0] = 1 

        for i in range(m):
            for j in range(1, n): ### DP for each row
                if matrix[i][j] != '0':
                    DP_table[i][j] = DP_table[i][j-1] + 1

        ### we will use the LC84 stack solution to solve the sub-problem
        def largestRectangleAreaInHistogram(heights):
            ### the stack will only store ascending height (monotonic stack), the min will always stay in the stack, because no one can pop it
            ### trick: the stack should keep -1 as the bottom, because at last, we can always count the min * len(height) as a rectangle
            stack = [-1, 0]
            MAX = 0
            for i in range(1, len(heights)):
                if heights[i] > heights[stack[-1]]: ### after each loop, the stack must have at least a number (besides of -1) which is the current min height
                    stack.append(i)
                else:
                    while stack[-1] != -1 and heights[i] <= heights[stack[-1]]: ### keep pop, if stack[i] is the min, then the stack will be pop over temporarily.
                        prevHeight = heights[stack.pop()] ### in the while loop, prevHeight will keep decreasing, because the stack is ascending
                        width = i - stack[-1] - 1 ### trick: we use i - stack[-1] - 1 as the width
                        MAX = max(MAX, width*prevHeight)
                    stack.append(i)
            ### the stack[1] must be the min height and stack[-1] must be the last number of heights array 
            while stack[-1] != -1:  ### at this time, the stack must be ascending and the last number must at the top of the stack
                curHeight = heights[stack.pop()] ### in the while loop, prevHeight will keep decreasing, because the stack is ascending
                width = len(heights) - stack[-1] - 1  ### that's why we put -1 at the bottom of the stack, at last we will use it to calculate the rectangle min * len(heights)
                MAX = max(MAX, width*curHeight)
            return MAX

        MAX = 0
        for j in range(n):
            MAX = max(MAX, largestRectangleAreaInHistogram([DP_table[i][j] for i in range(m)]))
        return MAX


### Optimized Stack Solution with DP
### TC: O(mn) and SC: O(m)
class Solution:
    def maximalRectangle(self, matrix):
        ### we will use the LC84 stack solution to solve the sub-problem
        def largestRectangleAreaInHistogram(heights):
            ### the stack will only store ascending height (monotonic stack), the min will always stay in the stack, because no one can pop it
            ### trick: the stack should keep -1 as the bottom, because at last, we can always count the min * len(height) as a rectangle
            stack = [-1, 0]
            MAX = 0
            for i in range(1, len(heights)):
                if heights[i] > heights[stack[-1]]: ### after each loop, the stack must have at least a number (besides of -1) which is the current min height
                    stack.append(i)
                else:
                    while stack[-1] != -1 and heights[i] <= heights[stack[-1]]: ### keep pop, if stack[i] is the min, then the stack will be pop over temporarily.
                        prevHeight = heights[stack.pop()] ### in the while loop, prevHeight will keep decreasing, because the stack is ascending
                        width = i - stack[-1] - 1 ### trick: we use i - stack[-1] - 1 as the width
                        MAX = max(MAX, width*prevHeight)
                    stack.append(i)
            ### the stack[1] must be the min height and stack[-1] must be the last number of heights array 
            while stack[-1] != -1:  ### at this time, the stack must be ascending and the last number must at the top of the stack
                curHeight = heights[stack.pop()] ### in the while loop, prevHeight will keep decreasing, because the stack is ascending
                width = len(heights) - stack[-1] - 1  ### that's why we put -1 at the bottom of the stack, at last we will use it to calculate the rectangle min * len(heights)
                MAX = max(MAX, width*curHeight)
            return MAX

        m, n = len(matrix), len(matrix[0])
        MAX = 0
        DP_table = [0] * m
        for j in range(n):
            for i in range(m): ### update the histogram for each column
                '''
                因为DP_table是一列一列更新的，所以我们不用维护整张表，维护一列就行了
                '''
                DP_table[i] = DP_table[i] + 1 if matrix[i][j] == '1' else 0
            MAX = max(MAX, largestRectangleAreaInHistogram(DP_table))
        return MAX