'''
Leetcode 32. Longest Valid Parentheses

Description:
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''

# @param s str 
# @return int

### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def longestValidParentheses(self, s):
        ### stack will only store the latest invalid ')' position and all unpaired '(' position
        ### both of them will be substituted or eliminated by a new ')'
        stack = [-1] ### trick: initialize with -1 (the latest invalid ')' position)
        MAX = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else: ### s[i] == ')'
                if len(stack) == 1: ### in this case, all '(' are paired and the latest invalid ')' position need to be updated
                    stack[0] = i
                elif len(stack) > 1: ### still have unpaired '('
                    stack.pop()
                curLength = i - stack[-1]
                MAX = max(MAX, curLength)
        return MAX




