'''
Leetcode 111. Minimum Depth of Binary Tree

Description:
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return int

'''
这题直接写一个depth(root)是行不通的，因为depth找的是maxDepth
'''

### TC: O(n) and SC: O(n)
class Solution:
    def minDepth(self, root):
        if not root: ### corner case: empty tree
            return 0 
        
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left: ### avoid that the non-leaf node being considered as the end of a path
            return self.minDepth(root.left) + 1
        elif root.right: ### avoid that the non-leaf node being considered as the end of a path
            return self.minDepth(root.right) + 1
        else: ### leaf node
            return 1

class Solution:
    res = float("inf")
    def minDepth(self, root):
        self.res = float("inf")
        def DFS(node, depth):
            if node:
                if node.left or node.right:
                    DFS(node.left, depth + 1)
                    DFS(node.right, depth + 1)
                else:
                    self.res = min(self.res, depth + 1)

        if root is None: ### corner case: empty tree
            return 0

        DFS(root, 0)
        return self.res


class Solution:
    def minDepth(self, root):
        if root is None: ### corner case: empty tree
            return 0
        
        stack = [(root, 1)]
        MIN_depth = float("inf")
        while stack:
            node, depth = stack.pop()
            if node.left or node.right:
                if node.left:
                    stack.append((node.left, depth+1))
                if node.right:
                    stack.append((node.right, depth+1))
            else:
                MIN_depth = min(MIN_depth, depth)
        return MIN_depth

