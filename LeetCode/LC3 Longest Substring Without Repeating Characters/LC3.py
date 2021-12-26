'''
Leetcode 3. Longest Substring Without Repeating Characters

Description:
Given a string s, find the length of the longest substring without repeating characters.
'''

# @param s str 
# @return int

### Sliding window solution
### TC: O(n) and SC: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        MAX = 0
        hashTable = [0] * 128 ### ASIIC 
        j = 0 ###
        for i in range(len(s)):
            cur = s[i]
            hashTable[ord(cur)] += 1
            while hashTable[ord(cur)] > 1: ### keeping narrowing the interval
                hashTable[ord(s[j])] -= 1
                j += 1
            MAX = max(MAX, i - j + 1)
        return MAX


### Skip solution
### TC: O(n) and SC: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        MAX = 0
        hashTable = [-1] * 128 ### ASIIC 
        j = 0 ###
        for i in range(len(s)):
            cur = s[i]s
            if hashTable[ord(cur)] >= j: ### the repeated char occurs in the window
                j = hashTable[ord(cur)] + 1
            hashTable[ord(cur)] = i
            MAX = max(MAX, i - j + 1)
        return MAX
