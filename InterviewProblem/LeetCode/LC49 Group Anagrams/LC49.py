'''
Leetcode 49. Group Anagrams

Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

# @param strs List[str] 
# @return List[List[str]]

### Brute Solution
### TC: O(nklogk) and SC: O(nk)
class Solution:
    def groupAnagrams(self, strs):
        Dict = {}
        for s in strs:
            pattern = tuple(sorted(s))
            if pattern in Dict:
                Dict[pattern].append(s)
            else:
                Dict[pattern] = [s]
        return Dict.values()

### Optimized Solution
### TC: O(nk) and SC: O(nk)
class Solution:
    def groupAnagrams(self, strs):
        Dict = {}
        for s in strs:
            count = [0]*26 ### we can not use Counter because it is unhashable
            for char in s:
                count[ord(char) - ord('a')] += 1
            count = tuple(count)
            if count in Dict:
                Dict[count].append(s)
            else:
                Dict[count] = [s]
        return Dict.values()