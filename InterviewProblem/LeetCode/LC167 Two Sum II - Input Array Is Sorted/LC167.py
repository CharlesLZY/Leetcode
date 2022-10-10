'''
Leetcode 167. Two Sum II - Input Array Is Sorted

Description:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''

# @param nums List[int]
# @param target int
# @return List[int]

### TC: O(n) and SC: O(1)
class Solution:
    def twoSum(self, nums, target):
        lp = 0
        rp = len(nums)-1

        while lp < rp:
            temp = nums[lp] + nums[rp]
            if temp == target:
                return [lp+1, rp+1] ### stupid requirement
            elif temp < target:
                lp += 1
            else:
                rp -= 1
