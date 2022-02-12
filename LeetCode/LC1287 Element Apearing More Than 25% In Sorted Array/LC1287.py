'''
Leetcode 1287. Element Appearing More Than 25% In Sorted Array

Description:
Given an integer array sorted in non-decreasing order, 
there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
'''

# @param arr List[int]
# @return int

### IntuitiveSolution
### TC: O(n) and SC: O(1)
class Solution:
    def findSpecialInteger(self, arr):
        gap = len(arr) // 4
        for i in range(len(arr)):
            if i+ gap > len(arr)-1:
                break ### in this problem, the mode must exist, this branch will never enter
            if arr[i+gap] == arr[i]:
                return arr[i]

