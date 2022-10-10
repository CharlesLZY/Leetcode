'''
Leetcode 127. Word Ladder

Description:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of 
words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
'''

# @param beginWord str
# @param endWord str
# wordList List[str] 
# @return int

### BFS Solution (BFS can ensure the current path is the shortest)
### TC: O(NL^2) and SC: O(NL^2) where L is the length of the words
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList: ### corner case
            return 0

        L = len(beginWord) ### all words have the same length

        patterns = {} ### build graph (this problem is a graph search)
        for word in wordList:
            for i in range(L):
                pattern = word[:i]+'*'+word[i+1:] ### we can only change one letter each time
                if pattern in patterns:
                    patterns[pattern].append(word)
                else:
                    patterns[pattern] = [word]


        queue = deque([(beginWord, 1)])
        visited = set([beginWord]) ### trick : graph search must maintain a visited list
        
        while queue:
            cur, depth = queue.popleft()
            if cur == endWord:
                return depth
            
            for i in range(L):
                pattern = cur[:i]+'*'+cur[i+1:]
                if pattern in patterns:
                    for word in patterns[pattern]:
                        if word not in visited: ### trick: must be here, or it will cause infinite loop
                            visited.add(word) ### trick: we can mark it as visited we append it into the queue
                            queue.append((word, depth+1))
                
        return 0


### Slow version
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList: ### corner case
            return 0

        L = len(beginWord) ### all words have the same length

        patterns = {}
        for word in wordList:
            for i in range(L):
                pattern = word[:i]+'*'+word[i+1:]
                if pattern in patterns:
                    patterns[pattern].append(word)
                else:
                    patterns[pattern] = [word]


        queue = deque([(beginWord, 1)])
        visited = set() ### trick : graph search must maintain a visited list
        
        while queue:
            cur, depth = queue.popleft()
            
            if cur == endWord:
                return depth
            visited.add(cur) ### the difference from the faster version
            
            for i in range(L):
                pattern = cur[:i]+'*'+cur[i+1:]
                if pattern in patterns:
                    for word in patterns[pattern]:
                        if word not in visited: ### trick: must be here, or it will cause infinite loop
                            queue.append((word, depth+1))
                
        return 0



