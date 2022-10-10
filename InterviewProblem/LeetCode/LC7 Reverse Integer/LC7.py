'''
Leetcode 7. Reverse Integer

Description:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

# @param x int
# @return int

class Solution:
    def reverse(self, x):
        if x == 0:
            return 0
        sign = 1 if x >= 0 else -1
        res = 0
        if sign == -1:
            x = -x
        ### skip zeors in the tail
        while x % 10 == 0:
            x = x // 10
        while x != 0:
            if res > (pow(2,31)-1)//10 or (res == (pow(2,31)-1)//10 and x % 10 > pow(2,31) % 10):
                return 0
            res = res * 10 + x % 10
            x = x // 10
        
        return res * sign