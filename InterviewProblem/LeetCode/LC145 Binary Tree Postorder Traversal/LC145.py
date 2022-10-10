'''
Leetcode 145. Binary Tree Postorder Traversal

Description:
Given the root of a binary tree, return the postorder traversal of its nodes' values.
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
    def postorderTraversal(self, root):
        ans = []
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                ans.append(node.val)
        postorder(root)
        return ans


### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def postorderTraversal(self, root):
        if root is None: ### corner case
            return []
        ans = []
        stack = [(root, False)]
        while stack:
            node, done = stack.pop()
            if done:
                ans.append(node.val)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        return ans
