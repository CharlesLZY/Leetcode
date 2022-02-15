'''
Leetcode 154. Find Minimum in Rotated Sorted Array II

Description:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,4,4,5,6,7] might become:
[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.
'''

# @param nums List[int] 
# @return int

### TC: O(logn) and SC: O(1)
class Solution:
    def findMin(self, nums):
        lp = 0
        rp = len(nums) - 1
        while lp < rp:
            if nums[lp] < nums[rp]:
                return nums[lp]

            mid = (lp + rp) // 2 ### the loop condition is lp < rp which ensures that rp > mid
            if nums[lp] < nums[mid]:
                lp = mid + 1
            elif nums[lp] > nums[mid]:
                rp = mid ### we must remain nums[mid]
            else: ### if mid == lp, it can only be 1 0 or 1 1. Because the 1 2 case will end at if nums[lp] < nums[rp]: return nums[lp]
                lp += 1

        return nums[lp]

### Another version
class Solution:
    def findMin(self, nums):
        lp = 0
        rp = len(nums)-1
        while lp < rp:
            if nums[lp] < nums[rp]:
                return nums[lp]
            mid = (lp + rp) // 2
            if nums[mid] > nums[rp]:
                lp = mid + 1
            elif nums[mid] < nums[rp]:
                rp = mid
            else:
                rp -= 1
        return nums[lp]