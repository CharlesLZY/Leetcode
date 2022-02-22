'''
Leetcode 543. Diameter of Binary Tree

Description:
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return int

'''
Similar to LC124
'''
'''
            1
          /   \
         2     5
        / \
       3   4

'''


### TC: O(n) and SC: O(n)
class Solution:
    MAX = 0
    def diameterOfBinaryTree(self, root):
        self.MAX = 0
        def maxHalfPath(node):
            if node is None:
                return -1
            leftPath = maxHalfPath(node.left)
            rightPath = maxHalfPath(node.right)
            ### left -> root -> right is always longer than left -> root or right -> root
            self.MAX = max(self.MAX, leftPath + rightPath + 2) ### trick: leftPath + rightPath (without + 1), middle node has no contribution to the length of path
            return max(leftPath, rightPath) + 1

        maxHalfPath(root)
        return self.MAX