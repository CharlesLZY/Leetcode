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
                curLength = i - stack[-1] ### i is current parentheses end and stack[-1] is the lastes invalid ')'
                MAX = max(MAX, curLength)
        return MAX

### Two Pass Solution
### TC: O(n) and SC: O(1)
class Solution:
    def longestValidParentheses(self, s):
        ans = 0
        ### the first pass
        n_lp = 0
        n_rp = 0
        for char in s:
            if char == '(':
                n_lp += 1
            elif char == ')':
                n_rp += 1
            if n_lp == n_rp:
                ans = max(ans, n_lp+n_rp)
            elif n_lp < n_rp: ### impossible to form a valid parentheses
                n_lp = 0
                n_rp = 0
            else:
                pass

        ### the second pass
        n_lp = 0
        n_rp = 0
        for char in s[::-1]:
            if char == '(':
                n_lp += 1
            elif char == ')':
                n_rp += 1
            if n_lp == n_rp:
                ans = max(ans, n_lp+n_rp)
            elif n_rp < n_lp: ### impossible to form a valid parentheses
                n_lp = 0
                n_rp = 0
            else:
                pass

        return ans










