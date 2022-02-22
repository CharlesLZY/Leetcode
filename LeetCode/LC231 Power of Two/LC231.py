'''
Leetcode 231. Power of Two

Description:
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.
'''

# @param n int 
# @return bool

'''
Power of two has just one 1-bit.
'''
### TC: O(n) and SC: O(n)
class Solution:
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0