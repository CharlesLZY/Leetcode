'''
JZ58 左旋转字符串

描述：
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列  S ，
请你把其循环左移 K 位后的序列输出。例如，字符序列 S = ”abcXYZdef” , 要求输出循环左移 3 位后的结果，即 “XYZdefabc” 
'''

# @param string str 
# @param n int
# @return str

### TC: O(n) and SC: O(n)
class Solution:
    def LeftRotateString(self, string, n):
        if len(string) <= 1: ### corner case 
            return string
        for i in range(n):
            string = string[1:] + string[0]
        return string