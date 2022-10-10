'''
JZ64 求1+2+3+...+n

描述：
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

'''
这都是什么几把玩意儿
'''

# @param n int
# @return int

class Solution:
    def Sum_Solution(self, n):
        '''
        exp1 and exp2
        if exp1 == False, exp2 will not be executed
        '''
        return n and n + self.Sum_Solution(n-1) ### ex1 and exp2 ... and exp_n will return the exp_n

