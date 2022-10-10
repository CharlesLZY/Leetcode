'''
Leetcode 87. Scramble String

Description:
We can scramble a string s to get a string t using the following algorithm:
1. If the length of the string is 1, stop.
2. If the length of the string is > 1, do the following:
    - Split the string into two non-empty substrings at a random index, 
      i.e., if the string is s, divide it to x and y where s = x + y.
    - Randomly decide to swap the two substrings or to keep them in the same order. 
      i.e., after this step, s may become s = x + y or s = y + x.
    - Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, 
return true if s2 is a scrambled string of s1, otherwise, return false.
'''

# @param s1 str 
# @param s2 str 
# @return bool

### Recursion with memorization
### TC: O(n^2) SC: O(n^2)
class Solution:
    def isScramble(self, s1, s2):
        DP_table = {}

        def DFS(s1, s2):
            if s1 == s2:
                return True
            else:
                state = s1+s2
                if state in DP_table:
                    return DP_table[state]
                else:
                    res = False
                    for i in range(1, len(s1)):
                        ### -/-
                        ### s[i:] + s[:i]
                        ### Swap
                        left = s1[i:]
                        right = s1[:i]
                        res = res or (DFS(left, s2[:len(left)]) and DFS(right, s2[len(left):]))
                        if res:
                            break
                        ### Not Swap
                        res = res or (DFS(s1[:i], s2[:i]) and DFS(s1[i:], s2[i:]))
                        if res:
                            break

                    DP_table[state] = res
                    return res
        
        return DFS(s1, s2)

