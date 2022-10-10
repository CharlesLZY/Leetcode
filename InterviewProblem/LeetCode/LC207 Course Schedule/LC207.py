'''
Leetcode 207. Course Schedule

Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example:
Input: numCourses = 4, prerequisites = [[1,0],[0,1]]
Output: false
'''

# @param numCourses int 
# @param prerequisites List[List[int]]
# @return bool


'''
The problem is to check whether a directed graph is acyclic.
'''
class Solution:
    def canFinish(self, numCourses, prerequisites):
        ### Build graph first
        adjMatrix = [[] for _ in range(numCourses)] ### adjacency matrix
        for course, preq in prerequisites:
            adjMatrix[preq].append(course)

        visited = [False] * numCourses
        lookup = [False] * numCourses ### trick: temporarily look-up record to decide whether there is cycle in this round

        def findCycle(course): ### find cycle
            visited[course] = True
            lookup[course] = True
            for succ in adjMatrix[course]:
                if lookup[succ]: ### cyclic
                    return True
                elif not visited[succ]: ### trick: avoid repeated checks
                    if findCycle(succ):
                        return True
            lookup[course] = False ### reset, only being used for this round of cycle checking
            return False

        for course in range(numCourses):
            if not visited[course] and findCycle(course): ### findCycle(course) equals to select the course first, check whether course itself has any prerequisite pointing to it
                return False
        return True

### Another way to build graph
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        ### Build graph first
        graph = defaultdict(set)
        for course, preq in prerequisites:
            graph[preq].add(course)
        
        visited = [False] * numCourses
        lookup = [False] * numCourses ### trick: temporarily look-up record to decide whether there is cycle in this round

        def findCycle(course): ### find cycle
            visited[course] = True
            lookup[course] = True
            for succ in graph[course]:
                if lookup[succ]: ### cyclic
                    return True
                elif not visited[succ]: ### trick: avoid repeated checks
                    if findCycle(succ):
                        return True
            lookup[course] = False ### reset, only being used for this round of cycle checking
            return False

        for course in range(numCourses):
            if not visited[course] and findCycle(course): ### findCycle(course) equals to select the course first, check whether course itself has any prerequisite pointing to it
                return False
        return True

### Another Solution to find cycle
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(set)
        visited = set()
        def DFS(node, target):
            # print(node, target)
            if node not in visited:
                visited.add(node)
                if node == target:
                    return True
                else:
                    for neighbour in graph[node]:
                        if DFS(neighbour, target):
                            return True
            return False
        
        for course, preq in prerequisites:
            visited.clear()
            if course == preq:
                return False
            if course in graph and preq in graph and DFS(course, preq):
                return False
            graph[preq].add(course)
            if course not in graph:
                graph[course] ### add course to the graph
        
        return True