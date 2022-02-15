'''
Leetcode 268. Missing Number

Description:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

# @param nums List[int] 
# @return int

### Sort Solution
### TC: O(nlogn) and SC: O(1)
class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums) ### the only left one is n

### Hash Set Solution
### TC: O(n) and SC: O(n)
class Solution:
    def missingNumber(self, nums):
        hashTable = set(nums)
        for i in range(len(nums)+1):
            if i not in hashTable:
                return i

### Sum Solution
### TC: O(n) and SC: O(1)
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        S = int(n * (n+1) / 2)
        return S - sum(nums)

### XOR Solution
### TC: O(n) and SC: O(1)
class Solution:
    def missingNumber(self, nums):
        res = 0
        for i in range(1, len(nums)+1):
            res ^= i

        for n in nums:
            res ^= n

        return res