'''
Leetcode 115. Distinct Subsequences

Description:
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string 
by deleting some (can be none) of the characters without disturbing 
the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.
'''

# @param s str 
# @param t str 
# @return int

### DP Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def numDistinct(self, s, t):
        DP_table = [[0]*(len(t)) for _ in range(len(s))] ### DP[i][j] : # distinct subseq of s[:i] equals to t[:j]
        if s[0] == t[0]:
            DP_table[0][0] = 1
        ### Base Case 
        for i in range(1, len(s)): ### first column of the DP table
            DP_table[i][0] = DP_table[i-1][0] + (1 if s[i] == t[0] else 0)
        
        for i in range(1, len(s)):
            for j in range(1, min(i+1, len(t))): ### DP[i][j] = 0 where j > i
                DP_table[i][j] = DP_table[i-1][j] + (DP_table[i-1][j-1] if s[i] == t[j] else 0)
        
        return DP_table[-1][-1]








