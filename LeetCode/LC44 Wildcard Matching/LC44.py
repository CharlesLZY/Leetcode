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
x
'''
The key is to check all the possibility of '*'
We tried to skip every '*', if match fails without the '*', backtrack to the previous star
'''
### Backtrack Solution
### TC: O(s) and SC: O(1)
class Solution:
    def isMatch(self, s, p):
        s_i, p_j = 0, 0
        match = -1 ### first location can be matched with *
        star = -1 ### lastest star
        while s_i < len(s):

            ### pattern does not run out
            if p_j < len(p) and p[p_j] == '*': 
                '''
                为什么可以不管之前的*
                s = abced
                p = *abc*d
                因为第二个*之前的都已经匹配上了，就不需要再考虑了，不会出现abc需要被s用上的情况，因为第二个*可以把后面如果再出现的abc都给指代了
                '''
                star = p_j ### so far we keep matched, we can abandon the former *, update the new *
                match = s_i
                p_j += 1
                ### in this branch we do not move s_i
                ### because we remain the possibility that * matches nothing
            elif p_j < len(p) and (s[s_i] == p[p_j] or p[p_j] == '?'): ### direct match
                s_i += 1
                p_j += 1
            
            ### if pattern runs out or we can not match directly, but we still have previous * to use
            elif star != -1: 
                p_j = star + 1 ### backtrack
                match += 1 
                s_i = match ### backtrack

            else: ### p runs out
                return False

        while p_j < len(p) and p[p_j] == '*':
            p_j += 1

        return p_j == len(p)

### Refer to LC10 Solution
class Solution:
    def isMatch(self, s, p):
        def match(s_i, p_j):
            if p_j >= len(p):
                return s_i == len(s)
            if p[p_j] == '*':
                if match(s_i, p_j+1):
                    return True
                else:
                    if s_i == len(s): ### trick: both branches need this if
                        return False
                    else:
                        return match(s_i+1,p_j)
            else:
                if s_i == len(s): ### trick: both branches need this if
                    return False
                else:
                    
                    if p[p_j] == '?' or s[s_i] == p[p_j]:
                        return match(s_i+1, p_j+1)
                    else:
                        return False
        
        return match(0,0)

### DP Solution (Refer to LC10 Solution, different from the Leetcode official solution)
### TC: O(s*p) and SC: O(s*p)
class Solution:
    def isMatch(self, s, p):
        ### DP[s_i][p_j] means whether s[s_i:] and p[p_j:] can match
        DP_table = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        DP_table[len(s)][len(p)] = True

        for s_i in range(len(s), -1, -1):
            for p_j in range(len(p)-1, -1, -1):
                if p[p_j] == '*':
                    DP_table[s_i][p_j] = DP_table[s_i][p_j+1] or (s_i < len(s) and DP_table[s_i+1][p_j])
                else:
                    if s_i < len(s):
                        direct_match = (p[p_j] == s[s_i]) or (p[p_j] == '?')
                        DP_table[s_i][p_j] = direct_match and DP_table[s_i+1][p_j+1]
                    else:
                        DP_table[s_i][p_j] = False
        
        return DP_table[0][0]
            
        

