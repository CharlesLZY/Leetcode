'''
Leetcode 3. Longest Substring Without Repeating Characters

Description:
Given a string s, find the length of the longest substring without repeating characters.
'''

# @param s str 
# @return int

### Sliding Wwindow Solution
### TC: O(n) and SC: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        MAX = 0
        hashTable = [0] * 128 ### ASIIC 
        lp = 0 
        for i in range(len(s)):
            cur = s[i]
            hashTable[ord(cur)] += 1
            while hashTable[ord(cur)] > 1: ### keeping narrowing the interval
                hashTable[ord(s[lp])] -= 1
                lp += 1
            MAX = max(MAX, i - lp + 1)
        return MAX


### Skip solution
### TC: O(n) and SC: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        MAX = 0
        hashTable = [-1] * 128 ### ASIIC 
        lp = 0 ### the left end of current subsring without repeating characters
        for i in range(len(s)):
            cur = s[i]
            if hashTable[ord(cur)] >= lp: ### the repeated char occurs in the window, default is -1 (never occur)
                lp = hashTable[ord(cur)] + 1 ### skip the left pointer
            hashTable[ord(cur)] = i ### update to latest index
            MAX = max(MAX, i - lp + 1)
        return MAX
