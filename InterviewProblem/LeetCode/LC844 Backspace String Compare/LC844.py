'''
Leetcode 844. Backspace String Compare

Description:
Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace(删除) character.

Note that after backspacing an empty text, the text will continue empty.
'''

# @param s str 
# @param t str 
# @return bool

### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def parse(s):
            stack = []
            for char in s:
                if char == '#':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack)
        return parse(s) == parse(t)

### Iterator Solution
### TC: O(n) and SC: O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def curChar(s):
            skip = 0
            for char in s[::-1]:
                if char == '#':
                    skip += 1
                else:
                    if skip > 0:
                        skip -= 1
                    else:
                        yield char
        
        sIter, tIter = curChar(s), curChar(t) ### iterator
        while True:
            s = next(sIter, "EOF")
            t = next(tIter, "EOF")
            if s == "EOF" and t == "EOF":
                return True
            elif s != t:
                return False
            else:
                continue