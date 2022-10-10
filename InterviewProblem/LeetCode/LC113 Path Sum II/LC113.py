'''
Leetcode 113. Path Sum II

Description:
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode 
# @param targetSum int 
# @return List[List[int]]

### Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    def pathSum(self, root, targetSum):
        ans = []
        def DFS(node, res, path):
            ### 不能if node is None: return 因为这样会误判叶节点
            res += node.val
            path.append(node.val)
            if node.left is None and node.right is None:  ### leaf node
                if res == targetSum:
                    ans.append(path[:])
            else:
                if node.left:
                    DFS(node.left, res, path)
                if node.right:
                    DFS(node.right, res, path)
            path.pop() ### backtrack

        if root is None: ### corner case
            return []

        DFS(root, 0, [])
        return ans


### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def pathSum(self, root, targetSum):
        ans = []
        if root is None: ### corner case
            return []

        stack = [(root, 0, [])]
        while stack:
            node, res, path = stack.pop()
            path.append(node.val)
            res = res + node.val
            if node.left is None and node.right is None: ### leaf node
                if res == targetSum:
                    ans.append(path[:])
            else:
                if node.left:
                    stack.append((node.left, res, path[:]))
                if node.right:
                    stack.append((node.right, res, path[:]))
        return ans

