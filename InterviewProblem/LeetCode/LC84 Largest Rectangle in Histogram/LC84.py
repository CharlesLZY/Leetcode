'''
Leetcode 84. Largest Rectangle in Histogram

Description:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.
'''

# @param heights List[int]
# @return int

### Brute Solution
### TC: O(n^2) and SC: O(1)
class Solution:
    def largestRectangleArea(self, heights):
        MAX = 0
        for i in range(len(heights)):
            curMIN = float("inf")
            for j in range(i, len(heights)):
                curMIN = min(curMIN, heights[j])
                MAX = max(MAX, curMIN * (j - i + 1))
        return MAX

### Monotonic Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def largestRectangleArea(self, heights):
        ### the stack will only store ascending height (monotonic stack), the min will always stay in the stack, because no one can pop it
        ### trick: the stack should keep -1 as the bottom, because at last, we can always count the min * len(height) as a rectangle
        ### the purpose of maintaining an ascending stack is to ensure, the left height in the stack can always use the current rightmost height to count width
        stack = [-1, 0] 
        MAX = 0
        for i in range(1, len(heights)):
            if heights[stack[-1]] <= heights[i]: ### after each loop, the stack must have at least a number (besides of -1) which is the current min height
                stack.append(i)
            else:
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]: ### keep pop, if stack[i] is the min, then the stack will be pop over temporarily.
                    prevHeight = heights[stack.pop()] ### in the while loop, prevHeight will keep decreasing, because the stack is ascending
                    width =  i - stack[-1] - 1 ### trick: we use i - stack[-1] - 1 as the width
                    '''
                      |   stack = [-1,0,1,2] 
                      |   heights[3] < heights[stack[-1]]: keep popping stack until the stack is ascending:
                     ||   pop 2 from stack, prevHeight = 5, width = 3 - 1 - 1 = 1, update rectangle area: 5
                     |||  pop 1 from stack, prevHeight = 3, width = 3 - 0 - 1 = 2, update rectangle area: 6                   
                    ||||  stack = [-1,0,3] stop popping, because heights[0] < heights[3], push 3
                    '''
                    MAX = max(MAX, width * prevHeight) 
                stack.append(i)
        ### the stack[1] must be the min height and stack[-1] must be the last number of heights array      
        while stack[-1] != -1: ### at this time, the stack must be ascending and the last number must at the top of the stack
            curHeight = heights[stack.pop()]  ### in the while loop, prevHeight will keep decreasing, because the stack is ascending
            width =  len(heights) - stack[-1] - 1 ### that's why we put -1 at the bottom of the stack, at last we will use it to calculate the rectangle min * len(heights)
            MAX = max(MAX, width*curHeight)
        return MAX

