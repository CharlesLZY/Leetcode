'''
Leetcode 986. Interval List Intersections

Description:
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. 
For example, the intersection of [1, 3] and [2, 4] is [2, 3].
'''

# @param firstList List[List[int]]
# @param secondList List[List[int]]
# @return List[List[int]]

### TC: O(n) and SC: O(1)
class Solution:
    def intervalIntersection(self, firstList, secondList):
        ans = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            '''
            firstList: lp        rp
            secondList:      lp      rp
            '''
            lp = max(firstList[i][0], secondList[j][0])
            rp = min(firstList[i][1], secondList[j][1])
            if lp <= rp:
                ans.append([lp, rp])

            ### trick: remove the interval with the smallest endpoint
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans

### Intuitive Solution
class Solution:
    def intervalIntersection(self, firstList, secondList):
        ### nums[i] = 1 means [i,i+1) is occupied
        nums = [0] * 1000000 ### the actual constraint in this problem is 10^9
        for lp, rp in firstList:
            for i in range(lp, rp):
                nums[i] += 1
            nums[rp] += 0.1
        for lp, rp in secondList:
            for i in range(lp, rp):
                nums[i] += 1
            nums[rp] += 0.1

        res = []
        i = 0
        while i < len(nums):
            if nums[i] == 2:
                lp = i
                while (i < len(nums)) and (nums[i] == 2):
                    i += 1
                res.append([lp, i])
                i += 1 ### trick
            elif nums[i] == 1.1:
                res.append([i,i])
                i += 1
            else:
                i += 1
        return res

