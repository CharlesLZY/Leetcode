'''
Leetcode 56. Merge Intervals

Description:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

# @param intervals List[List[int]]
# @return List[List[int]]

### TC: O(nlogn) and SC: O(n)
class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x: x[0]) ### [[1,3], [5,7], [6,8], [8,10]]
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] >= ans[-1][0] and cur[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], cur[1])
            else:
                ans.append(cur)
        return ans


