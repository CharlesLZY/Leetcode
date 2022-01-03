'''
Leetcode 207. Course Schedule

Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
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

        def DFS(course):
            visited[course] = True
            lookup[course] = True
            for neighbour in adjMatrix[course]:
                if lookup[neighbour]: ### cyclic
                    return True
                elif not visited[neighbour]:
                    if DFS(neighbour):
                        return True
            lookup[course] = False ### reset, only being used for this round of cycle checking
            return False

        for course in range(numCourses):
            if not visited[course] and DFS(course):
                return False
        return True
