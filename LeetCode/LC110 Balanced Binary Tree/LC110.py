'''
Leetcode 110. Balanced Binary Tree

Description:
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return bool

### Easy to understand
class Solution:
    def isBalanced(self, root):
        def depth(node):
            if node is None:
                return 0
            else:
                return max(depth(node.left), depth(node.right)) + 1

        if root is None:
            return True
        else:
            if abs(depth(root.left) - depth(root.right)) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)

### Optimized Solution
### TC: O(n) and SC: O(n)
class Solution:
    def isBalanced(self, root):
        def depth(node):
            if node is None:
                return 0
            left = depth(node.left)
            if left == -1:
                return -1 ### not balanced
            right = depth(node.right)
            if right == -1:
                return -1 ### not balanced
            if abs(left - right) > 1:
                return -1 ### not balanced
            else:
                return max(left, right) + 1

        return depth(root) != -1