'''
Leetcode 285. Inorder Successor in BST

Description:
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. 
If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param root TreeNode
# @param p TreeNode
# @return TreeNode

### TC: O(n) and SC: O(1) if the BST is balanced, TC will be O(logn)
class Solution:
    def inorderSuccessor(self, root, p):
        successor = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
