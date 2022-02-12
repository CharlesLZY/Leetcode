'''
Leetcode 1002. Find Common Characters

Description:
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
You may return the answer in any order.
'''

# @param words List[str]
# @return List[str]

'''
Choose a word as reference, keep shrinking the counter dictionary
'''
### TC: O(n) and SC: O(k) where k is the length of a single word
from collections import *
class Solution:
    def commonChars(self, words):
        ans = []
        if words:
            counter = Counter(words[0]) ### can be optimized to find the shortest word as initial counter
            for word in words[1:]:
                temp = Counter(word)
                toDel = []
                for char in counter:
                    if char in temp:
                        counter[char] = min(counter[char], temp[char])
                    else:
                        toDel.append(char)
                for char in toDel: ### during iteration dictionary size can not be changed
                    del counter[char]
            for char in counter:
                for i in range(counter[char]):
                    ans.append(char)
        return ans
