'''
JZ71 跳台阶扩展问题

描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶(n为正整数)总共有多少种跳法。
'''

# @param number int 
# @return int

'''
f[n]   = f[n-1] + f[n-2] + .. + f[1] + f[0]
f[n-1] =          f[n-2] + .. + f[1] + f[0]
f[n] = 2 * f[n-1] 
'''

class Solution:
    def jumpFloorII(self, number):
        return 2**(number-1)