'''
Leetcode 889. Construct Binary Tree from Preorder and Postorder Traversal

Description:
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values 
and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param s str 
# @return int

### TC: O(n) and SC: O(n)
class Solution:
    def constructFromPrePost(self, pre, post):
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])

        if len(pre) > 1:
            leftBranch = pre[1] ### assume it has left branch
            loc = post.index(leftBranch)
            root.left = self.constructFromPrePost(pre[1:loc+1+1], post[:loc+1])
            root.right = self.constructFromPrePost(pre[loc+1+1:], post[loc+1: len(post)-1])
        return root