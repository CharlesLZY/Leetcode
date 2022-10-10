'''
Leetcode 30. Substring with Concatenation of All Words

Description:
You are given a string s and an array of strings words of the same length. 
Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Example
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
'''

# @param s str 
# @param words List[str]
# @return List[int]

### TC: O(n^2logn) and SC: O(n)
class Solution:
    def findSubstring(self, s, words):
        n, w = len(words), len(words[0])
        words.sort()
        def check(string):
            combo = []
            for i in range(0,len(string), w):
                combo.append(string[i:i+w])
            return sorted(combo) == words

        ans = []
        lp = 0
        for rp in range(w*n, len(s)+1):
            if check(s[lp:rp]):
                ans.append(lp)
            lp += 1
        return ans 


