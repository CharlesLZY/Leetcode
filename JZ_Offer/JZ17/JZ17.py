'''
JZ17 打印从1到最大的n位数

描述：
输入正整数 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
用返回一个整数列表来代替打印
'''

# @param n int
# @return List[int]

class Solution:
    def printNumbers(self, n):
        N = 10**n
        res = []
        for i in range(1,N):
            res.append(i)
        return res