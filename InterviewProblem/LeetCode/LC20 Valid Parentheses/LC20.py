'''
Leetcode 20. Valid Parentheses

Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
'''

# @param s str 
# @return bool

### TC: O(n) and SC: O(n)
class Solution:
    def isValid(self, s):
        
        stack = []
        
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            
            elif s[i] == ")":
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if prev != "(":
                    return False 
            
            elif s[i] == "}":
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if prev != "{":
                    return False
            
            elif s[i] == "]":
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if prev != "[":
                    return False
            
        if len(stack) > 0:
            return False
        else:
            return True