'''
Leetcode 538. Convert BST to Greater Tree

Description:
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:
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
# @return TreeNode

### Recursion Solutiom
### TC: O(n) and SC: O(n)
class Solution:
    res = 0
    def convertBST(self, root):
        self.res = 0
        def inorder(node):
            if node:
                inorder(node.right)
                self.res += node.val
                node.val = self.res
                inorder(node.left)
        inorder(root)
        return root

### Stack Solutiom (refer to LC94)
### TC: O(n) and SC: O(n)
class Solution:
    def convertBST(self, root):
        if root is None: ### corner case
            return None
        res = 0
        stack = [root]
        while stack:
            if stack[-1]: 
                stack.append(stack[-1].right)
            else:
                stack.pop()
                if stack:
                    node = stack.pop()
                    res += node.val
                    node.val = res
                    stack.append(node.left)
        return root

