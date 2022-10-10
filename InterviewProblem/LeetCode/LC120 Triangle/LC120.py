'''
Leetcode 120. Triangle

Description:
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, 
you may move to either index i or index i + 1 on the next row.

Example:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
    2
   3 4
  6 5 7
 4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11
'''

# @param triangle List[List[int]]
# @return int

### BFS Solution
### TC: O(2^n) and SC: O(n)
class Solution:
    def minimumTotal(self, triangle):
        ans = float("inf")
        queue = [(0,0,triangle[0][0])] ### (depth, idx, cur_path)
        while queue:
            depth, idx, cur_path = queue.pop(0)
            if depth == len(triangle)-1:
                ans = min(ans, cur_path)
            else:
                queue.append((depth+1, idx, cur_path+triangle[depth+1][idx]))
                queue.append((depth+1, idx+1, cur_path+triangle[depth+1][idx+1]))
        return ans

### DP Solution
### TC: O(n^2) and SC: O(1)
class Solution:
    def minimumTotal(self, triangle):
        '''
        This solution we use in-place, to store DP value.
        If in-place is not allowed, just maintain a copy of the triangle
        '''
        for row in range(1, len(triangle)):
            for col in range(row+1):
                if col == 0:
                    triangle[row][0] += triangle[row-1][0]
                elif col == row:
                    triangle[row][row] += triangle[row-1][row-1]
                else:
                    triangle[row][col] += min(triangle[row-1][col], triangle[row-1][col-1])
        return min(triangle[-1])