'''
Leetcode 252. Meeting Rooms

Description:
Given an array of meeting time intervals where intervals[i] = [start_i, end_i], determine if a person could attend all meetings.

Example 1
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2
Input: intervals = [[7,10],[2,4]]
Output: true
'''

# @param intervals List[List[int]] 
# @return bool

### Intuitive Sort Solution
### TC: O(nlogn) and SC: O(1)
class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
