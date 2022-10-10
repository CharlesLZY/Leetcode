'''
Leetcode 14. Longest Common Prefix

Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

# @param strs List[str] 
# @return str

### TC: O(n) and SC: O(1)
class Solution:
    def longestCommonPrefix(self, strs):
        idx = 0
        while True:
            if len(strs[0]) <= idx:
                break
            
            cur = strs[0][idx]
            matched = True
            for s in strs:
                if len(s) <= idx:
                    matched = False
                    break
                if s[idx] != cur:
                    matched = False
                    break
            if matched:
                idx += 1
            else:
                break
        return strs[0][:idx]