'''
Leetcode 10. Regular Expression Matching

Description:
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
    - '.' Matches any single character.
    - '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
'''

# @param s string
# @param p string
# @return bool

### Recursive Solution
class Solution:
    def isMatch(self, s, p):
        ### s stride always 1, p stride can be 1 or 2
        def match(s_i, p_j): ### match s[s_i:] with p[p_j:]
            if p_j >= len(p): ### p is run out
                return s_i == len(s) ### if s is also run out, then whole string is 

            ### judgement for s_i cannot be placed here, testcase: s="aa" p="a*"

            if p_j + 1 < len(p) and p[p_j + 1] == "*": ### handle _* pattern
                if match(s_i, p_j+2): ### if we skip this _*, the string can be matched
                    return True
                else: ### if skip current _* pattern will not lead to a successful match, then we have to match it
                    ### trick: important to check whether s has run out
                    if s_i == len(s): ### s is run out, but skiping current _* will not give a successful match, then failed
                        ### example case: s = abc p = .*c                              
                        return False ### in this case p has not run out
                    else:
                        if (p[p_j] == "." or s[s_i] == p[p_j]): ### arbitrary entry .* or _ matched with _*
                            return match(s_i+1, p_j) ### p_j stays, because next turn will keep trying to skip current _*
                        else: ### fail to match current _* pattern
                            return False
                        
            else: ### without * postfix, the pattern can not be skiped and must be matched
                ### trick: important to check whether s has run out
                if s_i == len(s): ### s is run out, p still has remains
                    ### example case: s = abc p = .*c  
                    return False
                else:
                    if (p[p_j] == "." or s[s_i] == p[p_j]): ### arbitrary entry . or _ matched with _
                        return match(s_i+1, p_j+1) ### move forward
                    else:  ### fail to match current pattern
                        return False

        return match(0,0)

### DP Solution
class Solution:
    def isMatch(self, s, p):
        DP_table = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        ### the DP_table need to be filled from bottom to top
        ### DP[i][j] means whether s[i:] is valid according to p[j:] 
        DP_table[len(s)][len(p)] = True ### empty string empty pattern 
        for s_i in range(len(s), -1, -1):
            for p_j in range(len(p) - 1, -1, -1): ### starting from len(p) - 1 , DP_table[len(s)][len(p)] = True and DP_table[s_i < len(s)][len(p)] = False
                direct_match = s_i < len(s) and (p[p_j] == s[s_i] or p[p_j] == '.') ### at first we need have string to match (s_i < len(string)?), then we consider whether the current pattern is matched
                if p_j+1 < len(p) and p[p_j+1] == '*': ### we can skip the current _* or match it
                    ### if skip the current _* pattern, the result will depend on the successor match dp[s_i][p_j+2]
                    ### if directly match the current _* pattern, the result will depend on whether the current pattern is matched and the successor match dp[s_i+1][p_j]
                    DP_table[s_i][p_j] = DP_table[s_i][p_j+2] or (direct_match and DP_table[s_i+1][p_j])
                else: ### without * postfix, we have to match the current pattern
                    DP_table[s_i][p_j] = direct_match and DP_table[s_i+1][p_j+1] ### the result depends on whether the current pattern is matched and the successor match dp[s_i+1][p_j+1]
        return DP_table[0][0]








