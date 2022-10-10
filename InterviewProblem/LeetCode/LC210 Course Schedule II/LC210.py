'''
Leetcode 210. Course Schedule II

Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, 
return any of them. If it is impossible to finish all courses, return an empty array.

Example:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
'''

# @param numCourses int
# @param prerequisites List[List[int]] 
# @return List[int]

### Topological Sort Solution
### TC: O(V+E) and SC: O(V+E)
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = {}
        for n in range(numCourses):
            graph[n] = set() ### we can not use defaultdict here, because some courses have no in-degree but they still should appears in nodes
        for course, preq in prerequisites:
            graph[preq].add(course)

        nodes = list(graph.keys())
        in_degree = defaultdict(int)
        for node in nodes:
            for succ in graph[node]:
                in_degree[succ] += 1
        
        res = []
        queue = [node for node in nodes if in_degree[node] == 0] ### new zero in-degree nodes
        while queue:
            node = queue.pop(0)
            res.append(node) ### if a node's in-degree becomes 0, push it into res

            for succ in graph[node]:
                in_degree[succ] -= 1
                if in_degree[succ] == 0:
                    queue.append(succ) ### append new zero in-degree nodes

        ### if res does not contain all nodes in the graph, then the graph has cycle
        if len(res) != numCourses: ### not all nodes can be reduced to 0 in-degree
            return []

        return res