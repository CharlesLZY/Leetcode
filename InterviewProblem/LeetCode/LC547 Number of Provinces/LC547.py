'''
Leetcode 547. Number of Provinces

Description:
There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 
if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''

# @param isConnected List[List[int]]
# @return int

### BFS solution (similar to LC200)
### TC: O(n^2) and SC: O(n)
class Solution:
    def findCircleNum(self, isConnected):
        ### isConnected is the adjacent matrix
        N = len(isConnected) ### the number of nodes
        ans = 0
        visited = [False]*N
        for i in range(N):
            if visited[i]:
                continue
            ans += 1
            queue = [i]
            visited[i] = True
            while queue:
                cur = queue.pop(0)
                for j in range(N):
                    if (isConnected[cur][j] == 1) and not visited[j]:
                        queue.append(j)
                        visited[j] = True
        return ans

### Disjoint Set Soluion
### TC: O(E*α(V)) and SC: O(V)
class DisjointSet:
    def __init__(self, size):
        self.root = [-1 for _ in range(size)] ### root[x] < 0 means that it is the root of a disjoint tree

    def find(self, x):
        if self.root[x] < 0:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.root[root_x] < self.root[root_y]:
                self.root[root_y] = root_x
            elif self.root[root_x] > self.root[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.root[root_x] -= 1

class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        disjointSet = DisjointSet(n)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    disjointSet.union(i, j)
        return len([r for r in disjointSet.root if r < 0]) ### how many disjoint tree roots are there