'''
Leetcode 50. Pow(x, n)

Description:
Implement pow(x, n), which calculates x raised to the power n (i.e. x^n)
'''

# @param x float
# @param n int
# @return float

### TC: O(logn) and SC: O(1)
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -n
        '''
        Fast Power:
        bin(11) = '0b1011'
        a^11 = a^(2^0) * a^(2^1) * a^(2^3)
             = a       * a^2     * a^2^2^2
        '''
        def fastPower(b, n):
            ans = 1
            while n:
                if n&1: ### last bit is 1
                    ans *= b
                b *= b ### base
                n >>= 1
            return ans

        return fastPower(x, n)