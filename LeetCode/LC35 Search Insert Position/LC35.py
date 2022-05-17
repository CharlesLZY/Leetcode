'''
Leetcode 35. Search Insert Position

Description:
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

# @param nums List[int]
# @param target int
# @return int

### TC: O(logn) and SC: O(1)
class Solution:
    def searchInsert(self, nums, target):
        lp = 0
        rp = len(nums)-1
        while lp <= rp:
            mid = (lp + rp) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lp = mid + 1
            else:
                rp = mid - 1
        return lp

### Another Version
class Solution:
    def searchInsert(self, nums, target):
        lp = 0
        rp = len(nums)-1
        while lp < rp:
            mid = (lp + rp) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rp = mid
            else:
                lp = mid + 1
        if nums[lp] < target:
            return lp + 1
        else:
            return lp