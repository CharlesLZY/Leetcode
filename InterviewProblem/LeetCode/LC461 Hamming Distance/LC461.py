'''
Leetcode 461. Hamming Distance

Description:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Example:
Input: x = 1 (0 0 0 1), y = 4 (0 1 0 0)
Output: 2
'''

# @param x int
# @param y int
# @return int

class Solution:
    def hammingDistance(self, x, y):
        # return bin(x ^ y).count('1') 
        xor = x ^ y
        distance = 0
        while xor:
            # mask out the rest bits
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance
