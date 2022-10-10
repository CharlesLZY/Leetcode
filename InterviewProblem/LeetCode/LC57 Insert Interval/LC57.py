'''
Leetcode 57. Insert Interval

Description:
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent 
the start and the end of the ith interval and intervals is sorted in ascending order by start_i. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and 
intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
'''

# @param intervals List[List[int]]
# @param newInterval List[int]
# @return List[List[int]]

### TC: O(n) and SC: O(1)
class Solution:
    def insert(self, intervals, newInterval):
        '''
        [[1,3], [8,10]] [2,9]/[0,4]/[5,11]/[0,11]/[-1,0]/[2,5]/[9,11]
        1. [l, r] l and r both are in the intervals
        2. [l, r] l and r both are not in the intervals
        3. [l, r] l in the intervals
        4. [l, r] r in the intervals

        intervals = [[1,3], [8,10]]
        case1:
        newInterval = [2,9] ### 0 True 1 True
        case2:
        newInterval = [-1,0] ### 0 false 0 false
        newInterval = [11,12] ### 2 false 2 false
        newInterval = [0,4] ### 0 false 1 false
        newInterval = [5,11] ### 1 false 2 false
        newInterval = [0,11] ### 0 false 2 false
        case3:
        newInterval = [2,5] ### 0 true 1 false
        case4:
        newInterval = [9,11] ### 1 true 2 false
        
        '''
        def search(target):
            flag = False ### whether target is in any intervals
            lp = 0
            rp = len(intervals) - 1
            while lp <= rp:
                mid = (lp + rp) // 2
                if intervals[mid][0] <= target and intervals[mid][1] >= target:
                    flag = True
                    return mid, flag
                elif intervals[mid][1] < target:
                    lp = mid + 1
                else:
                    rp = mid - 1

            return lp, flag ### trick: return lp because lp ranges from 0 to len(arr)
        
        left, flag1 = search(newInterval[0])
        right, flag2 = search(newInterval[1])
        if flag1 and flag2: ### case 1
            return intervals[:left] + [[intervals[left][0], intervals[right][1]]] + intervals[right+1:]
        elif flag1: ### case 3
            return intervals[:left] + [[intervals[left][0], newInterval[1]]] + intervals[right:]
        elif flag2: ### case 4
            return intervals[:left] + [[newInterval[0], intervals[right][1]]] + intervals[right+1:]
        else: ### case 2
            return intervals[:left] + [newInterval] + intervals[right:]


        

