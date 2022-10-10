'''
Leetcode 437. Path Sum III

Description:
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @param targetSum int
# @return int

class Solution:
    res = 0
    def pathSum(self, root, targetSum):
        self.res = 0
        def DFS(node, curSum):
            if node:
                curSum += node.val
                if curSum == targetSum:
                    self.res += 1
                DFS(node.left, curSum) ### keep searching
                DFS(node.right, curSum) ### keep searching

        def startPathFrom(node):
            if node:
                DFS(node, 0)
                startPathFrom(node.left)
                startPathFrom(node.right)

        startPathFrom(root)
        return self.res
