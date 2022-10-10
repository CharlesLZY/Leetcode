'''
Leetcode 323. Number of Connected Components in an Undirected Graph

Description:
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] 
indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example:
Input: n = 5 edges = [[0,1],[1,2],[3,4]]
Output: 2
'''

# @param n int
# @param edges List[List[int]]
# @return int

### BFS Solution (refer to LC547)
### TC: O(E+V) and SC: O(E+V)
from collections import defaultdict
class Solution:
    def countComponents(self, n, edges):
        adjacent_table = defaultdict(set)
        for p,q in edges: ### build adjacent table
            adjacent_table[p].add(q)
            adjacent_table[q].add(p)

        ans = 0
        visited = [False]*n
        for i in range(n):
            if visited[i]:
                continue
            ans += 1
            queue = [i]
            visited[i] = True
            while queue:
                cur = queue.pop(0)
                for neighbour in adjacent_table[cur]:
                    if not visited[neighbour]:
                        queue.append(neighbour)
                        visited[neighbour] = True
        
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
    def countComponents(self, n, edges):
        disjointSet = DisjointSet(n)
        for u,v in edges:
            disjointSet.union(u, v)
        return len([r for r in disjointSet.root if r < 0]) ### how many disjoint tree roots are there