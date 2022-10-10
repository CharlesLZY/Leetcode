'''
Leetcode 438. Find All Anagrams in a String

Description:
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

# @param s str 
# @param p str 
# @return List[int]

### TC: O(n) and SC: O(1) (O(1) is because there are only constant number of characters)
from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p): ### corner case
            return []
        ans = []
        template = Counter(p)
        counter = Counter()
        lp = 0 ### left pointer

        for rp in range(len(s)):
            cur = s[rp]
            counter[cur] += 1
            while counter[cur] > template[cur] and lp <= rp:
                counter[s[lp]] -= 1
                if counter[s[lp]] == 0:
                    del counter[s[lp]]
                lp += 1 ### move on
            if counter == template:
                ans.append(lp)

        return ans

### Array Version
class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p): ### corner case
            return []
        ans = []
        template = [0]*26 ### the constraints of this problem is that s and p are consist of lowercase English letters.
        counter = [0]*26
        for char in p:
            template[ord(char)-ord('a')] += 1

        lp = 0 ### left pointer

        for rp in range(len(s)):
            cur = s[rp]
            counter[ord(cur)-ord('a')] += 1
            while counter[ord(cur)-ord('a')] > template[ord(cur)-ord('a')] and lp <= rp:
                counter[ord(s[lp])-ord('a')] -= 1
                lp += 1 ### move on
            if counter == template:
                ans.append(lp)

        return ans
