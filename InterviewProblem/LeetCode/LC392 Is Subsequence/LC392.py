'''
Leetcode 392. Is Subsequence

Description:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
i.e., "ace" is a subsequence of "abcde" while "aec" is not
'''

# @param s str 
# @param t str 
# @return bool

### Two Pointer Solution
### TC: O(n) and SC: O(1)
class Solution:
    def isSubsequence(self, s, t):
        p1 = 0
        p2 = 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        return p1 == len(s)