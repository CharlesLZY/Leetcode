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
            '''
            如果不是因为题目要求返回两个数的index，其实用set就可以了，hash已经包含了complement的信息
            3sum那题就可以用hashTable[complement]记录pivot的index用来判断这个解是不是重复的
            '''
            hashTable[nums[i]] = i

### Follow up: if there are multiple solutions
from collections import defaultdict
class Solution:
    def twoSum(self, nums, target):
        res = []
        hashTable = defaultdict(list)
        for i in range(len(nums)):
            complement = target - nums[i] ### to achieve one pass
            if complement in hashTable:
                for j in hashTable[complement]:   
                    res.append([i, j])
            hashTable[nums[i]].append(i)
        return res
