'''
Leetcode 190. Reverse Bits

Description:
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. 
In this case, both input and output will be given as a signed integer type. 
They should not affect your implementation, as the integer's internal binary representation is the same, 
whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. 
Therefore, in Example 2 above, the input represents the signed integer -3 and 
the output represents the signed integer -1073741825.
'''

# @param n int
# @return int

### TC: O(n) and SC: O(n)
class Solution:
    def reverseBits(self, n):
        res = 0
        power = 31 
        while n != 0:
            res += (n & 1) << power
            n = n >> 1
            power -= 1
        return res
