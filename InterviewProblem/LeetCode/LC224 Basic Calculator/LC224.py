'''
Leetcode 224. Basic Calculator

Description:
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Constraints:
- s consists of digits, '+', '-', '(', ')', and ' '.
- s represents a valid expression.
- '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
- '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
- There will be no two consecutive operators in the input.
'''

# @param s str 
# @return int

'''
This problem is just the apetizer, which only contains + and -. We can treat '-' as add a negative number.
'''

### Intuitive Solution
### TC: O(n) and SC: O(n)
class Solution:
    def calculate(self, s):
        def findRP(s, idx): ### find paired right parenthesis in s[idx:]
            count = 1
            for i in range(idx, len(s)):
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    count -= 1
                if count == 0:
                    return i

        def cal(formula):
            res = 0
            i = 0
            while i < len(formula):
                sign = 1

                while i < len(formula) and formula[i] == ' ': ### skip white spaces
                    i += 1
                if i == len(formula): 
                    break

                if formula[i] == '-':
                    sign = -1
                    i += 1
                elif formula[i] == '+':
                    i += 1

                while formula[i] == ' ': ### skip white spaces
                    i += 1

                if formula[i] == '(':
                    rp = findRP(formula, i+1)
                    res += sign * cal(formula[i+1:rp])
                    i = rp + 1

                elif formula[i].isdigit():
                    num = int(formula[i])
                    while i+1 < len(formula) and formula[i+1].isdigit():
                        i += 1
                        num *= 10
                        num += int(formula[i])
                    res += num * sign
                    i += 1
                
            return res

        return cal(s)


'''
维护numStack和operatorStack
遇到一个新的operator, 如果优先级小于等于operatorStack之前的operator, 就把前面所有优先级高的operator处理掉
每处理完一个operator, 把结果push回numStack
在这题里面栈里面最多只会有一个'+'或'-'
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

            elif s[i] == '(':
                operatorStack.append('(')
                i += 1
                if s[i] == '-': ### trick: avoid negative number corner case
                    numStack.append(0)
                    operatorStack.append('-')
                    i += 1

            elif s[i] == '+':
                if len(operatorStack) == 0 or operatorStack[-1] == '(':
                    operatorStack.append('+')
                else: ### handle the previous operator in the stack
                    cal()
                    operatorStack.append('+')
                i += 1

            elif s[i] == '-':
                if len(operatorStack) == 0 or operatorStack[-1] == '(':
                    operatorStack.append('-')
                else: ### handle the previous operator in the stack
                    cal()
                    operatorStack.append('-')
                i += 1

            elif s[i] == ')':
                while operatorStack[-1] != '(':
                    cal()
                operatorStack.pop() ### pop the '('
                i += 1

        if operatorStack:
            cal()

        
        return numStack[-1]




