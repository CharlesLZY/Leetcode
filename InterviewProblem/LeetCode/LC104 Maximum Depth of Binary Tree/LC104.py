'''
Leetcode 104. Maximum Depth of Binary Tree

Description:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return int

### TC: O(n) and SC: O(n)
class Solution:
    def maxDepth(self, root):
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else:
            return 0

class Solution:
    res = 0
    def maxDepth(self, root):
        self.res = 0
        def DFS(node, depth):
            if node:
                self.res = max(self.res, depth + 1)
                DFS(node.left, depth + 1)
                DFS(node.right, depth + 1)
        DFS(root, 0)
        return self.res

class Solution:
    def maxDepth(self, root):
        if root is None: ### corner case: empty tree
            return 0
        
        stack = [(root, 1)]
        MAX_depth = float("-inf")
        while stack:
            node, depth = stack.pop()
            if node.left or node.right:
                if node.left:
                    stack.append((node.left, depth+1))
                if node.right:
                    stack.append((node.right, depth+1))
            else:
                MAX_depth = max(MAX_depth, depth)
        return MAX_depth

