'''
JZ15 二进制中1的个数

描述：
输入一个整数 n ，输出该数32位二进制表示中1的个数。其中负数用补码表示。
'''

'''
正数和0 的补码就是该数字本身。 负数的补码则是将其对应正数按位取反再加1，代码实现：n & 0xffffffff。 
补码系统的最大优点是可以在加法或减法处理中，不需因为数字的正负而使用不同的计算方式。
'''

# @param n int 
# @return int

class Solution:
    def NumberOf1(self, n):
        ans = 0
        if n<0:
            n = n & 0xffffffff ### Negative number converted to Two's complement
        while n != 0:
            if n & 1:
                ans += 1
            n = n >> 1
        return ans