'''
Leetcode 81. Search in Rotated Sorted Array II

Description:
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
'''

# @param nums List[int]
 # @param target int
# @return bool

### TC: O(logn) and SC: O(1)
class Solution:
    def search(self, nums, target):
        def findPivot():
            lp = 0
            rp = len(nums) - 1

            while lp < rp:
                if nums[lp] <= nums[rp]: ### this line is the key point
                    return lp

                mid = (lp + rp) // 2
                if nums[mid] > nums[rp]: 
                    lp = mid + 1
                elif nums[mid] < nums[rp]:
                    rp = mid
                else:
                    rp -= 1 ### trick

            return lp

        def binarySearch(low, high):
            lp = low
            rp = high
            while lp <= rp:
                mid = (lp + rp) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    lp = mid + 1
                else:
                    rp = mid - 1

            return False

        ### THE MOST IMPORTANT TRICK！！！
        while len(nums)> 1 and nums[0] == nums[-1]: ### trick: remove the duplicates at the end
            nums.pop()

        pivotIdx = findPivot()
        # if pivotIdx == 0:
        #     return binarySearch(0, len(nums)-1)
        # elif nums[pivotIdx] > target:
        #     return False
        # elif nums[pivotIdx-1] < target:
        #     return False
        # elif nums[pivotIdx] <= target <= nums[-1]:
        #     return binarySearch(pivotIdx, len(nums)-1)
        # else:
        #     return binarySearch(0, pivotIdx-1)
        return binarySearch(0, pivotIdx-1) or binarySearch(pivotIdx, len(nums)-1)



class Solution:
    def search(self, nums, target):
        def findPivot():
            lp = 0
            rp = len(nums) - 1

            while lp < rp:
                if nums[lp] <= nums[rp]: ### this line is the key point
                    return lp

                mid = (lp + rp) // 2
                if nums[mid] > nums[lp]:
                    lp = mid + 1
                elif nums[mid] < nums[lp]:
                    rp = mid
                else:
                    lp += 1 ### trick

            return lp

        def binarySearch(low, high):
            lp = low
            rp = high
            while lp <= rp:
                mid = (lp + rp) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    lp = mid + 1
                else:
                    rp = mid - 1

            return False

        ### THE MOST IMPORTANT TRICK！！！
        while len(nums)> 1 and nums[0] == nums[-1]: ### trick: remove the duplicates at the end
            nums.pop(0)

        pivotIdx = findPivot()
        # if pivotIdx == 0:
        #     return binarySearch(0, len(nums)-1)
        # elif nums[pivotIdx] > target:
        #     return False
        # elif nums[pivotIdx-1] < target:
        #     return False
        # elif nums[pivotIdx] <= target <= nums[-1]:
        #     return binarySearch(pivotIdx, len(nums)-1)
        # else:
        #     return binarySearch(0, pivotIdx-1)
        return binarySearch(0, pivotIdx-1) or binarySearch(pivotIdx, len(nums)-1)

