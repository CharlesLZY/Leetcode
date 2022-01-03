'''
Leetcode 112. Path Sum

Description:
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode 
# @param targetSum int 
# @return bool

### Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    def hasPathSum(self, root, targetSum):
        def DFS(node, res):
            if node.left is None and node.right is None:  ### leaf node
                if res + node.val == targetSum:
                    return True
                else:
                    return False
            else:
                return (DFS(node.left, res+node.val) if node.left else False) or (DFS(node.right, res+node.val) if node.right else False)
        if root is None: ### corner case
            return False
        return DFS(root, 0)


### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None: ### corner case
            return False
        stack = [(root,0)]
        while stack:
            node, res = stack.pop()
            if node.left is None and node.right is None:  ### leaf node
                if res + node.val == targetSum:
                    return True
                else:
                    continue  ### different from recursion solution, can not return False here, just continue
            else:
                if node.left:
                    stack.append((node.left, res+node.val))
                if node.right:
                    stack.append((node.right, res+node.val))
        return False


