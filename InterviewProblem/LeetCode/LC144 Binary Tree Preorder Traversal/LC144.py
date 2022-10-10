'''
Leetcode 144. Binary Tree Preorder Traversal

Description:
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return List[int]

### Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    def preorderTraversal(self, root):
        ans = []
        def preorder(node):
            if node:
                ans.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ans


### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def preorderTraversal(self, root):
        if root is None: ### corner case
            return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right: ### trick: push right node first, LIFO
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans