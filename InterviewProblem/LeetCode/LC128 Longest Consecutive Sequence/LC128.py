'''
Leetcode 128. Longest Consecutive Sequence

Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

# @param nums List[int]
# @return int

### TC: O(n) and SC: O(n)
class Solution:
    def longestConsecutive(self, nums):
        hashTable = set(nums) ### trick: hashTable support O(1) find operation
        MAX = 0
        for num in nums:
            curLength = 1
            if num+1 not in hashTable: ### trick: when the consecutive sequence finished, then count the length
                while num-1 in hashTable:
                    curLength += 1
                    # hashTable.remove(num-1) ### can be deleted
                    num -= 1
                MAX = max(MAX, curLength)
        return MAX

class Solution:
    def longestConsecutive(self, nums):
        hashTable = set(nums) ### trick: hashTable support O(1) find operation
        MAX = 0
        for num in nums:
            curLength = 1
            if num-1 not in hashTable: ### trick: when the consecutive sequence finished, then count the length
                while num+1 in hashTable:
                    curLength += 1
                    
                    num += 1
                MAX = max(MAX, curLength)
        return MAX

### TC: O(nlogn) and SC: O(1)
class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        nums.sort()
        MAX = 1
        curLength = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                curLength += 1
                MAX = max(MAX, curLength)
            else:
                curLength = 1

        return MAX