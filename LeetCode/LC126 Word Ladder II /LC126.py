'''
Leetcode 126. Word Ladder II

Description:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of 
words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, 
return all the shortest transformation sequences from beginWord to endWord, 
or an empty list if no such sequence exists. 
Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
'''

# @param beginWord str
# @param endWord str
# wordList List[str] 
# @return List[List[str]]:

'''
这题和LC127不一样，一个word只能在从queue中pop出来以后才能算标记为visited，而不能在进queue前被标记为visited，
在从queue中pop出来之后标记成visited，可以保证从beginword到这个word的path是最小的，但其他路径在同一深度依然可以把
这个word放进queue中
'''
from collections import deque
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList: ### corner case
            return []

        L = len(beginWord) ### all words have the same length

        patterns = {} ### build graph (this problem is a graph search)
        for word in wordList:
            for i in range(L):
                pattern = word[:i]+'*'+word[i+1:] ### we can only change one letter each time
                if pattern in patterns:
                    patterns[pattern].append(word)
                else:
                    patterns[pattern] = [word]

        ans = []
        minDepth = -1
        queue = deque([[beginWord, [beginWord]]])
        visited = set() ### trick : graph search must maintain a visited list
        
        while queue:
            cur, path = queue.popleft()
            if minDepth != -1 and len(path) > minDepth:
                break
            if cur == endWord:
                if minDepth == -1:
                    minDepth = len(path)
                ans.append(path[:])
                continue

            visited.add(cur) 
            
            for i in range(L):
                pattern = cur[:i]+'*'+cur[i+1:]
                if pattern in patterns:
                    for word in patterns[pattern]:
                        if word not in visited: ### trick: must be here, or it will cause infinite loop
                            queue.append([word, path+[word]])
                
        return ans





