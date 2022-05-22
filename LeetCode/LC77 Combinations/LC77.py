'''
Leetcode 77. Combinations

Description:
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.
'''

# @param n int
# @param k int
# @return List[List[int]]

class Solution:
    def combine(self, n, k):
        ans = []
        def DFS(path, candidates):
            if len(path) == k:
                ans.append(path[:])
                return
            else:
                for i in range(len(candidates)):
                    path.append(candidates[i])
                    DFS(path, candidates[i+1:])
                    path.pop()
                return
        DFS([], [i for i in range(1, n+1)])
        return ans

### Optimized Version
class Solution:
    def combine(self, n, k):
        ans = []
        def DFS(path, start):
            if len(path) == k:
                ans.append(path[:])
                return
            else:
                for i in range(start, n+1):
                    path.append(i)
                    DFS(path, i+1) ### trick, exclude the former numbers
                    path.pop()
                return
        DFS([], 1)
        return ans