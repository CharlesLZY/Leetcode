'''
Leetcode 205. Isomorphic Strings

Description:
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
'''

# @param s str
# @param t str 
# @return bool

### Intuitive Solution
### TC: O(n) and SC: O(n) (pattern string needs O(n))
class Solution:
    def isIsomorphic(self, s, t):
        def parse(string):
            res = ""
            record = {}
            for char in string:
                if char in record:
                    res += record[char]
                else:
                    record[char] = chr(ord('a')+len(record))
                    res += record[char]
            return res

        return parse(s) == parse(t)


### Mapping Solution
### TC: O(n) and SC: O(1)
class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t): ### corner case
            return False
        mapping_s_t = {}
        mapping_t_s = {}
        for i in range(len(s)):
            if s[i] not in mapping_s_t and t[i] not in mapping_t_s:
                mapping_s_t[s[i]] = t[i]
                mapping_t_s[t[i]] = s[i]
            elif s[i] not in mapping_s_t or t[i] not in mapping_t_s:
                return False
            else:
                if mapping_s_t[s[i]] != t[i] or mapping_t_s[t[i]] != s[i]:
                    return False
        return True

