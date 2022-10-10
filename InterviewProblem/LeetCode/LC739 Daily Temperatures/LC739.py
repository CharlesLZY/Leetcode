'''
Leetcode 739. Daily Temperatures

Description:
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
'''

# @param temperatures List[int] 
# @return List[int]

### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def dailyTemperatures(self, temperatures):
        ### We are going to maintain a monotonic(sorted) stack
        ans = [0]*len(temperatures) ### default 0
        stack = [] ### descending, only store the day which does not have warmer temperature yet
        for day in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[day]:
                prev_day = stack.pop()
                ans[prev_day] = day - prev_day
            stack.append(day)
        return ans
