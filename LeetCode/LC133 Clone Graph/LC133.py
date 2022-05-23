'''
Leetcode 133. Clone Graph

Description:
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
'''

# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

# @param node Node
# @return Node

### TC: O(n) and SC: O(n)
class Solution:
    def cloneGraph(self, node):
        self.visited = {} ### trick: if node has been visited, return it from the visited dictionary
        def clone(node):
            if node in self.visited:
                return self.visited[node]

            copy = Node(node.val, [])
            self.visited[node] = copy
            if node.neighbors:
                copy.neighbors = [clone(n) for n in node.neighbors]

            return copy

        if node:
            return clone(node)
        else:
            return None












