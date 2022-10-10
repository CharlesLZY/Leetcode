'''
JZ43 整数中1出现的次数（从1到n整数中1出现的次数）

描述：
输入一个整数 n ，求 1～n 这 n 个整数的十进制表示中 1 出现的次数
例如， 1~13 中包含 1 的数字有 1 、 10 、 11 、 12 、 13 因此共出现 6 次
注意：11 这种情况算两次
'''

'''
什么几把题，无不无聊。

用数学归纳法证明这个规律：
0-9（1个9）中有1*10^0个1
0-99（2个9）中有2*10^1个1
0-999（3个9）中有3*10^2个1
0-9999（4个9）中有4*10^3个1
...
'''

# @param n int 
# @return int

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        res = 0
        for i in range(1,n+1):
            while i > 0:
                if i % 10 == 1:
                    res += 1
                i = i // 10
        return res




