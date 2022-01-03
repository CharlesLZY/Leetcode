'''
Leetcode 1. Two Sum

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

# @param nums List[int] 
# @param target int
# @return List[int]

### TC: O(n) and SC: O(n) 
class Solution:
    def twoSum(self, nums, target):
        hashTable = {}
        for i in range(len(nums)):
            complement = target - nums[i] ### to achieve one pass
            if complement in hashTable:
                return [i, hashTable[complement]]
            hashTable[nums[i]] = i