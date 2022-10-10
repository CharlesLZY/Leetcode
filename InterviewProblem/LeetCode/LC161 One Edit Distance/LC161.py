'''
Leetcode 161. One Edit Distance

Description:
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
A string s is said to be one distance apart from a string t if you can:
- Insert exactly one character into s to get t.
- Delete exactly one character from s to get t.
- Replace exactly one character of s with a different character to get t.
'''

# @param s str 
# @param t str 
# @return bool

### TC: O(n) and SC: O(n)
class Solution:
    def isOneEditDistance(self, s, t):
        if abs(len(s)-len(t)) > 1:
            return False
        if len(t) > len(s):
            s, t = t, s

        if len(s) == len(t):
            n_diff = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    n_diff += 1
            return n_diff == 1
        else:
            n_diff = 0
            j = 0
            for i in range(len(s)): ### len(s) = len(t) + 1
                if j < len(t) and s[i] == t[j]:
                    j += 1
                else:
                    n_diff += 1
                    continue
            return n_diff == 1
