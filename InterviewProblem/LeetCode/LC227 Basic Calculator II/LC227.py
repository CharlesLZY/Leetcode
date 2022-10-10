'''
Leetcode 227. Basic Calculator II

Description:
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Constraints:
- s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
- s represents a valid expression.
'''

# @param s str 
# @return int

'''
This problem is easy, we do not need to consider parenthesis.
'''

'''
维护numStack和operatorStack
遇到一个新的operator, 如果优先级小于等于operatorStack之前的operator, 就把前面所有优先级高的operator处理掉
每处理完一个operator, 把结果push回numStack
在这题里面栈里面最多只会有一个'+'或'-'和一个'*'或'/'
'''

### TC: O(n) and SC: O(n)
class Solution:
    def calculate(self, s):

        raw = s.split(' ')
        s = ''.join(raw) ### remove all white space

        numStack = [] ### initialize with 0 to handle the case that the first number is negative
        operatorStack = []

        def cal():
            nonlocal numStack, operatorStack
            num2 = numStack.pop()
            num1 = numStack.pop()
            operator = operatorStack.pop()
            if operator == '+':
                numStack.append(num1 + num2)
            elif operator == '-':
                numStack.append(num1 - num2)
            elif operator == '*':
                numStack.append(num1 * num2)
            elif operator == '/':
                numStack.append(int(num1 / num2))

        i = 0
        if s[0] == '-': ### trick: avoid negative number corner case
            numStack.append(0)
            operatorStack.append('-')
            i += 1


        while i < len(s):

            if s[i].isdigit():
                num = int(s[i])
                while i+1 < len(s) and s[i+1].isdigit():
                    i += 1
                    num *= 10
                    num += int(s[i])
                numStack.append(num)
                i += 1

            elif s[i] == '+':
                if len(operatorStack) == 0:
                    operatorStack.append('+')
                else: ### handle the previous operator in the stack
                    while len(operatorStack) > 0:
                        cal()
                    operatorStack.append('+')
                i += 1

            elif s[i] == '-':
                if len(operatorStack) == 0:
                    operatorStack.append('-')
                else: ### handle the previous operator in the stack
                    while len(operatorStack) > 0:
                        cal()
                    operatorStack.append('-')
                i += 1

            elif s[i] == '*':
                if len(operatorStack) == 0 or operatorStack[-1] == '+' or operatorStack[-1] == '-':
                    operatorStack.append('*')
                else: ### handle the previous operator in the stack
                    cal()
                    operatorStack.append('*')
                i += 1

            elif s[i] == '/':
                if len(operatorStack) == 0 or operatorStack[-1] == '+' or operatorStack[-1] == '-':
                    operatorStack.append('/')
                else: ### handle the previous operator in the stack
                    cal()
                    operatorStack.append('/')
                i += 1


        while operatorStack: ### at last, operator may contains two operator one is '-' or '+', another will be '*' or '/'
            cal()



        
        return numStack[-1]