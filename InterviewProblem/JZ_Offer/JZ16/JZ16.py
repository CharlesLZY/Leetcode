'''
JZ16 数值的整数次方
描述：
实现函数 double Power(double base, int exponent)，求base的exponent次方。
'''

# @param base float 
# @param exponent int
# @return float

### TC: O(logn) and SC: O(1)
class Solution:
    def Power(self, base, exponent):
        if exponent < 0:
            base = 1/base
            exponent = -exponent

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

        return fastPower(base, exponent)
