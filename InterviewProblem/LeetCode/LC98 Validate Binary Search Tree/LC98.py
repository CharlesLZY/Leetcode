'''
Leetcode 98. Validate Binary Search Tree

Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode 
# @return bool

### Inorder Traversal Solution
### TC: O(n) and SC: O(n)
class Solution:
    def isValidBST(self, root):
        traversal = []
        def inorder(node):
            if node:
                inorder(node.left)
                traversal.append(node.val)
                inorder(node.right)
        for i in range(1, len(traversal)-1):
            if traversal[i] > traversal[i+1]:
                return False
        return True

'''
Recursively checking whether left and right sub-tree are BST is not enough.
All node of left/right sub-tree must smaller/larger than the root.
'''

### Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    def isValidBST(self, root):
        def validate(node, low, high):
            if node:
                if low < node.val < high:
                    return validate(node.left, low, node.val) and validate(node.right, node.val, high)
                else:
                    return False
            else:
                return True

        return validate(root, float("-inf"), float("inf"))