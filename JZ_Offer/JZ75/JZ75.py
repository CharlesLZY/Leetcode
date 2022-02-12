'''
JZ75 字符流中第一个不重复的字符

描述：
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符 "go" 时，第一个只出现一次的字符是 "g" 。当从该字符流中读出前六个字符 “google" 时，第一个只出现一次的字符是"l"。

如果当前字符流没有存在出现一次的字符，返回#字符。
'''

class Solution:
    hashTable = [0]*128
    queue = []
    def FirstAppearingOnce(self):
        while self.queue: ### can not use for char in queue because queue can not be modified while iteration
            char = self.queue[0]
            if self.hashTable[ord(char)] > 1:
                self.queue.pop(0)
            else:
                return char
        return '#'


    def Insert(self, char):
        if self.hashTable[ord(char)] == 0:
            self.queue.append(char)
        self.hashTable[ord(char)] += 1
