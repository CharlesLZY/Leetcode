'''
Leetcode 42. Trapping Rain Water

Description:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

# @param height List[int] 
# @return int

### Two Pointer Solution
### TC: O(n) and SC: O(1)
class Solution:
    def trap(self, height):
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0

        ans = 0
        while left < right:
            ''' 
                |
                |         |
            |   |   |     |   
            | | | | | | | |  
            '''
            if height[left] < height[right]: ### if the left side is shorter than the right side, we can always store left_max - left water for each step
                if height[left] < left_max:
                    ans += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1 ### move on
            else:
                if height[right] < right_max:
                    ans += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return ans


### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def trap(self, height):
        ans = 0
        stack = []
        for i in range(len(height)):
            ### stack will only store descending height (monotonic stack)
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop()
                if len(stack) != 0:
                    '''
                    no left boundary case:      |
                                             |  |
                    '''
                    distance = i - stack[-1] - 1
                    bounded_height = min(height[i], height[stack[-1]]) - height[cur]
                    ans += distance*bounded_height
            stack.append(i)
        return ans

'''
      |
|     |         |
| |   |   |     |   
| | | | | | | | |  

Stack: [0]
       [0, 1, 2]
       height[3] > height[2]
       cur = stack.pop(), [0, 1] ans += (min(height[stack[-1]], height[3]) - height[cur]) * (3 - stack[-1] - 1) = (min(2, 4) - 1) * (3-1-1)
       cur = stack.pop(), [0]    ans += (min(height[stack[-1]], height[3]) - height[cur]) * (3 - stack[-1] - 1) = (min(3, 4) - 2) * (3-0-1)
       cur = stack.pop(), len(stack) == 0

       [3]
       [3, 4]
       height[5] > height[4]
       cur = stack.pop(), [3] ans += (min(height[stack[-1]],height[5]) - height[cur]) * (5 - stack[-1] - 1) = (min(4,2) - 1) * (5-3-1)
       height[5] < height[3]

       [3,5]
       ...
'''