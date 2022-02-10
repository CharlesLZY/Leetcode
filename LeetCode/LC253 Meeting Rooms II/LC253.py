'''
Leetcode 253. Meeting Rooms II

Description:
Given an array of meeting time intervals where intervals[i] = [start_i, end_i], return the minimum number of conference rooms required.
'''

# @param intervals List[List[int]] 
# @return int

'''
Maintain a min heap according to the end time.
The intuition of this solution is from the perspective of the people who want to have a meeting.
They just check whether the former meeting is finished. If not, just ask a new meeting room.
'''
### Heap Solution
### TC: O(nlogn) and SC: O(n)
from heapq import *
class Solution:
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0: ### corner case
            return 0

        intervals.sort(key = lambda x: x[0])
        minHeap = [intervals[0][1]] ### earliest end time
        heapify(minHeap)
        MAX = 1
        for start, end in intervals[1:]:
            while minHeap and minHeap[0] <= start: ### check whether former meetings have ended
                heappop(minHeap)
            heappush(minHeap, end) ### trick: heap is maintained for the end time
            MAX = max(MAX, len(minHeap))
        return MAX

'''
The key idea of this solution is to treat starts and endings as independent things.
If start happens, then number of meeting rooms add 1. if ending happens, then number of meeting rooms minus 1. 
The number of start event happend must larger than the number of end event happend
'''
### Another Solution
### TC: O(nlogn) and SC: O(n)
class Solution:
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0: ### corner case
            return 0

        start = sorted([meet[0] for meet in intervals])
        end = sorted([meet[1] for meet in intervals])
        start_P = 1 ### start from the second meeting, the first meeting has been counted
        end_P = 0
        roomNumber = 1
        MAX = 1
        while start_P < len(intervals):
            while end[end_P] <= start[start_P]:
                end_P += 1
                roomNumber -= 1
            start_P += 1
            roomNumber += 1
            MAX = max(MAX, roomNumber)

        return MAX