'''
Leetcode 630. Course Schedule III

Description:
There are n different online courses numbered from 1 to n. 
You are given an array courses where courses[i] = [durationi, lastDayi] indicate that 
the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

Example:
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3 (taking course 0, 1 and 2)
'''

# @param courses List[List[int]] 
# @return int

### Greedy Solution 
### TC: O(nlogn) and SC: O(n)
from heapq import *
class Solution:
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x:x[1]) ### trick: sort according to the deadline

        maxHeap = []
        cur_time = 0
        for time, deadline in courses:
            if cur_time + time <= deadline: ### greedy, as long as we can take the course, we take it
                heappush(maxHeap, -time) ### trick: max heap
                cur_time += time
            else: ### cur_time + time > deadline
                if maxHeap and -maxHeap[0] > time:
                    heappush(maxHeap, -time) ### trick: max heap
                    cur_time += time
                    cur_time -= -heappop(maxHeap) ### remove older course with longer time
        
        return len(maxHeap)