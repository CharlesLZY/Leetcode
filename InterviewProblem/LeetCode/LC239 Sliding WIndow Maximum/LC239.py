'''
Leetcode 239. Sliding Window Maximum

Description:
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
'''

# @param nums List[int]
# @param k int 
# @return List[int]

### Monotonic Stack Solution
### TC: O(n) and SC: O(N)
class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []
        stack = [] ### maintain a descending stack, storing the index of the number, sorted by the value of nums[i]
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]: ### if a larger number occurs, pop its smaller predecessors
                stack.pop() ### this numbers are not important, we only care the max in current window
            stack.append(i)

            if i - stack[0] == k: ### exceed window size
                stack.pop(0)

            if i + 1 >= k: ### until the first window is formed
                ans.append(nums[stack[0]])
        return ans

### Use deque instead of list can significantly improve the performance
from collections import deque    
class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []
        stack = deque() ### maintain a descending stack, storing the index of the number, sorted by the value of nums[i]
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]: ### if a larger number occurs, pop its smaller predecessors
                stack.pop() ### this numbers are not important, we only care the max in current window
            stack.append(i)

            if i - stack[0] == k: ### exceed window size
                stack.popleft()

            if i + 1 >= k: ### until the first window is formed
                ans.append(nums[stack[0]])
        return ans