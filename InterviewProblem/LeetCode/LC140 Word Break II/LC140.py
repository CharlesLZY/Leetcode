'''
Leetcode 140. Word Break II

Description:
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence 
where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

# @param s str 
# @param wordDict List[str]
# @return List[str]

'''
LC139&LC140 类似于 LC127&LC126的关系
'''

class Solution:
    def wordBreak(self, s, wordDict):
        def generatePath(path):
            if path:
                res = s[:path[0]]
                if len(path) > 1:
                    for i in range(1, len(path)):
                        res += " "
                        res += s[path[i-1]:path[i]]
                return res

        ans = []
        wordDict = set(wordDict) 
        stack = [[0, []]]
        while stack:
            idx, path = stack.pop()
            if idx == len(s):
                ans.append(generatePath(path))
                continue
            for i in range(idx, len(s)):
                if s[idx:i+1] in wordDict:
                    stack.append([i+1, path+[i+1]])
        return ans
        