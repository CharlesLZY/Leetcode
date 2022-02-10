'''
Leetcode 387. First Unique Character in a String

Description:
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

# @param s str 
# @return int

### TC: O(n) and SC: O(1) (Because the number of chars is limited)
class Solution:
    def firstUniqChar(self, s):
        hashTable = [0]*26 ### English alphabet only has 26 letters
        for char in s:
            hashTable[ord(char)-ord('a')] += 1

        for idx, char in enumerate(len(s)):
            if hashTable[ord(char)-ord('a')] == 1:
                return idx

        return -1