'''
Leetcode 153. Find Minimum in Rotated Sorted Array

Description:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.
(旋转次数和正常人类理解的不一样，就是翻折了一次)
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

# @param nums List[int]
# @return int

'''
无论哪种写法都是rp = mid, 所以只能mid = (lp+rp) // 2 不能+1
'''

### General Solution (tolerant of duplicate numbers)
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

### General Solution (tolerant of duplicate numbers)
### TC: O(logn) and SC: O(1)
class Solution:
    def findMin(self, nums):
        lp = 0
        rp = len(nums) - 1
        while lp < rp:
            if nums[lp] < nums[rp]:
                return nums[lp]

            mid = (lp + rp) // 2 
            if nums[rp] < nums[mid]:
                lp = mid + 1
            elif nums[rp] > nums[mid]:
                rp = mid ### we must remain nums[mid]
            else: ### the loop condition is lp < rp which ensures that rp > mid
                rp -= 1

        return nums[lp]

### Specific Solution for array with unique elements
class Solution:
    def findMin(self, nums):
        lp = 0
        rp = len(nums) - 1
        if nums[lp] <= nums[rp]:
            return nums[0]

        while lp <= rp:
            mid = (lp + rp) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            if mid - 1 >= 0 and nums[mid-1] > nums[mid]:
                return nums[mid]

            if nums[0] < nums[mid]: ### trick
                lp = mid + 1
            else:
                rp = mid - 1


class Solution:
    def findMin(self, nums):
        lp = 0
        rp = len(nums) - 1
        if nums[lp] <= nums[rp]:
            return nums[0]

        while lp <= rp:
            mid = (lp + rp) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            if nums[lp] > nums[mid]:
                rp = mid - 1
            else:
                lp = mid + 1