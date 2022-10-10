'''
Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal

Description:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and 
inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param preorder List[int] 
# @param inorder List[int]
# @return TreeNode

### Recursive Solution
### TC: O(n) and SC: O(n)
class Solution:
    def buildTree(self, preorder, inorder):
        if preorder:
            root = TreeNode(preorder[0])
            idx = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
            root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
            return root
        else:
            return None

