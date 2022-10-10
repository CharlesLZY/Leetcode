'''
JZ50 第一个只出现一次的字符

描述：
在一个字符串中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回-1。
'''

# @param str string字符串 
# @return int整型

### TC: O(n) and SC: O(n)
class Solution:
    def FirstNotRepeatingChar(self, string):
        hashTable = {}
        for i in range(len(string)):
            char = string[i]
            if char in hashTable:
                hashTable[char] += 1
            else:
                hashTable[char] = 1

        for i in range(len(string)):
            if hashTable[string[i]] == 1:
                return i
        return -1 ### corner case