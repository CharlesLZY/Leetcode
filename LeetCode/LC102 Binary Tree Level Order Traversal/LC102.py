'''
Leetcode 102. Binary Tree Level Order Traversal

Description:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return List[List[int]]

### Queue Solution
class Solution:
    def levelOrder(self, root):
        result = []
        if root is None: ### corner case
            return result
        
        queue = [(root,0)]
        
        while queue:
            root, level = queue.pop(0)
            if len(result) <= level:
                result.append([])
            result[level].append(root.val)
            if root.left:
                queue.append((root.left,level+1))
            if root.right:
                queue.append((root.right,level+1))
        return result

