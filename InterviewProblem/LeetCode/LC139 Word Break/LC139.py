'''
Leetcode 139. Word Break

Description:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

# @param s str 
# @param wordDict List[str] 
# @return bool

### Recursion Solution
### TC: O(n^2) and SC: O(n^2)
class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict) ### key point (enable O(1) find operation)
        visited = [] ### key point
        def DFS(idx): ### idx is the current char location
            if idx in visited: ### key point: to avoid repeated recursion
                return False
            if idx == len(s):
                return True
            for i in range(idx, len(s)):
                if s[idx:i+1] in wordDict:
                    if DFS(i+1):
                        return True
            visited.append(idx) ### key point: to avoid repeated recursion (s[:i] can have several combination possibilities)
            return False
        return DFS(0)

### Stack Solution
### TC: O(n^2) and SC: O(n)
class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict) ### key point (enable O(1) find operation)
        stack = [0]
        visited = [] ### key point
        while stack:
            idx = stack.pop()
            if idx == len(s):
                return True
            if idx in visited: ### key point
                continue
            for i in range(idx, len(s)):
                if s[idx:i+1] in wordDict:
                    stack.append(i+1)
            visited.append(idx) ### key point
        return False


### DP Solution
### TC: O(n^2) and SC: O(n)
class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict) ### key point (enable O(1) find operation)
        DP_table = [False]*(len(s)+1) ### DP[i] means whether s[:i] can be seperated into the words in wordDict
        DP_table[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if DP_table[j] and s[j:i] in wordDict:
                    DP_table[i] = True
                    break

        return DP_table[len(s)]



