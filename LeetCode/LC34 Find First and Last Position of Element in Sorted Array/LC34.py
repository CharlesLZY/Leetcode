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


### Another Solution
### TC: O(logn) and SC: O(1)
class Solution:
    def searchRange(self, nums, target):
        def search(target):
            lp = 0
            rp = len(nums)
            while lp < rp:
                mid = (lp + rp) // 2
                if nums[mid] >= target:
                    rp = mid
                else:
                    lp = mid + 1
            return lp
        
        lp = search(target)
        rp = search(target+1)-1
        
        if rp < lp: ### not found
            return [-1,-1]
        else:
            return [lp, rp]

### Another Solution
### TC: O(logn) and SC: O(1)
class Solution:
    def searchRange(self, nums, target):
        def search(n): ### we want to find the position before n
            lp = 0
            rp = len(nums) - 1
            while lp <= rp:
                mid = (lp + rp) // 2
                if nums[mid] > n:
                    rp = mid - 1
                elif nums[mid] < n:
                    lp = mid + 1
                elif nums[mid] == n:
                    rp = mid - 1 ### trick: rp can be -1
            # return min(lp,rp)
            return rp ### find first number less than n
        
        lp = search(target)
        rp = search(target+1)
        
        if rp <= lp: ### not found
            return [-1,-1]
        
        return [lp+1, rp]