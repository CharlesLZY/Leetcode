'''
Leetcode 34. Find First and Last Position of Element in Sorted Array

Description:
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
'''

# @param nums List[int]
# @param target int
# @return List[int]

'''
Binary search twice for low boundary and high bounday
'''

### TC: O(logn) and SC: O(1)
class Solution:
    def searchRange(self, nums, target):
        def findLow():
            lp = 0
            rp = len(nums)-1
            while lp <= rp:
                mid = (lp + rp) // 2
                if nums[mid] < target:
                    lp = mid + 1
                elif nums[mid] > target:
                    rp = mid - 1
                else:
                    if mid > 0 and nums[mid-1] != target:
                        return mid
                    elif mid == 0:
                        return mid
                    else:
                        rp = mid - 1
            return -1

        def findHigh():
            lp = 0
            rp = len(nums)-1
            while lp <= rp:
                mid = (lp + rp) // 2
                if nums[mid] < target:
                    lp = mid + 1
                elif nums[mid] > target:
                    rp = mid - 1
                else:
                    if mid+1 < len(nums) and nums[mid+1] != target:
                        return mid
                    elif mid == len(nums)-1:
                        return mid
                    else:
                        lp = mid + 1
            return -1



        return [findLow(), findHigh()]

