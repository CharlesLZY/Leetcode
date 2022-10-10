'''
Leetcode 684. Redundant Connection

Description:
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, 
with one additional edge added. The added edge has two different vertices chosen from 1 to n, 
and was not an edge that already existed. 
The graph is represented as an array edges of length n where edges[i] = [ai, bi] 
indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
If there are multiple answers, return the answer that occurs last in the input.
'''

# @param edges List[List[int]]
# @return List[int]

### DFS Solution (find the edge that forms the cycle)
### TC: O(n^2) and SC: O(n)
from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges):
        '''
        Trick: Keep adding edge to the graph.
        For a new edge(u,v), if both u and v have been in the graph, then DFS(u) to check whether u can already reach v
        '''
        graph = defaultdict(set)
        visited = set()
        def DFS(node, target):
            if node not in visited:
                visited.add(node)
                if node == target:
                    return True
                else:
                    for neighbour in graph[node]:
                        if DFS(neighbour, target):
                            return True
            return False
        
        for u, v in edges:
            visited.clear()
            if u in graph and v in graph and DFS(u,v):
                return [u,v]
            graph[u].add(v)
            graph[v].add(u)

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
            return True
        else:
            return False

class Solution:
    def findRedundantConnection(self, edges):
        disjointSet = DisjointSet(1001) ### in this problem, there are at most 1000 vertices
        for u, v in edges:
            if not disjointSet.union(u, v):
                return [u,v]