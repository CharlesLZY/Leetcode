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

### Stack Solution
class Solution:
    def levelOrder(self, root):
        result = []
        if root is None: ### corner case
            return result
        
        stack = [(root,0)]
        
        while stack:
            root, level = stack.pop(0)
            if len(result) <= level:
                result.append([])
            result[level].append(root.val)
            if root.left:
                stack.append((root.left,level+1))
            if root.right:
                stack.append((root.right,level+1))
        return result


### Queue Solution
class Solution:
    def levelOrder(self, root):
        res = []
        if root is None:
            return res
        
        queue = [root]

        while queue:
            cur_level = queue[:]
            queue.clear()
            res.append([])
            while cur_level:
                cur = cur_level.pop(0)
                res[-1].append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return res