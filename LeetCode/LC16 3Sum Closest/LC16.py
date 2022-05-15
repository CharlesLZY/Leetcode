'''
Leetcode 16. 3Sum Closest

Description:
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''

# @param nums List[int]
# @param target int 
# @return int

### TC: O(n^2) and SC: O(n)
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        MIN_diff = float("inf") ### min diff

        for i in range(len(nums)):
            pivot = nums[i]
            lp = i + 1
            rp = len(nums)-1
            while lp < rp:
                temp = pivot + nums[lp] + nums[rp]
                diff = temp - target

                if abs(diff) < abs(MIN_diff):
                    MIN_diff = diff

                if temp > target:
                    rp -= 1
                elif temp < target:
                    lp += 1
                else:
                    return target

        return target + MIN_diff

