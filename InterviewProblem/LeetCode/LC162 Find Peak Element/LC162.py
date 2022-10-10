'''
Leetcode 162. Find Peak Element

Description:
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -inf.

Constraint: nums[i] != nums[i + 1] for all valid i.

You must write an algorithm that runs in O(log n) time.
'''

# @param nums List[int]
# @return int

### TC: O(logn) and SC: O(1)
class Solution:
    def findPeakElement(self, nums):
        lp = 0
        rp = len(nums)-1
        while lp < rp:
            mid = (lp + rp) // 2
            if nums[mid] > nums[mid+1]: ### then on the left half, there must be a peak, if the left half is strictly descending, then nums[0] is the peak
                rp = mid
                '''
                Strictly descending left half, then nums[0] is the peak
                     \
                      \
                      mid
                        \
                        mid+1

                else, somehow there will be a peak on the left half
                    peak
                    / \
                      mid
                        \
                        mid+1
                '''
            elif nums[mid] < nums[mid+1]: ### nums[i] != nums[i + 1] for all valid i for this problem
                lp = mid + 1
                '''
                Strictly ascending right half, the nums[-1] is the peak
                         /
                        /
                      mid+1
                      /
                    mid

                else, somehow there will be a peak on the right half
                        peak
                        / \
                      mid+1
                      /
                    mid
                '''
        return lp