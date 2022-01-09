'''
JZ10 斐波那契数列

描述：
大家都知道斐波那契数列，现在要求输入一个正整数 n ，请你输出斐波那契数列的第 n 项。
'''

# @param n int整型 
# @return int整型

### Replicated computation TC: O(2^n)
class Solution:
    def Fibonacci(self, n):
        if n <= 2:
            return 1
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)

### TC: O(n) and SC: O(n)
class Solution:
    def __init__(self):
        self.DP_table = [0] * 50

    def Fibonacci(self , n):
        if n <= 2:
            return 1
        if self.DP_table[n] > 0:
            return self.DP_table[n]
        else:
            self.DP_table[n] = self.Fibonacci(n-1) + self.Fibonacci(n-2)
            return self.DP_table[n]

### TC: O(n) and SC: O(1)
class Solution:
    def Fibonacci(self, n):
        if n <= 2:
            return 1
        prev1 = 1
        prev2 = 1
        ans = None
        for i in range(3, n+1):
            ans = prev1 + prev2
            prev1, prev2 = prev2, ans
        return ans  