'''
Leetcode 510. Inorder Successor in BST II

Description:
Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. 
'''

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None

# @param node Node 
# @return Node

### TC: O(H) and SC: O(1) 
class Solution:
    def inorderSuccessor(self, node):
        successor = None
        if node:
            if node.right:
                node = node.right
                while node:
                    successor = node
                    node = node.left
            else:
                while node.parent and node.parent.right == node:
                    node = node.parent
                successor = node.parent

        return successor