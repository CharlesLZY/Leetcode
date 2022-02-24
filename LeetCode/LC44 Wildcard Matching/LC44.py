'''
Leetcode 44. Wildcard Matching

Description:
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
- '?' Matches any single character.
- '*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
'''

# @param s str
# @param p str
# @return bool

### Backtrack Solution
### TC: O(s) and SC: O(1)
class Solution:
    def isMatch(self, s, p):
        s_i, p_j = 0, 0
        match = -1 ### first location can be matched with *
        star = -1 ### lastest star
        while s_i < len(s):
            if p_j < len(p) and (s[s_i] == p[p_j] or p[p_j] == '?'):
                s_i += 1
                p_j += 1
            elif p_j < len(p) and p[p_j] == '*':
                star = p_j ### so far we keep matched, we can abandon the former *, supdate the new *
                match = s_i
                p_j += 1
                ### in this branch we do not move s_i
                ### because we remain the possibility that * matches nothing
            elif star != -1: ### if we have no choose but to use *
                p_j = star + 1
                match += 1
                s_i = match
            else:
                return False

        while p_j < len(p) and p[p_j] == '*':
            p_j += 1

        return p_j == len(p)
