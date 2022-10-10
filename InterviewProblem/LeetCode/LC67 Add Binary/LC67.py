'''
Leetcode 67. Add Binary

Description:
Given two binary strings a and b, return their sum as a binary string.
'''

# @param a str 
# @param b str 
# @return str

### TC: O(n) and SC: O(1)
from itertools import zip_longest
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        a = a[::-1]
        b = b[::-1]
        carry = 0
        for n1, n2 in zip_longest(a,b, fillvalue=0):
            temp = int(n1) + int(n2) + carry
            ans.append(temp % 2)
            carry = temp // 2
        if carry == 1:
            ans.append(1)
        ans.reverse()
        return "".join([str(n) for n in ans])
