'''
Leetcode 136. Single Number

Description:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

# @param nums List[int]
# @return int

'''
A XOR 0 = A
A XOR A = 0
A XOR B = B XOR A
(A XOR B) XOR C = A XOR (B XOR C) 
'''

### TC: O(n) and SC: O(1)
class Solution:
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res ^= n
        return res