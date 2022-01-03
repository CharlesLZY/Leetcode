'''
Leetcode 226. Invert Binary Tree

Description:
Given the root of a binary tree, invert the tree, and return its root.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return TreeNode

### TC: O(n) and SC: O(n)
class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
